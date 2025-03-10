import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud

def plot_sentiment_trends(sentiment_data):
    try:
        if isinstance(sentiment_data, pd.DataFrame):
            # Plotting the distribution of sentiment scores
            plt.figure(figsize=(10, 6))
            sns.histplot(sentiment_data['sentiment'], discrete=True, kde=False)
            plt.title('Distribution of Sentiments')
            plt.xlabel('Sentiment')
            plt.ylabel('Number of Tweets')
            plt.savefig('sentiment_distribution.png')
            plt.close()
        else:
            print("Invalid sentiment data format for plotting.")
    except Exception as e:
        print(f"Error plotting sentiment distribution: {e}")

def plot_environmental_impact(env_report):
    try:
        # Extract the numeric values from the report
        carbon_emissions = float(env_report.split('Carbon Emissions: ')[1].split(' tons CO2e')[0])
        water_consumption = float(env_report.split('Water Consumption: ')[1].split(' cubic meters')[0])
        textile_waste = float(env_report.split('Textile Waste: ')[1].split(' tons')[0])
        microplastic_pollution = float(env_report.split('Microplastic Pollution: ')[1].split(' tons')[0])
        #chemical_usage = float(env_report.split('Chemical Usage: ')[1].split(' kg')[0])

        # Prepare the data for the bar chart
        metrics = ['Carbon Emissions', 'Water Consumption', 'Textile Waste', 'Microplastic Pollution']
        values = [carbon_emissions, water_consumption, textile_waste, microplastic_pollution]

        # Create a bar chart
        plt.figure(figsize=(12, 6))
        sns.barplot(x=metrics, y=values)
        plt.title('Environmental Impact Metrics')
        plt.xlabel('Metrics')
        plt.ylabel('Value')
        plt.savefig('environmental_impact.png')
        plt.close()

    except Exception as e:
        print(f"Error plotting environmental impact: {e}")

def plot_topic_distribution(lda_model, vectorizer, data):
    try:
        # Get feature names (words)
        feature_names = vectorizer.get_feature_names_out()

        # For each topic, plot the top words
        for topic_idx, topic in enumerate(lda_model.components_):
            top_words_idx = topic.argsort()[-10:]  # Get the indices of the top 10 words
            top_words = [feature_names[i] for i in top_words_idx]
            top_values = [topic[i] for i in top_words_idx]
        
            # Combine words and their weights into a dictionary
            word_weights = dict(zip(top_words, top_values))
        
            # Create a WordCloud object
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_weights)

            # Display the generated image:
            plt.figure(figsize=(10, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.title(f'Topic {topic_idx + 1} - Word Cloud')
            plt.tight_layout()
            plt.savefig(f'topic_{topic_idx + 1}_wordcloud.png')
            plt.close()
    except Exception as e:
        print(f"Error plotting topic distribution: {e}")

def plot_key_influencers(influencer_data):
    try:
        if isinstance(influencer_data, pd.DataFrame):
            plt.figure(figsize=(12, 6))
            sns.barplot(x=influencer_data.index, y=influencer_data['total_engagement'])
            plt.title('Top 10 Key Influencers')
            plt.xlabel('Influencer')
            plt.ylabel('Total Engagement')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig('key_influencers.png')
            plt.close()
        else:
            print("Invalid influencer data format for plotting.")
    except Exception as e:
        print(f"Error plotting key influencers: {e}")
