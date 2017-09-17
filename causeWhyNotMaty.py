import praw
import datetime
import random

bot = praw.Reddit(user_agent='rick and morty only post v0.1',
                  client_id='w8Y8oai91XGJ1g',
                  client_secret='UBSkHGEcDcsF-TktfTJUCv40dX8',
                  username='I_am_a_haiku_bot',
                  password='asdfasdf')
submitSubreddit = bot.subreddit('loggingmyfavthoughts')
subreddit = bot.subreddit('all')
comments = subreddit.stream.comments()

fileName = "quotes.txt"

quotes = {}

with open(fileName) as f:
    for line in f:
        quotes[line[:-1]] = "1"
quotes_lower = {k.lower():v for k,v in quotes.items()}
blackList=[
    "anime",
    "asianamerican",
    "askhistorians",
    "askscience",
    "askreddit",
    "aww",
    "chicagosuburbs",
    "cosplay",
    "cumberbitches",
    "d3gf",
    "deer",
    "depression",
    "depthhub",
    "drinkingdollars",
    "forwardsfromgrandma",
    "geckos",
    "giraffes",
    "grindsmygears",
    "indianfetish",
    "me_irl",
    "misc",
    "movies",
    "mixedbreeds",
    "news",
    "newtotf2",
    "omaha",
    "petstacking",
    "pics",
    "pigs",
    "politicaldiscussion",
    "politics",
    "programmingcirclejerk",
    "raerthdev",
    "rants",
    "runningcirclejerk",
    "salvia",
    "science",
    "seiko",
    "shoplifting",
    "sketches",
    "sociopath",
    "suicidewatch",
    "talesfromtechsupport",
    "torrent",
    "torrents",
    "trackers",
    "tr4shbros",
    "unitedkingdom",
    "crucibleplaybook",
    "benfrick",
    "bsa",
    "futurology",
    "graphic_design",
    "historicalwhatif",
    "lolgrindr",
    "malifaux",
    "nfl",
    "toonami",
    "trumpet",
    "ps2ceres",
    "duelingcorner"
  ]
def getEntireCommentContext(comment, message):
        submission = comment.submission
        op = submission.author
        author = comment.author
        context = str(op.name)+'@'+str(submission.subreddit) + ": " + str(submission.title) + '\n\n' + str(submission.url) +'\n' + str(submission.selftext) + '\n' + submission.shortlink + '\n'
        context += '\n' + '_________________________________________________________________________________________'
        parentcommentlist=[]
        parentcomments = getAllParentReplies(comment, parentcommentlist).reverse()
        context += ''.join(parentcommentlist)
        context += '\n\n' + '* ' + 'causeWhyNotMate: ' + str(message)
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

def deleteShitIfItHitsTheFan():
    for comment in bot.user.me().comments.new(limit=25):
        if comment.score < -3:
            print "deleted comment = " + str(comment.body) + " " + str(comment.score)
            comment.delete()


while 1<2:
        for comment in comments:
                submission = comment.submission
                try:
                                text = comment.body
                                author = comment.author
                                subscript = '\n' + '______________________________________________________________________________' + '\n' + '                                               ^^^-haiku_bot '#'#, ^^^and ^^^my ^^^only ^^^purpose ^^^is ^^^to ^^^serve ^^^you ^^^random ^^^Rick ^^^and ^^^Morty ^^^quotes.'
                                if len(text.split()) == 17 and (len(text.split("\n")) == 1 or len(text.split("\n")) == 2 )and author != 'I_am_a_haiku_bot' and str(submission.subreddit).lower() not in blackList:
                                    words = text.split()
                                    line1 = "*" + words[0] + " " + words[1]+ " "  + words[2]+ " " + words[3]+ " "  + words[4] + "*"
                                    line2 = "*" + words[5]+ " "  + words[6]+ " "  + words[7]+ " "  + words[8] + " " + words[9]+ " "  + words[10]+ " "  + words[11] + "*"
                                    line3 = "*" + words[12] + " " + words[13] + " " + words[14]+ " "  + words[15]+ " "  + words[16] + "*"
                                    message = line1 + "\n\n" + line2 + "\n\n" + line3 + "\n\n" + subscript
                                    print message
                                    comment.reply(message)
                                    getEntireCommentContext(comment, message)
                                    deleteShitIfItHitsTheFan()
                except Exception as e:
                        print e
