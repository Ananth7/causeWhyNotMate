import praw
import datetime
bot = praw.Reddit(user_agent='causeWhyNotMaty only post v0.1',
                  client_id='6wpV85OogUi3Cg',
                  client_secret='3c7v5itxbRkeBKgxYOWUVONsiTc',
                  username='causeWhyNotMaty',
                  password='asdfasdf')
submitSubreddit = bot.subreddit('causeWhyNotMate')
subreddit = bot.subreddit('all')
comments = subreddit.stream.comments()

blackList=['suicidewatch','depression']

def getEntireCommentContext(comment, message):
        submission = comment.submission
        op = submission.author
	author = comment.author
        context = str(op.name)+'@'+str(submission.subreddit) + ": " + str(submission.title) + '\n' + str(submission.selftext) + '\n' + submission.shortlink + '\n'
        context += '\n' + '_________________________________________________________________________________________'
        parentcommentlist=[]
        parentcomments = getAllParentReplies(comment, parentcommentlist).reverse()
        context += ''.join(parentcommentlist)
        context += '\n\n' + '* ' + 'causeWhyNotMaty: ' + str(message)
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
                                if 'why?' == text.lower() and author != 'causeWhyNotMaty' and str(submission.subreddit).lower() not in blackList:
                                        message='[*why not, mate?*](https://www.reddit.com/r/causeWhyNotMate/)'
                                        comment.reply(message)
                                        getEntireCommentContext(comment, message)
                                if 'why did you' in text.lower() and 'you not' not in text.lower() and  len(text)<200 and author != 'causeWhyNotMaty' and str(submission.subreddit).lower() not in blackList:
                                        message='[*cause why not, mate?*](https://www.reddit.com/r/causeWhyNotMate/)'
                               		replyMessage='This is in reply to your recent comment.'+'\n\n>' + text + '\n\n'
                                        fullContext=getEntireCommentContext(comment, message)
					fullContext+='_________________________________________________________________________________________'
                                        author.message('cause why not, mate?',replyMessage +'\n\n>' + message)
				if 'why do you' in text.lower() and 'you not' not in text.lower() and len(text)<200 and author != 'causeWhyNotMaty' and str(submission.subreddit).lower() not in blackList:
                                        message='[*cause why not, mate?*](https://www.reddit.com/r/causeWhyNotMate/)'
					replyMessage='This is in reply to your recent comment.'+ '\n\n>'+ text +'\n\n'
                                        fullContext=getEntireCommentContext(comment, message)
					fullContext+='_________________________________________________________________________________________'
                                        author.message('cause why not, mate?',replyMessage +'\n\n>'+ message)
                except Exception as e:
                        print e
