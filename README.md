# Sentweements

### Sentiments analysis for Tweets!

### Installation

Install requirements using

`pip install -r requirements.txt`

Register your application [here](https://apps.twitter.com/) to get an API_KEY and an API_SECRET which you need to export as environment variables using

`export API_KEY=<your_API_KEY>`

`export API_SECRET=<your API_SECRET>`

**Note:** Since these are environmet variables, you will have to do this every time you start a new shell. So you might want to write a bash script to do that. You just need to put the above two commands in a file and then use `sh [filename]`. 

### Usage

 - `./smile <text>` does sentiment analysis of the text. E.g. -> `./smile "I love coding."`

- `./tweet <@screen_name>(without @)` analyses last 50 tweets of the user with that `screen_name`. E.g -> `./tweets realDonaldTrump`

- `python application.py` hosts the website at localhost:8000.
  - Open `localhost:8000` in your browser.
  - Gives a downloadable pie-chart for the last 100 tweets by the user.

#### Author - [Akash Trehan](https://codemaxx.github.io/)
