from pytube import YouTube
from sys import argv, exit

def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    filledLength = int(50 * current)
    bar = '█' * filledLength + '-' * (50 - filledLength)
    print(f'\rDownloading |{bar}| {current:.0%}', end = '\r')

if len(argv) > 1 and argv[1]:
    pass
else:
    print('Command usage:\n python main.py <your youtube link>')
    exit()

link = str(argv[1])
yt = YouTube(link, on_progress_callback=progress_function)
what = str()

while what != 'mp3' or what != 'mp4':
    what = input('What do you want to download: MP3 or MP4?\n').lower()
    if what == 'mp3' or what == 'mp4':
        break
    print('Please enter a valid option.\n\n')

if what == 'mp3':
    audio = yt.streams.filter(only_audio=True).first()
    print('Downloading audio...')
    audio.download(output_path=f'./Downloaded Audios')
    print('\nDownloaded successfully!')

elif what == 'mp4':
    for stream in yt.streams:
        print(stream.resolution)
    res = input("Enter the resolution you want to download: ")
    stream = yt.streams.filter(res=res).first()
    print('Downloading video...')
    stream.download(output_path="./Downloaded Videos")
    print('\nDownloaded successfully!')
