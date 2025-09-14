# 📌 Roadmap Enxuto (pré-TensorFlow)

## 1. Métricas de avaliação
- [x] Estudar **accuracy, precision, recall, F1, ROC-AUC** (classificação).  
- [ ] Estudar **R², RMSE, MAE** (regressão).  
- [ ] Reavaliar o modelo de preço de casas com **todas as métricas relevantes**.  
- [x] Escrever uma explicação curta para cada métrica em linguagem simples.

> **Projeto:** atualizar o notebook de preço de casas mostrando métricas e interpretações.

---

## 2. Feature Engineering & Pipelines (scikit-learn)
- [ ] Revisar **imputação** (SimpleImputer, KNNImputer).  
- [ ] Revisar **scaling** (StandardScaler, MinMaxScaler).  
- [ ] Revisar **encoding** (OneHotEncoder, OrdinalEncoder).  
- [ ] Testar **polynomial features** para regressão.  
- [ ] Reorganizar o fluxo com `Pipeline` + `ColumnTransformer`.

> **Projeto:** recriar o pipeline de preço de casas usando `Pipeline`, com encoding + scaling automáticos.

---

## 3. Validação e tuning de modelos
- [ ] Implementar **k-fold cross-validation** no projeto.  
- [ ] Testar **GridSearchCV** para hiperparâmetros.  
- [ ] Testar **RandomizedSearchCV** para hiperparâmetros.  
- [ ] Comparar baseline (**Linear Regression**) com **RandomForest**.  
- [ ] Adicionar **XGBoost ou GradientBoosting** e comparar resultados.

> **Projeto:** relatório comparando baseline vs. RandomForest vs. XGBoost com cross-validation.

---

## 4. Conceitos de Deep Learning (sem código ainda)
- [ ] Entender o que é um **neurônio artificial**.  
- [ ] Estudar **funções de ativação** (ReLU, Sigmoid, Tanh, Softmax).  
- [ ] Estudar o que é uma **loss function**.  
- [ ] Entender o que é um **otimizador** (SGD, Adam).  
- [ ] Revisar **overfitting vs. underfitting** em redes neurais.  
- [ ] Conseguir explicar em texto **como funciona um perceptron + backpropagation**.

> **Meta:** escrever um texto de 5–10 linhas explicando redes neurais com suas palavras.
