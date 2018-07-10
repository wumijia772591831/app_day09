import os,sys,pytest
sys.path.append(os.getcwd())
from Page.login_page import Login_Page
from Base.get_driver import get_server_settings
from Base.read_data import Op_Data
def put_data():
    data = Op_Data("data.yml").read_yaml().get('Login_data')
    data_list = []
    for i in data:
        for o in i.keys():
            data_list.append((o,i.get(o).get("phone"),i.get(o).get("passwd"),i.get(o).get("get_mess"),i.get(o).get("expect_message"),i.get(o).get("tag")))

    return data_list
class Test_TP():

    def setup_class(self):
        self.TP_driver = Login_Page(get_server_settings("com.tpshop.malls",".SPMainActivity"))
        #点击我的按钮
        self.TP_driver.click_my_btn()

    def teardown_class(self):
        self.TP_driver.driver.quit()

    @pytest.mark.parametrize("num,phone,password,get_mess,xpect_message,tag",put_data())
    def test_login(self,num,phone,password,get_mess,xpect_message,tag):
        #点击登录注册按钮
        self.TP_driver.click_login_sign_btn()
        #登录操作
        self.TP_driver.login_input_page(phone,password)
        if tag:
            try:
                #获取登录成功toast
                toast_mes = self.TP_driver.get_toast(get_mess)
                #获取登录后状态
                status = self.TP_driver.if_my_order_status()
                #退出登录
                self.TP_driver.logout_page()
                assert toast_mes == xpect_message and status
            except Exception as e:
                #退出登录信息输入页面
                self.TP_driver.login_close_page()
                assert False
        else:
            try:
                #获取登录失败toast
                toast_fail_toast = self.TP_driver.get_toast(get_mess)
                if toast_fail_toast:
                    assert toast_fail_toast == xpect_message
                else:
                    assert False

            finally:
                self.TP_driver.login_close_page()




