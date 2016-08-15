__author__ = 'Remigius'
import tweepy
import time
import sys
import os

#Change system encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

#setting up twitter bot authentication
#Add your keys here
consumer_key = '###'
consumer_secret = '###'
access_token = '###'
access_token_secret = '###'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Creating an instance to connect to the twitter api
api = tweepy.API(auth)


'''a is a counter and b is kinda like the total tweets deleted'''
def delete_old_tweets(a,b):
    for status in api.user_timeline("BlaveKalahn"):#, max_id=657288237862539265): #max id is an optional parameter
    #status from twitters api comes as an object
        if status.id != 661804492581507072:
            #sometimes as I code listen to random songs, I tweet thier names and this little bit saves them in a text file.
            if status.text.startswith("#np"):
                with open('Tweet_Songs.txt', 'a') as writter:
                    writter.writelines(status.text[4:])
                    writter.writelines('\n')
                    writter.close() 
            api.destroy_status(status.id)
        print str(status.text), a, "Deleted"
        a+=1
        b+=1
        #print a

    if a >= 100:
        print "We need a rest"
        print "Deleted", b ,"tweets so far"
        time.sleep(60)
        delete_old_tweets(1,b)
    elif a < 100:
        delete_old_tweets(a,b)
    else:
        print "Tiimy Turner needs a burner"

    return b

def main():

    a = api.rate_limit_status()
    b =  a['resources']['statuses']['/statuses/user_timeline']

    print b["remaining"]

    if b["remaining"] >= 1:
        try:
            print b["remaining"]
            delete_old_tweets(1,0)
        except Exception as e:
            print "Error: ", e
            print "*"*10
            time.sleep(60)
            print b["remaining"], "Second"
            delete_old_tweets(1,0)
        except:
            print "Probably time out"
            print "Getting back up!"
            print b["remaining"], "Third"
            delete_old_tweets(1,0)

    else:
        print "@"*20
        print "Rate limit is: ", b

main()
