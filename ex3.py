import os

print("Now you will see the streaming using the localhost")
os.system("ffmpeg -re -i BBB_160x120.mp4 -c:v copy -f flv udp://@localhost:135")

