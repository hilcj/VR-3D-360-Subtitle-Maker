# VR-3D-360-Subtitle-Maker

Please see installation first!

## Usage

1. Create subtitles to image files.
2. Add subtitles to the VR image.

![CreatSubtitle.png](/imgs_readme/create_subtitle.png?raw=true "CreateSubtitle")

![AddPatterns.png](/imgs_readme/add_patterns.png?raw=true "AddPatterns")

## Installation

PS: I haven't packed up the code yet, so you need to manually apply a few commands to compile the code.

The package is coded in python and need a few packages.  To manage things around, I would like to recommend you to work with python anaconda environment https://www.anaconda.com/distribution/

After download and install the anaconda latest version,

### Step 1
(on windows) open anaconda-navigator, click "Environments" tab, and then click on the triangle near "base" and select "Open Terminal".  (on Linux/mac) Just open a normal terminal.

### Step 2
in terminal, type below commands to install the environment.  This may take up to 5 minutes.
```bash
conda create --name env_for_subtitle_maker python=3.6.2
conda activate env_for_subtitle_maker

conda install numpy opencv cython kivy matplotlib -y
pip install kivy-garden
garden install matplotlib
```
### Step 3
then download the source code (https://github.com/hilcj/VR-3D-360-Subtitle-Maker/archive/v1.0.zip), unzip it.  Then, use the same terminal as the step 2 and type below commands:
```bash
cd YOUR_UNZIPPED_FOLDER
python setup.py develop
```
then you are ready to go!

Just type
``` bash
python create_subtitles.py
```
or
``` bash
python add_patterns.py
```
to start the GUI.

### Step 4
to start the GUI in future, just follow step 1 to open a terminal, and type:
``` bash
conda activate env_for_subtitle_maker
cd YOUR_UNZIPPED_FOLDER
python create_subtitles.py # or add_patterns.py
```

## Input VR image
The input VR image should be a top/bottom VR image in omnidirectional stereo projection (https://support.google.com/jump/answer/6399843?hl=en), with left image on top and right image on bottom.

Input patterns can be any image format of any size.

## Support me
Paypal
http://paypal.me/hilcj0001

Wechat / Alipay
![alipay_wechat.png](/imgs_readme/alipay_wechat.png?raw=true "alipay_wechat")

