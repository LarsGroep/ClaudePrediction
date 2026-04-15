import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

class MarketDataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.model = LogisticRegression()

    def preprocess_data(self):
        # Assuming 'close' price is used for predictions
        self.data['price_change'] = self.data['close'].diff()  # Calculate price difference
        self.data['target'] = np.where(self.data['price_change'] > 0, 1, 0)  # 1 for up, 0 for down
        self.data.dropna(inplace=True)

    def train_model(self):
        features = self.data[['open', 'high', 'low', 'close', 'volume']]
        target = self.data['target']
        self.model.fit(features, target)

    def generate_confidence_scores(self):
        features = self.data[['open', 'high', 'low', 'close', 'volume']]
        probabilities = self.model.predict_proba(features)[:, 1]  # Confidence scores for 'up' predictions
        return probabilities

# Example usage:
# df = pd.read_csv('path_to_your_data.csv')
# analyzer = MarketDataAnalyzer(df)
# analyzer.preprocess_data()
# analyzer.train_model()
# scores = analyzer.generate_confidence_scores()
