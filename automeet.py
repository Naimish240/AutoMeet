# ----------------------------------------------
# Creator : Naimish Mani B
# Date : 26th July 2021
# ----------------------------------------------
# Automate joining the WebinarJam webinars
# It makes use of Selenium and Chromedriver
# ----------------------------------------------
# Download the correct chromedriver from the url
# https://chromedriver.chromium.org/downloads
# To ensure this runs smoothly.
# ----------------------------------------------

from selenium import webdriver
from time import sleep
import captcha
import os
import glob
from tqdm import tqdm


# Mute the browser on open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")


# User settings
USER_NAME = ""                       # Edit with your Name
EMAIL_ID = ""         # Edit with your email
BITLY_URL = ""        # Edit with your URL
SESSION_DURATION = 2                        # Duration of session in hrs


def openBrowser():
    # Initialize the webdriver object
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # Navigates to the website with chrome
    driver.get(BITLY_URL)
    # Wait 5 seconds, for the website to load
    sleep(5)
    print("Browser Opened")
    return driver


def textButtons(driver):
    # Find Name Button
    nameButton = driver.find_element_by_xpath(
        '//*[@id="login-form"]/div/div/div/div[2]/div[1]/input'
    )
    # Insert Name into field
    nameButton.send_keys(USER_NAME)
    sleep(1)

    # Find Email Button
    emailButton = driver.find_element_by_xpath(
        '//*[@id="login-form"]/div/div/div/div[2]/div[2]/input'
    )
    # Insert Email into field
    emailButton.send_keys(EMAIL_ID)
    sleep(1)

    print("Logged In")


def solveCaptcha(driver):
    try:
        # Get image url
        captcha_url = driver.find_element_by_xpath(
            '//*[@id="login-form"]/div/div/div/div[2]/div[3]/div/div[1]/img'
        )
        captcha_url = captcha_url.get_attribute("src")
        print(captcha_url)

        # Download the image
        os.system(f"wget {captcha_url}")

        # Load Image
        img = glob.glob('*.jpg')
        img = img[0]

        # Get CAPTCHA text
        text = captcha.getText(img)

        # Submit CAPTCHA
        captchaBox = driver.find_element_by_xpath(
            ''
        )
        captchaBox.send_keys(text)

        # Delete image
        os.system(f"rm {img}")

    except:
        print("Captcha not found")


def joinMeet(driver):
    # Find Submit Button
    submitButton = driver.find_element_by_xpath(
        '//*[@id="register_btn"]'
    )
    # Click it
    submitButton.click()

    print("Meet joined")


def playVideo(driver):
    loaded = False
    while loaded is False:
        # Check if Play Button is Visible
        try:
            playButton = driver.find_element_by_xpath(
                '//*[@id="user_start_broadcast_overlay"]/button'
            )
            playButton.click()
            loaded = True

        except:
            print("Play button not visible yet, trying again in 60 seconds")
            with tqdm(total=60) as t:
                for i in range(60):
                    sleep(1)
                    t.update(1)

            continue

    print("Play Button Clicked!")


def run(driver):
    # Let the session run
    with tqdm(total=SESSION_DURATION*60*60) as t:
        for i in range(SESSION_DURATION*60*60):
            sleep(1)
            t.update(1)

    # End the session
    driver.close()
    driver.quit()


if __name__ == '__main__':
    driver = openBrowser()
    textButtons(driver)
    solveCaptcha(driver)
    joinMeet(driver)
    playVideo(driver)
    run(driver)
