# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestServiceDMZ():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_serviceDMZ(self):
    # Test name: serviceDMZ
    # Step # | name | target | value
    # 1 | open | http://192.168.0.1 
    # time.sleep(10)| 
    self.driver.get("http://192.168.0.1")
    # 2 | setWindowSize | 1243x969 | 
    time.sleep(10)
    self.driver.set_window_size(1243, 969)
    # 3 | type | name=input-password-field | 000000
    time.sleep(10)
    self.driver.find_element(By.NAME, "input-password-field").send_keys("000000")
    # 4 | sendKeys | name=input-password-field | ${KEY_ENTER}
    time.sleep(10)
    self.driver.find_element(By.NAME, "input-password-field").send_keys(Keys.ENTER)
    # 5 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 6 | click | css=.has-child-menu:nth-child(5) > .el-submenu__title > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(5) > .el-submenu__title > span").click()
    # 7 | click | css=.is-opened .el-menu-item:nth-child(5) > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(5) > span").click()
    # 8 | click | css=.el-switch__core | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".el-switch__core").click()
    # 9 | pause | 5 | 
    time.sleep(10)
    # 10 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 11 | pause | 5 | 
    time.sleep(10)
    # 12 | click | css=.el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".el-switch__core").click()
    # 13 | pause | 5 | 
    time.sleep(10)
    # 14 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 15 | pause | 5 | 
    time.sleep(10)
  
