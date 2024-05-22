[**Install:**](https://ohmyposh.dev/docs/installation/windows)  
```
Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
Install-Module posh-git -Scope CurrentUser  
Install-Module -Name Terminal-Icons -Repository PSGallery
Install-Module PSReadLine -AllowPrerelease -Force
```

**Settings:**  
create the profile file.  
```
notepad $PROFILE 
```

Set themes and load the module.  
```
Set-PoshPrompt -Theme agnosterplus  
$env:POSH_GIT_ENABLED=$true  
Import-Module posh-git  
Import-Module oh-my-posh  
Import-Module -Name Terminal-Icons
```

```
$env:POSH_GIT_ENABLED=$true  
Import-Module posh-git  
Import-Module -Name Terminal-Icons

## Set theme
oh-my-posh init pwsh --config 'https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/agnosterplus.omp.json'  | Invoke-Expression
#For local theme:
# oh-my-posh init pwsh --config ~/.custom.omp.json | Invoke-Expression


Import-Module -Name Terminal-Icons
Import-Module PSReadLine

Set-PSReadLineOption -HistorySearchCursorMovesToEnd
Set-PSReadlineKeyHandler -Chord UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward

Set-PSReadLineOption -PredictionSource History 
Set-PSReadLineOption -PredictionViewStyle ListView

New-Alias -Name l -value "ls"


## Fro update:
# Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
```
