# VR-3D-360-Subtitle-Maker

Adding subtitles to VR-360 images / video.

To work with a VR-360 video, please use ffmpeg to convert video to image sequences, and use the batch mode in the software to add subtitle to each image file, and then compose video back from image files.

For examples:
```bash
ffmpeg -i vr_video.mp4 temp/out%d.png
```
and
```bash
ffmpeg -i temp/out%d.png out.mp4
```

To run the software from source code, please see "Installation"!

## Usage

1. Create subtitles to image files.
2. Add subtitles to the VR image.

![CreatSubtitle.png](/imgs_readme/create_subtitle.png?raw=true "CreateSubtitle")

![AddPatterns.png](/imgs_readme/add_patterns.png?raw=true "AddPatterns")

## Installation

The package is coded in python.
To manage things around, I would like to recommend you to work with python anaconda environment https://www.anaconda.com/distribution/

After download and install the anaconda latest version,

### Step 1: open terminal
(on windows) open anaconda-navigator, click "Environments" tab, and then click on the triangle near "base" and select "Open Terminal".  (on Linux/mac) Just open a normal terminal.

### Step 2: install
in terminal, type below commands to install the environment.  This may take up to 5 minutes.
```bash
pip install cython vrsubtitlemaker
```

### Step 3: run
in the same terminal, just type
``` bash
create_subtitles
```
or
``` bash
add_patterns
```
to start the GUI.

### Step 4
to start the GUI in future, just follow step 1 to open a terminal, and type:
``` bash
create_subtitles # or add_patterns
```

## Input VR image
The input VR image should be a top/bottom VR image in omnidirectional stereo projection (https://support.google.com/jump/answer/6399843?hl=en), with left image on top and right image on bottom.

Input patterns can be any image format of any size.

## Support me
Paypal
http://paypal.me/hilcj0001

Wechat / Alipay
![alipay_wechat.png](/imgs_readme/alipay_wechat.png?raw=true "alipay_wechat")

