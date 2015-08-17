__author__ = 'gunnarkleemann'

### the function finds twitter followers and inserts the data into a mongoDB
###
### name_ls, list of names to find followers for
### date, arbitrary date string to mark time of acquisition
### DBcollect the database alias
###
### example call: foll_harvest(Uniq_Top30.OrigScrNm, '7/26/15+5hrs', FollColl)


def foll_harvest (name_ls, date, DBcollect):
    import time
    import tweepy
    os.chdir("/Users/gunnarkleemann/Dropbox/coursework/BerkeleyDataSciences/BerkeleyCODE/205code/DataStoreRetrieval/205Assignments/Asn3")
    from credentials import *
     # includes credentials and api specification
    for Nm in (range(len(name_ls))):
        ids = []
        data ={}
        ScrnNm =name_ls.iloc[Nm]#Uniq_Top30.OrigScrNm.iloc[Nm]
        for page in tweepy.Cursor(api.followers_ids, screen_name=ScrnNm).pages():
            ids.extend(page)
            time.sleep(60)
        data['follower_id'] = ids
        data['tweeter_id'] = ScrnNm
        data['harv_date'] = date
        # Insert process
        DBcollect.insert(data)
        print len(ids)