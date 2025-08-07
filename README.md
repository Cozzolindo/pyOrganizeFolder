# pyOrganizeFolder 🗃️✨

**A simple yet powerful Python tool to intelligently organize your files by type.**

---

## 🚀 Project Overview

**pyOrganizeFolder** is a clean, user-centric script that streamlines file organization by automatically sorting files into categorized folders—ideal for creatives, students, professionals, or anyone looking to tame a messy desktop.

---

##  Features at a Glance

- **Smart Categorization** — Sorts into relevant folders like **VIDEO**, **AUDIO**, **IMAGE**, **DOCUMENT**, **SPREADSHEET**, **PRESENTATION**, **ARCHIVE**, **EXECUTABLE**, **CODE**, **DATA**, and **OTHERS**.
- **Safe & Non-Destructive** — The script intelligently avoids moving itself, asks for user confirmation before proceeding, and only creates folders as needed.
- **Conflict Handling** — Automatically resolves naming clashes by appending numbered suffixes.
- **Transparent Summary** — Presents a detailed log of what’s being moved, ensuring full visibility.
- **Highly Customizable** — Simply tweak the `file_categories` dictionary in `organize_files()` to suit your file types and preferences.
- **Zero Dependencies** — Built using only Python’s standard library (requires Python 3.6+), making it lightweight and easy to use.

---

##  Quick Start Guide

1. **Download:**  
   Copy `pyOrganizer.py` into the directory you want to organize.

2. **Run the Script:**  
   ```bash
   cd /path/to/your-folder
   python pyOrganizer.py
   ```

3. **Confirm:**  
   The script will prompt for confirmation—just confirm and watch the transformation unfold.

---

##  Example in Action

**Before:**
```
my_folder/
├── pyOrganizer.py
├── vacation.mp4
├── song.mp3
├── document.pdf
└── photo.jpg
```

**After:**
```
my_folder/
├── pyOrganizer.py
├── VIDEO/
│   └── vacation.mp4
├── AUDIO/
│   └── song.mp3
├── DOCUMENT/
│   └── document.pdf
└── IMAGE/
    └── photo.jpg
```

---

##  Customization Tips

Easily adapt to your needs:

```python
file_categories = {
    "VIDEO": [".mp4", ".avi", ...],
    "ARCHIVE": [".zip", ".rar", ...],
    "PROJECT": [".psd", ".ai", ".blend"]  # Example new category
}
```

Pro Tip: Keep extensions lowercase for consistent matching.

---

##  Why This Stands Out

- **Efficient** – Organizes scattered files in seconds.
- **Intuitive** – Requires no installations—just run it where you need.
- **Adaptable** – Add or modify categories to personalize.
- **Reliable** – Built with safety checks for peace of mind.
- **Portfolio-Ready** – Demonstrates clean scripting, usability, and attention to user experience.

---

##  Who Should Care?

- **Recruiters & Hiring Managers** – A clear example of well-structured, maintainable code with real-world utility.
- **End-users** – A hassle-free way to sort files, whether for daily organization or big cleanup sessions.
- **Other Developers** – A great starting point to build upon—add GUI, add-more logic, integrate scheduling, or extend functionality.

---

##  Contribution & Future Roadmap

**Want to help?**

- Add support for more customized categories (e.g. design files, e-books, archives of specific types).
- Build a scheduling or CLI interface.
- Add support for nested folder structures or intelligent tagging.

Contributions, feature ideas, and feedback are deeply appreciated!

---

## 🧑‍💻 Author

Developed by [Carlos Cozzolino](https://github.com/Cozzolindo)  
Back-End Developer | Passionate about clean code, design patterns, and full-stack engineering.

---

## 📫 Contact

- GitHub: [@Cozzolindo](https://github.com/Cozzolindo)
- LinkedIn: [linkedin.com/in/carloscozzolino](https://linkedin.com/in/carloscozzolino)

---

## ⭐️ If you like this project

Give it a star ⭐ on GitHub to show support and follow for more updates!
