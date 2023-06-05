# Reddit Post Analytics

Reddit Post Analytics is a web application that allows users to gain valuable insights and visualizations for any Reddit post. By simply entering the URL of a Reddit post, the app analyzes its comments, extracts important information, and generates visualizations to help users understand the post's engagement and community sentiments.

## Features

- **Post Information**: The app displays the title, author, score, and number of comments for the given Reddit post.
- **Active Redditors**: Visualizes the top 10 active redditors by the number of comments and score.
- **Comments Analysis**: Provides visualizations such as the number of comments by hour and word frequency analysis.
- **Sentiment Analysis**: Performs sentiment analysis on the comments and presents a pie chart showing the sentiment distribution.
## Preview
![gif-preview](https://github.com/ahmedkltn/Reddit-Post-Analytics/assets/88550715/aa367965-c4ab-422d-b28e-aaa963ae9752)
## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/ahmedkltn/Reddit-Post-Analytics.git
    ```
    
- Navigate to the project directory:
    
    ```bash
    cd reddit-post-analytics
    ```
    
- Install the required dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    

## Usage

1. Run the Streamlit web app:
    
    ```
    streamlit run app.py
    ```
    
2. Access the app in your web browser at `http://localhost:8501`.
3. Enter the URL of a Reddit post in the provided text input and click the **Search** button.
4. View the post information, visualizations, and sentiment analysis results.

## Technologies Used

- Streamlit: Python library for building interactive web applications.
- pandas: Data manipulation and analysis library.
- Matplotlib: Plotting library for creating static, animated, and interactive visualizations.
- Plotly Express: High-level data visualization library based on Plotly.
- NLTK: Natural Language Toolkit library for sentiment analysis.
- PRAW: Python wrapper for the Reddit API.

## Prerequisites

Before running the Reddit Post Analytics web app, you'll need to set up your credentials for the Reddit API. Follow the steps below:

1. Create a Reddit account if you don't already have one.
2. Go to the [Reddit App Preferences](https://www.reddit.com/prefs/apps) page and click on the **Create App** or **Create Another App** button.
3. After creating the app, you'll see the **client ID** and **client secret**. Open the `credentials.json` file in the project directory and input the `client_id` and `client_secret` values from the created app. The `credentials.json` file should look like this:

```json
{
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}
```

Replace `YOUR_CLIENT_ID` with the client ID obtained from the Reddit App Preferences page, and `YOUR_CLIENT_SECRET` with the client secret.
