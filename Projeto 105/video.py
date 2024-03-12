import cv2
import os

path = "Images/"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)

print(size)

out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*'mp4v'), 0.8, size)

for i in range (count-1, 0, -1):
    frame =  cv2.imread(Images[i])
    cv2.imshow("nascer do Sol",frame)
    out.write(frame)
    print("Concluido")