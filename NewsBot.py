import requests
import streamlit as st
# Function to fetch news based on category
def fetch_news(category, api_key):
    if category == "Indian News":
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    elif category == "BBC News":
        url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}"
    elif category == "Hacker News":
        url = f"https://newsapi.org/v2/top-headlines?sources=hacker-news&apiKey={api_key}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&q={category.lower()}"
    
    response = requests.get(url)
    data = response.json()
    return data.get("articles", [])

# Streamlit app
def main():
    st.title("Top News Bot Headlines")

    st.sidebar.title("News Options")
    api_key = "b7175abb766646199d8a2f07553a7a00"
    category = st.sidebar.selectbox("Select News Category", ("Indian News", "BBC News", "Hacker News", "Sports", "Technology", "Science", "Health", "Entertainment"))
    
    if st.sidebar.button("Get News"):
        news_articles = fetch_news(category, api_key)
        
        if news_articles:
            for article in news_articles:
                st.subheader(article['title'])
                
                st.write(article['content'])
                
                st.markdown(f"[Read more...]({article['url']})")
                
        else:
            st.write("No news found for this category.")

if __name__ == "__main__":
    main()
