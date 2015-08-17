#Gunnar Kleemann
# W241_1, Prof. Arash Norain
#Assignment 3, 7/26/15


#Data architecture#



#Resiliance#
Resiliance was increased by backing up tweets progressively. ALso the the use of automatic time limits ensured that my
downloads did not exceed the limit and therefore I could pull tweets continuously.

#Addressing Goals#
1.1

* Since I only captured tweets from the previous assignment I ran a new query with the tags # EU an #Debt. Select
* I used the my function TwpyCursByTime.py for this section.

* the captured tweets were stored in three ways

1) selected fields were stored in my MongoDB database
2) all of thedata for a each day was captured from each tweet._json field and stored in a text file on my hard disk>
 the tweet_jsons were appended in series with a single line to delimit each tweet.
3) As a backup all of the tweet_Json files were synced with my S3 bucket (http://kleew205asn3.s3.amazonaws.com/).
* the address for one of these files is here :
https://s3-us-west-2.amazonaws.com/kleew205asn3/tweetbackup/out2015-07-11_2015-07-12_%2523Debt%2B%252B%2523EU
and the rest are in the file s3TweetBkp.txt

1.2 I used the chunked tweet_jsons to build the


2.1
2.2
2.3 To check the followers of highly retweeted individuals, I used my function *foll_harvest.py* which takes in a
list of individual screen names and uses *api.followers_ids* to gather followers for each focal individual. The results
were loaded into a Mongobd database *db_followers* capturing a 1) list of followers _ids 2) the date of the query and the
screen name of the original author. To identify flux in followers I did a second follower harvest after the first follower
count ranged from
retweeted tweets
3.1


# backups 3.1


#key resources#

I have also included my ipython notebook in the github folder (TweepyAsn3_W205_1V5_Kleemann.ipynb)  if you want to
look at my process
