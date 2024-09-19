import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from downloader import download_video

def update_button_text(*args):
    download_button.config(text = f"Download {format_var.get()}")

# Main
root = tk.Tk()
root.title("YouTube Video Downloader")

# Entry field for the URL input
tk.Label(root, text = "Enter YouTube Video URL:").pack(pady = 10)
url_enter = tk.Entry(root, width = 50)
url_enter.pack(pady = 10)

# Dropdown box for Video Quality
tk.Label(root, text = "Select Video Quality:").pack(pady = 10)
quality_var = tk.StringVar(value = '1080')
quality_option = ['360', '480', '720', '1080', '1440', '2160']
quality_dropdown = ttk.Combobox(root, textvariable = quality_var, values = quality_option)
quality_dropdown.pack(pady = 10)

# Dropdown box for File Format
tk.Label(root, text = "Select File Format:").pack(pady = 20)
format_var = tk.StringVar(value = "Video")
format_options = ['Audio', 'Video', 'GIF']
format_dropdown = ttk.Combobox(root, textvariable = format_var, values = format_options)
format_dropdown.pack(pady = 10)

format_var.trace_add("write", update_button_text)

# Button to download the video
def on_download():
    
    url = url_enter.get()
    quality = quality_var.get()
    file_format = format_var.get()
    
    file_path = filedialog.asksaveasfilename(
        defaultextension = 'mp4',
        filetypes = [("MP4 files", "*.mp4"), ("MP3 files", "*.mp3"), ("GIF files", "*.gif")],
        title = "save as"
    )
    
    download_video(url, quality, file_format, file_path)
    
download_button = tk.Button(root, text = f"Download {format_var.get()}", command = on_download)
download_button.pack(pady = 20)

root.mainloop()