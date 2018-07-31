import cv2
import csv
import random


video_dir = '/datahdd/Dataset/UCF_Crimes/Videos/Normal_Videos_event/'
save_dir = '/datahdd/Dataset/Trimmed_UCF_Crimes/Normal_Videos_event/'

save_txt = []

with open('normal.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # row[ ] ->  0:videoname
        # directory
        video_fulldir = video_dir + row[0]
        save_fulldir = save_dir + row[0][0:-8] + 'trimmed.mp4'

        # ready to load & save video
        cap = cv2.VideoCapture(video_fulldir)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(save_fulldir, fourcc, 30, (320, 240))

        # random start & range
        num = int(cap.get(7)) #get the number of frames
        start = random.randrange(1,num-59) # at least 2 sec
        range_ = random.randrange(60,num - start)
        end = start + range_

        cap.set(1, start)
        for i in range(range_):
            ret, frame = cap.read()
            if (ret):
                # cv2.imshow('frame',frame)
                out.write(frame)
        print(row[0] + ' complete')
        out.release()


        #print(row[0])
        #print('total frame = ' + str(num))
        #print('start frame = ' + str(start))
        #print('end frame = ' + str(end))
        #print('')

        save_txt.append([row[0],str(start),str(end)])

        cap.release()
        cv2.destroyAllWindows()


with open('normal_rand_frames.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerows(save_txt)
