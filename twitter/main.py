#!/usr/bin/python

from twitter import *
OAUTH_TOKEN='19202628-1t97auu1YH1zxtIOB4rQ3F056TEZPlUqUs3LoFCTa'
OAUTH_SECRET='kuAD2MAExNlu7IwImoRAm1wbpdm5xc9gCGctL83c'
CONSUMER_TOKEN='kXPnvcf4UzGUi57e6LaLw'
CONSUMER_SECRET='HHlRwgG0F6qY0DYFH8yIUaRiDgvOkphoijamueJvjwY'

# <codecell>

t = Twitter(auth=OAuth(OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_TOKEN,CONSUMER_SECRET))

# <codecell>

#jstr = t.statuses.retweets_of_me()
search_result = t.search.tweets(q="cvs :(",lang="en",count = 10,max_id="384815208189132800")

# <codecell>

#print search_result;
for tweet in search_result["statuses"]:
    if "text" in tweet:
        print tweet['id_str']
        print tweet['text']
# <codecell>


