import streamlit as st

# Configure Streamlit app settings
st.set_page_config(
    page_title="About - Cat & Dog Classifier",
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


st.title("About: Cat & Dog Classifier")
# Links to your Colab notebook & GitHub repo
st.markdown(
    """Author: [Alister Animesh Baroi](https://github.com/AlisterBaroi)    
       Project Source Code: [GitHub Repositoy](https://github.com/AlisterBaroi/cat_and_dog_classifier)      
       Deployed on: [GCP Cloud Run](https://cloud.google.com/run)  
       Model created from scratch: [Link to Colab Notebook](https://colab.research.google.com/github/AlisterBaroi/cat_and_dog_classifier/blob/main/Alister's_Copy_of_fcc_cat_dog.ipynb)      
    """
)
st.subheader("Overview:")
st.write(
    "Developed a robust image classification web application using Streamlit, TensorFlow, and Keras deployed on Google Cloud Platform's Cloud Run. This application allows users to upload images of cats or dogs, and the custom-built deep learning model accurately identifies and classifies the uploaded images while providing confidence scores."
)
st.subheader("Key Features:")
st.write(
    """
        **1. User-Friendly Interface:**   
        The Streamlit-based web interface offers an intuitive user experience, enabling seamless image uploads and interactions.

        **2. Custom Deep Learning Model:**  
        Implemented a convolutional neural network (CNN) model from scratch using TensorFlow and Keras. The model was trained on a diverse dataset of cat and dog images, achieving high accuracy in classification.

        **3. Real-time Prediction:**   
        The model processes the uploaded images in real-time, swiftly identifying whether the image contains a cat or a dog, along with a confidence score expressed as a percentage.

        **4. GCP Cloud Run Deployment:**   
        Leveraged Google Cloud Build for continuous integration and continuous deployment (CI/CD) pipeline, ensuring efficient and automated updates to the application on Cloud Run. This deployment strategy ensures scalability, reliability, and easy accessibility.
    """
)
st.subheader("Technical Stack:")
st.markdown(
    """ 
        - Python   
        - TensorFlow   
        - Keras     
        - Streamlit     
        - Google Cloud Platform (Cloud Run, Cloud Build)  
    """
)
st.subheader("Outcome and Impact:")
st.markdown(
    """ 
        This project demonstrates proficiency in machine learning, deep learning, web development, and cloud deployment. The accurate classification of images with confidence scores showcases the effectiveness of the developed model. Additionally, the seamless deployment on GCP Cloud Run reflects expertise in leveraging cloud infrastructure for scalable applications. 
    """
)
st.subheader("Future Improvements:")
st.markdown(
    """ 
        Potential enhancements could involve expanding the classifier to recognize more animal categories or refining the user interface for a more engaging experience. Additionally, integrating monitoring tools or implementing user authentication could further enhance the application's functionality and security.
    """
)
st.subheader("Conclusion:")
st.markdown(
    """ 
        This project showcases the integration of machine learning and web technologies to create an interactive and efficient image classification tool. Its successful deployment on Google Cloud Platform demonstrates proficiency in building end-to-end machine learning applications and leveraging cloud services for scalable deployment.
    """
)
