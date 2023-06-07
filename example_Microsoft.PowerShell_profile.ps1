## OH MY POSH settings
Set-PoshPrompt -Theme agnosterplus
$env:POSH_GIT_ENABLED=$true
Import-Module posh-git
Import-Module oh-my-posh

## Make the terminal beutifull & productive
Import-Module -Name Terminal-Icons
Import-Module PSReadLine

## History search
Set-PSReadLineOption -HistorySearchCursorMovesToEnd
Set-PSReadlineKeyHandler -Chord UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward

Set-PSReadLineOption -PredictionSource History 
Set-PSReadLineOption -PredictionViewStyle ListView


# Add bin to PATH
$env:Path += "; $env:UserProfile\\.local\\bin"

New-Alias -Name l -value "ls"
New-Alias -Name cc -value "rich"
New-Alias -Name onelogin -value cloud-sso

# shortcut for which python
function wp()
{
	python -c 'import sys; print(sys.executable)'
}


# make a nice version of cat utilizing rich
function ccc([string]$File)
{
    C:\\Users\\avit\\.local\\bin\\rich.exe -n -g "$File"
}

# imitate bash's realpath
function realpath([string]$File)
{
    Resolve-Path "$File"
} 

function ecr()
{
    aws ecr get-login-password | docker login --username AWS --password-stdin <YOUR ECR REGISTRY>
}
