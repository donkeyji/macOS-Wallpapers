#!/bin/sh
cd /Users/$USER/Pictures/Wallpapers
# 获取图片的文件名
title=$(/Users/$USER/Pictures/Wallpapers/env/bin/python /Users/$USER/Pictures/Wallpapers/random_pic.py)
echo $title
# 暂停5秒等待图片缓存写入文件
sleep 5
# 图片地址
localpath="/Users/$USER/Pictures/Wallpapers/images/$title.jpg"
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$localpath\""
# 提示壁纸更换完成
osascript -e "display notification \"壁纸更换成功\n$title\" with title \"壁纸更换脚本\""