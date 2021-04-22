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

class TestPrimaryWireless():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_primaryWireless(self):
    # Test name: primaryWireless
    # Step # | name | target | value
    # 1 | open | http://192.168.0.1 | 
    self.driver.get("http://192.168.0.1")
    # 2 | setWindowSize | 1243x969 | 
    self.driver.set_window_size(1243, 969)
    # 3 | type | name=input-password-field | 000000
    self.driver.find_element(By.NAME, "input-password-field").send_keys("000000")
    # 4 | sendKeys | name=input-password-field | ${KEY_ENTER}
    self.driver.find_element(By.NAME, "input-password-field").send_keys(Keys.ENTER)
    # 5 | pause | 10 | 
    time.sleep(20)
    # 6 | click | css=.header-status:nth-child(1) .menu-icon-header | 
    self.driver.find_element(By.CSS_SELECTOR, ".header-status:nth-child(1) .menu-icon-header").click()
    # 7 | click | css=.has-child-menu:nth-child(3) > .el-submenu__title > span | 
    time.sleep(20)
    self.driver.find_element(By.CSS_SELECTOR, ".has-child-menu:nth-child(3) > .el-submenu__title > span").click()
    # 8 | click | css=.is-opened .el-menu-item:nth-child(2) > span |
    time.sleep(20) 
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(2) > span").click()
    # 9 | pause | 10 | 
    time.sleep(20)
    # 10 | click | css=.wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner").click()
    # 11 | click | xpath=//span[contains(.,'WPA2/WPA-PSK')] | 
    self.driver.find_element(By.XPATH, "//span[contains(.,\'WPA2/WPA-PSK\')]").click()
    # 12 | pause | 10 | 
    time.sleep(20)
    # 13 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 14 | pause | 20 | 
    time.sleep(40)
    # 15 | click | css=.wrap-form-card:nth-child(1) .wrap-custom-select .el-input__inner | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(1) .wrap-custom-select .el-input__inner").click()
    # 16 | click | xpath=//li[contains(.,'AES')] | 
    time.sleep(20)
    self.driver.find_element(By.XPATH, "//li[contains(.,\'AES\')]").click()
    # 17 | pause | 20 | 
    time.sleep(20)
    # 18 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 19 | pause | 20 | 
    time.sleep(40)
    # 20 | click | css=.wrap-form-card:nth-child(1) .wrap-custom-select .el-input__inner | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(1) .wrap-custom-select .el-input__inner").click()
    # 21 | pause | 20 | 
    time.sleep(20)
    # 22 | click | xpath=//li[contains(.,'AES/TKIP')] | 
    self.driver.find_element(By.XPATH, "//li[contains(.,\'AES/TKIP\')]").click()
    # 23 | pause | 20 | 
    time.sleep(20)
    # 24 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 25 | pause | 20 | 
    time.sleep(40)
    # 26 | click | css=.wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner").click()
    # 27 | click | xpath=//li[contains(.,'WPA3-SAE')] | 
    time.sleep(20)
    self.driver.find_element(By.XPATH, "//li[contains(.,\'WPA3-SAE\')]").click()
    # 28 | pause | 20 | 
    time.sleep(20)
    # 29 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 30 | pause | 20 | 
    time.sleep(20)
    # 31 | click | css=.confirm-family | 
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-family").click()
    # 32 | pause | 20 | 
    time.sleep(40)
    # 33 | click | css=.wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner").click()
    # 34 | click | xpath=//span[contains(.,'WPA2-PSK/WPA3-SAE Mixed')] | 
    #self.driver.find_element(By.XPATH, "//span[contains(.,\'WPA2-PSK/WPA3-SAE Mixed\')]").click()
    time.sleep(20)
    self.driver.find_element(By.XPATH, "//li[contains(.,\'WPA2-PSK/WPA3-SAE Mixed\')]").click()
    # 35 | pause | 20 | 
    time.sleep(20)
    # 36 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 37 | pause | 20 | 
    time.sleep(40)
    # 38 | click | css=.wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(2) .wrap-custom-select .el-input__inner").click()
    # 39 | click | xpath=//li[contains(.,'None')] | 
    time.sleep(20)
    self.driver.find_element(By.XPATH, "//li[contains(.,\'None\')]").click()
    # 40 | pause | 20 | 
    time.sleep(20)
    # 41 | click | css=.apply | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply").click()
    # 42 | click | css=.text-box > .wrap-custom-select .el-input__inner | 
    time.sleep(40)
    self.driver.find_element(By.CSS_SELECTOR, ".text-box > .wrap-custom-select .el-input__inner").click()
    # 43 | pause | 20 | 
    time.sleep(20)
    # 44 | click | xpath=//li[contains(.,'WPA2-PSK')] | 
    self.driver.find_element(By.XPATH, "//li[contains(.,\'WPA2-PSK\')]").click()
    # 46 | type | name=input-password-field | 00000000
    time.sleep(20)
    self.driver.find_element(By.NAME, "input-password-field").send_keys("00000000")
    # 47 | pause | 20 | 
    time.sleep(20)
    # 48 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 49 | pause | 20 | 
    time.sleep(40)
    # 50 | click | css=.wrap-form-card:nth-child(4) .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(4) .el-switch__core").click()
    # 51 | pause | 20 | 
    time.sleep(20)
    # 52 | click | css=.confirm-family | 
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-family").click()
    # 53 | pause | 20 | 
    time.sleep(20)
    # 54 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 55 | pause | 20 | 
    time.sleep(40)
    # 56 | click | css=.wrap-form-card:nth-child(4) .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(4) .el-switch__core").click()
    # 57 | pause | 20 | 
    time.sleep(20)
    # 58 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 59 | pause | 20 | 
    time.sleep(40)
    # 60 | click | css=.wrap-form-card:nth-child(5) .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(5) .el-switch__core").click()
    # 61 | pause | 20 | 
    time.sleep(20)
    # 62 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 63 | pause | 20 | 
    time.sleep(40)
    # 64 | click | css=.wrap-form-card:nth-child(5) .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(5) .el-switch__core").click()
    # 65 | pause | 20 | 
    time.sleep(20)
    # 66 | click | css=.wrap-form-card:nth-child(6) .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(6) .el-switch__core").click()
    # 67 | pause | 20 | 
    time.sleep(20)
    # 68 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 69 | pause | 20 | 
    time.sleep(40)
    # 70 | click | css=.wrap-form-card:nth-child(7) .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(7) .el-switch__core").click()
    # 71 | pause | 20 | 
    time.sleep(20)
    # 72 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 73 | pause | 20 | 
    time.sleep(40)
    # 74 | click | css=.wrap-form-card:nth-child(7) .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".wrap-form-card:nth-child(7) .el-switch__core").click()
    # 75 | pause | 20 | 
    time.sleep(20)
    # 76 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 77 | pause | 20 | 
    time.sleep(40)
    # 78 | click | css=.is-checked > .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-checked > .el-switch__core").click()
    # 79 | pause | 20 | 
    time.sleep(20)
    # 80 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
    # 81 | pause | 20 | 
    time.sleep(20)
    # 82 | click | css=.confirm-family > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-family > span").click()
    # 83 | pause | 20 | 
    time.sleep(40)
    # 84 | click | css=.bs-switch .el-switch__core | 
    self.driver.find_element(By.CSS_SELECTOR, ".bs-switch .el-switch__core").click()    
    # 85 | pause | 20 | 
    time.sleep(20)
    # 86 | click | css=.apply > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".apply > span").click()
  