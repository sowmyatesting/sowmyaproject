import pytest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver():
    # Specify the path to the ChromeDriver executable
    chrome_driver_path = r"C:\Users\nandu\Downloads\chromedriver-win32 (2)\chromedriver-win32\chromedriver.exe"

    # Set up and tear down the WebDriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    yield driver
    driver.quit()


def test_verify_testcaseone_projecttwo_resetpassword(driver):
    # Code to perform login with valid credentials
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    print("hello")
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/form/div[1]/div/div[2]/input").send_keys("Admin")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/form/div[2]/button[2]").click()
    time.sleep(10)
def test_verify_testcasetwo_projecttwo(driver):
    # Code to perform login with valid credentials
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    # Wait until the username input is present
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )

    # Corrected: Use find_element instead of find_element_by_xpath
    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    login_button = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")

    username_input.send_keys("admin")
    password_input.send_keys("admin123")
    login_button.click()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    time.sleep(15)

