from flask import Flask, render_template, request

import helpers
from analyzer import Analyzer

app = Flask(__name__)


@app.route("/")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name")
    if not screen_name:
        return render_template("search.html")

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    positive, negative, neutral = 0.0, 0.0, 0.0

    # instantiate analyzer
    analyzer = Analyzer()

    if tweets is not None:
        for tweet in tweets:
            score = analyzer.analyze(tweet)
            if score > 0:
                positive += 1
            elif score < 0:
                negative += 1

    neutral = 100 - positive - negative

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)

# Run the app :)
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=8000
  )