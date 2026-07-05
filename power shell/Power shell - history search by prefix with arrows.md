```ps
Set-PSReadLineOption -HistorySearchCursorMovesToEnd
Set-PSReadlineKeyHandler -Chord UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward
```
[Credit](https://stackoverflow.com/questions/62883762/powershell-bind-arrow-keys-to-command-history-search)
