# macOS-Wallpapers

使用 python 获取 unsplash 的图片，并配合 shell 脚本设置桌面壁纸。

## 基本要求
1. python == 3.5.4
  另外还需要以下 python 组件
  - requests
  - bs4
2. macOS == 10.13.6 (理论上通用)

## 步骤

### 第一步：安装 python3 及相关模块
使用 `brew` 安装，如果没有 `brew`，请跳转到[此处](https://brew.sh)
```
brew update
brew upgrade
brew install python3
pip3 update
pip3 install virtualenv
```

### 第二步：创建文件夹
在你的用户文件夹 `Pictures` 下创建 `Wallpapers`，并将 `wallpaper.sh` & `random_pic.py` 放入到该文件夹

### 第三步：设置 python 虚拟环境并安装模块
在 `/Users/username/Pictures/Wallpapers` 文件夹下执行
```
virtualenv env
source env/bin/activate
pip install requests bs4 lxml
```

### 第三步：设置自动更新
将 `com.unsplash.plist` 放入到 `~/Library/LaunchAgents` 中
加载并启用
```
launchctl load -w 'com.unsplash.plist`
launchctl start 'com.unsplash.plist`
```
注意把 `com.unsplash.plist` 中的用户文件夹设置为你自己的用户文件夹

其中的一些参数需要自行修改。
