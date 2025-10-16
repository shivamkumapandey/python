from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from PIL import Image
import pytesseract


# Replace these with your actual details
USERNAME = "shivam24122005"
PASSWORD = "Shivam@321"
FROM_STATION = "Delhi"
TO_STATION = "Mumbai"
DATE_OF_JOURNEY = "2025-09-30"
QUOTA = "General"
CLASS = "SL"

def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def solve_and_fill_captcha(driver):
    # Wait for captcha image to appear
    captcha_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'captcha')]"))
    )
    captcha_image.screenshot("captcha.png")
    # OCR to get captcha text
    captcha_text = pytesseract.image_to_string(Image.open("captcha.png"), config='--psm 8 --oem 3').strip()
    # Fill captcha
    captcha_field = driver.find_element(By.XPATH, "//input[@formcontrolname='captcha']")
    captcha_field.send_keys(captcha_text)

def login(driver):
    driver.get("https://www.irctc.co.in/nget/train-search")
    # Open login pop-up
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'LOGIN')]"))
    )
    login_button.click()

    # Fill in credentials
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='User Name']"))
    )
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    # Captcha handling
    solve_and_fill_captcha(driver)

    # Submit login
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'SIGN IN')]")
    submit_button.click()
    time.sleep(5)

def fill_address(driver):
    try:
        # Typical XPATHs for registration, adjust as necessary
        address_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='resAddress']"))
        )
        address_field.send_keys("123 Main Street")
        city_field = driver.find_element(By.XPATH, "//input[@formcontrolname='resCity']")
        city_field.send_keys("Delhi")
        pincode_field = driver.find_element(By.XPATH, "//input[@formcontrolname='resPinCode']")
        pincode_field.send_keys("110001")
        continue_button = driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
        continue_button.click()
        time.sleep(2)
    except Exception:
        print("Address form not found or already filled. Skipping address autofill...")

def search_train(driver):
    from_station_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='From*']"))
    )
    from_station_field.send_keys(FROM_STATION)
    to_station_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='To*']"))
    )
    to_station_field.send_keys(TO_STATION)
    date_of_journey_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Journey Date(dd-mm-yyyy)*']"))
    )
    date_of_journey_field.send_keys(DATE_OF_JOURNEY)
    search_button = driver.find_element(By.XPATH, "//button[contains(text(),'Search')]")
    search_button.click()
    time.sleep(5)

def select_train(driver):
    train_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='train-list']"))
    )
    first_train = train_list.find_element(By.XPATH, ".//div[@class='train-row'][4]")
    first_train.click()
    time.sleep(3)

def select_class_and_quota(driver):
    class_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@formcontrolname='class']"))
    )
    for option in class_dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.text == CLASS:
            option.click()
            break
    quota_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@formcontrolname='quota']"))
    )
    for option in quota_dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.text == QUOTA:
            option.click()
            break
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
    continue_button.click()
    time.sleep(3)

def add_passengers(driver):
    passenger_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='passenger-form']"))
    )
    passenger_name_field = passenger_form.find_element(By.XPATH, ".//input[@formcontrolname='passengerName']")
    passenger_name_field.send_keys("John Doe")
    passenger_age_field = passenger_form.find_element(By.XPATH, ".//input[@formcontrolname='passengerAge']")
    passenger_age_field.send_keys("30")
    passenger_gender_field = passenger_form.find_element(By.XPATH, ".//select[@formcontrolname='passengerGender']")
    for option in passenger_gender_field.find_elements(By.TAG_NAME, 'option'):
        if option.text == "Male":
            option.click()
            break
    continue_button = driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
    continue_button.click()
    time.sleep(3)

def make_payment(driver):
    payment_options = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='payment-options']"))
    )
    payment_method = payment_options.find_element(By.XPATH, ".//div[@class='payment-method'][4]")
    payment_method.click()
    pay_button = driver.find_element(By.XPATH, "//button[contains(text(),'Pay')]")
    pay_button.click()
    time.sleep(5)

def main():
    driver = init_driver()
    try:
        login(driver)
        fill_address(driver)  # Only needed for registration or when updating profile
        search_train(driver)
        select_train(driver)
        select_class_and_quota(driver)
        add_passengers(driver)
        make_payment(driver)
    except TimeoutException:
        print("Timeout occurred while waiting for an element to load.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
