import praw
import datetime
bot = praw.Reddit(user_agent='WhyNot Mortyy only post v0.1',
                  client_id='7C6e4AzK9fcKQw',
                  client_secret='gP22anUSCpVkksfHhWv-oSICBJA',
                  username='causeWhyNotMorty',
                  password='asdfasdf')
subreddit = bot.subreddit('all')
comments = subreddit.stream.comments()

while 1<2:
        for comment in comments:
                try:
                                text = comment.body
                                if 'why did you' in text.lower() and 'you not' not in text.lower() and  len(text)<300 and author != 'causeWhyNotMorty':
                                        message='[*cause why not, mate?*](https://www.reddit.com/r/causeWhyNotMate/)'
                                        comment.reply(message)
                				        if 'why do you' in text.lower() and 'you not' not in text.lower() and len(text)<300 and author != 'causeWhyNotMorty':
                                        message='[*cause why not, mate?*](https://www.reddit.com/r/causeWhyNotMate/)'
                                        comment.reply(message)
				except Exception as e:
                        print e
