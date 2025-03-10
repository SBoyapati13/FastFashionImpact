import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import tweepy
from api_credentials import *
from data_analysis import perform_topic_modeling, analyze_sentiment_trends, identify_key_influencers
from environmental_impact import calculate_carbon_emissions, estimate_water_consumption, analyze_textile_waste, calculate_microplastic_pollution, generate_environmental_impact_report, estimate_landfill_usage
from visualization import plot_sentiment_trends, plot_environmental_impact, plot_topic_distribution, plot_key_influencers
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

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
    # Remove duplicates, handle missing values, and standardize text format
    data = data.drop_duplicates()
    data = data.dropna(subset=['text'])

    # Convert text to lowercase
    data['text'] = data['text'].str.lower()

    # Remove punctuation
    data['text'] = data['text'].str.replace('[^\w\s]','')

    # Remove numbers
    data['text'] = data['text'].str.replace('\d','')

    # Remove URLs
    data['text'] = data['text'].str.replace('http\S+|www.\S+', '', case=False)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

    return data

def perform_sentiment_analysis(data):
    sid = SentimentIntensityAnalyzer()
    data['sentiment_scores'] = data['text'].apply(lambda text: sid.polarity_scores(text))
    data['sentiment'] = data['sentiment_scores'].apply(lambda score_dict: 'positive' if score_dict['compound'] >= 0.05 else ('negative' if score_dict['compound'] <= -0.05 else 'neutral'))
    return data

def quantify_environmental_impact(production_data, sales_data, return_data, synthetic_fiber_data):
    carbon_emissions = calculate_carbon_emissions(production_data)
    water_consumption = estimate_water_consumption(production_data)
    textile_waste = analyze_textile_waste(sales_data, return_data)
    microplastic_pollution = calculate_microplastic_pollution(synthetic_fiber_data)
    landfill_usage = estimate_landfill_usage(sales_data, return_data)


    report = generate_environmental_impact_report(carbon_emissions.sum(), water_consumption.sum(), textile_waste.sum(), microplastic_pollution.sum(), landfill_usage)

    return report

def identify_trends(data):
    lda_model, vectorizer = perform_topic_modeling(data, n_topics=5)
    return lda_model, vectorizer

def visualize_results(sentiment_data, lda_model, vectorizer, env_report, influencer_data):
    plot_sentiment_trends(sentiment_data)
    plot_environmental_impact(env_report)
    plot_topic_distribution(lda_model, vectorizer, sentiment_data)  #To do: Implement and provide right inputs
    plot_key_influencers(influencer_data)

def main():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('vader_lexicon') #ADDED: need this for the sentiment intesity analyser to work properly
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

    lda_model, vectorizer = identify_trends(cleaned_data)

    #This is expecting particular inputs, i am sending the cleaned data frame so it doesnt break
    #plot_sentiment_trends(sentiment_data) #Something with the plot sentitment is not working properly

    influencer_data = identify_key_influencers(cleaned_data)

    #The following code is not working because a lot of the parameters are just pass
    visualize_results(sentiment_data, lda_model, vectorizer, env_report, influencer_data)
    print(env_report)

if __name__ == "__main__":
    main()
