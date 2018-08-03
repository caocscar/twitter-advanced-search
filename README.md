# Twitter Advanced Search

This Python 3 code is a port of https://github.com/PJHRobles/Twitter-Get-Old-Tweets-Scraper which is originally based on https://github.com/Jefferson-Henrique/GetOldTweets-python

I've made the following changes:
- exchanged `pyparsing` for `BeautifulSoup`
- exchanged `getopt` for `argparse`
- added `pandas` for data management and file write
- refactored code
- added *filename* argument

## Example
Here is a sample command line which uses all the available keyword arguments.  
`python twitter_advanced_search.py --query tennis --username nytimes --since 2016-08-01 --until 2016-09-01 --max_tweets 100 --filename sample.txt`

Argument|Shorthand|Usage
---|:---:|---
--query|-q|`python twitter_advanced_search.py --query "data science"`
--username|-u|`python twitter_advanced_search.py --username arc_um`
--since|-s|`python twitter_advanced_search.py -q nadal --since 2012-03-14`
--until|-e|`python twitter_advanced_search.py -u rogerfederer --until 2017-08-09`
--max_tweets|-m|`python twitter_advanced_search.py -q tennis --max_tweets 100`
--filename|-f|`python twitter_advanced_search.py -u mlive --filename output.txt`

**Tip:** You have to specify either a `--query` or a `--username` argument or it will complain.

## Notes
- The default number of tweets to collect is 20.
- The default delimiter is `|` to make the data more analysis friendly
