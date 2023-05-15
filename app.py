import streamlit as st
import pandas as pd
import time

# ******************************Text Utility************************
st.title('Startup Dashboard')   # prints the title of the website
st.header('Learning Streamlit')    # prints header 
st.subheader('I am Rajat Bahuguna')     # prints subheader


st.write('This is a normal text')        # prints paragraphs

st.markdown("""                     
### My Favourite Movies
- Pusuits of happiness
- Matrix
""")                           # Makes a list and more, look for markdown guide


st.code("""
def foo(input):
    return foo**2
    
x = foo(2)
""")                          # Shows code blocks


st.latex('x^2+y^2+2 = 0')            # Makes latex symbols, great for writing equations


# ******************************Display elements************************

df = pd.DataFrame({                           # Define a dataframe
    'name':['Ankit', 'kartik', 'Rick'],
    'marks':[50, 60, 70],
    'package':[10, 12, 14]})

st.dataframe(df)                        # prints df on website


st.metric('Revenue', 'Rs 3 lakhs', '-3%')  # Name, Value, if positive: shows green, if negative: shows red on webpage

st.json({                           # printing JSON on web app
    'name':['Ankit', 'kartik', 'Rick'],
    'marks':[50, 60, 70],
    'package':[10, 12, 14]})

# ******************************Displaying media************************
st.image('unnamed.jpg')        # loads image
# st.video('video_name.mp4')       # loads video
# st.audio('audio_name.mp4')       # loads audio

# ******************************Creating Layouts************************
st.sidebar.title('Sidebar kaa title')     # Creates sidebar and you can toggle beteween the full view and sidebar view

col1, col2 = st.columns(2)         # Gives 2 column objects

with col1:                          # Image on left
    st.image('unnamed.jpg')
    
with col2:                          # Image on right
    st.image('unnamed.jpg')

# ******************************Showing status************************
    
st.error('Login Failed')       # Gives error msg
st.success('Login passed')       # Gives success msg
st.info('Login Failed')       # Gives information
st.warning('Login passed')       # Gives warning


## Progress bar
bar = st.progress(0)           # Can be used for file uploading

for i in range(101):
    time.sleep(0.001)
    bar.progress(i)

#******************************Taking user input************************
# Text input --> Number input --> Number input --> Date Input

email = st.text_input('Enter email')        # Taking text input from the user
age = st.number_input('Enter age')        # Taking number input from the user
date = st.date_input('Enter registration input')        # Taking date from the user


# Buttons --> baloons
# Let us use what we have learned above
e_mail = st.text_input('Enter your email')  
password = st.text_input('Enter password')
gender = st.selectbox('Select gender', ['male', 'female', 'others'])   # Makes a select box

button = st.button('Login')            # Creates button

if button:           # IF button is clicked only then the loop runs
    if e_mail == 'Rajatbahuguna4445@gmail.com' and password == '1234':
        st.success('Login Successful')
        st.write(gender)                   # Prints out the gender also
        st.balloons()                       # Brings out balloons!!!!
    else:
        st.error('Login Failed')
        
#******************************File Uploader************************
file = st.file_uploader('Upload a csv file')  

if file is not None:        # If the file is available
    df = pd.read_csv(file)            # Read the file and store it in df
    st.dataframe(df.describe())        # Now print the output of the describe function on the web app
        
        
        







