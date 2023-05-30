import streamlit as st
import pandas as pd
from data_retrieval import get_data

# Title and introduction
st.title("Reddit Post Analytics")
st.write("The Reddit Post Analytics web app allows you to gain valuable insights and visualizations for any Reddit post. Simply enter the URL of a Reddit post, and our app will analyze its comments, extract important information, and generate visualizations to help you understand the post's engagement and community sentiments.")

# Welcome container


def welcome_container():
    post_url = st.text_input('Enter post URL:')
    submit = st.button('Search', key='submit')
    if submit:
        post_info(post_url)


def post_info(post_url):
    with st.spinner("Analyzing the post..."):
        is_data_exist = get_data(post_url)
    if is_data_exist:
        df = pd.read_csv("../data/raw_post_info.csv")

        # Display post information
        st.subheader("Post information:")
        st.divider()
        st.write(f'**Title :** {df["Title"].iloc[0]} ')
        st.write(f'**Author :** {df["Author"].iloc[0]}')
        st.write(f'**Score :** {df["Score"].iloc[0]} ')
        st.write(
            f'**Number of comments :** {df["Number of comments "].iloc[0] }')
    else:
        st.write("Something went wrong!")


# Call the welcome container function
welcome_container()
