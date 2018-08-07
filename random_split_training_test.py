import csv
import random

csv_dir = '/datahdd/workdir/hyeongeun/temporal-segment-networks/'

save_txt1 = []
save_txt2 = []


class_txt=[]


with open('trimmed_ucfcrimes_classification_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        class_txt.append(row)

for i in range(7):
    tmp_= class_txt[50*2*i:50*(2*i+1)] # 2i 0 2 4 6 8 10 12 ...  2i+1 1 3 5 7 9 11 13
    tmp_1 = random.sample(tmp_,50)
    save_txt1.append(tmp_1[0:37])
    save_txt2.append(tmp_1[37:50])


    tmp_= class_txt[50*(2*i+1):50*(2*i+2)] # 1 3 5 7 9 11 13.... 2 4 6 8 10 12 14
    tmp_1 = random.sample(tmp_, 50)
    save_txt1.append(tmp_1[0:38])
    save_txt2.append(tmp_1[38:50])




with open('trimmed_ucfcrimes_trainingset.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(14):
        spamwriter.writerows(save_txt1[i])

with open('trimmed_ucfcrimes_testset.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(14):
        spamwriter.writerows(save_txt2[i])


print(len(save_txt1))
print(len(save_txt2))
