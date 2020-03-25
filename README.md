# Twitter Advanced Search

This Python 3 code is a heavily modified version of https://github.com/PJHRobles/Twitter-Get-Old-Tweets-Scraper which was originally based on https://github.com/Jefferson-Henrique/GetOldTweets-python.

## Example
Here is a sample command line which uses most of the available keyword arguments.  
`python twitter_advanced_search.py --query tennis --username nytimes --since 2016-08-01 --until 2016-09-01 --max_tweets 100 --filename sample.txt`

Another similar example using a userlist in lieu of a single user. See example [input userlist file](userlist.txt).  
`python twitter_advanced_search.py --query tennis --since 2016-08-01 --until 2016-09-01 --max_tweets 100 --filename sample.txt --userlist userlist.txt`

Argument|Shorthand|Usage
---|:---:|---
--query|-q|`python twitter_advanced_search.py --query "data science"`
--username|-u|`python twitter_advanced_search.py --username arc_um`
--since|-s|`python twitter_advanced_search.py -q nadal --since 2012-03-14`
--until|-e|`python twitter_advanced_search.py -u rogerfederer --until 2017-08-09`
--max_tweets|-m|`python twitter_advanced_search.py -q tennis --max_tweets 100`
--filename|-f|`python twitter_advanced_search.py -u mlive --filename output.txt`
--userlist|-ul|`python twitter_advanced_search.py -ul usernamelist.txt`
--delay|-d|`python twitter_advanced_search.py -d 0.1`

**Tip:** You have to specify either a `--query` or a `--username` or a `userlist` argument or it will complain.

Here is an example [output file](tweets_collected.tsv) (tab delimited for GitHub).

## Notes
- The default number of tweets is 20.
- The default time delay is 0.8s after each GET request.
- The default output filename is *tweets.txt*.
- The file delimiter is `|` to make the data more analysis friendly.
- The program will output how many tweets it has collected so far after every GET request.

## Code Changes
I've made the following changes after cloning the repository:
- exchanged `pyparsing` for `BeautifulSoup`
- exchanged `getopt` for `argparse`
- used `requests` with the `params` argument for clarity
- added *filename* and *userlist* keyword argument
- added `pandas` for data management and file write
- refactored code
