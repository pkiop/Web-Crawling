import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=aBxsREZinYA") #다운 받을 동영상 URL 지정
videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) :  # range (1, 6) 1 이상 6 미만
    print(i, ' , ', videos[i])

down_dir = "D:/section2_name/youtube"

videos[0].download(down_dir)
