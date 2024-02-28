import unittest
from  colorama import Fore
import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Edge()
driver.implicitly_wait(50)
driver.get("https://imeetify.com/login")
parentwindowhandle = driver.current_window_handle
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID, "email").send_keys("imeetifydemo@gmail.com")
driver.find_element(By.ID, "password").send_keys("Welcome@123")
driver.find_element(By.ID, "rememberMe").click()
driver.find_element(By.XPATH, "//*[@id=\"content\"]/div/div/div[2]/div/form/div[5]/button").click()
print(Fore.RED+"Login Successfully")
time.sleep(5)



def Appointment(Ctype, Fn, Ln, mail , slot_time):
    next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
    next.click()
    next.click()
    driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
    ft = driver.find_element(By.ID, slot_time)
    ft.click()
    time.sleep(1.2)
    button = driver.find_element(By.ID, "nextbtn")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(ft))
    button.click()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys(Fn)
    driver.find_element(By.ID, "lastname").send_keys(Ln)
    driver.find_element(By.ID, "email").send_keys(mail)
    try:
        driver.find_element(By.ID, "mobile").send_keys("432427342354")
        time.sleep(1)
        driver.find_element(By.ID, "btn_submit").click()
        time.sleep(7)
        driver.close()
        print(Ctype + "  Appointment  successfully")
        driver.switch_to.window(parentwindowhandle)
    except:
        time.sleep(1)
        driver.find_element(By.ID, "btn_submit").click()
        time.sleep(7)
        driver.close()
        print(Ctype + "  Appointment successfully")
        driver.switch_to.window(parentwindowhandle)
def Reschdule(Ctype,type,Reschedule_Time,):
    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
    time.sleep(3)
    changemonth = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
    changemonth.click()
    changemonth.click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]/div[1]").click()
    driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div/div[2]/div/a/div").click()
    Type = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/p")
    Appointment_Type = Type.text
    print("Appointment Type  :  " + Appointment_Type)
    if Appointment_Type == "Online Meeting":
        link = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[5]/td[2]/p/a")
        if link.is_displayed():
            Meeting_link = link.get_attribute('href')
            print("Meeting link  : " + Meeting_link)
        else:
            print("Meeting link is Not Generated")
    elif Appointment_Type == "Over Phone":
        Mobile = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/p")
        Number = Mobile.text
        if Mobile.is_displayed():
            print("This is a Mobile Number :  " + Number)
        else:
            print("Mobile Number is Not Showing")
    elif Appointment_Type == "In-person":
        pass
    else:
        print("Appointment Type IS Not Showing")
    driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[2]/div/div/div/a[2]/button").click()
    for windowhandle in driver.window_handles:
        if windowhandle != parentwindowhandle:
            driver.switch_to.window(windowhandle)
            break
    driver.find_element(By.XPATH,
                        "/html/body/div/div/form/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/a/button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, type).click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
    st = (driver.find_element(By.ID, Reschedule_Time))
    st.click()
    time.sleep(1.2)
    button = driver.find_element(By.ID, "nextbtn")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(st))
    button.click()
    time.sleep(3)
    driver.find_element(By.ID, "btn_submit").click()
    time.sleep(6)
    driver.close()
    print(Ctype + "  Appointment Reschdule successfully")
    driver.switch_to.window(parentwindowhandle)
def Cancel(Ctype):
    nb = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
    nb.click()
    nb.click()
    driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]/div[1]").click()
    driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div/div[2]/div/a/div").click()
    driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[2]/div/div/div/a[2]/button").click()
    for windowhandle in driver.window_handles:
        if windowhandle != parentwindowhandle:
            driver.switch_to.window(windowhandle)
            break
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "/html/body/div/div/form/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/a/button").click()
    time.sleep(4.5)
    print(Ctype + "  Appointment canceled successfully")
    driver.close()
    driver.switch_to.window(parentwindowhandle)
def Approval_Pending_Appointment_Request(Ctype, Fn, Ln, mail , Frist_time , Secound_time):
    next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
    next.click()
    next.click()
    driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
    ft = driver.find_element(By.ID, Frist_time)
    Frist_slot_time = ft.text
    ft.click()
    time.sleep(1)
    st = driver.find_element(By.ID, Secound_time)
    Secound_time = st.text
    print(Frist_slot_time + " - " + Secound_time)
    st.click()
    time.sleep(1)
    button = driver.find_element(By.ID, "nextbtn")
    button.click()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys(Fn)
    driver.find_element(By.ID, "lastname").send_keys(Ln)
    driver.find_element(By.ID, "email").send_keys(mail)
    time.sleep(1)
    driver.find_element(By.ID, "btn_submit").click()
    time.sleep(3)
    driver.close()
    print(Ctype + " Type Appointment Request Sended successfully")
    driver.switch_to.window(parentwindowhandle)
def Approve(Ctype):
    driver.refresh()
    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
    time.sleep(1.5)
    driver.find_element(By.ID, "nav-pending-tab").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div[2]/a").click()
    time.sleep(1.5)
    appointment = driver.find_element(By.XPATH, "//*[@id=\"screen6\"]/div[1]/div/p/span[3]/a")
    js = driver.execute_script
    js("arguments[0].scrollIntoView(true);", appointment)
    appointment.click()
    time.sleep(1.5)
    driver.find_element(By.ID, "app-proceed").click()
    print(Ctype + " Type Approved Successfully")
    time.sleep(5)
    model = driver.find_element(By.XPATH, "//*[@id=\"app-success\"]/div/div/div[2]/div[2]/button")
    model.click()
    time.sleep(1)
    driver.refresh()
def Approval_Pending_Reschedule(Ctype, type, R_Frist_time, R_Secound_time):
    driver.refresh()
    changemonth = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
    changemonth.click()
    changemonth.click()
    driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]").click()
    driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div/div[2]/div/a/div").click()
    Type = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/p")
    Appointment_Type = Type.text
    print('Appointment Type : ' + Appointment_Type)
    if Appointment_Type == "Online Meeting":
        link = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[5]/td[2]/p/a")
        if link.is_displayed():
            Meeting_link = link.get_attribute('href')
            print("Meeting link  : " + Meeting_link)
        else:
            print("Meeting link is Not Generated")
    elif Appointment_Type == "Over Phone":
        Mobile = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/p")
        Number = Mobile.text
        if Mobile.is_displayed():
            print("This is a Mobile Number :  " + Number)
        else:
            print("Mobile Number is Not Showing")
    elif Appointment_Type == "In-person":
        pass
    else:
        print("Appointment Type IS Not Showing")
    driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[2]/div/div/div/a[2]/button").click()
    for windowhandle in driver.window_handles:
        if windowhandle != parentwindowhandle:
            driver.switch_to.window(windowhandle)
            break
    driver.find_element(By.XPATH,
                        "/html/body/div/div/form/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/a/button").click()
    # select the type
    driver.find_element(By.XPATH, type).click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
    time.sleep(1)
    driver.find_element(By.ID, R_Frist_time).click()
    time.sleep(1)
    driver.find_element(By.ID, R_Secound_time).click()
    time.sleep(5)
    driver.find_element(By.ID, "nextbtn").click()

    try:
        if driver.find_element(By.XPATH,
                               "/html/body/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/form/div[4]/label").is_displayed():
            driver.find_element(By.ID, "mobile").send_keys("2432323452")
            time.sleep(3)
            driver.find_element(By.ID, "btn_submit").click()
            time.sleep(3)
            driver.close()
            print(Ctype + " Type Appointment Reschdule Request Sended successfully")
            driver.switch_to.window(parentwindowhandle)
    except:
        time.sleep(5)
        driver.find_element(By.ID, "btn_submit").click()
        time.sleep(3)
        driver.close()
        print(Ctype + " Type Appointment Reschdule Request Sended successfully")
        driver.switch_to.window(parentwindowhandle)





class Hybrid_Calendar(unittest.TestCase):


  def test_01_Online(self):
    # Online Type Hybrid Core Function
    driver.switch_to.new_window('tab')
    driver.get("https://imeetify.com/testpurplemeet/Hybrid-Calendar")
    time.sleep(1)
    # click the online type
    online_type = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/a")
    online_type.click()
    time.sleep(5)
    Appointment("Online",Fn="Online",Ln="Type",mail="sathishtest16@gmail.com",slot_time = "9:00 AM")
    time.sleep(1)
    type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/a"
    Reschdule("Online To Online ",type,"10:00 AM")
    time.sleep(2.5)
    driver.refresh()
    Cancel('Online')
    driver.refresh()
    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
    time.sleep(3)


  def test_02_Inperson(self):
    # Inperson Type Hybrid Core Function
    driver.switch_to.new_window('tab')
    driver.get("https://imeetify.com/testpurplemeet/Hybrid-Calendar")
    time.sleep(1)
    # click the online type
    online_type = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/a")
    online_type.click()
    time.sleep(5)
    Appointment("Inperson","Inperson","Type","sathishtest16@gmail.com",slot_time='11:00 AM')
    time.sleep(1)
    type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/a"
    Reschdule("Inperson To Inperson ",type,'12:00 PM')
    time.sleep(2.5)
    driver.refresh()
    Cancel('Inperson')
    driver.refresh()
    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
    time.sleep(3)


  def test_03_OverThePhone(self):
      driver.switch_to.new_window('tab')
      driver.get("https://imeetify.com/testpurplemeet/Hybrid-Calendar")
      time.sleep(1)
      # click the online type
      otp = driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/a")
      otp.click()
      time.sleep(5)
      Appointment("OverThePhone", "Sam", "Root", "sathishtest16@gmail.com", slot_time='11:30 AM')
      time.sleep(1)
      type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/a"
      Reschdule("OverThePhone To OverThePhone", type, '12:00 PM')
      time.sleep(2.5)
      driver.refresh()
      Cancel('OverThePhone')
      driver.refresh()
      driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
      driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
      time.sleep(3)


  def test_04_Online_To_Inperson(self):
      driver.switch_to.new_window('tab')
      driver.get("https://imeetify.com/testpurplemeet/Hybrid-Calendar")
      time.sleep(1)
      # click the online type
      online_type = driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/a")
      online_type.click()
      time.sleep(5)
      Appointment("Online", Fn="Hybrid", Ln="Calendar", mail="sathishtest16@gmail.com",slot_time='1:00 PM')
      time.sleep(1)
      type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/a"
      Reschdule('Online To inperson',type,Reschedule_Time='2:00 PM')
      driver.refresh()
      time.sleep(1)
      changemonth = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
      changemonth.click()
      changemonth.click()
      time.sleep(3)
      driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]/div[1]").click()
      time.sleep(5)
      driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div/div[2]/div/a/div").click()
      Type = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/p")
      Appointment_Type = Type.text
      if Appointment_Type == "In-person":
          print("Appointment Type :  " + Appointment_Type)
          print("Appointment Online To Inperson Convert successfully ")
      else:
          print("Appointment Type :  " + Appointment_Type)
          print("Appointment Online To Inperson Convert Failed")


  def test_05_Inperson_To_OverThePhone(self):
      type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/a"
      driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
      time.sleep(3)
      driver.refresh()
      changemonth = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
      changemonth.click()
      changemonth.click()
      driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]/div[1]").click()
      driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div/div[2]/div/a/div").click()
      driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[2]/div/div/div/a[2]/button").click()
      for windowhandle in driver.window_handles:
          if windowhandle != parentwindowhandle:
              driver.switch_to.window(windowhandle)
              break
      driver.find_element(By.XPATH,
                          "/html/body/div/div/form/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/a/button").click()
      # select the type
      driver.find_element(By.XPATH, type).click()
      time.sleep(3)
      driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
      ft = driver.find_element(By.ID, "3:00 PM")
      ft.click()
      time.sleep(1.2)
      button = driver.find_element(By.ID, "nextbtn")
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable(ft))
      button.click()
      time.sleep(1)
      driver.find_element(By.ID, "mobile").send_keys("34592782393")
      time.sleep(1)
      driver.find_element(By.ID, "btn_submit").click()
      time.sleep(7)
      driver.close()
      print("Inperson To OverThePhone Type Appointment successfully")
      driver.switch_to.window(parentwindowhandle)
      time.sleep(1)
      driver.refresh()
      time.sleep(1)
      changemonth = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
      changemonth.click()
      changemonth.click()
      time.sleep(3)
      driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]/div[1]").click()
      time.sleep(5)
      driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div/div[2]/div/a/div").click()
      Type = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/p")
      Appointment_Type = Type.text
      if Appointment_Type == "Over Phone":
          print("Appointment Type :  " + Appointment_Type)
          print("Appointment Inperson To OverThePhone Convert successfully ")
          Mobile = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/p")
          Number = Mobile.text
          if Mobile.is_displayed():
              print("This is a Mobile Number :  " + Number)
          else:
              print("Mobile Number is Not Showing")
      else:
          print("Appointment Type :  " + Appointment_Type)
          print("Appointment Inperson To OverThePhone Convert Failed")


  def test_06_OverThePhone_To_Online(self):
      type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/a"
      Reschdule('OverThephone To Online',type,"12:00 PM")
      driver.refresh()
      time.sleep(1)
      changemonth = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
      changemonth.click()
      changemonth.click()
      time.sleep(3)
      driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]/div[1]").click()
      time.sleep(5)
      driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div/div[2]/div/a/div").click()
      Type = driver.find_element(By.XPATH, "//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/p")
      Appointment_Type = Type.text
      if Appointment_Type == "Online Meeting":
          print("Appointment Type :  " + Appointment_Type)
          print("Appointment OverThePhone To Online Convert successfully ")
          link = driver.find_element(By.XPATH,"//*[@id=\"screen4\"]/div[2]/div[1]/div/table/tbody/tr[5]/td[2]/p/a")
          if link.is_displayed():
              Meeting_link = link.get_attribute('href')
              print("Meeting link  : " + Meeting_link)
          else:
              print("Meeting link is Not Generated")
      else:
          print("Appointment Type :  " + Appointment_Type)
          print("Appointment OverThePhone To Online Convert Failed")
      Cancel('Online')
      driver.refresh()
      driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
      driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
      time.sleep(5)


  def test_07_Approval_Pending(self):
      # Online Type Hybrid Core Function
      driver.switch_to.new_window('tab')
      driver.get("https://imeetify.com/testpurplemeet/H-Approval-Pending")
      time.sleep(1)
      # click the online type
      online_type = driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/a")
      online_type.click()
      time.sleep(5)
      Approval_Pending_Appointment_Request('Online','Online','Approval',"sathishtest16@gmail.com",'9:00 AM','10:00 AM')
      Approve("Online")


      driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
      type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/a"
      Approval_Pending_Reschedule('Inperson',type,"12:00 PM","1:00 PM")
      Approve("Inperson")


      type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/a"
      Approval_Pending_Reschedule('Over The Phone', type, "10:00 AM", "1:30 PM")
      Approve("Over The Phone")
      type = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/a"
      Approval_Pending_Reschedule('Online', type, "9:00 AM", "9:30 AM")
      Approve("Online")
      time.sleep(3)
      driver.refresh()
      Cancel("Online")







if __name__ == '__main__':
    unittest.main()
