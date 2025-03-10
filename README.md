# Environmental Impact Analysis of Fast Fashion using Social Media Data

## Description

This project analyzes the environmental impact of fast fashion by leveraging social media data and advanced analytics techniques. It aims to quantify the industry's effect on carbon emissions, water consumption, and textile waste while identifying emerging trends in sustainable fashion.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
    - [Data Collection](#data-collection)
    - [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
    - [Sentiment Analysis](#sentiment-analysis)
    - [Environmental Impact Quantification](#environmental-impact-quantification)
    - [Trend Identification](#trend-identification)
- [Results](#results)
- [Visualization](#visualization)
    - [Sentiment Analysis Visualization](#sentiment-analysis-visualization)
    - [Environmental Impact Visualization](#environmental-impact-visualization)
    - [Key Influencers Visualization](#key-influencers-visualization)
    - [Topics Visualization](#topics-visualization)
- [Future Work](#future-work)
- [Contributing](#contributing)

## Installation

1.  Clone the repository:

git clone <https://github.com/yourusername/FastFashionImpact.git>

2.  Navigate to the project directory:

cd FastFashionImpact

3.  Create a virtual environment:

python -m venv env

4.  Activate the virtual environment:

\*   On Windows:

env\\Scripts\\activate

\*   On macOS and Linux:

source env/bin/activate

5.  Install the required dependencies:

pip install -r requirements.txt

## Usage

1.  Set the required environment variables

TWITTER_API_KEY
TWITTER_API_SECRET
TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET

2.  Run the main script:

python fast_fashion_analysis.py

## Data Sources

This project uses the following data sources:

*   Twitter API: For collecting tweets related to fast fashion and sustainability.

## Methodology

### Data Collection

The project collects data from social media platforms using the Twitter API. The collected data includes tweets related to fast fashion and sustainability.

### Data Cleaning and Preprocessing

The collected data is cleaned and preprocessed to remove duplicates, handle missing values, and standardize text format. The following steps are performed:

1.  Removal of duplicates

2.  Handling missing values

3.  Standardizing text format

4.  Removing punctuation, numbers, URLs, and stopwords

### Sentiment Analysis

The preprocessed data is analyzed for sentiment using NLTK's SentimentIntensityAnalyzer. The sentiment of each tweet is categorized as positive, negative, or neutral.

### Environmental Impact Quantification

The environmental impact of fast fashion is quantified using industry reports and scientific studies. The following metrics are calculated:

1.  Carbon emissions

2.  Water consumption

3.  Textile waste

4.  Microplastic pollution

### Trend Identification

Trends in sustainable fashion and consumer behavior are identified using topic modeling with Latent Dirichlet Allocation (LDA). The number of topics is set to 5.

## Results

The results of the analysis will be presented in the following sections.

## Visualization

The project includes several visualizations to present the results of the analysis.

### Sentiment Analysis Visualization

The distribution of sentiments is visualized using a histogram. The histogram shows the number of tweets with positive, negative, and neutral sentiments.

### Environmental Impact Visualization

The environmental impact metrics are visualized using a bar chart. The bar chart shows the carbon emissions, water consumption, textile waste, and microplastic pollution associated with fast fashion.

### Key Influencers Visualization

The top 10 key influencers are visualized using a bar chart. The bar chart shows the total engagement (retweets + likes) for each influencer.

### Topics Visualization

The top topics are visualized using bar charts.

## Future Work

The project can be extended in the following ways:

1.  Implement data collection from Facebook and Instagram
2.  Refine topic modeling and key influencer identification
3.  Create interactive dashboards

## Contributing

Contributions to this project are welcome. Please submit a pull request with your proposed changes.
