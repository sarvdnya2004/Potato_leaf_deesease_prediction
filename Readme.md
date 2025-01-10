# 🌱 Potato Leaf Disease Prediction 🍃  

An AI-powered solution to assist farmers and agricultural professionals in identifying diseases in potato leaves. This project uses a **Convolutional Neural Network (CNN)** built with **TensorFlow** and **Keras**, coupled with a user-friendly **Streamlit** frontend for real-world accessibility.

---

## 🌟 Features  
- **Automated Disease Detection**: Identifies and classifies potato leaf images into three categories:  
  - `Early Blight`  
  - `Healthy`  
  - `Late Blight`  
- **Efficient Model**: CNN architecture ensures high accuracy and performance.  
- **Frontend Interface**: Streamlit-powered frontend for easy accessibility.  
- **Scalable Design**: Can be extended to include other plant diseases.  

---

## 🚀 Technologies Used  
- **TensorFlow & Keras**: For building and training the CNN model.  
- **NumPy**: For efficient numerical computations.  
- **Streamlit**: For developing the interactive user interface.  
- **ImageDataGenerator**: For preprocessing and augmenting training data.  

---

## 📂 Project Structure  
```plaintext
Potato-Leaf-Disease-Prediction/
│
├── DATASET/                       # Folder for training and testing data
│   ├── PLD_3_Classes_256/         # Subfolders with images for 'Training' & 'Testing'
│
├── potato_desease.h5              # Saved CNN model
├── app.py                         # Streamlit frontend script
├── requirements.txt               # Dependencies for the project
├── README.md                      # Project overview
└── main.py                        # Model training and prediction script
