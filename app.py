from flask import Flask, render_template, request

from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_review():
    review = request.form['review']
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        sentiment = 'Positive'
        score = 5
        emoji = '\U0001F604'
    elif polarity < -0.2:
        sentiment = 'Negative'
        score = 1
        emoji = '\U0001F614'
    else:
        sentiment = 'Neutral'
        score = 3
        emoji = '\U0001F610'
    result = {'sentiment': sentiment, 'score': score, 'emoji': emoji}
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
