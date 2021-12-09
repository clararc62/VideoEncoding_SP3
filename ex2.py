import os

print("720\n"
      "480\n"
      "360x240\n"
      "160x120")
res = str(input("Choose the resolution of the video you want to compare, write it in quotes:\n"))

print("0 = VP8\n"
      "1 = VP9\n"
      "2 = h265\n"
      "3 = AV1")

list1 = ['vp8','vp9','h265','avi']
list = ['_vp8.webm','_vp9.webm','_h265.mov','_avi.avi']

vid1 = int(input("select the first video you want to compare [0,1,2,3]\n"))
vid2 = int(input("select the second video you want to compare [0,1,2,3]\n"))

#swap variable names in order to match it with the subtitles later
if vid2<vid1:
    hola = vid1
    vid1=vid2
    vid2=hola

#it does not make sense to compare the same video
if vid1==vid2:
    print("It's the same video bro")

#here we create two outputs, one with the name of the codecs in each side of the screen and the other without it
else:
    print("You have chosen the comparision between %s and %s" %(list1[vid1], list1[vid2]))
    os.system(
        "ffmpeg -i BBB_" + res + list[vid1]+ " -i BBB_" + res + list[vid2]+ " -filter_complex hstack join_"+ list1[vid1]+ list1[vid2]+".mp4")
    os.system(
        "ffmpeg -i join_"+ list1[vid1]+ list1[vid2]+".mp4 -vf subtitles="+ list1[vid1]+'_'+list1[vid2]+".srt join_"+ list1[vid1]+ list1[vid2]+"_s.mp4")

