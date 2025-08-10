# 🧼 CleanHtmlTable
by Tom Salaj

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/tom591/CleanHtmlTable?tab=MIT-1-ov-file)
[![Demo](https://img.shields.io/badge/demo-vycistihtml.cz-brightgreen)](https://vycistihtml.cz)

---

📝 The live demo is available in **Czech** at the link above.

**CleanHtmlTable** is a web application designed to clean HTML code by removing unwanted styles and unnecessary elements.

---

## ⚡ Quick Demo of Simplicity

This project is a minimal demonstration of what Flask can do — the core logic fits in just **40 lines of Python**  
(and could be even shorter 😄).

---

## 🛠️ About the App

A small and simple **Flask (Python)** web app built to sanitize styled HTML tables.  
It strips away unwanted attributes and inline styles — some of which can be re-enabled via checkboxes.

---

## 📦 Dependencies

Only **three modules** are needed:

- `Flask` – web framework  
- `beautifulsoup4` – HTML parsing and cleaning  
- `Flask-WTF` – used only for basic CSRF protection ([Flask-WTF docs](https://flask-wtf.readthedocs.io))

---

## 🎨 Frontend

The template uses CSS styles imported from **[w3schools.com](https://www.w3schools.com/w3css/)** —  
meaning it’ll survive even the end of the world 😄  
Inline styles ensure basic mobile responsiveness.

---

## 📸 Screenshots

### 🖥️ Fullscreen view
![CleanHtmlTable Fullscreen](screen_full.png)

### 📱 Responsive view (mobile/tablet)
![CleanHtmlTable Responsive](screen_responsive.png)

---

## ▶️ Getting Started

To run locally:

1. Download or clone the repository  
2. Install dependencies using pip:  
   ```bash
   pip install -r requirements.txt
   ```
3. In the app folder, start the server:  
   ```bash
   flask run
   ```
4. Done! Nothing more, nothing less.

---

## 🪪 License

Licensed under the **MIT License** — you're free to:

- use it  
- modify it  
- extend it  
- integrate it (e.g. with a WYSIWYG editor to paste tables from Word or Excel)

---

## 🚀 Final Words

**Learn, code, enjoy — good luck!**  
*Tom Salaj*
