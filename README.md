# vasttrafikDepartures
Python/Flask web app to find and display the next buses from a particular stop. This was built to assist in finding the next bus from the bus stop near the office heading into town. The main corporate app and site are feature full, but therefore require a certain amount of entry and review. This takes just the needed information and presents it.

It was as much a chance for me to get back into using Python, as it has been some time. There are other, more comprehensive soltuions out there such as PyTrafik.

## Initiation
Download the files, edit config.py and include your Key and Secret and then just run from the command line with python server.py

You will need to have installed the various modules of course, but all can be done with "pip install XXXX"

## Developer account
You will need to sign up to the developer portal on Vasttrafik to use this app. That will give you the key and secret needed to run it.

## Future changes
The intent is to parameterize the URL structure so that other bus, stop or track information can be passed into the app. 
Future development includes integration with Slack API to allow users to request the next bus from a slack channel rather than going to the website.
Further development is integration with Amazon Alexa to allow for querys to be asked of Alexa on the next approaching bus.
