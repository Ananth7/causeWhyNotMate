import praw
import datetime
import random
import re

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
    for comment in bot.user.me().comments.new(limit=37):
        if comment.score < -3:
            print "deleted comment = " + str(comment.body) + " " + str(comment.score)
            comment.delete()


def sylco(word) :

    word = word.lower()

    # exception_add are words that need extra syllables
    # exception_del are words that need less syllables

    exception_add = ['serious','crucial']
    exception_del = ['fortunately','unfortunately']

    co_one = ['cool','coach','coat','coal','count','coin','coarse','coup','coif','cook','coign','coiffe','coof','court']
    co_two = ['coapt','coed','coinci']

    pre_one = ['preach']

    syls = 0 #added syllable number
    disc = 0 #discarded syllable number

    #1) if letters < 3 : return 1
    if len(word) <= 3 :
        syls = 1
        return syls

    #2) if doesn't end with "ted" or "tes" or "ses" or "ied" or "ies", discard "es" and "ed" at the end.
    # if it has only 1 vowel or 1 set of consecutive vowels, discard. (like "speed", "fled" etc.)

    if word[-2:] == "es" or word[-2:] == "ed" :
        doubleAndtripple_1 = len(re.findall(r'[eaoui][eaoui]',word))
        if doubleAndtripple_1 > 1 or len(re.findall(r'[eaoui][^eaoui]',word)) > 1 :
            if word[-3:] == "ted" or word[-3:] == "tes" or word[-3:] == "ses" or word[-3:] == "ied" or word[-3:] == "ies" :
                pass
            else :
                disc+=1

    #3) discard trailing "e", except where ending is "le"

    le_except = ['whole','mobile','pole','male','female','hale','pale','tale','sale','aisle','whale','while']

    if word[-1:] == "e" :
        if word[-2:] == "le" and word not in le_except :
            pass

        else :
            disc+=1

    #4) check if consecutive vowels exists, triplets or pairs, count them as one.

    doubleAndtripple = len(re.findall(r'[eaoui][eaoui]',word))
    tripple = len(re.findall(r'[eaoui][eaoui][eaoui]',word))
    disc+=doubleAndtripple + tripple

    #5) count remaining vowels in word.
    numVowels = len(re.findall(r'[eaoui]',word))

    #6) add one if starts with "mc"
    if word[:2] == "mc" :
        syls+=1

    #7) add one if ends with "y" but is not surrouned by vowel
    if word[-1:] == "y" and word[-2] not in "aeoui" :
        syls +=1

    #8) add one if "y" is surrounded by non-vowels and is not in the last word.

    for i,j in enumerate(word) :
        if j == "y" :
            if (i != 0) and (i != len(word)-1) :
                if word[i-1] not in "aeoui" and word[i+1] not in "aeoui" :
                    syls+=1

    #9) if starts with "tri-" or "bi-" and is followed by a vowel, add one.

    if word[:3] == "tri" and word[3] in "aeoui" :
        syls+=1

    if word[:2] == "bi" and word[2] in "aeoui" :
        syls+=1

    #10) if ends with "-ian", should be counted as two syllables, except for "-tian" and "-cian"

    if word[-3:] == "ian" :
    #and (word[-4:] != "cian" or word[-4:] != "tian") :
        if word[-4:] == "cian" or word[-4:] == "tian" :
            pass
        else :
            syls+=1

    #11) if starts with "co-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.

    if word[:2] == "co" and word[2] in 'eaoui' :

        if word[:4] in co_two or word[:5] in co_two or word[:6] in co_two :
            syls+=1
        elif word[:4] in co_one or word[:5] in co_one or word[:6] in co_one :
            pass
        else :
            syls+=1

    #12) if starts with "pre-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.

    if word[:3] == "pre" and word[3] in 'eaoui' :
        if word[:6] in pre_one :
            pass
        else :
            syls+=1

    #13) check for "-n't" and cross match with dictionary to add syllable.

    negative = ["doesn't", "isn't", "shouldn't", "couldn't","wouldn't"]

    if word[-3:] == "n't" :
        if word in negative :
            syls+=1
        else :
            pass

    #14) Handling the exceptional words.

    if word in exception_del :
        disc+=1

    if word in exception_add :
        syls+=1

    # calculate the output
    return numVowels - disc + syls

while 1<2:
        for comment in comments:
                submission = comment.submission
                try:
                                text = comment.body
                                author = comment.author
                                subscript = '\n' + '______________________________________________________________________________' + '\n' + '^^^-haiku_bot '#'#, ^^^and ^^^my ^^^only ^^^purpose ^^^is ^^^to ^^^serve ^^^you ^^^random ^^^Rick ^^^and ^^^Morty ^^^quotes.'
                                subscript1 = '\n' + '______________________________________________________________________________' + '\n' + '^^^-haiku_botv2'#'#, ^^^and ^^^my ^^^only ^^^purpose ^^^is ^^^to ^^^serve ^^^you ^^^random ^^^Rick ^^^and ^^^Morty ^^^quotes.'
                                if len(text.split()) == 17 and (len(text.split("\n")) == 1 or len(text.split("\n")) == 2 )and author != 'I_am_a_haiku_bot' and str(submission.subreddit).lower() not in blackList:
                                    words = text.split()
                                    line1 = "*" + words[0] + " " + words[1]+ " "  + words[2]+ " " + words[3]+ " "  + words[4] + "*"
                                    line2 = "*" + words[5]+ " "  + words[6]+ " "  + words[7]+ " "  + words[8] + " " + words[9]+ " "  + words[10]+ " "  + words[11] + "*"
                                    line3 = "*" + words[12] + " " + words[13] + " " + words[14]+ " "  + words[15]+ " "  + words[16] + "*"
                                    message = line1 + "\n\n" + line2 + "\n\n" + line3 + "\n\n" + subscript
                                    #print message
                                    comment.reply(message)
                                    getEntireCommentContext(comment, message)
                                    deleteShitIfItHitsTheFan()
                            elif (len(text.split()) < 18 and len(text.split()) > 11 ):
                                    words = text.split()
                                    sylCount = []
                                    totalSyl = 0
                                    for word in words:
                                        sylc = sylco(word)
                                        sylCount.append(sylc)
                                        totalSyl += sylc

                                    if (totalSyl == 17 or totalSyl == 16):
                                        numwords = []
                                        indx = 0
                                        sylencountered = 0
                                        for word in words:
                                            sylencountered += sylCount[indx]
                                            if (sylencountered >= 5):
                                                line1index = indx
                                                break
                                            indx += 1

                                        sylencountered = 0
                                        for word in words:
                                            sylencountered += sylCount[indx]
                                            if (sylencountered >= 11):
                                                line2index = indx
                                                break
                                            indx += 1

                                        line1 = ""
                                        line2 = ""
                                        line3 = ""
                                        for i in range(0, line1index):
                                            line1 += words[i] + " "
                                        for i in range(line1index, line2index):
                                            line2 += words[i] + " "
                                        for i in range(line2index, len(words)):
                                            line3 += words[i] + " "
                                        line1 = "*" + line1.rstrip() + "*"
                                        line2 = "*" + line2.rstrip() + "*"
                                        line3 = "*" + line3.rstrip() + "*"
                                        message = line1 + "\n\n" + line2 + "\n\n" + line3 + "\n\n" + subscript1
                                        #print str(line1index) + " " + str(line2index)
                                        #print message
                                        comment.reply(message)
                                        getEntireCommentContext(comment, message)
                                        deleteShitIfItHitsTheFan()
                except Exception as e:
                        print e
