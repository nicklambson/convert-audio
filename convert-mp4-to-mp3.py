import subprocess
import os
from pathlib import Path
from tkinter import Tk, filedialog

def convert_and_delete_m4a_to_mp3(directory):
    # Recursively find all .m4a files in the directory
    audio_files = list(Path(directory).rglob('*.m4a')) + list(Path(directory).rglob('*.m4p'))
    
    for m4a_file in audio_files:
        mp3_file = m4a_file.with_suffix('.mp3')
        
        # Convert .m4a to .mp3 using ffmpeg
        subprocess.run(['ffmpeg', '-i', str(m4a_file), str(mp3_file)], check=True)
        
        # Delete the .m4a file
        if m4a_file.exists():
            m4a_file.unlink()

if __name__ == "__main__":
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()
    
    # Ask the user to select a directory
    directory = filedialog.askdirectory(title="Select Directory")
    
    if directory:
        convert_and_delete_m4a_to_mp3(directory)