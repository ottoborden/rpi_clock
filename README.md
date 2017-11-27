# rpi_clock

## What is this?
I'm learning about electronics and product design by building my dream 'Wake up device'. This is the repo for the code. Feel free to use anything that may be useful to you.

## 2.8 PiTFT+ from breadboard:
[The display and touchscreen uses the hardware SPI pins (SCK, MOSI, MISO, CE0, CE1) as well as GPIO #25 and #24.](https://www.adafruit.com/product/2298)
* Any 5V (Pin 2 or 4)
* Any 3.3V (Pin 1 or 17)
* Any Ground (Pin 6, 9, 14, 20, 25, 30, 34, or 39)
* GPIO #18 (Pin 12) - Optional for backlight control
* GPIO #24 (Pin 18)
* GPIO10/SPI MOSI (Pin 19)
* GPIO #9/SPI MISO (Pin 21)
* GPIO #25 (Pin 22)
* GPIO #11/SPI CLK (Pin 23)
* GPIO #8/SPI CE0 (Pin 24)
* GPIO #7/SPI CE1 (Pin 26)

**Turn off ‘power-saving’ mode (screen blanks in 30 mins)**
* Add the following line to `/etc/rc.local`
  * `sudo sh -c "TERM=linux setterm -blank 0 >/dev/tty0"`


## Setting up Wifi SSH (no keyboard/monitor)
Modify `/etc/network/interfaces`
```
allow-hotplug wlan0
auto wlan0
iface wlan0 inet dhcp
	wpa-ssid "<wifi_ssid>"
	wpa-psk "<wifi_password>”
```

Connect to RPi
```
ssh pi@raspberrypi.local
```
default password is `raspberry`

## GUI
Start a program and a single X server from CLI
* `startx some-app --kiosk`

**Bash script to launch python script with virtualenv**
```
#!/bin/bash

app="$(pwd)/"
pythonEnv="${app}ui/"
. ${pythonEnv}"bin/activate"
"${pythonEnv}bin/python" "${app}test.py"
```

Run with `sudo startx ~/ui/run`

## How to run
How to get software up and running on Adafruit's Raspian Jessie Lite image

**NOTE:** 
* PyGame @ 1.9.4.dev0 as 11/26/17
* Python v2.7.9

```
sudo apt-get update
sudo apt-get install xorg openbox xserver-xorg xinit
sudo apt-get install mercurial python-dev python-numpy python-opengl libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm musescore-soundfont-gm xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install virtualenv
mkdir ui && cd ui
virtualenv venv
source ui/bin/activate
echo hg+http://bitbucket.org/pygame/pygame >> requirements.txt
pip install -r requirements.txt
```

**Copy the script below into installsdl.sh**
```
#!/bin/bash
  
#enable wheezy package sources
echo "deb http://archive.raspbian.org/raspbian wheezy main
" > /etc/apt/sources.list.d/wheezy.list

#set stable as default package source (currently jessie)
echo "APT::Default-release \"jessie\";
" > /etc/apt/apt.conf.d/10defaultRelease

#set the priority for libsdl from wheezy higher than the jessie package
echo "Package: libsdl1.2debian
Pin: release n=jessie
Pin-Priority: -10
Package: libsdl1.2debian
Pin: release n=wheezy
Pin-Priority: 900
" > /etc/apt/preferences.d/libsdl

#install
apt-get update
apt-get -y --force-yes install libsdl1.2debian/wheezy
```

`sudo chmod +x installsdl.sh`
`sudo ./installsdl.sh`
