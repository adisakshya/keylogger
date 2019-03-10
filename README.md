# A keylogger for Windows
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=2.0.0&x2=0)](http://badge.fury.io/gh/boennemann%2Fbadges)

Welcome to the keylogger repo! 

Keystroke logging, often referred to as keylogging or keyboard capturing, is the action of recording (logging) the keys struck on a keyboard, typically covertly, so that the person using the keyboard is unaware that their actions are being monitored. 
Data can then be retrieved by the person operating the logging program.
A keylogger is a program that records your keystrokes, and this program saves them in a log file on your local computer.

Currently, there is one keylogger program for one of the major operating systems; Windows.

---
## Windows Installation
keylogger requires:
  1. python 3X
  2. pynput

### Step 1: 
Download the repository using github or git eg.git clone https://github.com/adisakshya/keylogger

### Step 2: 
Install the modules by running `pip install -r requirements.txt`

---
## How to run it?

### Step 1:

copy the server.py file from bin/server.py to the desired directory you want to transfer the logs to.
and run
```
py server.py
```
This will activate the server.

#### NOTE: 
hostname and port number in the "server.py" and "client.py" file can be edited to send it to                                            some other server other than localhost:9999</b>

### Step 2:

Run following command to activate the key-logger
```
py key_logger.py
```

Run following command to activate the mouse-logger
```
py mouse_logger.py
```

This will activate the logger, and it will start logging keyboard strokes and mouse-clicks in two separate log files (txt).

As soon as the user press the "ESC" key, the logger sends the files to the remote server active in another directory
and logs are transfered into one server copy of logs (txt).

---
## Example Logs

Keyboard Logs: [key_log.txt](https://github.com/adisakshya/keylogger/blob/master/examples/keyboard_log_example/key_log.txt)

Mouse Logs: [mouse_log.txt](https://github.com/adisakshya/keylogger/blob/master/examples/mouse_log_example/mouse_log.txt)

Server Logs: [server_copy.txt](https://github.com/adisakshya/keylogger/blob/keylogger_v2.0_patch_1/examples/server_copy_of_logs_example/server_copy_of_logs.txt)

---
### Uses

Some uses of a keylogger are:

- Business Administration: Monitor what employees are doing.
- School/Institutions: Track keystrokes and log banned words in a file.
- Personal Control and File Backup: Make sure no one is using your computer when you are away.
- Parental Control: Track what your children are doing.
- Self analysis

---
### To-Do
  1. create setup file for v2.0
  2. keylogger for mac
  3. keylogger for linux
  4. Make the keylogger undetectable


Feel free to contribute to fix any problems, or to submit an issue!

Please note, this repo is for educational purposes only. No contributors, major or minor, are to fault for any actions done by this program.

Don't really understand licenses or tl;dr? Check out the [MIT license summary](https://tldrlegal.com/license/mit-license).

Distributed under the MIT license. See [LICENSE](https://github.com/adisakshya/keylogger/blob/master/LICENSE) for more information.

Adisakshya – [Website](https://adisakshya.github.io)
