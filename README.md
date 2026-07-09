# 📸 Photo Duplicate Finder

A modern desktop application built with **Python** and **PySide6** to detect duplicate and visually similar photos, helping users organize large media collections efficiently.

> 🚧 **Project Status:** In active development

---

## ✨ Features

### ✅ Current Features

- 🔍 Scan folders recursively
- 📷 Detect duplicate images using **SHA-256**
- 🧠 Detect visually similar images using **Perceptual Hash (pHash)**
- 🖼️ Thumbnail previews
- 🔎 Full-size image preview
- ☑️ Select images to delete
- 🗑️ Move selected files to the Recycle Bin
- 📊 Scan statistics
- ⚡ Background scanning using **QThread**
- 🎨 Modern dark UI built with **PySide6**

---

## 🚀 Planned Features

- 🎥 Video duplicate detection
- 🤖 AI-powered similarity detection (CLIP)
- 📁 Smart duplicate recommendations
- 🔎 Search bar
- 📂 Filters
- ⭐ Favorite images
- 📊 Statistics dashboard
- 💾 SQLite cache
- ⚡ Multi-core scanning
- 📈 Real-time progress
- 🌙 Theme customization
- 🌍 Multi-language support

---

# 📷 Screenshots

> *(Coming soon)*

---

# 🏗️ Project Structure

```text
PhotoDuplicateFinder/

├── assets/
│
├── gui/
│   ├── components/
│   │   ├── duplicate_card.py
│   │   ├── sidebar.py
│   │   ├── thumbnail_widget.py
│   │   └── toolbar.py
│   │
│   ├── dialogs/
│   │   └── image_preview_dialog.py
│   │
│   ├── workers/
│   │   └── scan_worker.py
│   │
│   ├── styles.py
│   └── main_window.py
│
├── models/
│   └── file_info.py
│
├── services/
│   ├── delete_service.py
│   ├── duplicate_detector.py
│   ├── hashing.py
│   ├── image_hashing.py
│   ├── scanner.py
│   └── similar_image_detector.py
│
├── tests_files/
│
├── main.py
└── requirements.txt
```

---

# 🛠️ Technologies

- Python 3.12+
- PySide6
- Pillow
- OpenCV
- ImageHash
- NumPy
- Send2Trash

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/PhotoDuplicateFinder.git
```

Go to the project

```bash
cd PhotoDuplicateFinder
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# 📖 How it works

The application performs duplicate detection in multiple stages.

### 1️⃣ Exact Duplicate Detection

Uses **SHA-256** hashes.

```
Image
↓

SHA-256

↓

Compare

↓

Exact duplicate
```

---

### 2️⃣ Similar Image Detection

Uses **Perceptual Hash (pHash)**.

```
Image

↓

Perceptual Hash

↓

Hamming Distance

↓

Similar images
```

---

### 3️⃣ User Review

The application displays:

- Thumbnail
- Resolution
- File Size
- Full Preview
- Selection Checkbox

The user decides which files to remove.

---

# 🎯 Roadmap

## Version 0.2

- [x] Sidebar
- [x] Toolbar
- [x] Thumbnail cards
- [x] Image Preview
- [x] Background scanning
- [x] Safe deletion

---

## Version 0.3

- [ ] Real progress bar
- [ ] ETA
- [ ] Better duplicate grouping
- [ ] Better UI animations

---

## Version 0.4

- [ ] Video support
- [ ] Video thumbnails
- [ ] Video duplicate detection

---

## Version 0.5

- [ ] SQLite cache
- [ ] Faster scanning
- [ ] Multi-core processing

---

## Version 1.0

- [ ] AI Similarity Detection
- [ ] Smart Recommendations
- [ ] Dashboard
- [ ] Statistics
- [ ] Settings
- [ ] Installer
- [ ] Automatic Updates

---

# 🤝 Contributing

Contributions are welcome.

Feel free to submit Issues or Pull Requests.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Isaac Felipe Fonseca**

Bachelor's Degree in Systems Engineering

Passionate about:

- Data Analytics
- Business Intelligence
- Python Development
- Artificial Intelligence
- Desktop Applications

---

⭐ If you like this project, consider giving it a star!
