from subprocess import call
import os.path,subprocess
import time

states_abbr=["AL","AK","AS","AZ","AR","CA","CO","CT","DE","DC","FM","FL","GA","GU","HI","ID" 
        "IL","IN","IA","KS","KY","LA","ME","MH","MD","MA","MI","MN","MS","MO","MT","NE" 
        "NV","NH","NJ","NM","NY","NC","ND","MP","OH","OK","OR","PW","PA","PR","RI","SC" 
        "SD","TN","TX","UT","VT","VI","VA","WA","WV","WI","WY"]
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New_Hampshire","New_Jersey","New_Mexico","New_York","North_Carolina","North_Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode_Island","South_Carolina","South_Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West_Virginia","Wisconsin","Wyoming"]

firstBig=["Birmingham","Anchorage","Phoenix","Little Rock","Los Angeles","Denver","Bridgeport","Wilmington","Jacksonville","Atlanta","Honolulu","Boise","Chicago","Indianapolis","Des Moines","Wichita","Louisville","New Orleans","Portland","Baltimore","Boston","Detroit","Minneapolis","Jackson","Kansas City","Billings","Omaha","Las Vegas","Manchester","Newark","Albuquerque","New York","Charlotte","Fargo","Columbus","Oklahoma City","Portland","Philadelphia","Providence","Columbia","Sioux Falls","Memphis","Houston","Salt Lake City","Burlington","Virginia Beach","Seattle","Charleston","Milwaukee","Cheyenne"]
secondbig=["Montgomery","Fairbanks","Tucson","Fort Smith","San Diego","Colorado Springs","New Haven","Dover","Miami","Augusta","Hilo1","Nampa","Aurora","Fort Wayne","Cedar Rapids","Overland Park","Lexington","Baton Rouge","Lewiston","Columbia","Worcester","Grand Rapids","Saint Paul","Gulfport","Saint Louis","Missoula","Lincoln","Henderson","Nashua","Jersey City","Las Cruces","Buffalo","Raleigh","Bismarck","Cleveland","Tulsa","Eugene","Pittsburgh","Warwick","Charleston","Rapid City","Nashville","San Antonio","West Valley City","Essex","Norfolk","Spokane","Huntington","Madison","Casper"]
thirdbig=["Mobile","Juneau","Mesa","Fayetteville","San Jose","Aurora","Stamford","Newark","Tampa","Columbus","Kailua1","Meridian","Rockford","Evansville","Davenport","Kansas City","Bowling Green","Shreveport","Bangor","Germantown","Springfield","Warren","Rochester","Hattiesburg","Springfield","Great Falls","Bellevue","North Las Vegas","Concord","Paterson","Rio Rancho","Rochester","Greensboro","Grand Forks","Cincinnati","Norman","Salem","Allentown","Cranston","North Charleston/Greenville","Aberdeen","Knoxville","Dallas","Provo","South Burlington","Chesapeake","Tacoma","Parkersburg","Green Bay","Laramie"]

#echo ${#firstBig[@]}
#echo ${#secondbig[@]}
#echo ${#thirdbig[@]}

#        ./main.py_onestate --location="$i" --term="century 21"  --maxrow=1000 --writeto="./output_1/${i}.log"

ter = "--term='century 21'"
mxr = "--maxrow=1000"
for e,st in zip(firstBig,states):
    loc = "--location="+e
    wri ="--writeto=output/"+st+"_1"
    p1 = subprocess.Popen(["./main.py_onestate",loc,ter,mxr,wri], stdout=subprocess.PIPE)
    time.sleep(1)

for e,st in zip(secondbig,states):
    loc = "--location="+e
    wri ="--writeto=output/"+st+"_2"
    p1 = subprocess.Popen(["./main.py_onestate",loc,ter,mxr,wri], stdout=subprocess.PIPE)
    time.sleep(1)

for e,st in zip(thirdbig,states):
    loc = "--location="+e
    wri ="--writeto=output/"+st+"_3"
    p1 = subprocess.Popen(["./main.py_onestate",loc,ter,mxr,wri], stdout=subprocess.PIPE)
    time.sleep(1)


