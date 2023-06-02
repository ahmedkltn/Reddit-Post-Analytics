import streamlit as st
import pandas as pd
import plotly.express as px
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
        df_post_info = pd.read_csv("../data/raw_post_info.csv")
        # Display post information
        st.subheader("Post information:")
        st.divider()
        st.write(f'**Title :** {df_post_info ["Title"].iloc[0]} ')
        st.write(f'**Author :** {df_post_info ["Author"].iloc[0]}')
        st.write(f'**Score :** {df_post_info ["Score"].iloc[0]} ')
        st.write(
            f'**Number of comments :** {df_post_info ["Number of comments "].iloc[0] }')
        df_post_info = pd.read_csv("../data/raw_comments_info.csv")
        visulization_container(df_post_info)
    else:
        st.write("Something went wrong!")
def visulization_container(df):
    st.subheader("Visualizations:")
    st.divider()
    # About the post
    st.write("**Information about the post:**")
    # bar chart on most active participants by comments
    # About redditors 
    st.write("**Information about the redditors:**")
    top_10_active_redditors = df.groupby("author").count()["body"].sort_values()[::-1][:11].reset_index()
    fig = px.bar(top_10_active_redditors,x="author",y="body",
             labels={'author': 'Redditors', 'body': 'Number of comments'},
             title='Top 10 Active Redditors by Number of Comments')
    st.plotly_chart(fig)
    # bar chart on most active participants by score
    top_10_active_redditors = df.groupby("author").sum()["score"].sort_values()[::-1][:11].reset_index()
    fig = px.bar(top_10_active_redditors,x="author",y="score",
                labels={'author': 'Redditors', 'score': 'Score'},
                title='Top 10 Active Redditors by Score')
    st.plotly_chart(fig)


# Call the welcome container function
welcome_container()
