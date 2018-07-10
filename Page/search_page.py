from Base.base import Base
class search_page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_search_btn(self,loc):
        """
        点击搜索按钮
        :param loc:
        :return:
        """
        self.click_element(loc)

    def input_message(self,loc,text):
        """
        输入搜索内容
        :param loc:
        :param text:
        :return:
        """
        self.send_mms(loc,text)

    def result_list(self,loc):
        """
        返回搜索结果列表
        :return:
        """
        res_list = self.search_elements(loc)
        return [i.text for i in res_list]
