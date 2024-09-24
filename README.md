# Convert MP4 to MP3 Script

This script converts all `.m4a` and `.m4p` audio files in a selected directory to `.mp3` format using `ffmpeg`, and then deletes the original `.m4a` and `.m4p` files.

## Requirements

- Python 3.x
- `ffmpeg` installed and available in your system's PATH

## Installation

1. **Install Python 3.x**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Install ffmpeg**:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and follow the installation instructions.
   - **macOS**: Install via Homebrew: `brew install ffmpeg`
   - **Linux**: Install via your package manager, e.g., `sudo apt-get install ffmpeg` for Debian-based systems.

## Usage

1. **Clone or download this repository** to your local machine.

2. **Run the script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Execute the script with Python:
     ```sh
     python convert-mp4-to-mp3.py
     ```

3. **Select the directory** containing the `.m4a` and `.m4p` files when prompted by the file dialog.

4. The script will:
   - Recursively find all `.m4a` and `.m4p` files in the selected directory.
   - Convert each file to `.mp3` format using `ffmpeg`.
   - Delete the original `.m4a` and `.m4p` files.

## Notes

- Ensure `ffmpeg` is correctly installed and accessible from the command line.

## License

This project is licensed under the MIT License.