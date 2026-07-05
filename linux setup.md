**Update packages &repos**
```zsh
sudo apt-get update -y
sudo apt-get upgrade -y
```

**Install utilities**
```zsh
sudo apt install vim
```

[Install zsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)
```zsh
sudo apt install zsh

chsh -s $(which zsh) #set as default
```

[Install Oh My ZSH](https://ohmyz.sh/#install)
```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```


[Install uv](https://docs.astral.sh/uv/getting-started/installation/)
```zsh
`curl -LsSf https://astral.sh/uv/install.sh | sh`
```
install rich-cli
```zsh
uv tool install rich-cli
```

install mcfly
```
uv tool install mcfly
```
