import streamlit as st
import random

st.title("Greetings")

st.sidebar.header("Name")

name = st.text_input("Enter your name: ")

def greetings_function(name):
    list_greeting = ["Hi", "What's up,", "How are you,"]
    chosen_greeting = random.choice(list_greeting)
    full_greeting = chosen_greeting + " " + name
    return full_greeting

if st.button("Output Greeting"):
    full_greeting = greetings_function(name)
    st.write(f"Output: {full_greeting}")
