import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import tweepy
from api_credentials import *
from data_analysis import perform_topic_modeling, analyze_sentiment_trends, identify_key_influencers
from environmental_impact import calculate_carbon_emissions, estimate_water_consumption, analyze_textile_waste, calculate_microplastic_pollution, generate_environmental_impact_report
from visualization import plot_sentiment_trends, plot_environmental_impact, plot_topic_distribution, plot_key_influencers

def collect_twitter_data():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweets = []
    search_query = "fast fashion OR sustainable fashion"

    for tweet in tweepy.Cursor(api.search_tweets, q=search_query, lang="en", count=200).items(1000):
        tweets.append(tweet._json)

    return pd.DataFrame(tweets)

def collect_facebook_data():
    # TODO: Implement Facebook data collection using Graph API
    pass

def collect_instagram_data():
    # TODO: Implement Instagram data collection
    pass

def clean_data(data):
    # TODO: Implement data cleaning and preprocessing
    # Remove duplicates, handle missing values, and standardize text format
    data = data.drop_duplicates()
    data = data.dropna(subset=['text'])
    # Convert text to lowercase
    data['text'] = data['text'].str.lower()
    return data

def perform_sentiment_analysis(data):
    # TODO: Implement sentiment analysis on social media data
    # Use NLTK or other sentiment analysis libraries
    # Example:
    from nltk.sentiment import SentimentIntensityAnalyzer
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    data['sentiment_scores'] = data['text'].apply(lambda text: sid.polarity_scores(text))
    data['sentiment'] = data['sentiment_scores'].apply(lambda score_dict: 'positive' if score_dict['compound'] >= 0.05 else ('negative' if score_dict['compound'] <= -0.05 else 'neutral'))
    return data

def quantify_environmental_impact(production_data, sales_data, return_data, synthetic_fiber_data):
  
    carbon_emissions = calculate_carbon_emissions(production_data)
    water_consumption = estimate_water_consumption(production_data)
    textile_waste = analyze_textile_waste(sales_data, return_data)
    microplastic_pollution = calculate_microplastic_pollution(synthetic_fiber_data)
    
    report = generate_environmental_impact_report(carbon_emissions.sum(), water_consumption.sum(), textile_waste, microplastic_pollution.sum())
    
    return report

def identify_trends(data):
    lda_model, vectorizer = perform_topic_modeling(data)
    return lda_model, vectorizer

def visualize_results(data, lda_model, env_metrics, sentiment_trends, key_influencers):
    #TODO: change the env_metrics to report.
    plot_sentiment_trends(sentiment_trends)
    #plot_environmental_impact(env_metrics) #env_metrics needs to be a dataframe or dictionary for the plot
    plot_topic_distribution(lda_model, vectorizer)
    plot_key_influencers(key_influencers)


def main():
    nltk.download('stopwords')
    nltk.download('punkt')
    twitter_data = collect_twitter_data()
    #facebook_data = collect_facebook_data()
    #instagram_data = collect_instagram_data()

    all_data = twitter_data #pd.concat([twitter_data, facebook_data, instagram_data])

    cleaned_data = clean_data(all_data)

    sentiment_data = perform_sentiment_analysis(cleaned_data)

    # Dummy data for environmental impact calculation (replace with actual data)
    production_data = pd.DataFrame({'total_production': [1000000, 2000000, 1500000]})
    sales_data = pd.DataFrame({'total_items': [3500000]})
    return_data = pd.DataFrame({'returned_items': [175000]})
    synthetic_fiber_data = pd.DataFrame({'synthetic_production': [1000000, 1500000]})
    
    env_report = quantify_environmental_impact(production_data, sales_data, return_data, synthetic_fiber_data)

    #lda_model, vectorizer = identify_trends(cleaned_data['text']) #This expects just the text
    lda_model, vectorizer = perform_topic_modeling(cleaned_data, n_topics=5)
    sentiment_trends = analyze_sentiment_trends(sentiment_data) #This is also expecting particular inputs
    key_influencers = identify_key_influencers(cleaned_data) #also this
    #TODO: fix those 3 above

    #The following code is not working because a lot of the parameters are just pass
    #visualize_results(cleaned_data, lda_model, env_report, sentiment_trends, key_influencers)
    print(env_report)
    plot_sentiment_trends(cleaned_data)

if __name__ == "__main__":
    main()
