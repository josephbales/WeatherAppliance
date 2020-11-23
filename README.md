Weather Appliance
=================

A set of python scripts I plan to use to drive a little weather display appliance I am building.

Cut me some slack, I am a C# developer trying to write python 😃

[Waveshare Docs](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT_(B))

- sudo apt install noto-fonts
- sudo apt install libopenjp2-7
- sudo apt install libtiff5
- sudo pip3 install RPi.GPIO
- sudo pip3 install spidev
- sudo pip3 install [Pillow](https://pypi.org/project/Pillow/)
- sudo pip3 install [pyyamml](https://pypi.org/project/PyYAML/)

### TODOs
- need to create something that handles program flow control, like should the program run, did the 
production of a new image fail, should it try again or display a fail message, I will probably just
run this as a cron job so the program will need to know whether to run again or not when triggered
- need something to control the display, just something that will take images and put them on the screen
- ~~need decide how I will handle creating the images to draw on the screen, since it is two tones, I will
need something to create the black image and something to create the red image~~
- ~~logging~~
- ~~figure out how to structure this project in a more pythonic way~~
- tests
- data retention, do I want to store any data in a database?
- Data in the bmp
  - datetime
  - tempurature
  - weather image
  - weather description (main)
  - barometric pressure
  - humidity
  - feels like temp
  - wind speed
  - wind direction
  - sunrise time
  - sunset time
  - alert info or fortune

