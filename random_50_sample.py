import csv
import os,os.path
import random

label_num=[0,57,46,53,52,102,54,72,950,157,170,57,64,144,67]

flow_txt=[]
rand_list=[]
label=[]

count=50

with open('trimmed_ucfcrimes_flow.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        flow_txt.append(row)

    #print(flow_txt[0])

    label.append(flow_txt[label_num[0]:label_num[1]])

    for i in range(13):
        label.append(flow_txt[ sum(label_num[1:i+2]):sum( label_num[1:i+3] ) ] )

    #for row in label:
     #   print(len(row))

    rand_list.append(random.sample(label[0],50))
    rand_list.append(label[1]+random.sample(label[1],4))
    for i in range(2,14):
        rand_list.append(random.sample(label[i],50))

with open('trimmed_ucfcrimes_classification_list.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)

    for i in range(14):
        spamwriter.writerows(rand_list[i])
