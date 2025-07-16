from src.data_loader import load_data, preprocess_data
from src.feature_engineering import add_features
from src.model import train_model
from src.evaluate import evaluate_model

from sklearn.model_selection import train_test_split

def main():
    df = load_data()
    df = preprocess_data(df)
    df = add_features(df)

    features = ['TX_AMOUNT', 'TX_HOUR', 'TX_DAY', 'TX_MONTH']
    X = df[features]
    y = df['TX_FRAUD']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)

    report = evaluate_model(y_test, y_pred)
    print(report)

if __name__ == "__main__":
    main()
