**Install:**  
```
Install-Module oh-my-posh -Scope CurrentUser  
Install-Module posh-git -Scope CurrentUser  
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
```
