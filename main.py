import tweepy
from random import randint
import time

#  tweepy documentation: http://docs.tweepy.org/en/latest/api.html#tweepy-api-twitter-api-wrapper

# authorization section ----------------------------------------

consumer_key = "consumer_key"
consumer_secret = "consumer_secret"

key = "key"
secret = "secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# general things ----------------------------------------

# api.update_status('Botinhoslz is live!')  # adds a tweet
# tweets = api.mentions_timeline()  # get all mentions
# print(tweets[0])
me = api.me()

# keyword section ----------------------------------------

keyword = "boytinhoslz"
numberOfTweets = 50
phrases = ["gostei do seu comentario", "bem apontado!", "boa, vamos tomar uma!", "discordo mas respeito"]


def mainLoop():
    followBack()
    retweet()
    like()


def followBack():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()


def retweet():
    for tweet in tweepy.Cursor(api.search, keyword).items(numberOfTweets):
        try:
            tweet.retweet()
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def like():
    for tweet in tweepy.Cursor(api.search, keyword).items(numberOfTweets):
        try:
            tweet.favorite()
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def reply():
    for tweet in tweepy.Cursor(api.search, keyword).items(numberOfTweets):
        if willReply():
            try:
                tweetId = api.get_user(tweet.user.screen_name).id
                username = tweet.user.screen_name
                phrase = getRandomPhrase()
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


def getRandomPhrase():
    return phrases[randint(0, len(phrases) - 1)]


# 15% chance of replying to a tweet
def willReply():
    if randint(1, 100) <= 15:
        return True
    else:
        return False


def runKeyword():
    while True:
        mainLoop()
        print("tick")
        time.sleep(12000)  # sleep in seconds


# fan section ----------------------------------------
# fans = ["jeangreydorole"]
fans = ["jeangreydorole", "euquaseCAIO", "isrrrlindo", "davigrijov", "victorswamilobo"]
numberOfFanTweets = 3
fanPhrases = ["Sou teu fã", "Bela atitude!", "Discordo mas respeito sua opinião!", "Intrigado!", "Ótimo comentário",
              "Não pode ser real", "Muito bom ahaha", "Tu inventa cada coisa...", "Incrível", "Bom dia!", "Durma bem!"]


def mainLoopFan():
    replyFan()
    likeFan()
    retweetFan()


# user_timeline counts replies
def retweetFan():
    for fan in fans:
        for tweet in api.user_timeline(fan, count=numberOfFanTweets):
            try:
                tweet.retweet()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


def likeFan():
    for fan in fans:
        for tweet in api.user_timeline(fan, count=numberOfFanTweets):
            try:
                tweet.favorite()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


def replyFan():
    for fan in fans:
        for tweet in api.user_timeline(fan, count=numberOfFanTweets):
            if not tweet.favorited:
                if willReplyFan():
                    try:
                        tweetId = tweet.id
                        username = "@"+tweet.user.screen_name
                        phrase = getRandomFanPhrase()
                        api.update_status(status=username + " " + phrase, in_reply_to_status_id=tweetId,
                                          auto_populate_reply_metadata=True)
                    except tweepy.TweepError as e:
                        print(e.reason)
                    except StopIteration:
                        break


def getRandomFanPhrase():
    return fanPhrases[randint(0, len(fanPhrases)-1)]


# 20% chance of replying to a tweet
def willReplyFan():
    if randint(1, 100) <= 10:
        return True
    else:
        return False


def runFan():
    while True:
        mainLoopFan()
        print("tick")
        time.sleep(12000)  # sleep in seconds


# main program (choose run method) ----------------------------------------
runFan()
