import praw
import datetime
import random

bot = praw.Reddit(user_agent='rick and morty only post v0.1',
                  client_id='f7hhEBXypE-tuA',
                  client_secret='YPEM7yQHWN1P2QldlXfMH1lWEFI',
                  username='RickAndMortyBotv2',
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
        if comment.score < 3:
            comment.delete()

while 1<2:
        for comment in comments:
                submission = comment.submission
                try:
                                deleteShitIfItHitsTheFan()
                                text = comment.body
                                author = comment.author
                                subscript = '\n' + '______________________________________________________________________________' + '\n' + '^^^I ^^^am ^^^a ^^^bot, ^^^and ^^^my ^^^only ^^^purpose ^^^is ^^^to ^^^serve ^^^you ^^^random ^^^Rick ^^^and ^^^Morty ^^^quotes.'
                                if text.lower() in quotes_lower and author != 'RickAndMorty_Bot' and str(submission.subreddit).lower() not in blackList:
                                    print text
                                    message = random.choice(quotes.keys()) + subscript
                                    comment.reply(message)
                                    getEntireCommentContext(comment, message)
                except Exception as e:
                        print e
