# Mass Youtube Downloader
with User Interface and various downloading options.

## With **Mass Youtube Downloader**, you can:
- Download video/audio from YouTube
- **Mass** download from a playlist
- Filter your download by durations of the videos


## To get started
### 1. For Window
- Open "Power Shell" app as Admin
- Install Choco package manager/installer: `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
- Install 2 required packages: `choco install ffmpeg youtube-dl`

<br>
## Package required: 
- [download_dl](http://ytdl-org.github.io/youtube-dl/download.html) (their [GitHub repo](https://github.com/ytdl-org/youtube-dl))
- ffmpeg