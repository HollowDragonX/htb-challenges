# HackTheBox Challenges Solutions

## 📘 About

This repository contains my solutions to HackTheBox challenges, organized by category. The scripts and write ups are meant for **educational purposes only**.

---

## 📂 Repository Structure

Each folder correspond to a category of HTB Challenges:

- `coding/`: Algorithmic and programming-based challenges. Each challenge in this category contains the following:
  -   📄 `challenge description`: Original challenge description.
  -   💻 `solution script`: Script used to solve the challenge.

---

## 🚀 Getting Started
The write-ups were made using `mkdocs-material` for a clean, navigable, and responsive experience, so it is highly recommended to use it for reading them.

To view the write-ups as a website locally (intended use):

## 1. Clone the repository

```bash
git clone https://github.com/HollowDragonX/htb-challenges.git
cd htb-challenges
```

## [OPTIONAL] Create a virtual environment
```bash
python3 -m venv myvenv

# Activate the environment on Windows (CMD)
myvenv\Scripts\activate.bat

# Activate the environment on Windows (PowerShell)
myvenv\Scripts\activate.ps1

# Activate the environment on MacOS
source myvenv/bin/activate
```

## 2. Install mkdocs-material

```bash
pip install mkdocs-material
```

## 3. Serve the site locally

⚠️ **Note:** Make sure to be in the folder where the notes are located (and where the ``mkdocs.yml`` file of those notes is located).

```bash
mkdocs serve
```

Now you can see the notes properly by visiting http://127.0.0.1:8000 in the browser.

If you want to serve the site for all the devices on the same network, run this instead:

```bash
mkdocs serve -a 0.0.0.0:8000
```

Then in the browser visit http://your-local-ip:8000

## Preview using mkdocs-material

<img width="1516" height="1328" alt="image" src="https://github.com/user-attachments/assets/5ed494bd-6842-43b3-8887-c8416ac86423" />
