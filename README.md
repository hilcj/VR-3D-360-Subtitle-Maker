# VR-3D-360-Subtitle-Maker

Please see installation first!

## Usage

On your termimal (linux/mac) or cmd(windows)
```bash
python create_subtitle.py
```
![CreatSubtitle.png](/imgs_readme/create_subtitle.png?raw=true "CreateSubtitle")

```bash
python add_patterns.py
```
![AddPatterns.png](/imgs_readme/add_patterns.png?raw=true "AddPatterns")

## Installation

PS: I haven't packed up the code yet, so you need to manually apply a few commands to compile the code.

The package is coded in python and need a few packages.  To manage things around, I would like to recommend you to work with python anaconda environment https://www.anaconda.com/distribution/

After download and install the anaconda latest version, goto your terminal or cmd interface, and type below commands:

(On windows, you may need to first open the "anaconda navigator", select "environment" tab, and on the list of environment, click the right triangle and select, "open in terminal"）

```bash
conda create --name env_for_subtitle_maker python=3.6.2
conda activate env_for_subtitle_maker

conda install numpy opencv cython kivy matplotlib -y
pip install kivy-garden
garden install matplotlib
```

Then, clone the git depository and compile the code in the same terminal.

```bash
# Download
cd $YOUR_WORKING_FOLDER$
git clone https://github.com/hilcj/VR-3D-360-Subtitle-Maker/
cd VR-3D-360-Subtitle-Maker

# Compile
cd implementations
python setup.py build_ext --inplace
cp implementations/* .
cd ..

# Ready to go
python create_subtitles.py

python add_patterns.py
```

## Input image
up/down, 360

## Support me
Paypal
http://paypal.me/hilcj0001

Wechat / Alipay
![alipay_wechat.png](/imgs_readme/alipay_wechat.png?raw=true "alipay_wechat")

