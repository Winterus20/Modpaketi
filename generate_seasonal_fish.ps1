# generate_seasonal_fish.ps1 — Python üreticisini çağırır (PS 5.1 uyumlu)
param(
    [string]$InstanceRoot = $PSScriptRoot,
    [switch]$ForceExtract
)

$pyScript = Join-Path $InstanceRoot "generate_seasonal_fish.py"
if (-not (Test-Path $pyScript)) {
    Write-Error "generate_seasonal_fish.py bulunamadı: $pyScript"
    exit 1
}

if ($ForceExtract) {
    $tmpTide  = Join-Path $InstanceRoot "tmp_tide"
    $tmpExtra = Join-Path $InstanceRoot "tmp_tide_extra"
    foreach ($d in @($tmpTide, $tmpExtra)) {
        $marker = Join-Path $d ".extracted"
        if (Test-Path $marker) { Remove-Item $marker -Force }
    }
}

python $pyScript
exit $LASTEXITCODE
