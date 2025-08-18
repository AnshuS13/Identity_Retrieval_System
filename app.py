import streamlit as st
import cv2
import os
import pandas as pd
from datetime import datetime

# Main Dataset Folder
DATASET_DIR = "dataset"
CSV_FILE = os.path.join(DATASET_DIR, "details.csv")

# Ensure dataset folder exists
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# Ensure CSV file exists
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Name", "Age", "DOB", "Email", "Phone",
                               "Emergency Contact", "Address", "Timestamp"])
    df.to_csv(CSV_FILE, index=False)

# -------------------------------
# Function to capture images
# -------------------------------
def capture_images(unique_id, num_images=50):
    save_path = os.path.join(DATASET_DIR, unique_id)
    os.makedirs(save_path, exist_ok=True)

    cap = cv2.VideoCapture(0)  # open webcam

    count = 0
    st.write("📸 Capturing images... please keep changing angles 😊")
    progress_bar = st.progress(0)

    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access webcam.")
            break

        # Save image
        img_name = f"{unique_id}_{count+1}.jpg"
        img_path = os.path.join(save_path, img_name)
        cv2.imwrite(img_path, frame)

        count += 1
        progress_bar.progress(count / num_images)

        # Live preview (press Q to stop early)
        cv2.imshow("Capturing Images - Press Q to Stop", frame)
        cv2.waitKey(100)

    cap.release()
    cv2.destroyAllWindows()
    st.success(f"✅ {count} images saved in {save_path}")

# -------------------------------
# Streamlit App
# -------------------------------
st.title("🧑‍🤝‍🧑 Identity Retrieval System")

# Ask user: Register or Recognize
choice = st.radio("What do you want to do?", ["Register", "Recognize"])

if choice == "Register":
    st.header("📝 Registration Form")

    with st.form("registration_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        dob = st.date_input("Date of Birth")
        email = st.text_input("Email ID (Unique ID)")
        phone = st.text_input("Contact Number")
        emergency_contact = st.text_input("Emergency Contact Number")
        address = st.text_area("Residential Address")

        submitted = st.form_submit_button("Register & Capture Images")

    if submitted:
        if not email.strip():
            st.error("❌ Email ID is required (used as unique ID).")
        else:
            # Save details to central CSV
            new_data = pd.DataFrame([{
                "Name": name,
                "Age": age,
                "DOB": str(dob),
                "Email": email,
                "Phone": phone,
                "Emergency Contact": emergency_contact,
                "Address": address,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }])
            new_data.to_csv(CSV_FILE, mode='a', header=False, index=False)

            st.success("📄 Personal details saved to central CSV file.")

            # Capture images
            capture_images(email, num_images=50)

elif choice == "Recognize":
    st.header("🔍 Recognition (Coming Soon)")
    st.info("This part will be connected to the backend (Person A's module).")
