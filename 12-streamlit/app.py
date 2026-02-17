"""
What is Streamlit?
Streamlit is the easiest way to turn your Python code into a beautiful interactive web app in minutes — no HTML, no CSS, no JavaScript needed.
You write normal Python code → run one command → boom, you have a live website in your browser.
Perfect for:

data dashboards
machine learning demos
simple tools
sharing your analysis
quick prototypes
"""

import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Python Bootcamp App", page_icon="🚀")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose Demo",
    ["Home", "Data Explorer", "CSV Uploader", "Todo App", "Guess Game"]
)

# home
if page == "Home":
    st.title("🚀 Python Bootcamp Dashboard")
    st.write("Welcome to Streamlit Day")

# data explorer
elif page == "Data Explorer":
    st.title("📊 Simple Data Explorer")

    number = st.slider("Pick a number", 1, 100, 50)
    data = np.random.normal(number, 10, 1000)

    st.write("Histogram")
    st.bar_chart(pd.Series(data).value_counts(bins=20))

# csv uploader
elif page == "CSV Uploader":
    st.title("📁 Upload Your CSV")

    uploaded = st.file_uploader("Choose CSV file", type="csv")

    if uploaded:
        df = pd.read_csv(uploaded)
        st.write("First 5 rows")
        st.dataframe(df.head())

        st.write("Basic Statistics")
        st.write(df.describe())

# todo app
elif page == "Todo App":
    st.title("📝 Todo List")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    task = st.text_input("Add new task")

    if st.button("Add Task"):
        if task:
            st.session_state.tasks.append(task)
            st.success(f"Added: {task}")

    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([8, 2])
        col1.write(t)
        if col2.button("Delete", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

# guess game
elif page == "Guess Game":
    st.title("🎯 Guess My Number")

    secret = 42
    guess = st.number_input("Guess a number 1–100", min_value=1, max_value=100)

    if st.button("Check"):
        if guess == secret:
            st.success("You got it!")
        elif guess < secret:
            st.warning("Too low")
        else:
            st.warning("Too high")




import streamlit as st
import pandas as pd

st.title("📁 Upload Your CSV File")

uploaded_file = st.file_uploader("Choose CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully ✅")

    st.subheader("Preview")
    st.dataframe(df.head())

    st.subheader("Basic Statistics")
    st.write(df.describe())
