import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import re

def create_query(search_params):
    query_parameters = []
    if hasattr(search_params, 'query'):
        query_parameters.append(search_params.query)   
    if hasattr(search_params, 'username'):
        query_parameters.append(f'from:{search_params.username}')        
    if hasattr(search_params, 'since'):
        query_parameters.append(f'since:{search_params.since}')
    if hasattr(search_params, 'until'):
        query_parameters.append(f'until:{search_params.until}')    
    return ' '.join(query_parameters)
    
def get_json_response(search_params, refresh_cursor):
    headers = {
        'Host': 'twitter.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive'
    }
    query = create_query(search_params)         
    params = {'f': 'realtime',
              'src': 'typd',
              'lang': 'en-US',
              'q': query,
              'max_position': refresh_cursor,
              }           
    url = 'https://twitter.com/i/search/timeline'
    R = requests.get(url, params=params, headers=headers)
    R.raise_for_status()
    
    return R.json()

def parse_tweet(tweet):
    regex_text = re.compile("TweetTextSize js-tweet-text .+")
    tweetid = tweet['data-tweet-id']
    username = tweet['data-name']
    text = tweet.find('p', class_ = regex_text).text.replace('\n',' ')
    span_retweet = tweet.find('span', class_ = "ProfileTweet-action--retweet")
    retweets = int(span_retweet.text.replace(',','').strip('\n').split()[0])
    span_favs = tweet.find('span', class_ = "ProfileTweet-action--favorite")
    favorites = int(span_favs.text.replace(',','').strip('\n').split()[0])
    span_timestamp = tweet.find('span', class_ = 'js-short-timestamp')
    raw_date_ms = int(span_timestamp['data-time'])
    timestamp = datetime.fromtimestamp(raw_date_ms).strftime('%Y-%m-%d %H:%M:%S')
    return (tweetid, timestamp, username, retweets, favorites, text)

def get_tweets(search_params, fout, columns):

    if search_params.max_tweets <= 0:
        return

    active = True
    refresh_cursor = ''
    counter = 0
    
    regex_tweet = re.compile("tweet js-stream-tweet .+")

    list_df = []

    while active:
        response = get_json_response(search_params, refresh_cursor)

        if not response or len(response['items_html'].strip()) == 0:
            break
        refresh_cursor = response['min_position']
        html = response['items_html']                  
        soup = BeautifulSoup(html, 'html.parser')       
        tweets = soup.find_all('div', class_ = regex_tweet)
        if len(tweets) == 0:
            break
           
        data = []
        for n, tweet in enumerate(tweets, start=counter+1):
            data.append(parse_tweet(tweet))
            if n >= search_params.max_tweets:
                active = False
                break

        df = pd.DataFrame(data, columns=columns)
        df.to_csv(fout, sep='|', index=False, header=False, line_terminator='\n')
        counter = n
        print('{} tweets collected'.format(counter))
        list_df.append(df)

    return pd.concat(list_df, ignore_index=True) if list_df else pd.DataFrame()


class TweetSearch(object):

    def __init__(self):
        self.max_tweets = 20

    def set_username(self, username):
        self.username = username
        return self

    def set_since(self, since):
        self.since = since
        return self

    def set_until(self, until):
        self.until = until
        return self

    def set_query(self, query):
        self.query = query
        return self

    def set_max_tweets(self, max_tweets):
        self.max_tweets = max_tweets
        return self
