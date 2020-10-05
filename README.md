# AutoVoiterForAz

Instalation Guide for Unix-based systems (Linux/MacOS) and for Windows 10 with installed Ubuntu terminal

## Requirements

Python 3 and 
Google Chrome

## Instalation Giude

```
git clone https://github.com/DarkKnight1005/AutoVoiterForAz.git

chmod -R 755 AutoVoiterForAz
```

Download ChromeDriver from 
```
https://chromedriver.chromium.org/downloads
```
ChromeDriver's path will be needed for inputing to the script after execution

```
cd AutoVoiterForAz

sudo pip3 install -r requirements.txt

sudo python3 automate.py
or
python3 automate.py
```

### After execution you have to input path to the ChromeDriver
If path enereted in the wrong way yuo will get an expeption like this:

```
FileNotFoundError: [Errno 2] No such file or directory: '/Users/username/Downloads/wrongpath'
```

## Note

If some connection interuptions happen then programm will throw an exeption and you have to execute it again.

### To stop script

```
Ctrl + C
```
