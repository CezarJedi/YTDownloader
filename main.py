import yt_dlp # pip install yt-dlp

url = input("Enter YouTube URL: ")

ydl_opts = {
    'format': 'best[ext=mp4]/best', 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# yea thats it :)