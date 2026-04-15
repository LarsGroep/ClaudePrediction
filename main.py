# main.py

def main():
    # Initialize components
    fetcher = CryptoDataFetcher()
    analyzer = MarketAnalyzer()
    engine = ReasoningEngine()

    # Fetch crypto data
    data = fetcher.fetch_data()

    # Analyze market trends
    analysis_results = analyzer.analyze(data)

    # Make predictions based on analysis
    predictions = engine.predict(analysis_results)

    # Output predictions
    print(predictions)

if __name__ == '__main__':
    main()