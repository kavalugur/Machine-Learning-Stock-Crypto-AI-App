from flask import Flask, jsonify, request
import yfinance as yf
import requests
from flask_cors import CORS
import math
from datetime import datetime

app = Flask(__name__)
CORS(app)

MESSARI_API_URL = 'https://data.messari.io/api/v1/assets/'

@app.route('/stock/<ticker>', methods=['GET'])
def get_stock(ticker):
    interval = request.args.get('interval', default='1d')  # Default to daily data
    stock = yf.Ticker(ticker)
    hist = stock.history(period="3mo", interval=interval)  # Fetch 3 months of data with the specified interval
    
    if hist.empty:
        return jsonify({"error": f"No data found for the given ticker {ticker} and interval {interval}"}), 404

    prices = hist['Close'].tolist()
    # Check for NaN values and replace with None
    prices = [price if not math.isnan(price) else None for price in prices]
    
    data = {
        "dates": hist.index.strftime("%Y-%m-%d %H:%M:%S").tolist(),
        "prices": prices
    }
    return jsonify(data)

@app.route('/crypto/<symbol>', methods=['GET'])
def get_crypto_data(symbol):
    interval = '1d'  # Fetch daily data
    limit = 90  # Fetch 3 months of data (90 days)
    
    # Binance API URL
    binance_url = f"https://api.binance.com/api/v3/klines?symbol={symbol.upper()}USDT&interval=1d&limit={limit}"
    response = requests.get(binance_url)

    if response.status_code == 200:
        data = response.json()
        prices = [float(candle[4]) for candle in data]  # Closing prices
        dates = [datetime.utcfromtimestamp(candle[0] / 1000).strftime('%Y-%m-%d %H:%M:%S') for candle in data]

        return jsonify({"prices": prices, "dates": dates})
    else:
        return jsonify({"error": f"No data found for the given symbol {symbol}"}), 404

@app.route('/crypto/prediction/<symbol>', methods=['GET'])
def get_crypto_prediction(symbol):
    # Fetch prediction data from a remote API
    prediction_url = 'https://ugurkaval.pythonanywhere.com/get-latest-prediction'
    response = requests.get(prediction_url)
    
    if response.status_code == 200:
        responseData = response.json()
        predictions = responseData['predictions']
        
        prediction = next((pred for pred in predictions if pred['symbol'].lower() == symbol.lower()), None)
        
        if prediction:
            return jsonify({
                'predictedPrice': prediction['predicted_price'],
                'timestamp': prediction['timestamp']
            })
        else:
            return jsonify({'error': f'Prediction data for {symbol} is missing or invalid'}), 404
    else:
        return jsonify({'error': 'Failed to load prediction data'}), 500

@app.route('/stock/prediction/<ticker>', methods=['GET'])
def get_stock_prediction(ticker):
    # Fetch prediction data from a remote API
    prediction_url = 'https://ugurkaval.pythonanywhere.com/get-latest-prediction'
    response = requests.get(prediction_url)
    
    if response.status_code == 200:
        responseData = response.json()
        predictions = responseData['predictions']
        
        prediction = next((pred for pred in predictions if pred['symbol'].lower() == ticker.lower()), None)
        
        if prediction:
            return jsonify({
                'predictedPrice': prediction['predicted_price'],
                'timestamp': prediction['timestamp']
            })
        else:
            return jsonify({'error': f'Prediction data for {ticker} is missing or invalid'}), 404
    else:
        return jsonify({'error': 'Failed to load prediction data'}), 500

@app.route('/crypto/details/<symbol>', methods=['GET'])
def get_crypto_details(symbol):
    # Fetch circulating supply data from Messari API
    messari_url = f"{MESSARI_API_URL}{symbol.lower()}/metrics"
    messari_response = requests.get(messari_url)
    
    if messari_response.status_code == 200:
        messari_data = messari_response.json()
        circulating_supply = messari_data['data']['supply'].get('circulating', 'Unknown')
    else:
        circulating_supply = 'Unknown'

    return jsonify({
        "circulating_supply": circulating_supply
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
