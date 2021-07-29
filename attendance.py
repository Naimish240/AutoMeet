# ----------------------------------------------
# Creator : Naimish Mani B
# Date : 27th July 2021
# ----------------------------------------------
# Automate marking attendance for sixphrase
# It makes use of Selenium and Chromedriver
# ----------------------------------------------
# Download the correct chromedriver from the url
# https://chromedriver.chromium.org/downloads
# To ensure this runs smoothly.
# ----------------------------------------------

from selenium import webdriver
from time import sleep
from datetime import datetime
from tqdm import tqdm

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")


BASE_URL = "http://3.12.107.113/"
EMAIL_ID = ""
PASSWORD = ""


def openBrowser():
    # Initialize the webdriver object
    driver = webdriver.Chrome('Driver/chromedriver', options=chrome_options)
    # Navigates to the website with chrome
    driver.get(BASE_URL + 'users/sign_in')
    # Wait 5 seconds, for the website to load
    sleep(5)
    print("Opened Browser")
    return driver


def login(driver):
    name = driver.find_element_by_xpath(
        '//*[@id="user_email"]'
    )
    name.send_keys(EMAIL_ID)

    pwd = driver.find_element_by_xpath(
        '//*[@id="user_password"]'
    )
    pwd.send_keys(PASSWORD)

    submitButton = driver.find_element_by_xpath(
        '//*[@id="new_user"]/input[3]'
    )
    submitButton.click()
    print("Logged In")

    sleep(5)


def attendanceWindow(driver):
    # Load Attendance Page
    driver.get(
        BASE_URL + 'course/60e1fa251d41c80b44389b30'
    )
    sleep(5)

    # Load all dates
    dropDownArrow = driver.find_element_by_xpath(
        '//*[@id="ld-lesson-list-56"]/div/div[1]/span/span[1]'
    )
    dropDownArrow.click()
    sleep(5)

    # Find today's attendance link
    datesTable = driver.find_element_by_xpath('//*[@id="ld-nav-content-list-68"]/div/div')
    today = datesTable.find_elements_by_xpath('./*')[-1]
    todayDropDown = today.find_elements_by_xpath('./*')
    sleep(1)

    print("Selecting Date: ", todayDropDown[0].text)

    # Opening today's dropdown
    todayDownArrow = todayDropDown[0].find_elements_by_xpath('./*')[1]
    todayDownArrow.click()
    sleep(1)

    # Get Current Hour
    hour = int(datetime.now().strftime("%H"))
    sessions = todayDropDown[1].find_elements_by_xpath('./*')[0].find_elements_by_xpath('./*')[0]

    # Morning Session
    if hour in [10, 11, 12]:
        morning = sessions.find_elements_by_xpath('./*')[0]
        morning.click()

    # Afternoon Session
    else:
        evening = sessions.find_elements_by_xpath('./*')[1]
        evening.click()

    sleep(5)

    # Start Quiz
    testButton = driver.find_element_by_xpath(
            '//*[@id="ld-table-list-item-66"]/a[1]/button'
    )
    testButton.click()
    print("Opened Quiz")

    goToQuiz(driver)


def goToQuiz(driver):
    # Wait for quiz to load
    with tqdm(total=35) as t:
        for i in range(35):
            sleep(1)
            t.update(1)

    # Mark presence
    yesButton = driver.find_element_by_xpath('//*[@id="options_quiz"]/div/label')
    yesButton.click()
    sleep(2)

    # Submit Result
    submitButton = driver.find_element_by_xpath('//*[@id="end_test"]')
    submitButton.click()
    sleep(3)

    # Confirm Submission
    endTestButton = driver.find_element_by_xpath('//*[@id="end_test_button"]')
    endTestButton.click()

    print("Submitted Attendance")
    sleep(5)


def quit(driver):
    sleep(10)
    driver.close()
    driver.quit()
    print("Exit Program")


if __name__ == '__main__':
    driver = openBrowser()
    login(driver)
    attendanceWindow(driver)
    quit(driver)
