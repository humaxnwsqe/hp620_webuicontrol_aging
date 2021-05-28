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

class TestInternetSettingChange():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_internetSettingChange(self):
    # Test name: InternetSettingChange
    # Step # | name | target | value
    # 1 | open | http://192.168.0.1 | 
    time.sleep(10)
    self.driver.get("http://192.168.0.1")
    # 2 | setWindowSize | 1369x752 | 
    time.sleep(10)
    self.driver.set_window_size(1243, 969)
    # 3 | type | name=input-password-field | 000000
    time.sleep(10)
    self.driver.find_element(By.NAME, "input-password-field").send_keys("000000")
    # 4 | sendKeys | name=input-password-field | ${KEY_ENTER}
    time.sleep(10)
    self.driver.find_element(By.NAME, "input-password-field").send_keys(Keys.ENTER)
    # 5 | click | css=.has-child-menu:nth-child(2) > .el-submenu__title | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(2) > .el-submenu__title").click()
    # 6 | click | css=.is-opened > .el-menu span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened > .el-menu span").click()
    # 7 | click | css=.wrap-form-card:nth-child(8) .el-input__inner | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(8) .el-input__inner").click()
    # 8 | click | css=.hover > span | 
    time.sleep(10)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Always On\')]").click()
    # 9 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 10 | click | css=.wrap-form-card:nth-child(8) .el-input__inner | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(8) .el-input__inner").click()
    # 11 | click | xpath=//span[contains(.,'Always Off')] | 
    time.sleep(10)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Always Off\')]").click()
    # 12 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 13 | click | css=.wrap-form-card:nth-child(8) .el-input__inner | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(8) .el-input__inner").click()
    # 14 | click | xpath=//span[contains(.,'On Demand')] | 
    time.sleep(10)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'On Demand\')]").click()
    # 15 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 16 | click | css=.wrap-form-card:nth-child(9) .el-input__inner | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(9) .el-input__inner").click()
    # 17 | click | xpath=//span[contains(.,'Unencrypted Password (PAP)')] | 
    time.sleep(10)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Unencrypted Password (PAP)\')]").click()
    # 18 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 19 | click | css=.wrap-form-card:nth-child(9) .el-input__inner | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(9) .el-input__inner").click()
    # 20 | click | xpath=//span[contains(.,'Challenge Handshake Authentication Protocol (CHAP)')] | 
    time.sleep(10)
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Challenge Handshake Authentication Protocol (CHAP)\')]").click()
    # 21 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 22 | click | css=.wrap-form-card:nth-child(9) .el-input__inner | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(9) .el-input__inner").click()
    # 23 | click | xpath=//li[contains(.,'Auto')] | 
    self.driver.find_element(By.XPATH, "//li[contains(.,\'Auto\')]").click()
    # 24 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 25 | click | css=.wrap-form-card:nth-child(10) .el-switch__core | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(10) .el-switch__core").click()
    # 26 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 27 | click | css=.wrap-form-card:nth-child(10) .el-switch__core | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(10) .el-switch__core").click()
    # 28 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 29 | click | css=.wrap-form-card:nth-child(14) .el-switch__core | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(14) .el-switch__core").click()
    # 30 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 31 | click | css=.wrap-form-card:nth-child(14) .el-switch__core | 
    time.sleep(15)
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(14) .el-switch__core").click()
    # 32 | click | css=.apply > span | 
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
  



#pytest.main(['test_internetSettingChange.py'])  
