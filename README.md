# AutoVoiterForAz

Instalation Guide for Unix-based systems (Linux/MacOS)

Please be sure that you have python 3.6+ installed 

```
git clone https://github.com/DarkKnight1005/AutoVoiterForAz.git

chmod -R 755 AutoVoiterForAz
```

Download ChromeDriver from 
```
https://chromedriver.chromium.org/downloads
```
Copy Path to downloaded ChromeDriver

```
cd AutoVoiterForAz

sudo pip3 install -r requirements.txt

sudo python3 automate.py
```

### After executed you have to input path to the ChromeDriver
If path enereted in the wrong way yuo will get an expeption like this:

```
FileNotFoundError: [Errno 2] No such file or directory: '/Users/username/Downloads/wrongpath'
```
