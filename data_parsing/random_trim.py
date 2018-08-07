import cv2
import csv
import random


video_dir = '/datahdd/Dataset/UCF_Crimes/Videos/Training_Normal_Videos_Anomaly/'
save_dir = '/datahdd/Dataset/Trimmed_UCF_Crimes/Normal/'
save_txt = []

with open('normal_training.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # row[ ] ->  0:videoname
        # directory
        video_fulldir = video_dir + row[0]

        save_fulldir = save_dir + 'Normal_Videos_' + row[0][13:-8] + 'trimmed.mp4'  # training_normal_anomaly

        # ready to load & save video
        cap = cv2.VideoCapture(video_fulldir)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(save_fulldir, fourcc, 30, (320, 240))

        # random start & range
        num = int(cap.get(7)) #get the number of frames
        start = random.randrange(1,num-60) # at least 2 sec
        if (num - start > 2500 ):
            pp = 2500
        else :
            pp = num - start
        range_ = random.randrange(60,pp)
        end = start + range_

        cap.set(1, start)
        for i in range(range_):
            ret, frame = cap.read()
            if (ret):
                # cv2.imshow('frame',frame)
                out.write(frame)
        print(save_fulldir + ' complete')
        out.release()


        print('')

        save_txt.append([row[0],str(start),str(end),str(end-start)])

        cap.release()
        cv2.destroyAllWindows()


with open('normal_training_rand_frames.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerows(save_txt)




video_dir = '/datahdd/Dataset/UCF_Crimes/Videos/Testing_Normal_Videos_Anomaly/'
save_dir = '/datahdd/Dataset/Trimmed_UCF_Crimes/Normal/'
save_txt = []

with open('normal_test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # row[ ] ->  0:videoname
        # directory
        video_fulldir = video_dir + row[0]

        save_fulldir = save_dir + row[0][0:-8] + 'trimmed.mp4'  # test_normal_anomaly

        # ready to load & save video
        cap = cv2.VideoCapture(video_fulldir)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(save_fulldir, fourcc, 30, (320, 240))

        # random start & range
        num = int(cap.get(7)) #get the number of frames
        start = random.randrange(1,num-60) # at least 2 sec
        if (num - start > 2500 ):
            pp = 2500
        else :
            pp = num - start
        range_ = random.randrange(60,pp)
        end = start + range_

        cap.set(1, start)
        for i in range(range_):
            ret, frame = cap.read()
            if (ret):
                # cv2.imshow('frame',frame)
                out.write(frame)
        print(save_fulldir + ' complete')
        out.release()

        print('')

        save_txt.append([row[0],str(start),str(end),str(end-start)])

        cap.release()
        cv2.destroyAllWindows()


with open('normal_testing_rand_frames.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerows(save_txt)
