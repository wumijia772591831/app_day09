from Base.base import Base
class send_mms_page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_create_mms(self,loc):
        """
        点击新建信息
        :param loc:
        :return:
        """
        self.click_element(loc)

    def input_tel(self,loc,text):
        """
        输入收件人电话
        :param loc:
        :return:
        """
        self.send_mms(loc,text)

    def input_mms(self,loc,text):
        """
        输入信息
        :param loc:
        :return:
        """
        self.send_mms(loc,text)

    def click_send_btn(self,loc):
        """
        点击发送按钮
        :param loc:
        :return:
        """
        self.click_element(loc)

    def res_mms(self,loc):
        """
        返回已发短信内容
        :param loc:
        :return:
        """
        res_mms_list = self.search_elements(loc)
        return [i.text for i in res_mms_list]
