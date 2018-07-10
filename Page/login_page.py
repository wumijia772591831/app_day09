from Base.base import Base
import Page
import allure

@allure.step(title="测试登录")
class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)


    def click_my_btn(self):
        # 点击我的按钮
        try:
            allure.attach("点击我的按钮","成功")
            self.click_element(Page.my_btn_xpath)
        except Exception as e:
            allure.attach("点击我的按钮","失败")
            assert False


    def click_login_sign_btn(self):
        # 点击登陆注册
        try:
            allure.attach("点击登录注册按钮","成功")
            self.click_element(Page.login_sing_btn_id)
        except Exception as e:
            allure.attach("点击登录注册按钮", "失败")
            assert False

    def login_input_page(self, username, passwd):
        allure.attach("输入登录信息", "用户名:%s\n密码:\n%s" % (username, passwd))
        # 登陆操作
        # 输入用户名
        self.send_mms(Page.login_name_id, username)
        # 输入密码
        self.send_mms(Page.login_pwd_id, passwd)
        # 点击登陆按钮
        try:
            allure.attach("点击登录按钮", "成功")
            self.click_element(Page.login_btn_id)
        except Exception as e:
            allure.attach("点击登录按钮", "失败")
            assert False


    def if_my_order_status(self):
        # 判断我的订单按钮是否存在
        try:
            allure.attach("判断我的订单按钮是否存在","存在")
            self.search_element(Page.my_order_btn)
            return True
        except Exception as e:
            allure.attach("判断我的订单按钮是否存在", "不存在")
            return False
    def login_close_page(self):
        # 关闭登陆信息输入页
        self.click_element(Page.login_close_page_id)

    def logout_page(self):
        # 退出登录
        # 点击设置按钮
        self.click_element(Page.person_setting_btn_id)
        # 点击安全退出
        self.click_element(Page.logout_btn_id)




