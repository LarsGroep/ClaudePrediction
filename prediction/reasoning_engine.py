class ReasoningEngine:
    def __init__(self):
        self.bias = "Down"

    def analyze_title(self, title):
        # A method to analyze the title and apply logic
        if 'Up' in title:
            self.bias = "Up"
        else:
            self.bias = "Down"

    def predict(self, title):
        self.analyze_title(title)
        # Addition of reasoning logic here
        # For example: more complex analysis can change bias
        return self.bias

# Usage
# engine = ReasoningEngine()
# prediction = engine.predict("BTC Up or Down - 15 minutes")
# print(prediction)  # Output: Up or Down depending on analysis