import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from data_retrieval import get_data
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
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
    st.write("**Information about the comments :**")
    #Number comments per hour
    # convert the created to valid time
    def to_valid_time(time: str):
        time = time.split(" ")
        return time[0] + " " + "".join(time[1:])
    df["created"] = pd.to_datetime(df["created"].apply(to_valid_time))
    df["hour"] = df["created"].dt.hour
    comments_by_hour = df.groupby("hour").count()["body"].reset_index()
    fig = px.bar(comments_by_hour,x="hour",y="body",
                 labels={"body" : "Number of comments"},
                 title="Number of Comments by Hour")
    fig.update_layout(xaxis_title='Hour', yaxis_title='Number of Comments')
    st.plotly_chart(fig)
    # word frequency barplot
    df["body"] = df["body"].astype(str)
    all_text = ' '.join(df["body"])
    words = all_text.split()
    word_counts = Counter(words)
    most_common_20 = word_counts.most_common(20)
    word = [word for word, count in most_common_20]
    count = [count for word, count in most_common_20]
    df_most_common = pd.DataFrame({'word': word, 'count': count})
    # Pie plot
    fig = px.pie(df_most_common,names="word",values="count",
                 title="Word Frequencies (pieplot)")
    fig.update_layout(xaxis_title="word",yaxis_title="count")
    st.plotly_chart(fig)
    # barplot
    fig = px.bar(df_most_common, x="word", y="count",
                 title="Word Frequencies (barplot)")
    fig.update_layout(xaxis_title="word", yaxis_title="count")
    st.plotly_chart(fig)
    # Sentiment analysis
    st.write("**Sentiment analysis:**")
    # Instantiate the sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    # Apply sentiment analysis to each comment and calculate sentiment scores
    df['sentiment_score'] = df['body'].apply(
        lambda x: sia.polarity_scores(x)['compound'])
    # Categorize sentiment based on score
    df['sentiment_label'] = df['sentiment_score'].apply(
        lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')
    # Calculate sentiment distribution
    sentiment_counts = df['sentiment_label'].value_counts()
    # Create DataFrame for sentiment distribution
    df_sentiment = pd.DataFrame(
        {'Sentiment': sentiment_counts.index, 'Count': sentiment_counts.values})
    fig = px.pie(df_sentiment, values='Count', names='Sentiment',
                 title='Sentiment Distribution')
    st.plotly_chart(fig)

# Call the welcome container function
welcome_container()
