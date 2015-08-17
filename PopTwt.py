__author__ = 'gunnarkleemann'

__author__ = 'gunnarkleemann'

#### 1.2 Pull backed up tweets from the S3 bucket and load them into a mongodb

# PLAN:
# Read in each file and identify which tweets are re-tweets using the "retweeted_status" field
# Go to mongoDB and find that tweet by the id_str
# in a retweeted tweet there are two sets of values, the tweet and the original
#tweet that is nested inside "retweeted status" some fields are different and
# I will capture these (screen name, location, there are two tweet id_strs!)

import pandas as pd
import glob as glob
# make a temporary folder and download the tweet backup from s3 into it
if not os.path.exists('/TempTweet'):
    os.makedirs('TempTweet')
os.chdir('TempTweet')
!aws s3 sync s3://kleew205asn3/tweetbackup . --exclude "*" --include "out*"

# I did not capture the correct fields so I will insert them from my backup using id_str as the reference
# backup location
#BackLoc = '/Users/gunnarkleemann/Dropbox/coursework/BerkeleyDataSciences/BerkeleyCODE/205code/DataStoreRetrieval/205Assignments/Asn3/TweetFldr/'

fileLs=glob.glob("*")
NewData=[]
df = pd.DataFrame(columns=('tweetID', 'OriginalTweetID', 'OrigLoc', 'OrigScrNm', 'RetweetCt'))

for FileNum in range(len(fileLs)):
    day_reads = open(fileLs[FileNum]).read().splitlines()
    for tweetIter in range(len(day_reads)):
        tweet=day_reads[tweetIter]
        if tweet == '':  #the tweets are delimited by blank lines
            next
        try:
            tweet=json.loads(tweet)
            #if tweet['retweeted_status']:
                #print 'XX'

            Tweet=tweet['text'].encode('utf-8')
            tweetID=tweet['user']['id_str']
            OriginalTweetID=tweet['retweeted_status']['user']['id_str']
            OrigLoc=tweet['retweeted_status']['user']['location']
            OrigScrNm=tweet['retweeted_status']['user']['screen_name']
            RetweetCt= tweet['retweet_count']

            #'retweeted_status' in tweet.keys()# just see if this exists
            myColl.insert({'id_srt':tweetID},{'$set':{
            'id_str_OrigTwt':OriginalTweetID,
            'location_OrigTwt':OrigLoc,
            'screenNm_OrigTwt':OrigScrNm,
            'retweet_count':RetweetCt}})
            df.loc[tweetIter] = [tweetID, OriginalTweetID, OrigLoc, OrigScrNm, RetweetCt]
        except:
            pass

#cleanup
!rm -rf TempTweet


# here I made a SORTED pandas dataframe of the retweeted data

df.sort(['RetweetCt'], ascending =[False], inplace=True)
print df.head()
df.to_csv('retweetCt.csv',  encoding='utf-8')


# SO use both arguments to filter ...
# Now that is better
CleanTwtLs3=df.drop_duplicates(subset = ['RetweetCt', 'OriginalTweetID'])
CleanTwtLs3=CleanTwtLs3.sort(['RetweetCt'], ascending =[False])
CleanTwtLs3.to_csv('Top30_Full.csv',  encoding='utf-8')
Top30 = CleanTwtLs3[0:38]
Top30

# making sure you have 30 unique .. top 30 is only 22!
Uniq_Top30=Top30.drop_duplicates(subset = ['OrigScrNm'], inplace= False)
len(Uniq_Top30)