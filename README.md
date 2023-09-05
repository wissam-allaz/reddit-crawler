# reddit-crawler
This python program scrapes reddit poll threads and generates a stylish image to represent the poll picks stylishly
## Summary
This Python project is designed to scrape the top comments from two Reddit threads discussing a poll for the most voted woman author of fictional books. It consists of three main components: RedditScraper.py, DataCleaning.py, and GeneratrCloudImg.py.

## Project Composition
1. RedditScraper.py
Description:

RedditScraper.py is the core component of this project, responsible for scraping the top comments from the specified Reddit threads. It utilizes the PRAW (Python Reddit API Wrapper) library to interact with Reddit's API and extract comments.

Usage: RedditScraper.py is used to collect top comments from Reddit threads related to the woman author poll.

Ensure you have PRAW installed (you can install it using pip install praw).
Set up a Reddit API application and obtain the necessary credentials (client ID, client secret, user agent).
Configure the script with your credentials and specify the target Reddit threads.
Run the script to scrape top comments and store them in a data file.

2. DataCleaning.py
Description:

DataCleaning.py is responsible for cleaning and preprocessing the scraped comment data. It may include tasks like removing duplicates, handling missing values, and performing any necessary text preprocessing (e.g., removing special characters, stemming, or lemmatizing).

Usage: DataCleaning.py takes the raw scraped data as input and produces clean, structured comment data.

Configure the script to read the raw scraped data.
Implement the required data cleaning steps, ensuring that the data is ready for analysis.
Run the script to obtain clean comment data.

3. GeneratrCloudImg.py
Description:

GeneratrCloudImg.py generates a word cloud image from the cleaned comment data. Word clouds provide a visual representation of the most frequently occurring words in the comments, helping to identify popular topics or trends in the discussion.

Usage: GeneratrCloudImg.py creates a word cloud image based on the cleaned comment data.

Configure the script to read the cleaned comment data.
Customize the word cloud settings, such as color schemes and fonts, as needed.
Run the script to generate and save the word cloud image.

## Requirements
Python 3.x

PRAW library (for Reddit API access)

Any additional libraries required for data cleaning or word cloud generation (specified within the scripts)
