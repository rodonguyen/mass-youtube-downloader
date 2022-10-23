import tkinter, os, threading
from tkinter import ttk

font = ("Courier", 20, "bold")
download_formats = {  "Audio" : "audio",
                      "Video" : "video", }

style = ttk.Style()
style.configure("TRadiobutton", foreground="black", background="gray", font=font)


def download():
  url = url_var.get()
  format = download_format_var.get()
  
  if format == 'audio':
    format = "-x --audio-format mp3"
  if format == 'video':
    # format = "-f 'mp4[filesize<10M]+bestaudio/bestvideo[filesize<50M]+bestaudio'" 
    format = "-f 'mp4+bestaudio/bestvideo+bestaudio'" 

  full_command = f"youtube-dl {format} --retries 10 --ignore-errors {url}"

  print(full_command)
  os.system(full_command)
  # print('===> ' + subprocess.check_output(full_command.split(' ')))

def run_background(afunction, args=()):
  thread = threading.Thread(target=afunction, args=args)
  thread.start()



# Window
# now = tkinter.Tk()
window = tkinter.Tk()
window.geometry('400x300')
window.title("Mass YouTube Downloader") 

url_var=tkinter.StringVar(window)
download_format_var=tkinter.StringVar(window)
# url_var=tkinter.StringVar()

# Entry
url_input = ttk.Entry(window, width=50, textvariable = url_var, font=font)
url_input.insert(0, 'https://youtu.be/FIhonBl-_pM')
url_input.grid(row=0,column=0)
row_count=1

# Radio buttons  x 2
for (text, value) in download_formats.items():
  ttk.Radiobutton(window, text = text, variable = download_format_var, value = value).grid(row=row_count,column=0)
  row_count += 1

# Download Button
download_button = ttk.Button(window, text='Download', command = lambda : run_background(download)).grid(row=4,column=0)

window.mainloop()
# https://www.geeksforgeeks.org/python-tkinter-tutorial/#basic

