import os

ip = str(input("Please write the IP to broadcast the video, in quotes [ex: '127.0.0.1']:\n"))

print("Now you will see the streaming using the selected IP")

os.system("ffmpeg -re -i BBB_160x120.mp4 -c:v copy -f flv udp://"+ip+":135")