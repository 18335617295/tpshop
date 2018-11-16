from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def find_toast(driver, message, timeout=3):
    """
    # message: 预期要获取的toast的部分消息
    """
    message1 = "//*[contains(@text,'" + message + "')]"
    try:
        print(message1)
        WebDriverWait(driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message1))
        return True
    except Exception as a:
        print(message1)
        return False
