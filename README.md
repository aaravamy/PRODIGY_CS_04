# 🔐 Keylogger using Python (pynput)

This project is a simple keylogger script written in Python using the pynput library. It logs every key pressed on the keyboard and saves the output to a text file called keylog.txt.

> *Disclaimer:* This tool is intended for educational purposes only. Do not use this software to monitor others without their consent. Unauthorized use may be illegal and unethical.

---

## 🚀 Features

* Logs every keypress
* Handles both regular and special keys (like Enter, Space, Shift)
* Appends to a log file: keylog.txt

---

## 🛠 Requirements

* Python 3.6+
* pynput library

Install pynput using pip:

bash
pip install pynput


---

## 📁 File Structure


📁 keylogger/
├── test.py           # The main keylogger script
└── keylog.txt        # Generated log file storing keypresses


---

## 📘 Usage

Run the script in a terminal or PowerShell:

bash
python test.py


Once running, every key you press will be logged into keylog.txt in the same directory.

To stop the logger, press Ctrl + C or close the terminal window.

---

## 💡 How It Works

* The script uses pynput.keyboard.Listener to listen to keypresses.
* Keys are logged in real-time into a file.
* Special keys like Key.space or Key.enter are handled separately from regular character keys.

---

## 🤝 Acknowledgements

* [pynput documentation](https://pynput.readthedocs.io/)

---

## 📜 License

This project is provided under the [MIT License](LICENSE).

*Author:* Radha

*Project Name:* Python Keylogger (Educational Purpose Only)
