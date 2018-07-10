from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver = driver

    def search_element(self,loc,timeout=15,poll_frequency=1):
        """
        定位单个元素  显示等待
        :param loc: 元组（定位类型（By.ID），定位属性值）
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))

    def search_elements(self,loc,timeout=15,poll_frequency=1.0):
        """
        定位一组元素  显示等待
        :param loc: 元组（定位类型（By.ID），定位属性值）
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self,loc):
        """
        点击单个元素
        :param loc: 元组（定位类型（By.ID），定位属性值）
        :return:
        """
        self.search_element(loc).click()

    def send_mms(self,loc,text):
        """
        输入内容
        :param loc: 元组（定位类型（By.ID），定位属性值）
        :param text: 测试脚本中输入的文本
        :return:
        """
        send_message = self.search_element(loc)
        send_message.clear()
        send_message.send_keys(text)

    def get_toast(self,message):
        try:
            #获取toast信息
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.search_element((By.XPATH,xpath),timeout=5,poll_frequency=0.5)
            return toast_message.text
        except Exception as e:
            return False



