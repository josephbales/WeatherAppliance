Weather Appliance
=================

A set of python scripts I plan to use to drive a little weather display appliance I am building.

Cut me some slack, I am a C# developer trying to write python 😃

- sudo apt-get install libcairo2
- pip3 install [svgwrite](https://pypi.org/project/svgwrite/)
- [svgwrite docs](https://svgwrite.readthedocs.io/en/latest/overview.html)
- [svgwrite source](https://github.com/mozman/svgwrite)
- icons (https://www.iconfinder.com/iconsets/good-weather-1) (https://creativecommons.org/licenses/by/3.0/)

### TODOs
- need to create something that handles program flow control, like should the program run, did the 
production of a new image fail, should it try again or display a fail message, I will probably just
run this as a cron job so the program will need to know weather to run again or not when triggered
- need something to control the display, just something that will take images and put them on the screen
- need decide how I will handle creating the images to draw on the screen, since it is two tones, I will
need something to create the black image and something to create the red image
- logging
- figure out how to structure this project in a more pythonic way
- tests
- data retention, do I want to store any data in a database?

