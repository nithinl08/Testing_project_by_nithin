import time
from selenium import webdriver
driver = webdriver.Chrome()

def test_login():
    driver.get('http://skillgun.com')
    time.sleep(5)

    mobile = driver.find_element('name', 'ctl00$ContentPlaceHolder1$tbPhoneNumber')
    mobile.send_keys('Number')
    time.sleep(5)

    email = driver.find_element('id', 'ContentPlaceHolder1_tbEmail')
    email.send_keys('nithinl2001@gmail.com')

    pw = driver.find_element('name', 'ctl00$ContentPlaceHolder1$tbPassword')
    pw.send_keys('password*****')

    cb = driver.find_element('xpath', '//*[@id="ckbkPolicyAgreement"]')
    cb.click()

    time.sleep(12)

    login = driver.find_element('id', 'ContentPlaceHolder1_btnLogin')
    login.click()

    time.sleep(5)

    assert 'Student' in driver.current_url

def test_skillgun_profilesetting():

    profile = driver.find_element('xpath', '//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[3]/div[3]/a')
    profile.click()

    time.sleep(5)

    assert 'ProfileSetting' in driver.current_url

def test_skillgun_editcontacts():
    edit = driver.find_element('id', 'ContentPlaceHolder1_hlEditContact')
    edit.click()

    time.sleep(5)

    assert 'EditContactDetails' in driver.current_url

def test_skillgun_editingcontacts():
    whatsapp_number=driver.find_element('id','ContentPlaceHolder1_RadioButtonList1_0')
    whatsapp_number.click()


    cur_add_line = driver.find_element('id', 'ContentPlaceHolder1_tbCALine1')
    cur_add_line.clear()  # first remove the current address data
    cur_add_line.send_keys('HSR LAYOUT')

    cur_city = driver.find_element('id', 'ContentPlaceHolder1_tbCACity')
    cur_city.clear()
    cur_city.send_keys('Bengaluru')

    cur_state = driver.find_element('id', 'ContentPlaceHolder1_ddlCAState')
    cur_state.send_keys('Karnataka')

    save = driver.find_element('id', 'ContentPlaceHolder1_btnSubmit')
    save.click()

    time.sleep(5)
    # assert 'Bengaluru' in cur_city.text
    driver.close()