import yt_dlp
import os
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
  yt_lock = "yt.lock"
  if os.path.exists(yt_lock):
    os.remove(yt_lock)
    print("got lock")
    url=sys.argv[1]
    name=sys.argv[2]
    ytdlp4(url,name)
    with open("yt.lock", "w") as file:
      file.write("yt_dlp mission lock\n")
    print("Lock returned successfully")
  else:
      print("No lock can get！")
      print("Something went wrong")