import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Tomato Disease Detection",
    page_icon="🍅",
    layout="centered"
)


# ---------------- LOAD MODEL ----------------

model = tf.keras.models.load_model("tomato_disease_model.keras")


# ---------------- TITLE ----------------

st.title("🍅 Tomato Plant Disease Detection")

st.caption(
    "AI-powered tomato leaf disease classification using a CNN model."
)

st.warning(
    "⚠️ Please upload only tomato plant leaf images. "
    "This model is trained specifically on tomato leaf images "
    "and may give incorrect predictions for unrelated images."
)

st.divider()


# ---------------- IMAGE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📤 Choose a tomato leaf image",
    type=["jpg", "jpeg", "png"]
)


# ---------------- IMAGE + PREDICTION ----------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Tomato Leaf",
        width=400
    )

    st.divider()

    # Predict button
    if st.button(
        "🔍 Predict Disease",
        use_container_width=True
    ):

        # Resize image
        image_resized = image.resize((224, 224))

        # Convert image to NumPy array
        image_array = np.array(image_resized)

        # Add batch dimension
        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        # Prediction
        prediction = model.predict(image_array)

        # Class names
        class_names = [
            "Early Blight",
            "Late Blight",
            "Healthy"
        ]

        # Disease information
        disease_info = {
            "Early Blight":
                "Early blight is a fungal disease that can cause "
                "dark spots and yellowing on tomato leaves.",

            "Late Blight":
                "Late blight can cause dark lesions on tomato leaves "
                "and may spread rapidly under favorable conditions.",

            "Healthy":
                "The leaf appears healthy based on the patterns "
                "learned by the model."
        }

        # Find predicted class
        predicted_class = np.argmax(
            prediction[0]
        )

        # Calculate confidence
        confidence = float(
            np.max(prediction[0]) * 100
        )

        # ---------------- RESULT ----------------

        st.subheader("🌿 Prediction Result")

        st.success(
            f"Detected: {class_names[predicted_class]}"
        )

        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(
            confidence / 100
        )

        st.info(
            disease_info[class_names[predicted_class]]
        )


# ---------------- DEVELOPER ----------------

st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <p>Developed by <strong>Lohith</strong> 🍅</p>
    </div>
    """,
    unsafe_allow_html=True
)