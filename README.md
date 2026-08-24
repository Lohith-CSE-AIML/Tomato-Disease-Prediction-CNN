# 🍅 Tomato Disease Prediction Using CNN

A deep learning project that uses a **Convolutional Neural Network (CNN)** to detect tomato leaf diseases from images.

The model classifies tomato leaves into three categories:

* 🍂 **Early Blight**
* 🦠 **Late Blight**
* 🌿 **Healthy**

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
10. Streamlit application

---

## 🎯 Objective

The main objective of this project is to develop a CNN-based image classification model capable of identifying tomato leaf diseases from images.

---

## 🗂️ Dataset

The project uses a tomato leaf image dataset containing images belonging to three classes.

### Classes

| Class           | Description                          |
| --------------- | ------------------------------------ |
| 🍂 Early Blight | Tomato leaf affected by Early Blight |
| 🦠 Late Blight  | Tomato leaf affected by Late Blight  |
| 🌿 Healthy      | Healthy tomato leaf                  |

The images were processed and resized to **224 × 224 pixels** before being passed to the CNN model.

> The complete image dataset is not included in this repository because of its large size.

---

## 🧠 CNN Model

A **Convolutional Neural Network (CNN)** was developed using **TensorFlow and Keras**.

The CNN learns important visual features from tomato leaf images through convolution and pooling operations.

### Main Components

* Convolutional layers
* ReLU activation
* Max Pooling
* Flatten layer
* Dense/Fully Connected layers
* Softmax output layer

The final output layer contains **3 neurons**, representing the three tomato leaf classes.

---

## 🔄 Data Preprocessing

Before training the model, the images were preprocessed.

### Image Size

```text
224 × 224 × 3
```

The three channels represent the RGB color channels.

### Data Augmentation

Data augmentation was used to improve model generalization.

The augmentation process included techniques such as:

* Rotation
* Horizontal flipping
* Zooming
* Cropping
* Other image transformations

These transformations help the model learn from different variations of the same type of leaf.

---

## 📊 Model Performance

The trained CNN model was evaluated using a separate test dataset.

### Test Results

| Metric        |     Result |
| ------------- | ---------: |
| Test Loss     |     0.4268 |
| Test Accuracy | **85.97%** |

### Classification Report

| Class        | Precision | Recall | F1-Score | Support |
| ------------ | --------: | -----: | -------: | ------: |
| Early Blight |      0.73 |   0.83 |     0.78 |     145 |
| Late Blight  |      0.91 |   0.84 |     0.88 |     288 |
| Healthy      |      0.94 |   0.95 |     0.94 |     244 |
| **Accuracy** |           |        | **0.88** | **677** |
| Macro Avg    |      0.86 |   0.87 |     0.87 |     677 |

### 📈 Training Results

The following graph shows the training and validation performance of the CNN model.

![Training Results](images/training_results.png)

### 📌 Confusion Matrix

The confusion matrix shows how the model performed across the three disease classes.

![Confusion Matrix](images/confusion_matrix.png)

---

## 💻 Streamlit Application

The trained CNN model was integrated into a **Streamlit web application**.

The application allows users to:

1. Upload a tomato leaf image.
2. Preprocess the image.
3. Pass the image through the trained CNN model.
4. Predict the disease class.
5. Display the prediction to the user.

### 📸 Application Screenshot

<img width="1202" height="887" alt="Screenshot 2026-08-24 225122" src="https://github.com/user-attachments/assets/c6931c82-be4e-4387-a9f8-ae2c81c003b8" />


---

## 🔬 Project Workflow

```text
                 Tomato Leaf Image
                         │
                         ▼
                Image Preprocessing
                         │
                         ▼
                  Data Augmentation
                         │
                         ▼
                    CNN Model
                         │
                         ▼
                  Feature Extraction
                         │
                         ▼
                    Classification
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
        Early Blight  Late Blight  Healthy
```

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
* **Git**
* **GitHub**
* **Git LFS**

---

## 📁 Project Structure

```text
Tomato-Disease-Prediction-CNN/
│
├── README.md
├── tomato_disease_prediction.ipynb
├── tomato_disease_model.keras
├── app.py
├── requirements.txt
├── .gitignore
├── .gitattributes
│
└── images/
    ├── streamlit_app.png
    ├── confusion_matrix.png
    └── training_results.png
```

### File Description

| File/Folder                       | Description                                   |
| --------------------------------- | --------------------------------------------- |
| `tomato_disease_prediction.ipynb` | Complete CNN training and evaluation notebook |
| `tomato_disease_model.keras`      | Trained CNN model                             |
| `app.py`                          | Streamlit application                         |
| `requirements.txt`                | Required Python libraries                     |
| `.gitignore`                      | Files excluded from Git                       |
| `.gitattributes`                  | Git LFS configuration                         |
| `images/`                         | Project screenshots and visual results        |

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Lohith-CSE-AIML/Tomato-Disease-Prediction-CNN.git
```

```bash
cd Tomato-Disease-Prediction-CNN
```

### 2. Install Git LFS

Because the trained model is a large file, Git LFS is used to store it.

If Git LFS is not already installed:

```bash
git lfs install
```

Then download the LFS files:

```bash
git lfs pull
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🖥️ Application Workflow

```text
Upload Tomato Leaf Image
          │
          ▼
   Image Preprocessing
          │
          ▼
     CNN Prediction
          │
          ▼
   Predicted Disease
          │
          ▼
 Display Result to User
```

---

## 📈 Future Improvements

Possible improvements for future versions include:

* Increase the size and diversity of the dataset.
* Improve Early Blight classification performance.
* Experiment with transfer learning models such as:

  * MobileNet
  * EfficientNet
  * ResNet
* Perform hyperparameter tuning.
* Add more tomato disease classes.
* Improve the Streamlit user interface.
* Deploy the application online.
* Display prediction confidence scores.
* Add explainable AI techniques such as Grad-CAM.

---

## ⚠️ Limitations

The model is trained specifically for the tomato leaf classes included in the dataset.

Therefore:

* It may not accurately identify diseases that were not included during training.
* Performance may vary with images captured under different lighting conditions.
* Very blurry or unclear images may produce incorrect predictions.
* The model should be considered an educational/project implementation rather than a replacement for professional agricultural diagnosis.

---

## 👨‍💻 Author

### Lohith

**B.Tech CSE – Artificial Intelligence & Machine Learning**

GitHub:
https://github.com/Lohith-CSE-AIML

---

## ⭐ If You Found This Project Useful

If you found this project interesting or useful, consider giving the repository a ⭐ on GitHub.
