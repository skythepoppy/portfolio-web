import streamlit as st
import pandas

col3, empty_col, col4 = st.columns([1.5 , 0.5 , 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:8].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Github Repo]({row['url']})")


with col4:
    for index, row in df[8:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Github Repo]({row['url']})")


