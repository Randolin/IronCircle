<#
.SYNOPSIS
  One-shot migration of the Obsidian vault content into this repo's docs/ folder.

.DESCRIPTION
  Copies Cadwallon, Fate Foretold, and Documentation from C:\Obsidian into docs/.
  Deliberately left behind:
    - C:\Obsidian\TTRPG\           (stale duplicate of the vault; top-level copies are canonical)
    - C:\Obsidian\Projects\        (Hot Springs Eternal — not a table project)
    - .obsidian\                   (workspace config)
    - Cadwallon\Rulebooks\         (commercial PDFs — copyrighted, not for a public repo)
    - *.pdf anywhere              (SRDs stay local; link to the publishers' pages instead)
    - Documentation\Documentation.md (replaced by docs/Documentation/index.md)

  Safe to re-run: robocopy only copies newer/changed files. It will not delete
  anything from docs/ that you've edited since.

.USAGE
  From the repo root, in PowerShell:
      .\tools\migrate-from-obsidian.ps1
#>

$ErrorActionPreference = "Stop"
$src  = "C:\Obsidian"
$repo = Split-Path -Parent $PSScriptRoot
$dst  = Join-Path $repo "docs"

if (-not (Test-Path $src)) { throw "Source vault not found at $src" }
if (-not (Test-Path $dst)) { New-Item -ItemType Directory -Path $dst | Out-Null }

function Copy-Tree {
    param([string]$Name, [string[]]$ExcludeDirs, [string[]]$ExcludeFiles)
    $from = Join-Path $src $Name
    $to   = Join-Path $dst $Name
    if (-not (Test-Path $from)) { Write-Warning "Skipping $Name (not found)"; return }
    Write-Host "==> $Name" -ForegroundColor Cyan
    $args = @($from, $to, "/S", "/NFL", "/NDL", "/NJH", "/NP", "/R:1", "/W:1")
    if ($ExcludeDirs)  { $args += "/XD"; $args += $ExcludeDirs }
    if ($ExcludeFiles) { $args += "/XF"; $args += $ExcludeFiles }
    & robocopy @args | Out-Null
    # robocopy exit codes 0-7 are success; 8+ are failures
    if ($LASTEXITCODE -ge 8) { throw "robocopy failed for $Name (exit $LASTEXITCODE)" }
    $count = (Get-ChildItem $to -Recurse -File | Measure-Object).Count
    Write-Host "    $count files in docs\$Name"
}

Copy-Tree -Name "Cadwallon"     -ExcludeDirs @(".obsidian", "Rulebooks") -ExcludeFiles @("*.pdf")
Copy-Tree -Name "Fate Foretold" -ExcludeDirs @(".obsidian")              -ExcludeFiles @("*.pdf")
Copy-Tree -Name "Documentation" -ExcludeDirs @(".obsidian")              -ExcludeFiles @("*.pdf", "*.txt", "Documentation.md")

Write-Host ""
Write-Host "Done. Next:" -ForegroundColor Green
Write-Host "  git add -A && git commit -m 'Migrate Obsidian vault' && git push"
Write-Host "  Then in GitHub: Settings > Pages > Source = 'GitHub Actions'"
