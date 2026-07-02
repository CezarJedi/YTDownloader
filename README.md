# YouTube Video Downloader

A simple Python script to download videos at the highest quality using `yt-dlp`. 

## What it does
- Downloads the best available video and audio quality.
- Automatically merges them into a single file (requires FFmpeg).
- Works with YouTube and most other video platforms.

## How to use it
1. Install the library: `pip install yt-dlp`
2. **Important:** Install [FFmpeg](https://ffmpeg.org/) on your system so the video and audio combine correctly.
3. Run the script: `python main.py`
4. Paste the link when prompted.

## Note
If you don't have FFmpeg installed, you will see two separate files (one for video, one for audio). Installing FFmpeg fixes this automatically.