from selenium.webdriver.common.by import By

"""
页面元素-设置
"""
#搜索按钮
search_btn = (By.ID,'com.android.settings:id/search')
#搜索输入框
search_input = (By.ID,'android:id/search_src_text')
#搜索结果列表
res_list = (By.ID,'com.android.settings:id/title')

"""
页面元素-短信
"""
#新建短信按钮
new_mms_btn = (By.ID,'com.android.mms:id/action_compose_new')
#短信接收者输入框
send_mms_tel = (By.ID,'com.android.mms:id/recipients_editor')
#短信输入框
input_mms = (By.ID,'com.android.mms:id/embedded_text_editor')
#发送短信按钮
send_mms_btn = (By.ID,'com.android.mms:id/send_button_sms')
#已发短信内容
mms_sended = (By.ID,'com.android.mms:id/text_view')


"""
    首页
"""
# 我的按钮
my_btn_xpath = (By.XPATH, "//*[contains(@text,'我的') and contains(@resource-id,'com.tpshop.malls:id/tab_txtv')]")
# 登陆注册按钮
login_sing_btn_id = (By.ID, "com.tpshop.malls:id/nickname_txtv")
# 输入账号
login_name_id = (By.ID, "com.tpshop.malls:id/edit_phone_num")
# 输入密码
login_pwd_id = (By.ID, "com.tpshop.malls:id/edit_password")
# 登陆按钮
login_btn_id = (By.ID, "com.tpshop.malls:id/btn_login")
# 登陆页面关闭按钮
login_close_page_id = (By.ID, "com.tpshop.malls:id/titlebar_back_imgv")
"""
    个人中心页面
"""
# 设置按钮
person_setting_btn_id = (By.ID, "com.tpshop.malls:id/setting_btn")
# 我的订单
my_order_btn = (By.XPATH, "//*[contains(@text,'我的订单') and contains(@resource-id,'com.tpshop.malls:id/title_txtv')]")
"""
    设置页面
"""
# 安全退出按钮
logout_btn_id = (By.ID, "com.tpshop.malls:id/exit_btn")