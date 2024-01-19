import requests
from flask import Flask, request, send_from_directory

API_KEY = "BMM1DIQERJ31OUWQ"
BASE_URL = "https://www.alphavantage.co/query"

app = Flask(__name__)


@app.route("/")
def index():
  return "Hello world!"


# This route contains the core functionality to get stock information.  This calls the "Quote Endpoint" API from Alpha Vantage: https://www.alphavantage.co/documentation/#latestprice
@app.route('/stock', methods=['GET'])
def get_stock_data():
  symbol = request.args.get('symbol')

  params = {"function": "GLOBAL_QUOTE", "symbol": symbol, "apikey": API_KEY}

  response = requests.get(BASE_URL, params=params)
  return response.json()


# ChatGPT will use this route to find the manifest file, ai-plugin.json; it will look in the "".well-known" folder
@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('.',
                             'ai-plugin.json',
                             mimetype='application/json')


# ChatGPT will use this route to find the API specification, openapi.yaml
@app.route('/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


'''
@app.route('/logo.png')
def plugin_logo():
  return send_from_directory('.', 'logo.png')
'''


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)