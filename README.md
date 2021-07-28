# AutoMeet

### DISCLAIMER : I neither use nor endorse the use of this repository. It was made for *purely academic purposes only*. Do not, I repeat do NOT use this for real.


**Programmer** (*/ˈprəʊɡramə/*), *noun*;

A person who spends 3 hours automating a 30 second task because they didn't want to repeat themselves.

So what's the 30 second task I set out to automate with this project? Joining a webinar and marking my attendance, of course.

# Requirements
1. Python (3.x)
2. Selenium
3. Chrome
4. ChromeDriver
5. Linux (For running the shell scripts)

# Setup

First, download the repo and extract it into a seperate folder.

Run `sh ./setup.sh` from the command line to create a venv locally and install all the required dependancies.

# Running Instructions

### Join a meet

- In `automeet.py`, enter your username, email id and the given bitly url into the appropriate variables (lines 27 to 29).
- Adjust the duration of the meet (in hours) to your liking, save and exit. The script will automatically exit the meet after the specified duration.
- Run `sh ./automeet.sh` to start the meet.

### Mark Attendance

- In `attendance.py`, enter your email id and password (lines 23 and 24), and save it.
- Run `sh ./attendance.sh` to mark the attendance for you.

# Examples

Check the videos in the [Videos/](https://github.com/Naimish240/AutoMeet/tree/main/Videos) directory to see how the scripts work.

# Trouble Shooting

As of now, there's only one "issue" that can crop up. That is the issue of the inappropriate webdriver. So check your version of chrome, and replace the driver found in `Driver/` with the appropriate .exe for your browser version. You can download appropriate drivers from [here](https://chromedriver.chromium.org/downloads)

# Current Status

Unfortunately, uni changed the webinar site from WebinarJam to Google Meets, so this project is obselete for the most part. But I'm leaving it up here for people to check out. Feel free to fork it and modify it for your personal use cases. But yeah, please don't hold me responsible for any unfortunate consequences of using this bit of software.
