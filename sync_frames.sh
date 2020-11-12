#! /bin/sh

peaks=$(python peak_finder.py "$1")

echo "$peaks" | while read line; do ffmpeg -ss 00:00:0$line -i "$1" -vframes 1 syncframe$line.jpg; done
