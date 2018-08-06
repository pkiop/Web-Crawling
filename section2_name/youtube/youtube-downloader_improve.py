import pytube
import os
import subprocess # 파이썬을 실행하면서 별도의 프로세스를 생성하면서 터미널이나 커맨드 실행하고 반환 값 받아올 수 있다.

url = input("주소 입력하세요 : ")
yt = pytube.YouTube(url) #다운 받을 동영상 URL 지정
videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) :  # range (1, 6) 1 이상 6 미만
    print(i, ' , ', videos[i])

cNUM = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "D:/section2_name/youtube"

videos[cNUM].download(down_dir)

ch = input("mp3 변환 ? : ")
if ch == "Y" :
    #원본 동영상 이름 필요하다
    newFileName = input("변환 할 mp3 파일명은?")
    OriFileName = videos[cNUM].default_filename

    #여기서 command 에서 날렸던 명령어를 그대로 써주면 된다.
    subprocess.call(['ffmpeg', '-i',
        os.path.join(down_dir, OriFileName),
        os.path.join(down_dir, newFileName)
    ])

print("동영상 다운로드 및 mp3 변환 완료!")
