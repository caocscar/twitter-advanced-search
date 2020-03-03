import argparse
from webscraper import TweetSearch, get_users_tweets
import pandas as pd  

def main():
        
    description = '''
    Twitter Scraper for CSCAR.
    '''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-q','--query', type=str, help='twitter query')
    parser.add_argument('-u','--username', type=str, help='twitter username')
    parser.add_argument('-s','--since', type=str, help='start date in UTC')
    parser.add_argument('-e','--until', type=str, help='end date in UTC')
    parser.add_argument('-m','--max_tweets', type=int, default=20, help='maximum number of tweets in reverse chronological order')
    parser.add_argument('-f','--filename', type=str, default='tweets_collected.txt', help='output filename')
    parser.add_argument('-ul','--userlist', type=str, help='input filename for username list')
    args = parser.parse_args()

    # debugging purposes
    args.query = 'tennis'
    args.since = '2016-08-01'
    args.until = '2016-09-01'
    args.max_tweets = 100
    args.filename = 'sample.txt'
    args.userlist = 'userlist.txt'
    # input error checking
    if not args.query and not args.username and not args.userlist:
        print('You need to specify at least a --query OR --username argument OR --userlist argument')
        return
    elif args.username and args.userlist:
        print(f'You can only specify either --username {args.username} OR --userlist {args.userlist} BUT NOT BOTH')
        return
    
    # set search parameters and list of usernames
    search_params = TweetSearch()
    if args.query:
        search_params.query = args.query
    if args.since:
        search_params.since = args.since
    if args.until:
        search_params.until = args.until
    if args.userlist:
        df = pd.read_csv(args.userlist, header=None)
        usernames = df[0]
    else:
        usernames = [args.username]
        
    search_params.max_tweets = args.max_tweets
    filename = args.filename

    # iterate through list of users
    with open(filename, 'w', encoding='utf-8') as fout:
        columns = ['id','timestamp','name','retweets','favorites','text']
        fout.write('{}\n'.format('|'.join(columns)) )
        df = get_users_tweets(search_params, fout, columns, usernames)
        df.columns = columns
    
    print(f'Finished scraping tweets into {filename}')
    return df

if __name__ == '__main__':
    data = main()
    
