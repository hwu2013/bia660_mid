#!/usr/bin/python

import json
import oauth2
import optparse
import urllib
import urllib2
import sys

outfile = open("./output.log", 'w')
parser = optparse.OptionParser()
"""
parser.add_option('-c', '--consumer_key', dest='consumer_key', help='OAuth consumer key (REQUIRED)')
parser.add_option('-s', '--consumer_secret', dest='consumer_secret', help='OAuth consumer secret (REQUIRED)')
parser.add_option('-t', '--token', dest='token', help='OAuth token (REQUIRED)')
parser.add_option('-e', '--token_secret', dest='token_secret', help='OAuth token secret (REQUIRED)')
"""
parser.add_option('-a', '--host', dest='host', help='Host', default='api.yelp.com')

parser.add_option('-q', '--term', dest='term', help='Search term')
parser.add_option('-l', '--location', dest='location', help='Location (address)')
parser.add_option('-b', '--bounds', dest='bounds', help='Bounds (sw_latitude,sw_longitude|ne_latitude,ne_longitude)')
parser.add_option('-p', '--point', dest='point', help='Latitude,longitude')
# Not sure if current location hints are currently working
parser.add_option('-i', '--current_location', dest='current_location', help='Current location latitude,longitude for location disambiguation')

parser.add_option('-o', '--offset', dest='offset', help='Offset (starting position)')
parser.add_option('-r', '--limit', dest='limit', help='Limit (number of results to return)')
parser.add_option('-x', '--maxrow', dest='maxrow', help='Maxrow (max number of results to return)')
parser.add_option('-u', '--cc', dest='cc', help='Country code')
parser.add_option('-n', '--lang', dest='lang', help='Language code')

parser.add_option('-d', '--radius', dest='radius', help='Radius filter (in meters)')
parser.add_option('-g', '--category', dest='category', help='Category filter')
parser.add_option('-z', '--deals', dest='deals', help='Deals filter')
parser.add_option('-m', '--sort', dest='sort', help='Sort')


options, args = parser.parse_args()

# Required options
"""
if not options.consumer_key:
  parser.error('--consumer_key required')
if not options.consumer_secret:
  parser.error('--consumer_secret required')
if not options.token:
  parser.error('--token required')
if not options.token_secret:
  parser.error('--token_secret required')
"""
options.consumer_key    = "0pYQvAy9JQoRiZTpEFiPLg"
options.consumer_secret = "-01DmjuOQeHjQdRJnUWvuRe1pz0"
options.token           = "kTYK94YSSF9jPZiOVvpttf5fZx9PtxAa"
options.token_secret    = "LrRVEVOIpnZ6CGwFKEHCz9W0-xA"


if not options.location and not options.bounds and not options.point:
  parser.error('--location, --bounds, or --point required')

maxrow = 999999;
# Setup URL params from options
url_params = {}
if options.offset:
    url_params['offset'] = options.offset;
if options.term:
  url_params['term'] = options.term
if options.location:
  url_params['location'] = options.location
if options.bounds:
  url_params['bounds'] = options.bounds
if options.point:
  url_params['ll'] = options.point
if options.offset:
  url_params['offset'] = options.offset
if options.limit:
  url_params['limit'] = options.limit
if options.maxrow:
  maxrow = int(options.maxrow)
if options.cc:
  url_params['cc'] = options.cc
if options.lang:
  url_params['lang'] = options.lang
if options.current_location:
  url_params['cll'] = options.current_location
if options.radius:
  url_params['radius_filter'] = options.radius
if options.category:
  url_params['category_filter'] = options.category
if options.deals:
  url_params['deals_filter'] = options.deals
if options.sort:
  url_params['sort'] = options.sort


def request(host, path, url_params, consumer_key, consumer_secret, token, token_secret):
  """Returns response for API request."""
  # Unsigned URL
  encoded_params = ''
  if url_params:
    encoded_params = urllib.urlencode(url_params)
  url = 'http://%s%s?%s' % (host, path, encoded_params)
  print 'URL: %s' % (url,)

  # Sign the URL
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                        'oauth_timestamp': oauth2.generate_timestamp(),
                        'oauth_token': token,
                        'oauth_consumer_key': consumer_key})

  token = oauth2.Token(token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()
  print 'Signed URL: %s\n' % (signed_url,)

  # Connect
  try:
    conn = urllib2.urlopen(signed_url, None)
    try:
      response = json.loads(conn.read())
    finally:
      conn.close()
  except urllib2.HTTPError, error:
    response = json.loads(error.read())

  return response

def show_location(loc):
    #if("city" in loc and "postal_code" in loc and "address"  in loc):
    outfile.write(u"\tlocation:   {0},{1},{2}\n".format(loc["city"],loc["postal_code"],
            loc["address"][0]  if (len(loc["address"])>0) else ""))

def show_cate(cate):
    outfile.write(u"\tCategories:")
    for elem in cate:
        for subelem in elem:
            outfile.write(subelem);
            outfile.write(",")
    outfile.write("\n")

def show_neighbor(nb):
    outfile.write(u"\tNeighbors:   ")
    for elem in nb:
        outfile.write(elem);
        outfile.write(",")
    outfile.write("\n")


def print_one_busi(busi,offset):
     outfile.write(u"\n#{0}---{1}\n".format(offset,busi["id"]))
     outfile.write(u"\turl:{0}\n".format(busi["url"]))
     if "categories" in busi:
         show_cate(busi["categories"])
     show_location(busi["location"])
     outfile.write(u"\tname:      {0}, rating:{1}, review_count:{2}\n".format(busi["name"],busi["rating"],busi["review_count"]))
     if "neighborhoods" in busi["location"]:
         show_neighbor(busi["location"]["neighborhoods"])
     outfile.write(u"\tcomment:   {0}\n:".format(busi["snippet_text"]))


def print_multi_busi(off):
    print "---------------------------------------------",off,maxrow
    url_params['off'] = off
    url_params['limit'] = 20
    _DEBUG=True
    response = request(options.host, '/v2/search', url_params, options.consumer_key, options.consumer_secret, options.token, options.token_secret)
    if(response and len(response["businesses"])>0):
        #print response //for debug
        for busi in response["businesses"]:
            if off > maxrow:
                print "log write to ./output.log"
                sys.exit()
            print_one_busi(busi,off)
            off += 1
    return len(response["businesses"])



offset = 1;
while( print_multi_busi(offset) >0  and  offset<=maxrow):
   offset += 20;


#print json.dumps(response, sort_keys=True, indent=2)

