**Identity Retrieval System**
Face Recognition Based Lost Person Identification System

**📌 Project Overview**

The Identity Retrieval System is a Machine Learning–based application that identifies a person using live webcam input and retrieves their registered personal details such as:

1. Name
2. Phone Number
3. Address
4. Emergency Contact


The system consists of two main modules:
- Registration Module (Built using Streamlit UI)
- Recognition Module (Built using OpenCV + LBPH Face Recognizer)

This project was developed as part of a Project Oriented Machine Learning Internship.

**🎯 Objective**
- To build a real-time face recognition system that:
- Registers individuals with facial data and personal information
- Stores images and metadata locally
- Recognizes a person via webcam
- Retrieves and displays their stored details


**🏗️ Project Architecture**
Identity_Retrieval_System/
│
├── app.py                  # Streamlit UI
├── recognition.py          # Face recognition logic
├── trainer.yml             # Trained LBPH model
├── labels.npy              # Label mapping file
│
├── registration/
│   └── dataset/
│       ├── Person1/
│       ├── Person2/
│       └── details.csv
│
└── requirements.txt


**⚙️ Technologies Used**
- Python
- OpenCV (opencv-contrib-python)
- NumPy
- Pandas
- Streamlit

**📝 How It Works**

1️⃣ Registration Module

User enters personal details in Streamlit UI

Webcam captures 20–30 face images

Images are stored inside:

registration/dataset/<Person_Name>/


User details are stored in:

registration/dataset/details.csv

2️⃣ Model Training

Images are converted to grayscale

Faces are resized to 200x200

LBPH algorithm trains on dataset

Model saved as:

trainer.yml

labels.npy

3️⃣ Recognition Module

Webcam detects face using Haar Cascade

Face is compared with trained model

If confidence threshold is satisfied:

Person name is retrieved

Corresponding details fetched from CSV

If not:

Displays Unknown


**🚀 How to Run the Project**
Step 1: Install Dependencies
pip install -r requirements.txt


OR manually:

pip install streamlit opencv-contrib-python numpy pandas

Step 2: Run the Application
streamlit run app.py


If streamlit is not recognized:

python -m streamlit run app.py

📷 Dataset Requirements

Minimum 20–30 images per person

Good lighting conditions

Clear frontal face

No multiple faces in a single image

🔐 Confidence Threshold

Recognition uses:

if conf < 90:


Lower values → stricter matching
Higher values → more tolerant matching

📊 Future Improvements

Use Deep Learning models (FaceNet / Dlib)

Deploy using Streamlit Cloud

Replace CSV with SQL database

Add Liveness Detection

Improve UI/UX

👨‍💻 Contributors

Ravikant Choubey – Recognition Module & Model Training

Anshu – Streamlit UI & Registration Module

📄 License

This project is developed for educational purposes as part of a Machine Learning internship.
