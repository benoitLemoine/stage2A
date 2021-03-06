import os
import cv2 as cv

folderPath = "../../../resources/CP_dataset/data"

folders = os.listdir(folderPath)

resFile = open(folderPath + "/info.txt", "w+")
for f in folders:
    videoName = f.split("/")[-1] + ".mp4"
    videoPath = folderPath + "/" + f + "/" + videoName
    cap = cv.VideoCapture(videoPath)

    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv.CAP_PROP_FPS)

    resFile.write("{}   {}  {}  {}  {}\n".format(videoName, width, height, frames, fps))
    cap.release()

resFile.close()
