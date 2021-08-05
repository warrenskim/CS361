from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
from wikiscraper import flagscraper, search_formatter, wiki_url, wikiscraper, formatted_wikiscraper
import os

app = Flask(__name__)
CORS(app)


# TAKE THIS OUT WHEN DEPLOYING
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

# Display homepage
@app.route("/")
def get_home():
    return render_template('index.html')


@app.route("/comparison", methods=['GET', 'POST'])
def get_comparison():
    state1_name = request.args.get('state1')
    state2_name = request.args.get('state2')

    state1_search = search_formatter(state1_name)
    state2_search = search_formatter(state2_name)

    url1 = wiki_url(state1_search)
    url2 = wiki_url(state2_search)

    scraped1 = wikiscraper(url1)
    scraped2 = wikiscraper(url2)

    flag1 = flagscraper(url1)
    flag2 = flagscraper(url2)

    return render_template('comparison.html', state1_name=state1_name, state2_name=state2_name, 
    state1_data=scraped1, state2_data=scraped2, flag1=flag1, flag2=flag2)


# Need to make a request for this --> If Python use requests.get(url for search) or if Node url parser
# How do they send the request from their language
@app.route("/search", methods=['GET', 'POST'])
def get_search():
    search_name = request.args.get('search')

    search_formatted = search_formatter(search_name)

    url = wiki_url(search_formatted)

    scraped = formatted_wikiscraper(url)
    return jsonify(scraped)


@app.route("/test", methods=['GET', 'POST'])
def get_test():
    Object = requests.get("http://127.0.0.1:3157/search?search=Smith+Rock+state+park")
    Object1 = Object.text

    return render_template('test.html', Object1=Object1)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3157)) 
    app.run(port=port, debug=True) 