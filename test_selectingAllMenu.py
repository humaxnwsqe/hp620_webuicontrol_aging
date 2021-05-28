# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSelectingAllMenu():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_selectingAllMenu(self):
    # Test name: SelectingAllMenu
    # Step # | name | target | value
    # 1 | open | http://192.168.0.1 | 
    time.sleep(10)
    self.driver.get("http://192.168.0.1")
    # 2 | setWindowSize | 1243x969 | 
    time.sleep(10)
    self.driver.set_window_size(1243, 969)
    # 3 | click | name=input-password-field | 
    #self.driver.find_element(By.NAME, "input-password-field").click()
    # 4 | type | name=input-password-field | 000000
    time.sleep(10)
    self.driver.find_element(By.NAME, "input-password-field").send_keys("000000")
    # 5 | sendKeys | name=input-password-field | ${KEY_ENTER}
    time.sleep(10)
    self.driver.find_element(By.NAME, "input-password-field").send_keys(Keys.ENTER)
    # 6 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 7 | click | css=.has-child-menu:nth-child(2) > .el-submenu__title > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(2) > .el-submenu__title > span").click()
    # 8 | click | css=.is-opened > .el-menu span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened > .el-menu span").click()
    # 9 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 10 | click | css=.has-child-menu:nth-child(3) > .el-submenu__title > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(3) > .el-submenu__title > span").click()
    # 11 | click | css=.is-opened .el-menu-item:nth-child(1) > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(1) > span").click()
    # 12 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 13 | click | css=.is-active .el-menu-item:nth-child(2) > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(2) > span").click()
    # 14 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 15 | click | css=.is-active .el-menu-item:nth-child(3) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(3) > span").click()
    # 16 | click | css=.header-status:nth-child(1) .menu-icon-header |
    time.sleep(10) 
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 17 | click | css=.is-active .el-menu-item:nth-child(4) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(4) > span").click()
    # 18 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 19 | click | css=.has-child-menu:nth-child(4) > .el-submenu__title | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(4) > .el-submenu__title").click()
    # 20 | click | css=.is-opened .el-menu-item:nth-child(1) > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(1) > span").click()
    # 21 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 22 | click | css=.is-active .el-menu-item:nth-child(2) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(2) > span").click()
    # 23 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 24 | click | css=.has-child-menu:nth-child(5) > .el-submenu__title | 
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(5) > .el-submenu__title").click()
    # 25 | click | css=.is-opened .el-menu-item:nth-child(1) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(1) > span").click()
    # 26 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 27 | click | css=.is-active .el-menu-item:nth-child(2) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(2) > span").click()
    # 28 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 29 | click | css=.is-active .el-menu-item:nth-child(3) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(3) > span").click()
    # 30 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 31 | click | css=.is-active .el-menu-item:nth-child(4) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(4) > span").click()
    # 32 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 33 | click | css=.is-active .el-menu-item:nth-child(5) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(5) > span").click()
    # 34 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 35 | click | css=.has-child-menu:nth-child(6) > .el-submenu__title > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(6) > .el-submenu__title > span").click()
    # 36 | click | css=.is-opened .el-menu-item:nth-child(1) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(1) > span").click()
    # 37 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 38 | click | css=.is-active .el-menu-item:nth-child(2) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(2) > span").click()
    # 39 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 40 | click | css=.is-active .el-menu-item:nth-child(3) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(3) > span").click()
    # 41 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 42 | click | css=.is-active .el-menu-item:nth-child(4) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(4) > span").click()
    # 43 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 44 | click | css=.has-child-menu:nth-child(7) > .el-submenu__title > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(7) > .el-submenu__title > span").click()
    # 45 | click | css=.is-opened .el-menu-item:nth-child(1) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(1) > span").click()
    # 46 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 47 | click | css=.is-active .el-menu-item:nth-child(2) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(2) > span").click()
    # 48 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 49 | click | css=.is-active .el-menu-item:nth-child(3) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(3) > span").click()
    # 50 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 51 | click | css=.is-active .el-menu-item:nth-child(4) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(4) > span").click()
    # 52 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 53 | click | css=.is-active .el-menu-item:nth-child(5) > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-active .el-menu-item:nth-child(5) > span").click()
    # 54 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 55 | click | css=.no-child-menu > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".no-child-menu > span").click()
  

#pytest.main(['test_selectingAllMenu.py'])  

"""def main():


if __name__ == "__main__":
  main()"""

