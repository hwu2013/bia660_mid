from subprocess import call
import os.path,subprocess
import time
import re

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New_Hampshire","New_Jersey","New_Mexico","New_York","North_Carolina","North_Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode_Island","South_Carolina","South_Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West_Virginia","Wisconsin","Wyoming"]

#echo ${#firstBig[@]}
#echo ${#secondbig[@]}
#echo ${#thirdbig[@]}

#        ./main.py_onestate --location="$i" --term="century 21"  --maxrow=1000 --writeto="./output_1/${i}.log"

for s in states:
    with open(s+".txt_2") as f:
            content = f.readlines()
            totalreview = 0.
            totalrate = 0.
            avgreview =0.
            avgrate = 0.
            #print content
            for l in content:
                #pattern = r"(?:^| )([a-zA-Z0-9][\w.+]*)@([\w.]+)\.(\w{1,3})\b"
                pattern=r"rating:([0-9.]+), review_count:([0-9.]+)\n"
                result = re.search(pattern, l)
                if None == result:
                    continue
                else:
                    #print result.group(1),result.group(2)
                    totalrate = totalrate+ float(result.group(1))
                    #print totalreview+float(result.group(2))
                    totalreview = totalreview+float(result.group(2));
            if len(content) != 0:
                avgreview = totalreview/(len(content)+0.)
                avgrate = totalrate/(len(content)+0.)
            print 'num:{0:3},treview:{1:6.2f},trate:{2:6.2f},areview:{3:6.2f},arate:{4:6.2f}'.format(len(content),
                                                                                         totalreview,
                                                                                         totalrate,
                                                                                         avgreview,
                                                                                         avgrate)
            #print s,"|number:",len(content), "|total review:", totalreview,"|total rate:", totalrate, "|avg review:",avgreview, "|avg rate:",avgrate

