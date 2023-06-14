from pytube import YouTube
from sys import argv, exit
from tqdm import tqdm

if len(argv) > 1 and argv[1]:
    pass
else:
    print('Command usage:\n python main.py <your youtube link>')
    exit()

link = str(argv[1])
yt = YouTube(link)
what = str()

while what != 'mp3' or what != 'mp4':
    what = input('What do you want to download: MP3 or MP4?\n').lower()
    if what == 'mp3' or what == 'mp4':
        break
    print('Please enter a valid option.\n\n')

if what == 'mp3':
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(output_path=f'./Downloaded Audios')
    print('Downloaded successfully!')

elif what == 'mp4':
    for stream in yt.streams:
        print(stream.resolution)
    res = input("Enter the resolution you want to download: ")
    stream = yt.streams.filter(res=res).first()
    stream.download(output_path="./Downloaded Videos")
    print('Downloaded successfully!')
