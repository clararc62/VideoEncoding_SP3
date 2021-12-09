# VideoEncoding_SP3

Here we find the exercises for SP3 of Video Encoding Systems. 
There are 4 exercises, each in different scripts and all of them can be run by main.py. 
It is necessary to have downloaded the Big Buck Bunny videos at different resolutions, that can be found in the repository.

The user can select the video of the resolution he wants. However, in order to provide some outputs, I have 
selected to work with 'BBB_720.mp4' video. Hence, we can find it in VP8, VP9, h265 & AV1 as it was asked in exercise 1.

For exercise 2, the user has again all the possible options to choose which videos want to do the comparision.
In my case, I selected vp8 vs avi, which is called 'join_vp8avi_s.mp4'. In it we can see the two different resolutions
that the codecs can offer, since we watch the two videos one next to the other. 
The one that has more quality is the vp8 one, since the resolution is much clearer. On the other hand, in the 
avi video the squares of the pixels can be distinguished providing a bad quality. 
The avi file is lossless, which results in immensely larger file sizes. In this case, the BBB_720_vp8 has a size of
1.769kb while the BBB_720_avi occupies 2.719kb. 

For exercise 3 and 4, we are able to create a live streaming. In ex3 the @localhost is used, while in ex4 the 
user has the possibility to select the IP. 
