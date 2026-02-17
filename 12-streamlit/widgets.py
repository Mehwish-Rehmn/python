''' What are widgets in Streamlit?

Widgets = interactive things you put in your app so users can click, type, choose, slide, upload, etc.  
Streamlit makes them dead easy — just one line of code, and they update the app automatically when changed.

Every time a widget changes, the whole script reruns from top to bottom (Streamlit magic — called “rerun on interaction”).
'''
### Most common widgets with super easy examples

# Create a file `widgets.py` and run `streamlit run widgets.py`

# 1. Text input
import streamlit as st

name = st.text_input("what's your name?")
if name:
    st.write(f"hello {name}!")

# 2. Number input & slider
age = st.number_input("enter your age", min_value=1, max_value=120, value=25)
st.write(f"you are {age} years old")

level = st.slider("difficulty level", 1, 10, 5)
st.write(f"level set to {level}")


#3. Button
if st.button("click me"):
    st.balloons()
    st.success("you clicked!")


#4. Checkbox
dark_mode = st.checkbox("dark mode")
if dark_mode:
    st.write("dark mode on")
else:
    st.write("light mode")


#5. Selectbox / Radio / Multiselect
city = st.selectbox("choose city", ["delhi", "mumbai", "bangalore", "chennai"])
st.write(f"you picked {city}")

fruit = st.radio("favorite fruit", ["apple", "banana", "mango"])
st.write(f"you love {fruit}")

hobbies = st.multiselect("hobbies", ["reading", "coding", "music", "sports"])
st.write(f"your hobbies: {', '.join(hobbies)}")


# 6. File uploader
uploaded = st.file_uploader("upload a csv", type="csv")
if uploaded:
    st.write("file uploaded!")
    # you can read it with pandas later


# 7. Date picker
birthday = st.date_input("your birthday")
st.write(f"happy birthday on {birthday}")


# 8. Color picker
color = st.color_picker("pick a color", "#ff0000")
st.write(f"you chose {color}")
st.markdown(f"<div style='background-color:{color}; width:100px; height:100px;'></div>", unsafe_allow_html=True)


# practice 
import streamlit as st

st.title("my profile form")

name = st.text_input("name")
age = st.slider("age", 10, 60, 25)
city = st.selectbox("city", ["delhi", "mumbai", "bangalore"])
hobby = st.multiselect("hobbies", ["reading", "coding", "gaming"])

if st.button("show profile"):
    st.write(f"name: {name}")
    st.write(f"age: {age}")
    st.write(f"city: {city}")
    st.write(f"hobbies: {', '.join(hobby)}")
