import argparse
from webscraper import get_tweets, TweetSearch
import pandas as pd

def get_users_tweets(search_params, fout, columns, usernames):
    list_df = []
    for user in usernames:
        print(f'user: {user}')
        search_params.username = user
        df = get_tweets(search_params, fout, columns)
        list_df.append(df)
        print(f'Finished scraping {df.shape[0]} tweets for {user}\n')    
    return pd.concat(list_df, ignore_index=True)

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
    parser.add_argument('-ul','--userlist', type=str, help='input filename for username list')
    args = parser.parse_args()

    # input error checking
    if not args.query and not args.username and not args.userlist:
        print('You need to specify at least a --query OR --username argument OR --userlist argument')
        return
    elif args.username and args.userlist:
        print(f'You can only specify either --username {args.username} OR --userlist {args.userlist} BUT NOT BOTH')
        return
    
    # set search parameters and list of usernames
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
    
    print(f'Finished scraping tweets into {filename}')
    return df

if __name__ == '__main__':
    df = main()
    
