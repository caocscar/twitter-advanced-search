import argparse
from webscraper import get_tweets, TweetSearch

def main():
    
    search_params = TweetSearch()
    
    description = '''
    Twitter Scraper for CSCAR.
    '''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-q','--query', type=str, help='twitter query')
    parser.add_argument('-u','--username', type=str, help='twitter username')
    parser.add_argument('-s','--since', type=str, help='start date in UTC')
    parser.add_argument('-e','--until', type=str, help='end date in UTC')
    parser.add_argument('-m','--max_tweets', type=int, default=search_params.max_tweets, help='maximum number of tweets in reverse chronological order')
    parser.add_argument('-f','--filename', type=str, default='tweets_collected.txt', help='output filename')
    args = parser.parse_args()

    if not args.query and not args.username:
        print('You need to specify at least a --query OR --username argument')
        return

    if args.query:
        search_params.query = args.query
    if args.username:
        search_params.username = args.username
    if args.since:
        search_params.since = args.since
    if args.until:
        search_params.until = args.until
    if args.max_tweets:
        search_params.max_tweets = args.max_tweets
    if args.filename:
        filename = args.filename
    
    df = get_tweets(search_params, filename)
    print('Finished scraping tweets into {}'.format(filename) )
    return df

if __name__ == '__main__':
    df = main()
    
