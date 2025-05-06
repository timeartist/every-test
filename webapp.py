from os import environ
from pprint import pp

import requests
from flask import Flask, render_template

app = Flask(__name__)

EVERY_ORG_API_KEY = environ.get('EVERY_ORG_API_KEY')
if not EVERY_ORG_API_KEY:
    raise ValueError("EVERY_ORG_API_KEY environment variable is not set.")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cause/<string:cause>')
def show_cause(cause):
    # Make API request to Every.org
    
    url = f"https://partners.every.org/v0.2/search/{cause}?apiKey={EVERY_ORG_API_KEY}"
    print(f'api call start - {url}')
    response = requests.get(url)
    print(f'response: {response}')
    data = response.json()
    pp(len(data))
    
    print(f'make non-profit list start')
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
    print(f'make non-profit list end')
    
    return render_template('cause.jinja', cause=cause, nonprofits=nonprofits)


if __name__ == '__main__':
    app.run(debug=True)
   