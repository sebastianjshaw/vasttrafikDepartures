# vasttrafikDepartures
Python/Flask web app to find and display the next buses from a particular stop. This was built to assist in finding the next bus from the bus stop near the office heading into town. The main corporate app and site are feature full, but therefore require a certain amount of entry and review. This takes just the needed information and presents it.

It was as much a chance for me to get back into using Python, as it has been some time. There are other, more comprehensive soltuions out there such as PyTrafik.

## Installation
Checkout the repository, and update the `config.py` file to include your `CONSUMER_KEY` and `CONSUMER_SECRET`.

You will then need to install the following modules:
```
$ pip install flask
$ pip install requests
```

>NB: It is suggested you do this through `virtualenv` to prevent dependency conflicts with other projects; a guide to running Flask through virtualenv can be found [here](http://flask.pocoo.org/docs/0.12/installation/#installation).


Finally, just run `server.py` to start the app:

```
$ python server.py
```

## Developer account
Keys can be obtained from the [Västtrafik developer portal](https://developer.vasttrafik.se) after registering for an account.

## Future changes
The intent is to parameterize the URL structure so that other bus, stop or track information can be passed into the app. 
Future development includes integration with Slack API to allow users to request the next bus from a slack channel rather than going to the website.
Further development is integration with Amazon Alexa to allow for querys to be asked of Alexa on the next approaching bus.
