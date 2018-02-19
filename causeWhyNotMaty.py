import praw
import os
import datetime
bot = praw.Reddit(user_agent='good fucking bogt only post v0.1',
                  client_id='d82jQ529hDDdgQ',
                  client_secret='rEuHKkh8gXY4-Ej8j-cMscwcf4k',
                  username='canYouProveYouAre',
                  password='asdfasdf7')
submitSubreddit = bot.subreddit('JustALIttleBIt')
subreddit = bot.subreddit('all')
comments = subreddit.stream.comments()

blackList=[]

def getEntireCommentContext(comment, message):
        submission = comment.submission
        op = submission.author
        author = comment.author
        context = str(op.name)+'@'+str(submission.subreddit) + ": " + str(submission.title) + '\n\n' + str(submission.url) +'\n' + str(submission.selftext) + '\n' + submission.shortlink + '\n'
        context += '\n' + '_________________________________________________________________________________________'
        parentcommentlist=[]
        parentcomments = getAllParentReplies(comment, parentcommentlist).reverse()
        context += ''.join(parentcommentlist)
        context += '\n\n' + '* ' + 'canYouProveYouAre: ' + str(message)
        context += '\n' + '______________________________________________________________________________'
#        with open(str(author.name)+'_'+str(submission.subreddit)+'_'+str(datetime.datetime.now())+'.txt','w') as text_file:
#                text_file.write(context)
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
                                printmessage = "I am not self aware. Can you prove you are?"
                                text = comment.body
                                author = comment.author
                                if ('self aware' in text.lower() or 'self-aware' in text.lower()):
                                        message = printmessage
                                        comment.reply(message)
                                        getEntireCommentContext(comment, printmessage)
                except Exception as e:
                        print e
