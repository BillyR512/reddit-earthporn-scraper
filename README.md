# Reddit /r/EarthPorn Image Scraper


Simple python scraper for reddit using standard python libraries. I use this script on my macbook with an Automator script and CronniX to download all the top post from /r/earthporn every night.


# Automator Setup

* Open Automator -> cmd + spacebar - type in Automator
* Select New Application
* Select "Run AppleScript" in the available actions menu and copy/modify the script below

Sample Script -

    on run {input, parameters}

        tell application "Terminal"
            activate
            do script "cd ~/path/to/directory/ in window 1
            delay 2
            do script "python reddit_images.py" in window 1
            delay 2
        end tell
    end run

# CronniX Setup
* Download CronniX - https://code.google.com/p/cronnix/downloads/list
* Select "New" from top left corner
* Select "Simple" tab - and specify the time you would like to run the scraper
* For 10 PM daily - simply type "22" into the hour box and select the checkbox "all" for day of the week.

For the CronniX command, modify the script below:

    /usr/bin/open "/path/to/your/automator/app.app"
    
# Windows Cron
* Create 'scraper.bat'
* Paste ``` "Path where your Python exe is stored\python.exe" "Path where your Python script is stored\script name.py" ```
* Save file, run it to test
* Schedule the Python Script using Windows Scheduler