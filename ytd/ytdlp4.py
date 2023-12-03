import yt_dlp
import sys
def ytdlp4(url,name):
  url = url
  ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl':name+'.mp4',
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
if __name__=='__main__':
  url=sys.argv[1]
  name=sys.argv[2]
  ytdlp4(url,name)