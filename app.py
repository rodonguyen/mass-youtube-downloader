import tkinter, os, threading
import subprocess
from turtle import down

from numpy import full

window = tkinter.Tk()
window.geometry("600x400")
window.title("Mass YouTube Downloader") 

font = ("Courier", 12, "bold")
download_formats = {  "Audio" : "audio",
                      "Video" : "video", }


url_var=tkinter.StringVar()
download_format_var=tkinter.StringVar()
# url_var=tkinter.StringVar()

def download():
  url = url_var.get()
  format = download_format_var.get()
  
  if format == 'audio':
    format = "-x --audio-format mp3"
  if format == 'video':
    # format = "-f 'mp4[filesize<10M]+bestaudio/bestvideo[filesize<50M]+bestaudio'"  # Limit filesize
    format = "-f 'mp4+bestaudio/bestvideo+bestaudio'" 

  full_command = f"youtube-dl {format} --retries 10 --ignore-errors {url}"

  print(full_command)
  os.system(full_command)
  # print('===> ' + subprocess.check_output(full_command.split(' ')))

def run_background(afunction, args=()):
  thread = threading.Thread(target=afunction, args=args)
  thread.start()


# Label
label = tkinter.Label(window, text='Enter URL of a video/playlist:')
label.grid(row=0,column=0)

# Entry
url_input = tkinter.Entry(window, width=50, textvariable = url_var, font=font)
url_input.insert(0, 'https://youtu.be/HQXPxR6yZoA')
url_input.grid(row=1,column=0)
row_count=2

# Radio buttons  x 2
for (text, value) in download_formats.items():
  tkinter.Radiobutton(window, text = text, font=font, variable = download_format_var, value = value).grid(row=row_count,column=0)
  row_count += 1

# Button
download_button = tkinter.Button(window, text='Download', font=font, command = lambda : run_background(download)).grid(row=row_count,column=0)




window.mainloop()
# https://www.geeksforgeeks.org/python-tkinter-tutorial/#basic