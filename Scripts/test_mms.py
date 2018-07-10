import pytest,os,sys
sys.path.append(os.getcwd())
from Base.get_driver import get_server_settings
from Page.send_mms_page import send_mms_page
import Base,Page
class Test_send_mms:
    def setup_class(self):
        self.sm_obj = send_mms_page(get_server_settings(Base.package_mms,Base.activity_mms))
    def teardown_class(self):
        self.sm_obj.driver.quit()

    @pytest.fixture(scope='class',autouse=True)
    def test_click_create_btn(self):
        """
        点击新建短信按钮
        :return:
        """
        self.sm_obj.click_create_mms(Page.new_mms_btn)

    @pytest.fixture(scope='class',autouse=True)
    def test_input_tel(self):
        """
        输入收件人
        :param text:
        :return:
        """
        self.sm_obj.input_tel(Page.send_mms_tel,15676783568)


    @pytest.mark.parametrize('input_data',["123","你好","hello"])
    def test_input_mms(self,input_data):
        """
        输入短信并断言是否发送成功
        :param input_data:
        :return:
        """
        #输入信息
        self.sm_obj.input_mms(Page.input_mms,input_data)
        #点击发送按钮
        self.sm_obj.click_send_btn(Page.send_mms_btn)
        #断言短信是否发送成功
        mms_res_list = self.sm_obj.res_mms(Page.mms_sended)
        assert input_data in mms_res_list
