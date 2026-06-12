import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class InvestmentIntelligencePlatform:
    def __init__(self, data_path):
        # Load main dataset
        self.df = pd.read_csv(data_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
        
    def engineer_features(self, symbol):
        """Calculates RSI and Moving Averages for the Predictor Engine"""
        stock_data = self.df[self.df['Symbol'] == symbol].copy()
        stock_data = stock_data.sort_values('Date').reset_index(drop=True)
        
        stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
        stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()
        
        delta = stock_data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        stock_data['RSI_14'] = 100 - (100 / (1 + (gain / loss)))
        
        return stock_data.dropna()

    def run_predictor_engine(self, symbol):
        """Mandatory Task A: Random Forest Directional Predictor"""
        data = self.engineer_features(symbol)
        data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)
        data = data.dropna()
        
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_50', 'SMA_200', 'RSI_14']
        X = data[features]
        y = data['Target']
        
        split = int(len(data) * 0.8)
        X_train, X_test = X.iloc[:split], X.iloc[split:]
        y_train, y_test = y.iloc[:split], y.iloc[split:]
        
        model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        print(f"[{symbol}] Predictor Engine Accuracy: {accuracy_score(y_test, predictions):.4f}")

    def calculate_risk_metrics(self, symbol, risk_free_rate=0.06):
        """Mandatory Task C: Risk Assessment Module"""
        data = self.df[self.df['Symbol'] == symbol].sort_values('Date').copy()
        data['Daily_Return'] = data['Close'].pct_change()
        
        annual_return = data['Daily_Return'].mean() * 252
        annual_volatility = data['Daily_Return'].std() * np.sqrt(252)
        sharpe = (annual_return - risk_free_rate) / annual_volatility
        
        downside = data.loc[data['Daily_Return'] < 0, 'Daily_Return']
        sortino = (annual_return - risk_free_rate) / (downside.std() * np.sqrt(252))
        
        print(f"[{symbol}] Return: {annual_return:.2%}, Volatility: {annual_volatility:.2%}, Sharpe: {sharpe:.2f}, Sortino: {sortino:.2f}")

if __name__ == "__main__":
    print("Initializing NIFTY-50 AI Platform...")
    platform = InvestmentIntelligencePlatform("NIFTY50_all.csv")
    platform.run_predictor_engine("INFY")
    platform.calculate_risk_metrics("TITAN")