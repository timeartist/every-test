from os import environ
from pprint import pp

import requests
from flask import Flask, render_template

app = Flask(__name__)

## GLOBAL TODO:
## - modify templates to use inheritence, so we don't have multiple header defintiions
## - move css, js into their own respective files
## - add pagination to results page
## - add direct donation link using every.org api
## - add filter by location/other values
## - add db/cache so we're not hitting the API for every call and so that we can slice and dice data better
## - add tests/build/deploy pipeline

EVERY_ORG_API_KEY = environ.get('EVERY_ORG_API_KEY')
# CAUSE_RESULTS_COUNT = 100

if not EVERY_ORG_API_KEY:
    raise ValueError("EVERY_ORG_API_KEY environment variable is not set.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cause/<string:cause>')
def show_cause(cause):
    # Make API request to Every.org
    ## TODO: implement pagination and/or increase limit of results.  
    ## TODO Use url builder if it gets more complicated than this
    url = f"https://partners.every.org/v0.2/search/{cause}?apiKey={EVERY_ORG_API_KEY}"#&take={CAUSE_RESULTS_COUNT}"
 
    print(f'api call start - {url}')
    response = requests.get(url)
    print(f'response: {response}')

    data = response.json()

    # Create list of nonprofit data
    nonprofits_raw = data.get('nonprofits', [])
    nonprofits = []
    for nonprofit in nonprofits_raw:
        nonprofit_data = {
            'name': nonprofit.get('name', ''),
            'location': nonprofit.get('location', ''),
            'website': nonprofit.get('websiteUrl', ''),
            'description': nonprofit.get('description', ''),
            'id': nonprofit.get('slug', '')
        }
        nonprofits.append(nonprofit_data)
    
    return render_template('cause.jinja', cause=cause, nonprofits=nonprofits)


if __name__ == '__main__':
    app.run(debug=True)
   