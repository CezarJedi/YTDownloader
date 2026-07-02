import sys
import yt_dlp

if len(sys.argv) < 2:
    print("Error: Please provide a YouTube URL.")
    print("Usage: ytd <URL>")
    sys.exit(1)

url = sys.argv[1]

ydl_opts = {
    'format': 'bestvideo[fps=60]+bestaudio/bestvideo+bestaudio/best',
    'format_sort': ['fps', 'res'],
    'merge_output_format': 'mp4',
    'outtmpl': '~/Videos/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])