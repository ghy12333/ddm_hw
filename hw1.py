#question1
''the image is in the report''

#question2
i=1;
mkdir hw1;
cd hw1;
while(( $i<=256))
do 
 mkdir MSDM2023fall$i
 cd MSDM2023fall$i
 touch time_till_now.txt
 printf "nanoseconds since 1970-01-01 00:00:00 UTC: \n">>./time_till_now.txt
 printf "<`date`>">>./time_till_now.txt
 let "i++"
 cd ..
done

#question 3
import re
file_xml = open('/Users/apple/Downloads/blocklist.xml')
data_xml = file_xml.read()
no_template = r'blockID="i\d\d\d"'
id_template = r'id="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3}"(?![/\\ˆ])'
a = re.findall(no_template, data_xml)
b = re.findall(id_template, data_xml)
print(a)
print(b)

#question4
''github is set''


































