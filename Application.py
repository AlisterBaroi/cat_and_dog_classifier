import streamlit as st

# from tensorflow.keras.models import load_model

# from tensorflow.compat.v1.keras.models import load_model
from keras.models import load_model
import numpy as np
from PIL import Image

# Configure Streamlit app settings
st.set_page_config(
    page_title="Cat & Dog Classifier",
    page_icon=":dog:",  # Set your desired icon
    layout="centered",  # Choose the layout style: "centered", "wide", "wide+sidebar"
    initial_sidebar_state="auto",  # Set the initial state of the sidebar: "auto", "expanded", "collapsed"
)

# Remove Streamlit footer
# MainMenu {visibility: hidden;}
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def preprocess_image(image):
    # Resize the image to match the input size of the model (150x150)
    image = image.resize((150, 150))

    # Convert the image to a numpy array
    image = np.array(image)
    # Normalize the pixel values to be in the range [0, 1]
    image = image / 255.0
    # Expand the dimensions to create a batch of 1
    image = np.expand_dims(image, axis=0)
    # st.write("image size:", image.size)
    # st.write("image shape:", image.shape)
    # st.write("image shape:", image.shape[1:3])
    return image


def load_and_predict(image, model):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Make predictions
    prediction = model.predict(processed_image)
    return prediction


def main():
    st.title("Cat & Dog Classifier")
    st.write("See '**About**' page for project details.")
    # st.markdown(
    #     """Author: [Alister Animesh Baroi](https://github.com/AlisterBaroi)
    #        Deployed using: [GCP Cloud Build](https://cloud.google.com/build)
    #        Deployed on: [GCP Cloud Run](https://cloud.google.com/run)
    #        Model created from scratch: [Link to Colab Notebook](https://colab.research.google.com/github/AlisterBaroi/cat_and_dog_classifier/blob/main/Alister's_Copy_of_fcc_cat_dog.ipynb)Looks like you're creating a hyperlink in Streamlit! It seems you want to direct users to an "About" page for project details and technical information. Is there anything specific you'd like to know or do with this code?
    #     """
    # )
    st.subheader("See Predictions:")
    uploaded_file = st.file_uploader(
        # "Choose an JPG, PNG or JPEG image", type=["jpg", "png", "jpeg"]
        "Upload an JPG, PNG or JPEG image of cat/dog, and press 'Classify' to see the results.",
        type=["jpg", "png", "jpeg"],
    )

    if uploaded_file is not None:
        st.write("Here is your uploaded image:")
        image = Image.open(uploaded_file)
        st.image(
            uploaded_file,
            caption=f"Uploaded Image: {uploaded_file.name}",
            use_column_width=True,
        )

        # Load the saved model
        model = load_model("cd_model.h5")

        if st.button("Classify"):
            # Make predictions when the button is clicked
            prediction = load_and_predict(image, model)
            # Assuming the model output is [probability_dog, probability_cat]
            probability_dog = prediction[0][1] * 100
            probability_cat = prediction[0][0] * 100
            # Display the predicted result
            if probability_dog > probability_cat:
                st.write(
                    f"This looks like a Dog! (Probability: {probability_dog:.4f}%)"
                )
            else:
                st.write(
                    f"This looks like a Cat! (Probability: {probability_cat:.4f}%)"
                )


if __name__ == "__main__":
    main()
