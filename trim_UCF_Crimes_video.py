import cv2
import csv

video_dir = '원본 영상 저장 경로'
video_label = ['Abuse','Arrest','Arson','Assault','Burglary','Explosion','Fighting','Normal_Videos_event','RoadAccidents','Robbery','Shooting','Shoplifting','Stealing','Vandalism'] # 14 classes
save_dir = '저장될 폴더 경로'

with open('filelist.csv', newline='|') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # row[ ] ->  0:videoname , 1:label , 2:start1 , 3:end1 , 4:start2 , 5:end2

        #directory
        video_fulldir = video_dir + video_label[int(row[1])-1] + '/' + row[0]
        save_fulldir = save_dir + video_label[int(row[1])-1] + '/' +row[0][0:-8]+'trimmed_1.mp4'
        save_fulldir2 = save_dir + video_label[int(row[1])-1] + '/' +row[0][0:-8]+'trimmed_2.mp4'


        #ready to load & save video
        cap = cv2.VideoCapture(video_fulldir)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(save_fulldir,fourcc, 30 ,(320,240))


        #check selected range of frame
        diff = int(row[3]) - int(row[2])

        #1st trim
        cap.set(1, int(row[2]))
        for i in range(diff):
            ret, frame = cap.read()
            if(ret):
                #cv2.imshow('frame',frame)
                out.write(frame)
        print(row[0] + ' 1 complete')
        out.release()

        #2nd trim
        if(int(row[4]) != -1 ):
            out2 = cv2.VideoWriter(save_fulldir2, fourcc, 30, (320, 240))
            diff = int(row[5]) - int(row[4])
            cap.set(1, int(row[4]))
            for i in range(diff):
                ret, frame = cap.read()
                if(ret):
                    #cv2.imshow('frame', frame)
                    out2.write(frame)
            print(row[0] + ' 2 complete')
            out2.release()

        cap.release()
        cv2.destroyAllWindows()
