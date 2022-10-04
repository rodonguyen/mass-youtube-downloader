import youtube_dl

options = {
  'format': 'bestaudio/best',
  'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            # 'preferredquality': '192', 
            }]
}


with youtube_dl.YoutubeDL(options) as y:
  y.download(['https://www.youtube.com/watch?v=3QkAbPDuLSI'])