---
title: How to compress photo size
aliases:
  - How to compress photo size
created: 2024-06-26T14:22:35
modified: 2025-06-14T23:00:50
type: how-to
tags-link:
  - "[[photo]]"
---

## Most tidy -> `webp`

<iframe src='https://developers.google.com/speed/webp' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://developers.google.com/speed/webp' target='_blank' class='external-link'>https://developers.google.com/speed/webp</a></center>

Download via: https://developers.google.com/speed/webp/docs/precompiled

```shell
$ sudo apt install webp
$ cwebp -q 50 -lossless picture.png -o picture_lossless.webp
$ cwebp -q 70 picture_with_alpha.png -o picture_with_alpha.webp
$ cwebp -sns 70 -f 50 -size 60000 picture.png -o picture.webp
$ cwebp -o picture.webp picture.png
# https://developers.google.com/speed/webp/docs/cwebp
```

## JEPG -> [[tjko-jpegoptim|jpegoptim]]

```shell
jpegoptim --size=1024k xxx.jpg
```

- Convert image to JPEG using https://imagemagick.org
- Convert image to JPEG using https://github.com/mozilla/mozjpeg

## PNG

### (lossy compress) pngquant

<iframe src='https://pngquant.org/' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://pngquant.org/' target='_blank' class='external-link'>https://pngquant.org/</a></center>

### optipng

<iframe src='https://optipng.sourceforge.net/' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://optipng.sourceforge.net/' target='_blank' class='external-link'>https://optipng.sourceforge.net/</a></center>

a PNG optimizer that recompresses image files to a smaller size, without losing any information. This program also converts external formats (BMP, GIF, PNM and TIFF) to optimized PNG, and performs PNG integrity checks and corrections."

用 optipng 压缩过的图片合成 == 未用 optipng 压缩过的图片合成（对比两个文件的哈希值都一样）

![[ShareX_39_1673338132238_0.png]]

```shell
optipng -o3 image.png -out output.png
# `-o0`~`-o7`，级别越高压缩率越高但速度越慢
```
