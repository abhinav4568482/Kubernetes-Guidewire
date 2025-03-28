# -*- coding: utf-8 -*-
"""Guidewire P1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JyepVmqglUp-9RedmXcAkOcItPnMGTxt
"""

!pip install pandas numpy scikit-learn tensorflow matplotlib seaborn

from google.colab import files
uploaded = files.upload()

import kagglehub

# Download latest version
path = kagglehub.dataset_download("yigitsever/misuse-detection-in-containers-dataset")

print("Path to dataset files:", path)

import os

# Verify the dataset path
print("Dataset Path:", dataset_path)

# List files in the dataset directory
print("Files in dataset path:", os.listdir(dataset_path))

import pandas as pd

# Correct dataset path
dataset_path = "/root/.cache/kagglehub/datasets/yigitsever/misuse-detection-in-containers-dataset/versions/1/dataset.csv"

# Load the dataset
df = pd.read_csv(dataset_path)

# Display first few rows
df.head()

import pandas as pd

# Define useful columns for Kubernetes failure prediction
useful_columns = [
    "Flow Duration", "Total Fwd Packet", "Total Bwd packets",
    "Flow Bytes/s", "Flow Packets/s", "Active Mean", "Idle Mean", "Label"
]

# Load only required columns (Modify based on dataset)
df = pd.read_csv("/content/dataset.csv", usecols=useful_columns)

df = df.sample(frac=0.1, random_state=42)  # Reduce dataset to 10%

for col in df.columns:
    if df[col].dtype == "float64":
        df[col] = df[col].astype("float32")
    elif df[col].dtype == "int64":
        df[col] = df[col].astype("int32")

print(df.info())  # Check memory usage reduction

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Drop non-numeric columns
df = df.drop(columns=["Flow ID", "Src IP", "Dst IP", "Timestamp"], errors="ignore")

# Features (X) and Target (y)
X = df.drop(columns=["Label"])
y = df["Label"]


from sklearn.preprocessing import StandardScaler

# Scale Features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Increase iterations
model = LogisticRegression(max_iter=1000)  # Increased from 500 to 1000
model.fit(X_train, y_train)

# Evaluate Model
accuracy = model.score(X_test, y_test)
print(f"Optimized Model Accuracy: {accuracy * 100:.2f}%")


# Evaluate Model
accuracy = model.score(X_test, y_test)
print(f"Optimized Model Accuracy: {accuracy * 100:.2f}%")

import joblib

# Save the model
joblib.dump(model, "k8s_failure_predictor.pkl")
print("Model saved as k8s_failure_predictor.pkl")

# Commented out IPython magic to ensure Python compatibility.
!git clone https://Kubernetes@github.com/abhinav4568482/Kubernetes-Guidewire.git
# %cd Kubernetes-Guidewire/

# Move files into repo
!mv /content/k8s_failure_predictor.pkl .
!mv /content/your_script.py .

# Commit and push
!git config --global user.email "abhichristine765@gmail.com"
!git config --global user.name "abhinav4568482"
!git add .
!git commit -m "Added trained model and scripts"
!git push origin main



