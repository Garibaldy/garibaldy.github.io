# Opcional: requiere cuenta en https://www.screenshotmachine.com/
# API: dimension = "1440xfull" (página completa, sin límite 9999)
# $env:SCREENSHOT_MACHINE_KEY = "tu_key"

param(
  [string]$Url = "https://intrepidux.vercel.app/",
  [string]$OutFile = "..\assets\review\vercel-full.png",
  [string]$Dimension = "1440xfull",
  [string]$Selector = ""
)

$key = $env:SCREENSHOT_MACHINE_KEY
if (-not $key) {
  Write-Error "Define SCREENSHOT_MACHINE_KEY (sign up en screenshotmachine.com)"
  exit 1
}

$base = "https://api.screenshotmachine.com"
$query = @{
  key = $key
  url = $Url
  dimension = $Dimension
  device = "desktop"
  format = "png"
  delay = "2000"
  cacheLimit = "0"
}
if ($Selector) { $query.selector = $Selector }

$uri = $base + "?" + (($query.GetEnumerator() | ForEach-Object { "$($_.Key)=$([uri]::EscapeDataString([string]$_.Value))" }) -join "&")
$outPath = Join-Path $PSScriptRoot $OutFile
New-Item -ItemType Directory -Force -Path (Split-Path $outPath) | Out-Null
Invoke-WebRequest -Uri $uri -OutFile $outPath
Write-Host "Guardado: $outPath"
