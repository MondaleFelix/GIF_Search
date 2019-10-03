from flask import Flask, render_template, request
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    search = request.args.get('search')
    # TODO: Make 'params' dict with query term and API key
    payload = {
    	"q": search,
    	"key": TENOR_API_KEY
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    req = requests.get("https://api.tenor.com/v1/search?", params=payload)
    data = req.json()
    # TODO: Get the first 10 results from the search results

    results = data["results"][0:10]


    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template(
        "index.html",
        results=results
        )


if __name__ == '__main__':
    app.run(debug=True)