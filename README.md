# Mass Youtube Downloader
With **Mass Youtube Downloader**, you can:
- Download video/audio from YouTube from a User Interface
- **Mass** download from a playlist
- Filter your download by durations of the videos (in development)

## Instructions
1. Download the app
    ```bash
    git clone https://github.com/rodonguyen/mass-youtube-downloader 
    cd mass-youtube-downloader
    ```

2. In the app directory, enter this command  to run the app:  
    ```bash
    ./dist/app
    ```

3. The app should appear on your screen:
  ![main interface](public/main_interface.png)

1. Paste the link of the video you want to download
1. Choose either audio/video
1. Click Download. This will create a thread and start downloading. You can view the progress in the command. You can also download another file if you wish to and all your downloading will run parallelly.


## Further development
- Migrate to PyQt5
- Option to ignore files whose sizes are out of allowed range
- Option to choose downloading format, resolution, audio quality


<br>

## To get started
### Package required: 
- [download_dl](http://ytdl-org.github.io/youtube-dl/download.html) (their [GitHub repo](https://github.com/ytdl-org/youtube-dl))
- ffmpeg

### For Window
- Open "Power Shell" app as Admin
- Install Choco package manager/installer: `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
- Install 2 required packages: `choco install ffmpeg youtube-dl`


## Others
### Generate an executable file
1. Generate: `pyinstaller --onefile app.py`
1. Execute that file:  `./dist/app`



