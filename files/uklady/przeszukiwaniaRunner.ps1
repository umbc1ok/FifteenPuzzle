$validStrategies = "astr"
$validParams = "hamm","manh"

foreach ($strategy in $validStrategies) {
    foreach ($param in $validParams) {
        $command = ".\przeszukiwania.ps1 -strategy $strategy -param $param"
        Write-Host "Running command: $command"
        Invoke-Expression $command
    }
}
