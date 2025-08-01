# Training-and-Analysis-of-a-CST64-Noiseless-Neural-Model

This project focuses on developing, training, and analyzing a neural network model on the CST64 dataset with noiseless image inputs. It aims to evaluate the model's ability to learn representations effectively under clean data conditions and analyze its performance using various evaluation metrics.

## 📌 Project Objectives

- Train a deep learning model on a clean (noiseless) version of the CST64 dataset.
- Perform performance evaluation using image similarity metrics.
- Analyze training/validation trends and model output.
- Explore the effects of data quality on model performance.

## 📊 Dataset - CST64

The CST64 dataset is a high-resolution image dataset often used in super-resolution and denoising tasks. For this project:
- Only **noiseless images** are used.
- Images were normalized and resized during preprocessing.
- Dataset is split into training and validation subsets.

## 🧠 Model Architecture

The model used is a custom **Convolutional Neural Network (CNN)** tailored for noiseless image feature learning. It includes:
- Multiple convolutional layers with ReLU activation
- Batch normalization
- Residual connections
- Optional dropout layers
- Optimized using Adam optimizer and MSE loss
