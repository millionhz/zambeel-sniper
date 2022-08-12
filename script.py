import argparse
from time import sleep
from tokenize import PseudoExtras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def enroll():
    proceed_selector = 'DERIVED_REGFRM1_LINK_ADD_ENRL$82$'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, proceed_selector)))
    driver.find_element(By.ID, proceed_selector).click()

    finish_enroll_selector = '#DERIVED_REGFRM1_SSR_PB_SUBMIT'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, finish_enroll_selector)))
    driver.find_element(
        By.CSS_SELECTOR, finish_enroll_selector).click()


parser = argparse.ArgumentParser(description='Snipe courses on zambeel.')
parser.add_argument('roll', type=str, help='zambeel roll number')
parser.add_argument('password', type=str, help='zambeel password')

parsed_args = parser.parse_args()
ROLL = parsed_args.roll
PASSWORD = parsed_args.password

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# login
driver.get("https://zambeel.lums.edu.pk/")

SUBMIT_BUTTON_CSS = 'input[type=submit]'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, SUBMIT_BUTTON_CSS)))

driver.find_element(By.ID, 'userid').send_keys(ROLL)
driver.find_element(By.ID, 'pwd').send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()
sleep(5)

while True:
    driver.get(
        'https://zambeel.lums.edu.pk/psc/ps_7/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL')
    print('REFRESHING...', end=' ')

    RADIO_ID = 'SSR_DUMMY_RECV1$sels$1$$0'
    CONTINUE_ID = 'DERIVED_SSS_SCT_SSR_PB_GO'
    COURSE_STATUS_CSS = r'#win7divDERIVED_REGFRM1_SSR_STATUS_LONG\$0 > div > img'

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, CONTINUE_ID)))

    driver.find_element(By.ID, RADIO_ID).click()
    driver.find_element(By.ID, CONTINUE_ID).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, COURSE_STATUS_CSS)))

    course_status = driver.find_element(
        By.CSS_SELECTOR, COURSE_STATUS_CSS)
    img_src = course_status.get_attribute('src')

    if 'CLOSED' not in img_src:
        print('BINGO')
        enroll()
        break

    print('CLOSED')


driver.close()
