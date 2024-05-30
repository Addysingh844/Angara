import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Chrome()

try:
    # Step 1: Visit the Angara.in homepage
    driver.get("https://www.angara.in")

    # Check if alert is present, if yes, accept it
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass

    # Step 2: Search for a product
    # search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
    # search_box.send_keys("diamond ring")
    # search_box.send_keys(Keys.RETURN)

    # Step 3: Select the product from the list
    time.sleep(5)
    product_link = driver.find_element(By.LINK_TEXT, "24KT (999) Goddess Lakshmi Yellow Gold Coin")
    product_link.click()

    # Step 4: Add the product to the cart
    time.sleep(5)
    add_to_cart_button = driver.find_element(By.ID, "add-to-card-btn")
    add_to_cart_button.click()

    # Step 5: Proceed to checkout
    time.sleep(3)
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Step 6: Fill in information details
    time.sleep(3)
    driver.find_element(By.NAME, "email").send_keys("addysingh844@gmail.com")
    driver.find_element(By.NAME, "firstName").send_keys("Aditya")
    driver.find_element(By.NAME, "lastName").send_keys("Singh")
    driver.find_element(By.NAME, "address1").send_keys("123 Main St")
    driver.find_element(By.NAME, "city").send_keys("New Delhi")
    driver.find_element(By.NAME, "postalCode").send_keys("110019")
    driver.find_element(By.NAME, "phone").send_keys("1122334455")

    # Step 7: Proceed to shipping
    time.sleep(5)

    Continue_to_shipping = driver.find_element(By.CLASS_NAME, "QT4by._1fragempw.rqC98._1m2hr9gd._1m2hr9ga._7QHNJ.VDIfJ.j6D1f.janiy")
    Continue_to_shipping.click()

    # Step 8: Continue to payment
    time.sleep(8)

    Continue_to_payment = driver.find_element(By.CLASS_NAME, "QT4by._1fragempw.rqC98._1m2hr9gd._1m2hr9ga._7QHNJ.VDIfJ.j6D1f.janiy")
    Continue_to_payment.click()

    time.sleep(5)

    # Step 9: Page to Pay now

    driver.find_element(By.CLASS_NAME, "QT4by._1fragempw.rqC98._1m2hr9gd._1m2hr9ga._7QHNJ.VDIfJ.j6D1f.janiy").click()

    time.sleep(10)


finally:
    driver.quit()