# MSCS532 Assignment 1: Getting Started

## Overview
This assignment introduces the setup of a Python development environment, the use of Visual Studio Code (VS Code) as an Integrated Development Environment (IDE), and version control with GitHub.  
The final component of this assignment is to implement the **Insertion Sort algorithm** that sorts an array in **monotonically decreasing order**.

---

## Steps Completed

### 1. Python Installation
- I Downloaded and installed **Python 3.8 or higher** from the official website:  
  https://www.python.org/downloads/
- During installation, i made sure to check the option **“Add Python to PATH.”**
- Verified the installation by running the command below in my command prompt:
  ```bash
  python --version
  ```
---

### 2. Visual Studio Code (VS Code) Installation and Setup
**Downloading and installing**
1. Downloaded VS Code for windows OS from: https://code.visualstudio.com/
2. Run the installer and followed the prompts.

**Installing recommended extensions**
1. Opened VS Code.
2. Opened the Extensions view: clicked the square icon on the lef. Alternatively, I pressed `Ctrl+Shift+X`.
3. Searched for and installed:
   - **Python** (Microsoft) — required for linting, IntelliSense, and debugging.
   - **Code Runner** (optional) — allows quick running of scripts from the editor.

**Selecting Python interpreter**
1. Opened the Command Palette: `Ctrl+Shift+P`.
2. Typed **Python: Select Interpreter** and choose the Python 3.x interpreter you installed.

**Creating and saving the project**
1. Createed a new folder for the project ( `MSCS532_Assignment1`).
2. In VS Code, opened that folder (`File > Open Folder...`).
3. Createed a new file named `insertion sort.py` and saved it.

---

### 3. Running the Python Program in VS Code
I run my program using this method:

**Running with the Python extension**
1. Opened `insertion sort.py`.
2. Click the green **Run Python File** button at the top-right of the editor.
3. Output will appear in the integrated Terminal.

These methods can also be used:

**Option B — Use Code Runner**
1. Open `insertion sort.py`.
2. Click **Run Code**.
3. Output will appear in the Output panel.

**Option C — Run from VS Code Terminal**
1. Open the terminal: `View > Terminal` or `Ctrl+`` (backtick).
2. Run:
   ```bash
   python insertion sort.py
   ```
   or, if your system uses `python3`:
   ```bash
   python3 insertion sort.py
   ```

---

### 4. GitHub Setup & Version Control
- Created a GitHub account at: https://github.com/ (using my UCumberlands email).
- Create a new **public** repository named:
  ```
  MSCS532_Assignment1
  ```
-

**Commit progression (minimum 3 commits)**
1. `Initial commit` — add README.md and .gitignore.
2. `Adding insertion sort implementation` — first working version of `insertion sort.py`.
3. `Assignment Report` — final formatting, comments, sample output, and README updates.



