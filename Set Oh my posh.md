Install-Module oh-my-posh -Scope CurrentUser  
Install-Module posh-git -Scope CurrentUser  

notepad $PROFILE 

 > Set-PoshPrompt -Theme agnosterplus  
 > $env:POSH_GIT_ENABLED=$true  
 > Import-Module posh-git  
 > Import-Module oh-my-posh  
