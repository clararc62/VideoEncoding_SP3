import os

class Codecs:
    def __init__(self,video):
        self.video = video

    def VP8(self):
        # convert to VP8
        os.system(
            "ffmpeg -i " + self.video + " -c:v libvpx -b:v 1M -c:a libvorbis " + self.video[1:-5]+"_vp8.webm")

    def VP9(self):
        # convert to VP9
        os.system(
            "ffmpeg -i " + self.video + " -c:v libvpx-vp9 -c:a libopus " + str(
                self.video[1:-5])+"_vp9.webm")

    def h265(self):
        # convert to h265
        # we obtain HEVC (High Efficiency Video Coding
        os.system(
            "ffmpeg -i "+ self.video +" -c:v libx265 -c:a copy -x265-params crf=25 "+ self.video[1:-5] + "_h265.mov")


    def avi(self):
        # convert to avi
        os.system("ffmpeg -i " + self.video + " -vcodec copy -acodec copy " + str(
            self.video[1:-5]) + "_avi.avi")



print("You have de following possible videos:\n"
      "BBB_720.mp4\n"
      "BBB_480.mp4\n"
      "BBB_360x240.mp4\n"
      "BBB_160x120.mp4\n")

video= str(input(
    "Insert the name of the video that you want to convert, in quotes:\n"))

print("1 = VP8\n"
      "2 = VP9\n"
      "3 = h265\n"
      "4 = AV1")
conv = int(input("select which type of conversion you want [1,2,3,4]\n"))

vid = Codecs(video)

# the name of the new videos are BBB_resolution_codec
if conv == 1:
    vid.VP8()
if conv == 2:
    vid.VP9()
if conv == 3:
    vid.h265()
if conv == 4:
    vid.avi()
