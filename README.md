# Twitter Advanced Search

This Python 3 code is a heavily modified version of https://github.com/PJHRobles/Twitter-Get-Old-Tweets-Scraper which was originally based on https://github.com/Jefferson-Henrique/GetOldTweets-python.

## Example
Here is a sample command line which uses most of the available keyword arguments.  
`python twitter_advanced_search.py --query tennis --username nytimes --since 2016-08-01 --until 2016-09-01 --max_tweets 100 --filename sample.txt`

Another similar example using a userlist in lieu of a single user. See example [input userlist file](userlist.txt).  
`python twitter_advanced_search.py --query tennis --since 2016-08-01 --until 2016-09-01 --max_tweets 100 --filename sample.txt --userlist userlist.txt`

Argument|Shorthand|Description|Default|Example
---|:---:|---|:---:|---
--query|-q|query to use||`python twitter_advanced_search.py --query "data science"`
--username|-u|twitter handle||`python twitter_advanced_search.py --username arc_um`
--since|-s|start date||`python twitter_advanced_search.py -q nadal --since 2012-03-14`
--until|-e|end date||`python twitter_advanced_search.py -u rogerfederer --until 2017-08-09`|
--max_tweets|-m|maximum number of tweets to get for each username|20|`python twitter_advanced_search.py -q tennis --max_tweets 100`
--filename|-f|output filename|tweets.txt|`python twitter_advanced_search.py -u mlive --filename output.txt`
--userlist|-ul|input file containing list of usernames||`python twitter_advanced_search.py -ul usernamelist.txt`
--delay|-d|time delay in seconds after each GET request|1.0|`python twitter_advanced_search.py -d 0.8`
--format|-fmt|choose from {tweets, live, realtime}. I honestly do not understand the difference between them.|tweets|`python twitter_advanced_search.py --format tweets`

**Tip:** You have to specify either a `--query` or a `--username` or a `userlist` argument or it will complain.

Here is an example [output file](tweets_collected.tsv) (tab delimited for GitHub).

## Notes
- The file delimiter is `|` to make the data more analysis friendly.
- The program will output how many tweets it has collected so far after every GET request.
- The program scrapes in reverse chronological order.
- It will scrape about 1200 tweets per minute.

## Code Changes
I've made the following changes after cloning the repository:
- exchanged `pyparsing` for `BeautifulSoup`
- exchanged `getopt` for `argparse`
- used `requests` with the `params` argument for clarity
- added *filename, userlist, delay, format* keyword arguments
- added `pandas` for data management and file write
- refactored code
