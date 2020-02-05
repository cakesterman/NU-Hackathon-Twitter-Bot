import twitter
import time
import parsing


def init():

    CONSUMER_KEY = 'xxx'
    CONSUMER_SECRET = 'xxx'
    ACCESS_TOKEN = 'xxx'
    ACCESS_TOKEN_SECRET = 'xxx'

    global api

    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)


def tweet_status(tweet):

    #status = api.PostUpdate(tweet)

    try:

        # if url != '':
        #
        #     status = api.PostUpdate(tweet, media=url)
        #
        # else:

        status = api.PostUpdate(tweet)

        print("Tweeted {0}".format(status.text))

    except twitter.error.TwitterError:

        print("Unable to post")


# Doesn't work for some reason
def tweet_direct_message(message, user):

    status = api.PostDirectMessage(message, screen_name=user)

    print(status)


# Dont use right now
def get_user():

    test = api.GetUser(screen_name="Codeplexity1")

    print(test)



def watch_bitcoin():

    while True:

        tweet_status("Current Bitcoin price is {} https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD".format(str(parsing.get_current_bitcoin_price()))
                     )

        time.sleep(60)

        
