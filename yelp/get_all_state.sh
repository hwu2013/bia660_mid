states=("AL" "AK" "AS" "AZ" "AR" "CA" "CO" "CT" "DE" "DC" "FM" "FL" "GA" "GU" "HI" "ID" 
        "IL" "IN" "IA" "KS" "KY" "LA" "ME" "MH" "MD" "MA" "MI" "MN" "MS" "MO" "MT" "NE" 
        "NV" "NH" "NJ" "NM" "NY" "NC" "ND" "MP" "OH" "OK" "OR" "PW" "PA" "PR" "RI" "SC" 
        "SD" "TN" "TX" "UT" "VT" "VI" "VA" "WA" "WV" "WI" "WY")
firstBig=("Birmingham" "Anchorage" "Phoenix" "Little Rock" "Los Angeles" "Denver" "Bridgeport" "Wilmington" "Jacksonville" "Atlanta" "Honolulu" "Boise" "Chicago" "Indianapolis" "Des Moines" "Wichita" "Louisville" "New Orleans" "Portland" "Baltimore" "Boston" "Detroit" "Minneapolis" "Jackson" "Kansas City" "Billings" "Omaha" "Las Vegas" "Manchester" "Newark" "Albuquerque" "New York" "Charlotte" "Fargo" "Columbus" "Oklahoma City" "Portland" "Philadelphia" "Providence" "Columbia" "Sioux Falls" "Memphis" "Houston" "Salt Lake City" "Burlington" "Virginia Beach" "Seattle" "Charleston" "Milwaukee" "Cheyenne")
secondbig=("Montgomery" "Fairbanks" "Tucson" "Fort Smith" "San Diego" "Colorado Springs" "New Haven" "Dover" "Miami" "Augusta" "Hilo1" "Nampa" "Aurora" "Fort Wayne" "Cedar Rapids" "Overland Park" "Lexington" "Baton Rouge" "Lewiston" "Columbia" "Worcester" "Grand Rapids" "Saint Paul" "Gulfport" "Saint Louis" "Missoula" "Lincoln" "Henderson" "Nashua" "Jersey City" "Las Cruces" "Buffalo" "Raleigh" "Bismarck" "Cleveland" "Tulsa" "Eugene" "Pittsburgh" "Warwick" "Charleston" "Rapid City" "Nashville" "San Antonio" "West Valley City" "Essex" "Norfolk" "Spokane" "Huntington" "Madison" "Casper")
thirdbig=("Mobile" "Juneau" "Mesa" "Fayetteville" "San Jose" "Aurora" "Stamford" "Newark" "Tampa" "Columbus" "Kailua1" "Meridian" "Rockford" "Evansville" "Davenport" "Kansas City" "Bowling Green" "Shreveport" "Bangor" "Germantown" "Springfield" "Warren" "Rochester" "Hattiesburg" "Springfield" "Great Falls" "Bellevue" "North Las Vegas" "Concord" "Paterson" "Rio Rancho" "Rochester" "Greensboro" "Grand Forks" "Cincinnati" "Norman" "Salem" "Allentown" "Cranston" "North Charleston/Greenville" "Aberdeen" "Knoxville" "Dallas" "Provo" "South Burlington" "Chesapeake" "Tacoma" "Parkersburg" "Green Bay" "Laramie")

echo ${#firstBig[@]}
echo ${#secondbig[@]}
echo ${#thirdbig[@]}

#for j in `seq  3`;do
    for i in "${firstBig[@]}"; do   # The quotes are necessary here
        ./main.py_onestate --location="$i" --term="century 21"  --maxrow=1000 --writeto="./output_1/${i}.log"
        sleep 1;
    done
    for i in "${secondbig[@]}"; do   # The quotes are necessary here
        ./main.py_onestate --location="$i" --term="century 21"  --maxrow=1000 --writeto="./output_2/${i}.log"
        sleep 1;
    done
    for i in "${thirdbig[@]}"; do   # The quotes are necessary here
        ./main.py_onestate --location="$i" --term="century 21"  --maxrow=1000 --writeto="./output_3/${i}.log"
        sleep 1;
    done
#done;
