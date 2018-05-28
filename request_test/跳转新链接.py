# -*- coding: utf-8 -*-
# 这个是百度的那个链接
url="http://www.baidu.com/link?url=5-5G-H0pZInCMzRA62XpgnOYanjzo8xl-Q5n65tnlwTlnwb22nGcn7Hm5F25hVumU7JxGcBTTesVj71QkTz0GHg1ruW9_Z6DTllF0s3r37_"

from selenium import webdriver


driver = webdriver.Chrome()
#隐式等待
driver.implicitly_wait(30)
driver.get(url)
#获取跳转后的最终url
redirected_url = driver.current_url
print (redirected_url)
driver.close() # Close the current window.
driver.quit() # Quit the driver and close every associated window.