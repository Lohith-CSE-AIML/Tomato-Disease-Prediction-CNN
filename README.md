# 🍅 Tomato Disease Prediction Using CNN

A deep learning project that uses a **Convolutional Neural Network (CNN)** to detect tomato leaf diseases from images.

The model classifies tomato leaves into three categories:

* **Early Blight**
* **Late Blight**
* **Healthy**

The trained CNN model is integrated with a **Streamlit web application** that allows users to upload a tomato leaf image and receive a disease prediction.

---

## 📌 Project Overview

Plant diseases can significantly affect crop production and quality. Early identification of diseases can help farmers take appropriate action and reduce crop losses.

This project uses **Deep Learning and Computer Vision** to automatically identify tomato leaf diseases from images.

The complete workflow includes:

1. Dataset preparation
2. Image preprocessing
3. Data augmentation
4. CNN model development
5. Model training
6. Validation
7. Testing
8. Model evaluation
9. Disease prediction
10. Streamlit deployment

---

## 🎯 Objective

The main objective of this project is to build a CNN-based image classification model capable of identifying tomato leaf diseases from images.

---

## 🗂️ Classes

The model predicts one of the following three classes:

| Class           | Description                          |
| --------------- | ------------------------------------ |
| 🍃 Healthy      | Healthy tomato leaf                  |
| 🟤 Early Blight | Tomato leaf affected by Early Blight |
| 🦠 Late Blight  | Tomato leaf affected by Late Blight  |

---

## 🧠 Model

A **Convolutional Neural Network (CNN)** was developed using **TensorFlow and Keras**.

The CNN learns visual features from tomato leaf images through convolutional and pooling layers.

### Main components

* Convolutional layers
* ReLU activation
* Max Pooling
* Flatten layer
* Fully Connected/Dense layers
* Softmax output layer

The final output layer contains **3 neurons**, corresponding to the three tomato leaf classes.

---

## 🔄 Data Preprocessing

The images were resized to:

```text
224 × 224 pixels
```

The dataset was divided into training, validation, and testing data.

Data augmentation techniques were also used to improve the model's ability to generalize to different images.

Examples of augmentation techniques include:

* Rotation
* Horizontal flipping
* Cropping/zooming
* Other image transformations

---

## 📊 Model Performance

The trained model was evaluated using a separate test dataset.

### Test Results

| Metric        | Result |
| ------------- | -----: |
| Test Loss     | 0.4268 |
| Test Accuracy | 85.97% |

### Classification Report

| Class        | Precision | Recall | F1-Score |
| ------------ | --------: | -----: | -------: |
| Early Blight |      0.73 |   0.83 |     0.78 |
| Late Blight  |      0.91 |   0.84 |     0.88 |
| Healthy      |      0.94 |   0.95 |     0.94 |

The model performs particularly well in identifying **healthy tomato leaves**, while Early Blight remains the more challenging class.

---

## 🛠️ Technologies Used

* **Python**
* **TensorFlow**
* **Keras**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Scikit-learn**
* **Pillow**
* **Streamlit**
* **Google Colab**
* **Git & GitHub**
* **Git LFS**

---

## 📁 Project Structure

```text
Tomato-Disease-Prediction-CNN/
│
├── tomato_disease_prediction.ipynb
├── tomato_disease_model.keras
├── app.py
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md
```

### File Description

**`tomato_disease_prediction.ipynb`**

Contains the complete CNN development process, including data loading, preprocessing, training, evaluation, and predictions.

**`tomato_disease_model.keras`**

The trained CNN model used for tomato disease classification.

**`app.py`**

Streamlit application used to create the web interface for making predictions.

**`requirements.txt`**

Contains the Python libraries required to run the project.

**`.gitignore`**

Specifies files and folders that should not be tracked by Git.

**`.gitattributes`**

Contains the Git LFS configuration used to track the large `.keras` model file.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Lohith-CSE-AIML/Tomato-Disease-Prediction-CNN.git
```

```bash
cd Tomato-Disease-Prediction-CNN
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💻 Streamlit Application

The project includes a Streamlit interface where the user can:

1. Upload a tomato leaf image.
2. Process the image.
3. Pass the image through the trained CNN model.
4. Get the predicted disease class.
5. View the prediction result.

---

## 🔬 Project Workflow

```text
Tomato Leaf Image
       ↓
Image Preprocessing
       ↓
Data Augmentation
       ↓
CNN Model
       ↓
Feature Extraction
       ↓
Classification
       ↓
┌─────────────────┐
│ Early Blight    │
│ Late Blight     │
│ Healthy         │
└─────────────────┘
```

---

## 📈 Future Improvements

Some possible improvements for future versions include:

* Increase the size and diversity of the dataset.
* Improve Early Blight classification performance.
* Experiment with transfer learning models such as MobileNet, EfficientNet, or ResNet.
* Perform hyperparameter tuning.
* Add more tomato disease classes.
* Improve the Streamlit user interface.
* Deploy the application online.
* Add prediction confidence scores and visual explanations.

---

## 👨‍💻 Author

**Lohith**

B.Tech CSE – Artificial Intelligence & Machine Learning

GitHub:
https://github.com/Lohith-CSE-AIML

---

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub.
