import yt_dlp # pip install yt-dlp

url = input("Enter YouTube URL: ")

ydl_opts = {
    # 'format': 'best[ext=mp4]/best', lower quality
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])