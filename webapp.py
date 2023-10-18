# importing libraries

from ctypes import alignment
from urllib import response
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd
import numpy as np
import re
import os
import string
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from functions import *
import pickle
from functions import custom_input_prediction

# Page title

image = Image.open('images/logo.png')

st.image(image, use_column_width= True)

st.write('''
# Cyberbulling Tweet Analysis App
This app predicts the nature of the tweet into the following Categories.
* Bullying
* Non-Bullying
* Age
* Ethnicity
* Gender
* Not Cyberbullying
* Other Cyberbullying
* Religion
***
''')

# Text Box
st.header('Enter Tweet ')
tweet_input = st.text_area("Tweet Input", height= 150)
print(tweet_input)
st.write('''
***
''')

# print input on webpage
st.header("Entered Tweet text ")
if tweet_input:
    tweet_input
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')

# Output on the page
st.header("Prediction")
if tweet_input:
    prediction = custom_input_prediction(tweet_input)
    # Append the prediction to a CSV file
    data = {'Prediction': [prediction]}
    df = pd.DataFrame(data)
    df.to_csv('predictions.csv', mode='a', header=False, index=False)
    # Read predictions from the CSV file
    predictions_df = pd.read_csv('predictions.csv')
    
    # Calculate the maximum type of cyberbullying
    max_category = predictions_df['Prediction'].value_counts().idxmax()
    max_count = predictions_df['Prediction'].value_counts().max()

    st.write("Category with Maximum Cyberbullying Occurrences:", max_category)
    st.write("Count of Maximum Cyberbullying Occurrences:", max_count)

    if prediction == "Age":
        st.image("images/age_cyberbullying.png",use_column_width= True)
        st.write('''
    ***Age Cyberbullying!***
    ''')
    elif prediction == "Ethnicity":
        st.image("images/ethnicity_cyberbullying.png",use_column_width= True)
        st.write('''
    ***Ethnicity Cyberbullying!***
    ''')
    elif prediction == "Gender":
        st.image("images/gender_cyberbullying.png",use_column_width= True)
        st.write('''
    ***Gender Cyberbullying!***
    ''')
    elif prediction == "Not Cyberbullying":
        st.image("images/not_cyberbullying.png",use_column_width= True)
        st.write('''
    ***Not Cyberbullying!***
    ''')
    elif prediction == "Other Cyberbullying":
        st.image("images/other_cyberbullying.png",use_column_width= True)
        st.write('''
    ***Other Cyberbullying!***
    ''')
    elif prediction == "Religion":
        st.image("images/religion_cyberbullying.png",use_column_width= True)
        st.write('''
    ***Religion Cyberbullying!***
    ''')
    elif prediction == "Bullying":
        st.image("images/bullying.png",use_column_width= True)
        st.write('''
    ***Bullying!***
    ''')
    elif prediction == "Non-Bullying":
        st.image("images/non_bullying.png",use_column_width= True)
        st.write('''
    ***Non-Bullying!***
    ''')
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')

st.write('''***''')

# About section
expand_bar = st.expander("About")
expand_bar.markdown('''
*  **ML CP PROJECT:** CyberBullying Analysis
 Presented by Siddhi,Mrunmayee,Rahul,Rajkumar,Atharva
''')

# importing libraries

# import pandas as pd
# import streamlit as st
# from PIL import Image
# from functions import custom_input_prediction  # Import the custom_input_prediction function

# # Page title
# image = Image.open('images/logo.png')

# st.image(image, use_column_width=True)

# st.write('''
# # Cyberbullying Tweet Analysis App
# This app predicts the nature of the tweet into the following Categories.
# * Bullying
# * Non-Bullying
# * Age
# * Ethnicity
# * Gender
# * Not Cyberbullying
# * Other Cyberbullying
# * Religion
# ***
# ''')

# # Text Box
# st.header('Enter Tweet ')
# tweet_input = st.text_area("Tweet Input", height=150)

# st.write('''
# ***
# ''')

# # print input on the webpage
# st.header("Entered Tweet text ")
# if tweet_input:
#     st.write(tweet_input)  # Change to display the input text
# else:
#     st.write('''
#     ***No Tweet Text Entered!***
#     ''')
# st.write('''
# ***
# ''')

# # Output on the page
# st.header("Prediction")
# if tweet_input:
#     prediction, prediction_counts = custom_input_prediction(tweet_input)

#     st.write("Most Frequent Prediction:", prediction)

#     # Display the counts of all predictions
#     st.write("Prediction Counts:")
#     for category, count in prediction_counts.items():
#         st.write(f"{category}: {count}")

#     # Find the prediction that occurred the maximum number of times
#     most_frequent_prediction = max(prediction_counts, key=prediction_counts.get)
#     st.write("Most Frequent Prediction:", most_frequent_prediction)
#     st.write("Count of Most Frequent Prediction:", prediction_counts[most_frequent_prediction])

#     # Display images based on predictions as you did before
#     if most_frequent_prediction == "Age":
#         st.image("images/age_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Age Cyberbullying!***
#     ''')
#     elif most_frequent_prediction == "Ethnicity":
#         st.image("images/ethnicity_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Ethnicity Cyberbullying!***
#     ''')
#     elif most_frequent_prediction == "Gender":
#         st.image("images/gender_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Gender Cyberbullying!***
#     ''')
#     elif most_frequent_prediction == "Not Cyberbullying":
#         st.image("images/not_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Not Cyberbullying!***
#     ''')
#     elif most_frequent_prediction == "Other Cyberbullying":
#         st.image("images/other_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Other Cyberbullying!***
#     ''')
#     elif most_frequent_prediction == "Religion":
#         st.image("images/religion_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Religion Cyberbullying!***
#     ''')
#     elif most_frequent_prediction == "Bullying":
#         st.image("images/bullying.png", use_column_width=True)
#         st.write('''
#     ***Bullying!***
#     ''')
#     elif most_frequent_prediction == "Non-Bullying":
#         st.image("images/non_bullying.png", use_column_width=True)
#         st.write('''
#     ***Non-Bullying!***
#     ''')
# else:
#     st.write('''
#     ***No Tweet Text Entered!***
#     ''')

# st.write('''***''')

# # About section
# expand_bar = st.expander("About")
# expand_bar.markdown('''
# *  **ML CP PROJECT:** CyberBullying Analysis
#  Presented by Siddhi, Mrunmayee, Rahul, Rajkumar, Atharva
# ''')
# import streamlit as st
# from PIL import Image
# from functions import custom_input_prediction  # Import the custom_input_prediction function

# # Page title
# image = Image.open('images/logo.png')

# st.image(image, use_column_width=True)

# st.write('''
# # Cyberbullying Tweet Analysis App
# This app predicts the nature of the tweet into the following Categories.
# * Bullying
# * Non-Bullying
# * Age
# * Ethnicity
# * Gender
# * Not Cyberbullying
# * Other Cyberbullying
# * Religion
# ***
# ''')

# # Text Box
# st.header('Enter Tweet ')
# tweet_input = st.text_area("Tweet Input", height=150)

# st.write('''
# ***
# ''')

# # print input on the webpage
# st.header("Entered Tweet text ")
# if tweet_input:
#     st.write(tweet_input)  # Change to display the input text
# else:
#     st.write('''
#     ***No Tweet Text Entered!***
#     ''')
# st.write('''
# ***
# ''')

# # Output on the page
# st.header("Prediction")
# if tweet_input:
#     prediction, max_category, max_count = custom_input_prediction(tweet_input)

#     st.write("Most Frequent Prediction:", prediction)

#     # Display the counts of all predictions
#     st.write("Category with Maximum Cyberbullying Occurrences:", max_category)
#     st.write("Count of Maximum Cyberbullying Occurrences:", max_count)

#     # Display images based on predictions
#     if max_category == "Age":
#         st.image("images/age_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Age Cyberbullying!***
#     ''')
#     elif max_category == "Ethnicity":
#         st.image("images/ethnicity_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Ethnicity Cyberbullying!***
#     ''')
#     elif max_category == "Gender":
#         st.image("images/gender_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Gender Cyberbullying!***
#     ''')
#     elif max_category == "Not Cyberbullying":
#         st.image("images/not_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Not Cyberbullying!***
#     ''')
#     elif max_category == "Other Cyberbullying":
#         st.image("images/other_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Other Cyberbullying!***
#     ''')
#     elif max_category == "Religion":
#         st.image("images/religion_cyberbullying.png", use_column_width=True)
#         st.write('''
#     ***Religion Cyberbullying!***
#     ''')
#     elif max_category == "Bullying":
#         st.image("images/bullying.png", use_column_width=True)
#         st.write('''
#     ***Bullying!***
#     ''')
#     elif max_category == "Non-Bullying":
#         st.image("images/non_bullying.png", use_column_width=True)
#         st.write('''
#     ***Non-Bullying!***
#     ''')
# else:
#     st.write('''
#     ***No Tweet Text Entered!***
#     ''')

# st.write('''***''')

# # About section
# expand_bar = st.expander("About")
# expand_bar.markdown('''
# *  **ML CP PROJECT:** CyberBullying Analysis
#  Presented by Siddhi, Mrunmayee, Rahul, Rajkumar, Atharva
# ''')
