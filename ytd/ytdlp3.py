import yt_dlp
import sys
def ytdlp3(url,name):
  url = url
  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl':name,
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)


if __name__=='__main__':
  url=sys.argv[1]
  name=sys.argv[2]
  ytdlp3(url,name)