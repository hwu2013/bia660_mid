for i in `ls *.txt`;do
    sed '/^ *$/d' $i > ${i}_1
    sed '/^\s*CATEGORIES:.*$/d' ${i}_1 > ${i}_2
done; 

