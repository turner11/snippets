**Install:**  
```
Install-Module oh-my-posh -Scope CurrentUser  
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
Set-PoshPrompt -Theme agnosterplus
$env:POSH_GIT_ENABLED=$true
Import-Module posh-git
Import-Module oh-my-posh
Import-Module -Name Terminal-Icons
Import-Module PSReadLine

Set-PSReadLineOption -HistorySearchCursorMovesToEnd
Set-PSReadlineKeyHandler -Chord UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward

Set-PSReadLineOption -PredictionSource History 
Set-PSReadLineOption -PredictionViewStyle ListView

New-Alias -Name l -value "ls"
```
