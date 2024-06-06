# Neural-Classifier
This streamlit based Web app checks if a image is AI generated or Real. We trained VGG16 model on 300 X 300 X 3 dimensional 9000 AI generated
and 5000 Real images using feature extraction transfer learning to classify images into two categories(AI generated, Real).

## Installation

To install the necessary dependencies, follow these steps:

1. Clone this repository in your machine.
2. Navigate to the project directory.
3. Install all the dependencies listed in the `requirements.txt` file:

<pre> pip install -r requirements.txt </pre>


## Usage

To run the image classifier application, use the following command:

<pre> streamlit run classifier.py </pre>


This will start the Streamlit application on localhost, and you can access it in your web browser.

Once web app is running on your localhost:

1. Select an image by clicking on the "Browse Files" button.
2. Model will predict image category.
3. The application will display the uploaded image along with the prediction result.
