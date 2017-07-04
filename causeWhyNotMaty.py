import praw
import datetime
bot = praw.Reddit(user_agent='justalilbit lalala v0.1',
                  client_id='UbwBYg5STT1TWw',
                  client_secret='KRN00vU1wGNRq0S73f8HzcERnPU',
                  username='JUST-A-LIL-BIT',
                  password='asdfasdf7')
submitSubreddit = bot.subreddit('JustALIttleBIt')
subreddit = bot.subreddit('all')
comments = subreddit.stream.comments()

blackList=['suicidewatch','depression']

def getEntireCommentContext(comment, message):
        submission = comment.submission
        op = submission.author
	author = comment.author
        context = str(op.name)+'@'+str(submission.subreddit) + ": " + str(submission.title) + '\n' + str(submission.url) +'\n' + str(submission.selftext) + '\n' + submission.shortlink + '\n'
        context += '\n' + '_________________________________________________________________________________________'
        parentcommentlist=[]
        parentcomments = getAllParentReplies(comment, parentcommentlist).reverse()
        context += ''.join(parentcommentlist)
        context += '\n\n' + '* ' + 'JUST-A-LIL-BIT: ' + str(message)
        context += '\n' + '______________________________________________________________________________'
        with open(str(author.name)+'_'+str(submission.subreddit)+'_'+str(datetime.datetime.now())+'.txt','w') as text_file:
                text_file.write(context)
        submitSubreddit.submit(str(author.name)+'@'+str(submission.subreddit), selftext=context)
        return context

def getAllParentReplies(comment, allParentReplies):
        parent = comment.parent()
        if type(parent) is praw.models.Submission:
                allParentReplies.append('\n\n' + '* ' + str(comment.author.name) + ': ' + str(comment.body))
                allParentReplies.append('\n\n' + 'Comment link: ' + comment.permalink(fast=False))
                return allParentReplies
        else:
                allParentReplies.append('\n\n' + '* ' + str(comment.author.name) + ': ' + str(comment.body))
                return getAllParentReplies(parent, allParentReplies)

while 1<2:
        for comment in comments:
                submission = comment.submission
                try:
                                text = comment.body
                                author = comment.author
                                if 'just a lil bit' == text.lower() and author != 'JUST-A-LIL-BIT' and str(submission.subreddit).lower() not in blackList:
                                        message='just a lil bit'
                                        comment.reply(message)
                                        getEntireCommentContext(comment, message)

                                if 'just a lil bit.' == text.lower() and author != 'JUST-A-LIL-BIT' and str(submission.subreddit).lower() not in blackList:
                                        message='just a lil bit'
                                        comment.reply(message)
                                        getEntireCommentContext(comment, message)
 
                                if 'just a lil bit!' == text.lower() and author != 'JUST-A-LIL-BIT' and str(submission.subreddit).lower() not in blackList:
                                        message='just a lil bit'
                                        comment.reply(message)
                                        getEntireCommentContext(comment, message)  
                except Exception as e:
                        print e
