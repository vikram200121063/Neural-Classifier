import streamlit as st
from PIL import Image
import numpy as np
# from tensorflow import keras
from keras.models import load_model
import tensorflow as tf

st.set_page_config(layout="wide")

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('image_classify.keras')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()
  
st.title("AI Image Classifier")

file = st.file_uploader('Upload an image to classify', type=["jpg", "png", "jpeg", "webm"],)
st.set_option('deprecation.showfileUploaderEncoding', False)

def check(image, model):
    # Load the image

    # Preprocess the image
    image = image.resize((300, 300))  # Resize the image to the desired dimensions
    image = np.array(image)  # Convert the image to a numpy array
    image = image.astype('float32') / 255.0  # Normalize pixel values between 0 and 1

    # Expand dimensions and create a batch
    image = np.expand_dims(image, axis=0)

    # model = load_model('.\\image_classify.keras')

    # Make predictions
    predictions = model.predict(image)
    p_value = predictions[0][0]
    

    return p_value

if file is None:
    st.warning("Please upload an image file")
else:
    st.success("Image uploaded successfully")
    image = Image.open(file)
    image = image.convert("RGB")
    
    try:
        prediction = check(image, model)
        
        if prediction <=0.25:
            prediction = '{:.4f}'.format(prediction)
            st.markdown(f'<font color="#3F875F" size="5">This image is most likely an </font> <font color="#6E9E26" size="5">**AI generated** </font><font color="#3F875F" size="5">image with probability </font> <font color="#6E9E26" size="5"> **{prediction}**</font>', unsafe_allow_html=True)
        
        elif prediction >0.25 and prediction <= 0.45:
            prediction = '{:.4f}'.format(prediction)
            st.markdown(f'<font color="#22568A" size="5">This image seems to be an </font> <font color="#58C3D2" size="5">**AI generated** </font> <font color="#22568A" size="5">image with probability </font> <font color="#58C3D2" size="5"> **{prediction}**</font>', unsafe_allow_html=True)
        
        elif prediction >0.45 and prediction <= 0.70:
            prediction = '{:.4f}'.format(prediction)
            st.markdown(f'<font color="#923B6F" size="5">This image seems to be a </font> <font color="#D01D62" size="5">**Real** </font> <font color="#923B6F" size="5">image with probability </font> <font color="#D01D62" size="5"> **{prediction}**</font>', unsafe_allow_html=True)
        
        else:
            prediction = '{:.4f}'.format(prediction)
            st.markdown(f'<font color="#7C299E" size="5">This image is most likely a </font> <font color="#D058D2" size="5">**Real** </font> <font color="#7C299E" size="5">image with probability </font> <font color="#D058D2" size="5"> **{prediction}**</font>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error("An error occurred during prediction")
        
    st.image(image, use_column_width=True)