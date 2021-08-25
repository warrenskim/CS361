from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import requests
from wikiscraper import search_formatter, wiki_url, wiki_scraper, formatted_wiki_scraper, flag_scraper
import os

app = Flask(__name__)
CORS(app)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

# Display homepage
@app.route("/")
def get_home():
    return render_template('index.html')


# Display comparison page
@app.route("/comparison", methods=['GET', 'POST'])
def get_comparison():
    state1 = request.args.get('state1')
    state2 = request.args.get('state2')

    state1_scraped = get_state_data(state1)
    state2_scraped = get_state_data(state2)
    
    state1_flag = get_state_flag(state1)
    state2_flag = get_state_flag(state2)

    return render_template('comparison.html', state1_name=state1, state2_name=state2, 
    state1_data=state1_scraped, state2_data=state2_scraped, flag1=state1_flag, flag2=state2_flag)


# State infobox scraper
def get_state_data(state):
    formatted_search = search_formatter(state)
    url = wiki_url(formatted_search)
    scraped_data = wiki_scraper(url)
    return scraped_data


# Flag scraper 
def get_state_flag(state):
    formatted_search = search_formatter(state)
    url = wiki_url(formatted_search)
    scraped_flag = flag_scraper(url)
    return scraped_flag


# Route for wikipedia infobox scraper microservice -- for teammate use 
@app.route("/search", methods=['GET', 'POST'])
def get_search():
    search_name = request.args.get('search')

    search_formatted = search_formatter(search_name)

    url = wiki_url(search_formatted)

    scraped = formatted_wiki_scraper(url)
    return jsonify(scraped)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3157)) 
    app.run(port=port, debug=True) 