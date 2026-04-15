import requests
import json

class PredictionEngine:
    def __init__(self, coin_ids):
        self.coin_ids = coin_ids

    def fetch_coin_data(self):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(self.coin_ids)}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data

    def analyze_market(self, data):
        predictions = {}
        for coin, values in data.items():
            price = values['usd']
            if price < 100:  # Threshold for down bias prediction
                predictions[coin] = "down/no"
            else:
                predictions[coin] = "up/yes"
        return predictions

    def predict(self):
        coin_data = self.fetch_coin_data()
        predictions = self.analyze_market(coin_data)
        return predictions

if __name__ == "__main__":
    coin_ids = ["bitcoin", "ethereum", "litecoin"]
    engine = PredictionEngine(coin_ids)
    prediction_results = engine.predict()
    print(prediction_results)