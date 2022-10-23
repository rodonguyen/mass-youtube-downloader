import os


old_playlist = "https://www.youtube.com/playlist?list=PLqOHj6mtp1CJrDAgTksXU-v5Y_2hIRimd"
newday_playlist = "https://www.youtube.com/playlist?list=PLqOHj6mtp1CKMkoQ50hm-S7FSoLXVPFgi"


# os.system(f"youtube-dl -x --audio-format mp3 --playlist-start 1 --playlist-end 80  {newday_playlist}")
# os.system(f"youtube-dl -x --audio-format mp3 --retries 10 --ignore-errors --playlist-start 396  {newday_playlist}")
# os.system(f"youtube-dl -x --audio-format mp3 --yes-playlist --get-duration   https://www.youtube.com/playlist?list=PLqOHj6mtp1CKQfXFRvi-FK__vkveQMrt1")


# To get started
#   Open Power Shell as Admin
#   Install Choco package manager/installer: Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
#   Install 2 required packages: choco install ffmpeg youtube-dl