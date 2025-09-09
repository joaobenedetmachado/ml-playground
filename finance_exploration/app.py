import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

FinAlvo = input(': ')

data = yf.download(FinAlvo, start="2022-01-01", end="2023-01-01")

# features
data['Return'] = data["Close"].pct_change()
data["Target"] = (data["Return"].shift(-1) > 0).astype(int)  # 1 = sobe, 0 = cai

# features mais simples
data["Lag1"] = data["Return"].shift(1)
data["Lag2"] = data["Return"].shift(2)
data["Lag3"] = data["Return"].shift(3)

data = data.dropna()

#feature
X = data[["Lag1", "Lag2", "Lag3"]]
y = data["Target"] #alvo

# treino e split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)

# usar os train's para treinar
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))

# Insight para o último dia conhecido
last_features = X.iloc[-1].values.reshape(1, -1)
prediction = model.predict_proba(last_features)[0]

print(f"Probabilidade de {FinAlvo} cair: {prediction[0]:.2f}")
print(f"Probabilidade de {FinAlvo} subir: {prediction[1]:.2f}")
