$validStrategies = "astr"
$validParams = "manh","hamm"

foreach ($strategy in $validStrategies) {
    foreach ($param in $validParams) {
        $command = ".\przeszukiwania.ps1 -strategy $strategy -param $param"
        Write-Host "Running command: $command"
        Invoke-Expression $command
    }
}
