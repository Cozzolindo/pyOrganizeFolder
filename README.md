# File Organizer

A Python script that automatically organizes files in a directory by their file types.

## Features

- Organizes files into folders based on their extensions
- Supports multiple file categories:
  - **VIDEO**: mp4, avi, mkv, mov, wmv, flv, webm, m4v, mpg, mpeg
  - **AUDIO**: mp3, wav, flac, aac, ogg, wma, m4a, opus
  - **IMAGE**: jpg, jpeg, png, gif, bmp, tiff, svg, webp, ico
  - **DOCUMENT**: pdf, doc, docx, txt, rtf, odt, pages
  - **SPREADSHEET**: xls, xlsx, csv, ods, numbers
  - **PRESENTATION**: ppt, pptx, odp, key
  - **ARCHIVE**: zip, rar, 7z, tar, gz, bz2, xz
  - **EXECUTABLE**: exe, msi, deb, rpm, dmg, app
  - **CODE**: py, js, html, css, java, cpp, c, php, rb, go, rs
  - **DATA**: json, xml, yaml, yml, sql, db, sqlite
  - **OTHERS**: any file type not listed above

- Handles file name conflicts by adding numbered suffixes
- Provides a detailed summary of organized files
- Safe operation with user confirmation prompt

## Usage

1. **Copy the script to the directory you want to organize**
   ```bash
   cp file_organizer.py /path/to/directory/to/organize/
   cd /path/to/directory/to/organize/
   ```

2. **Run the script**
   ```bash
   python file_organizer.py
   ```

3. **Confirm the operation when prompted**
   The script will ask for confirmation before organizing files.

## Example

Before running:
```
my_folder/
├── file_organizer.py
├── vacation.mp4
├── song.mp3
├── document.pdf
├── photo.jpg
└── archive.zip
```

After running:
```
my_folder/
├── file_organizer.py
├── VIDEO/
│   └── vacation.mp4
├── AUDIO/
│   └── song.mp3
├── DOCUMENT/
│   └── document.pdf
├── IMAGE/
│   └── photo.jpg
└── ARCHIVE/
    └── archive.zip
```

## Safety Features

- The script excludes itself from being moved
- Creates folders only when needed
- Handles file name conflicts automatically
- Provides detailed logging of all operations
- Asks for user confirmation before proceeding

## Customization

You can easily customize the file categories by modifying the `file_categories` dictionary in the `organize_files()` function. Add new extensions or create new categories as needed.

## Requirements

- Python 3.6 or higher
- No additional packages required (uses only standard library)
