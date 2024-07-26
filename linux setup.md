**Update packages &repos**
```zsh
sudo apt-get update -y
sudo apt-get upgrade -y
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

[Instal pipx](https://pipx.pypa.io/stable/installation/)
```zsh
sudo apt update
sudo apt install pipx
# optional to allow pipx actions in global scope. See "Global installation" section below.
pipx ensurepath
# sudo pipx ensurepath --global 
```
[Install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started)
```zsh
pipx install uv
```
[install rich-cli](https://github.com/Textualize/rich-cli?tab=readme-ov-file#windows--linux)
```zsh
pipx install rich-cli
```

[install mcfly](https://github.com/cantino/mcfly?tab=readme-ov-file#installing-using-our-install-script-macos-or-linux)
```

```
