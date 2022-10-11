import tkinter, os

window = tkinter.Tk()
window.geometry("1000x1000")
window.title("Mass YouTube Downloader") 

font = ("Courier", 12, "bold")
download_formats = { "MP3" : "mp3",
                    "MP4" : "mp4", }


url_var=tkinter.StringVar()
download_format_var=tkinter.StringVar()
# url_var=tkinter.StringVar()

def download():
  url = url_var.get()
  format = download_format_var.get()
  
  if format == 'mp3':
    format = '--audio-format' + format 
  os.system(f"youtube-dl -x {format} --retries 10 --ignore-errors  {url}")


url_input = tkinter.Entry(window, width=50, textvariable = url_var, font=font)
url_input.insert(0, 'https://www.youtube.com/watch?v=zaBy3X37Oa8')
url_input.pack(side='top', ipady=5)
for (text, value) in download_formats.items():
  tkinter.Radiobutton(window, text = text, font=font, variable = download_format_var, value = value).pack(side='top', ipady=5)


download_button = tkinter.Button(window, text='Download', font=font, command = download).pack(side='top', ipady=5)


# sample_text.configure(font = font)

window.mainloop()