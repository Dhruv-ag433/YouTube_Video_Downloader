from tkinter import messagebox
import yt_dlp
import os
import subprocess
import logging

logging.basicConfig(level=logging.WARNING, filename='app.log',
                    format = '%(asctime)s - %(levelname)s - %(message)s')

def check_ffmpeg():
    
    try:
        subprocess.run(['ffmpeg', '-version'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        return True
    except FileNotFoundError:
        logging.warning("FFmpeg not found. Install it from https://www.gyan.dev/ffmpeg/builds/")
        return False
    
# To convert Video into GIF    
def convert_to_gif(filepath):
    gif_output = filepath.replace('.mp4', '.gif')
    command = f'ffmpeg -i "{filepath}" -vf "fps=10,scale=320:-1" "{gif_output}"'
    os.system(command)
    messagebox.showinfo("GIF Conversion", f"GIF saved as {gif_output}")

def download_video(url, quality, file_format, file_path):
    
    if not check_ffmpeg():
        messagebox.showerror("FFmpeg Error",
                             "FFmpeg is not installed or not found in the system PATH.\n"
                             "Please download it from: https://www.gyan.dev/ffmpeg/builds/")
        return 
    
    if not url:
        messagebox.showerror("Input Error", "Please enter a URL.")
        return
    
    if not file_path:
        messagebox.showerror("Save Error", "No file path selected.")
        return
    
    try:
        if file_format == 'Audio':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': file_path,
                'postprocessor': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
        elif file_format == 'GIF':
            ydl_opts = {
                'format': f'bestvideo[height <= {quality}]+bestaudio/best',
                'outtmpl': file_path,
            }
        else:
            ydl_opts = {
                'format': f'bestvideo[height <= {quality}]+bestaudio/best',
                'outtmpl': file_path,
                'merge_output_format': 'mp4'
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
           
        if file_format == 'GIF':
            convert_to_gif(file_path)
            
        messagebox.showinfo("Success", "Download Complete")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occured: {e}")