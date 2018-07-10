import pytest,sys,os
sys.path.append(os.getcwd())
from Page.search_page import search_page
from Base.get_driver import get_server_settings
import Base,Page
class Test_search:
    def setup_class(self):
        self.se_obj = search_page(get_server_settings(Base.package_settings,Base.activity_settings))

    def teardown_clss(self):
        self.se_obj.driver.quit()

    @pytest.fixture(scope='class',autouse=True)
    def test_click_search(self):
        """
        点击搜索按钮
        :return:
        """
        self.se_obj.click_search_btn(Page.search_btn)

    @pytest.mark.parametrize('input_data,except_data',[("ip","IP地址"),("wl","WLAN直连"),("m","MAC地址")])
    def test_send_search_message(self,input_data,except_data):
        """
        输入搜索内容并断言结果列表与预期是否一致
        :param input_data:
        :param except_data:
        :return:
        """
        #输入内容
        self.se_obj.input_message(Page.search_input,input_data)
        # 断言
        res_list = self.se_obj.result_list(Page.res_list)
        assert except_data in res_list
