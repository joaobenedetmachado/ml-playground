# Machine Learning Studies

This repository organizes my Machine Learning studies with a focus on practical applications. The goal is to learn how to solve real-world problems efficiently, prioritizing what produces the most impact.

## Study Structure

# 📌 ML + DL Study Roadmap

### 1. Data Understanding & Preparation ✅  
- Data exploration using pandas, matplotlib, and seaborn  X
- Cleaning: handling missing values, duplicates, and outliers X  
- Normalization and standardization X
- Encoding categorical variables (one-hot, label encoding)  
- Train/validation/test split X

### 2. Core ML Models ✅  
- **Logistic Regression** — simple classification  X
- **Random Forest** — robust, good for tabular data  X
- **XGBoost / LightGBM** — strong performance on structured data X
- 👉 Compare baselines vs ensembles, using cross-validation  

### 3. Model Evaluation ✅  
- Metrics: accuracy, precision, recall, F1-score, ROC-AUC X
- Choose metrics according to the problem type X 

### 4. Avoiding Overfitting  
- Techniques: regularization, cross-validation, early stopping  
- Focus: train well and generalize to unseen data  

### 5. Hyperparameter Tuning  
- Tools: GridSearchCV, RandomizedSearchCV, Optuna  
- Apply to RandomForest / XGBoost / LightGBM  

---

### 6. Intro to Deep Learning (Concepts First)  
- Neurons, layers, activations, loss functions, optimizers  
- Backpropagation (high-level understanding)  
- Overfitting/underfitting in neural nets  

---

### 7. TensorFlow & PyTorch 🚀  
- **TensorFlow (Keras API)**  
  - Building dense feedforward networks  
  - Using callbacks (early stopping, checkpointing)  
  - Training on structured/tabular data  
- **PyTorch**  
  - Manual training loops vs high-level API (Lightning/FastAI)  
  - Understanding tensors & autograd  
  - Implementing a basic neural net from scratch  
👉 Project: train the same simple NN in both frameworks, compare coding style  

---

### 8. Text & Basic NLP  
- Vectorization: TF-IDF, word embeddings, BERT embeddings  
- Classification tasks (reviews, spam detection)  
- Try both **scikit-learn + TF-IDF** and **PyTorch/TensorFlow embeddings**  

---

### 9. Practical ML/DL Cycle  
1. Collect and prepare data  
2. Split into train/validation/test sets  
3. Train ML or DL models  
4. Evaluate and adjust  
5. Deploy (pickle/joblib for ML, SavedModel/torchscript for DL)  
6. Serve via FastAPI/Flask  

---

### 10. What to Avoid Initially  
- Very deep neural nets (CNNs/RNNs) without tabular basics  
- Reinforcement learning, GANs, diffusion models (too advanced for now)  
- MLOps heavy tools (Kubeflow, Airflow)  

---

📂 **Next Repo Section**:  
`/deep_learning_basics` → notebooks comparing TensorFlow and PyTorch on the same problems.  


## Getting Started
Clone the repository and follow the notebooks and scripts in the `/notebooks` folder for exercises and mini-projects.
