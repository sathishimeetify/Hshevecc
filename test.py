import unittest
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://imeetify.com/login")
parentwindowhandle = driver.current_window_handle
driver.maximize_window()
driver.find_element(By.ID, "email").send_keys("imeetifydemo@gmail.com")
driver.find_element(By.ID, "password").send_keys("Welcome@123")
driver.find_element(By.ID, "rememberMe").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id=\"content\"]/div/div/div[2]/div/form/div[5]/button").click()
time.sleep(5)


def Appointment(Ctype, Fn, Ln, mail):
    next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
    next.click()
    next.click()
    driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
    ft = driver.find_element(By.ID, "10:00 AM")
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
        driver.find_element(By.ID, "mobile").send_keys("5473298263")
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

def Reschdule(Ctype):
    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
    time.sleep(3)
    changemonth = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[1]")
    changemonth.click()
    changemonth.click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[6]/div[1]/div[2]/div[1]").click()
    time.sleep(5)
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
    driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
    time.sleep(1)
    st = (driver.find_element(By.ID, "12:00 PM"))
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


class MyTestCase(unittest.TestCase):

    def test_01_Basicfuncation_Online(self):
        driver.switch_to.new_window('tab')
        driver.get("https://imeetify.com/testpurplemeet/Online-Calendar")
        Appointment(Ctype="Online Calendar", Fn="online", Ln="Calendar", mail="sathishtest16@gmail.com")
        time.sleep(1)
        Reschdule(Ctype="Online")
        time.sleep(2.5)
        driver.refresh()
        Cancel(Ctype='Online')
        driver.refresh()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)


    def test_02_Basicfuncation_Inperson(self):
        driver.switch_to.new_window('tab')
        driver.get("https://imeetify.com/testpurplemeet/Inperson-Calendar")
        time.sleep(5)
        Appointment(Ctype="Inperson Calendar", Fn="Inperson", Ln="Calendar", mail="sathishtest16@gmail.com")
        time.sleep(1)
        Reschdule(Ctype="Inperson ")
        time.sleep(2.5)
        driver.refresh()
        Cancel(Ctype='Inperson ')
        driver.refresh()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)


    def test_03_Bas4cfuncation_OverThePhone(self):
        driver.switch_to.new_window('tab')
        driver.get("https://imeetify.com/testpurplemeet/OverThePhoneCalendar")
        time.sleep(6.5)
        Appointment('OverThePhone', 'Adam', 'Smith', 'sathishtest16@gmail.com')
        time.sleep(1)
        Reschdule('OverThePhone')
        time.sleep(2.5)
        driver.refresh()
        Cancel('OverThePhone')
        driver.refresh()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)


    def test_04_ConflictOnlineToInperson(self):
        driver.switch_to.new_window()
        FirstCalendarLink = "https://imeetify.com/testpurplemeet/C-online"
        driver.get(FirstCalendarLink)
        Appointment(Ctype="Online To Inperson", Fn="Conflict", Ln="Online - Inperon", mail="sathishtest16@gmail.com")
        driver.switch_to.window(parentwindowhandle)

        # Check the slot is bloked in secound calendar
        driver.switch_to.new_window()
        SecoundCalendarLink = "https://imeetify.com/testpurplemeet/C-Inperson"
        driver.get(SecoundCalendarLink)
        time.sleep(1)
        driver.refresh()
        next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
        next.click()
        next.click()
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
        time.sleep(2)
        check = driver.find_element(By.ID, "10:00 AM")
        classAttributeValue = check.get_attribute("class")
        if "disabled-sec" in classAttributeValue:
            print("1. Online to Inperson type calendar conflict working fine")
            time.sleep(1.5)
            driver.close()
            driver.switch_to.window(parentwindowhandle)
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
            Reschdule("Online Calendar")
            driver.switch_to.new_window()
            driver.get(SecoundCalendarLink)
            time.sleep(1.2)
            driver.refresh()
            next2 = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
            next2.click()
            next2.click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
            check3 = driver.find_element(By.ID, "10:00 AM")
            classAttributeValue3 = check3.get_attribute("class")
            if "disabled-sec" in classAttributeValue3:
                print("2. Old schedule not removed Inperson calendar")
            else:
                print("2. Old schedule is removed Inperson calendar")
                check2 = driver.find_element(By.ID, "12:00 PM")
                classAttributeValue2 = check2.get_attribute("class")
                if "disabled-sec" in classAttributeValue2:
                    print("3. Online to Inperson Conflict Reschdule is working fine")
                    driver.close()
                    driver.switch_to.window(parentwindowhandle)
                    driver.refresh()
                    Cancel("Online Calendar")
                    driver.refresh()
                    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
                    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
                    time.sleep(5)
                else:
                    print("3. Online to Inperson Conflict Reschdule not working ")
        else:
            print("1. Online to Inperson Conflict is not working ")
            driver.close()
            driver.switch_to.window(parentwindowhandle)
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
            driver.refresh()
            Cancel('Conflict Online To Inperson')
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
            time.sleep(5)


    def test_05_ConflictInpersonToOverThePhone(self):
        driver.switch_to.new_window()
        FirstCalendarLink = "https://imeetify.com/testpurplemeet/C-Inperson"
        driver.get(FirstCalendarLink)
        Appointment(Ctype="Inperson TO OTP", Fn="Conflict", Ln="Inperson To OTP ", mail="sathishtest16@gmail.com")
        driver.switch_to.window(parentwindowhandle)

        # Check the slot is bloked in secound calendar
        driver.switch_to.new_window()
        SecoundCalendarLink = "https://imeetify.com/testpurplemeet/C-OverThePhone"
        driver.get(SecoundCalendarLink)
        time.sleep(1)
        driver.refresh()
        next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
        next.click()
        next.click()
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
        time.sleep(2)
        check = driver.find_element(By.ID, "10:00 AM")
        classAttributeValue = check.get_attribute("class")
        if "disabled-sec" in classAttributeValue:
            print("1. Inperson to OverThePhone type calendar conflict working fine")
            time.sleep(1.5)
            driver.close()
            driver.switch_to.window(parentwindowhandle)
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
            driver.find_element(By.ID, "switchMonth").click()
            Reschdule(Ctype="Inperson Calendar")
            driver.switch_to.new_window()
            driver.get(SecoundCalendarLink)
            time.sleep(1.2)
            driver.refresh()
            next2 = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
            next2.click()
            next2.click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
            check3 = driver.find_element(By.ID, "10:00 AM")
            classAttributeValue3 = check3.get_attribute("class")
            if "disabled-sec" in classAttributeValue3:
                print("2. Old schedule not removed OverThePhone calendar")
            else:
                print("2. Old schedule is removed OverThePhone calendar")
                check2 = driver.find_element(By.ID, "12:00 PM")
                classAttributeValue2 = check2.get_attribute("class")
                if "disabled-sec" in classAttributeValue2:
                    print("3. Inperson to OverThePhone Conflict , Reschdule is working fine")
                    driver.close()
                    driver.switch_to.window(parentwindowhandle)
                    driver.refresh()
                    Cancel(Ctype="Inperson Calendar")
                    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
                    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
                    time.sleep(5)
                else:
                    print("3. Inperson to OverThePhone Conflict Reschdule not working ")
        else:
            print("1. InPerson to OverThePhone Conflict is not working ")
            driver.close()
            driver.switch_to.window(parentwindowhandle)
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
            driver.refresh()
            Cancel('Conflict Inperson To OverThePhone')
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
            time.sleep(5)


    def test_06_OneTimeCalendar(self):
        onetimelink = driver.find_element(By.XPATH, "//*[@id=\"features\"]/div[4]/div/div[3]/div/descendant::a")
        link = onetimelink.get_attribute("href")
        driver.switch_to.new_window()
        driver.get(link)

        next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
        next.click()
        next.click()

        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
        driver.find_element(By.ID, "10:00 AM").click()
        time.sleep(1)
        driver.find_element(By.ID, "nextbtn").click()

        driver.find_element(By.ID, "name").send_keys("Onetime")
        driver.find_element(By.ID, "lastname").send_keys("Calendar")
        driver.find_element(By.ID, "email").send_keys("sathishtest16@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "btn_submit").click()
        time.sleep(7)
        driver.close()
        driver.switch_to.window(parentwindowhandle)
        driver.switch_to.new_window()
        driver.get(link)
        time.sleep(3.5)
        if driver.find_element(By.XPATH,
                               "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[2]/a/button").is_enabled():
            print("One time link is working")
        else:
            print("One time link is not working")

        driver.close()
        driver.switch_to.window(parentwindowhandle)
        time.sleep(1)
        driver.refresh()
        e = driver.find_element(By.XPATH, "//*[starts-with(@id,'link-field')]/span[2]")
        js = driver.execute_script
        js("arguments[0].scrollIntoView(true);", e)
        e.click()
        time.sleep(3)
        rv = driver.find_element(By.XPATH, "//*[@id=\"features\"]/div[4]/div/div[3]/div/descendant::a")
        link2 = rv.get_attribute("href")
        driver.switch_to.new_window()
        driver.get(link2)
        n = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
        n.click()
        n.click()
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
        check = driver.find_element(By.ID, "10:00 AM")
        class_attribute_value = check.get_attribute("class")
        if "disabled-sec" in class_attribute_value:
            driver.close()
            print("No issue, same time after new link doesn't affect the old appointment")
            driver.switch_to.window(parentwindowhandle)
            driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
            Cancel("One Time Calendar")

        else:
            print("Showing same time slot available, so booking the slot")
            check.click()


    def test_07_ApprovalPending(self):
        driver.switch_to.new_window()
        driver.get("https://imeetify.com/testpurplemeet/Approval-Pending")
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[5]/td[6]/div").click()
        driver.find_element(By.ID, "10:00 AM").click()
        driver.find_element(By.ID, "10:30 AM").click()
        time.sleep(1)
        button = driver.find_element(By.ID, "nextbtn")
        button.click()

        # Fill in form fields
        driver.find_element(By.ID, "name").send_keys("Approval Pending")
        driver.find_element(By.ID, "lastname").send_keys("Calendar")
        driver.find_element(By.ID, "email").send_keys("sathishtest16@gmail.com")
        RB = driver.find_element(By.ID, "btn_submit")
        RB.click()
        if RB.is_selected and RB.is_displayed():
            print("First Appointment request sended successfully")
        else:
            print("First Appointment request not sended ")
        time.sleep(3)
        driver.get("https://imeetify.com/testpurplemeet/Approval-Pending")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[5]/td[6]/div").click()
        ten = driver.find_element(By.ID, "10:00 AM")
        value = ten.get_attribute("class")
        tentwo = driver.find_element(By.ID, "10:30 AM")
        valuetwo = tentwo.get_attribute("class")
        if "disabled-sec" in value and "disabled-sec" in valuetwo:
            print("Approval pending flow blocking is working fine")
            driver.close()
            driver.switch_to.window(parentwindowhandle)
        else:
            print("Approval pending Not working ")

        # Reject the appointment
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()
        time.sleep(1.5)
        driver.find_element(By.ID, "nav-pending-tab").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div[2]/a").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//*[@id=\"screen6\"]/div[3]/button").click()
        time.sleep(1.5)
        Reject_Button = driver.find_element(By.ID, "app-remove")
        Reject_Button.click()
        if Reject_Button.is_displayed() and Reject_Button.is_enabled():
            print("Appointment Rejected Successfully")
        else:
            print("Appointment Not Rejected")
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//*[@id=\"app-failure\"]/div/div/div[2]/div[2]/button").click()
        time.sleep(1.5)
        driver.switch_to.new_window()
        driver.get("https://imeetify.com/testpurplemeet/Approval-Pending")
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[5]/td[6]/div").click()

        # Check if slots are blocked
        az = driver.find_element(By.ID, "12:00 PM")
        aa = az.get_attribute("class")
        bz = driver.find_element(By.ID, "12:30 PM")
        bb = bz.get_attribute("class")

        if "disabled-sec" in aa and "disabled-sec" in bb:
            print("Slot is blocked")
        else:
            print("Old appointment rejected, and now block is free")
            az.click()
            bz.click()
            time.sleep(5)
            driver.find_element(By.ID, "nextbtn").click()
            driver.find_element(By.ID, "name").send_keys("Approval Pending")
            driver.find_element(By.ID, "lastname").send_keys("Secound Request")
            driver.find_element(By.ID, "email").send_keys("sathishtest16@gmail.com")
            Second_Request_Button = driver.find_element(By.ID, "btn_submit")
            Second_Request_Button.click()
            if Second_Request_Button.is_selected and Second_Request_Button.is_displayed():
                print("Second Appointment request sended successfully")
            else:
                print("Second Appointment request not sended ")
            time.sleep(3)

        # Close the driver
        driver.close()
        driver.switch_to.window(parentwindowhandle)
        time.sleep(1)
        driver.refresh()
        driver.find_element(By.ID, "nav-pending-tab").click()
        driver.find_element(By.XPATH, "//*[@id=\"apptListSec\"]/div[2]/a").click()

        # Approve the 1/11/23 10:00 AM
        time.sleep(3)
        appointment = driver.find_element(By.XPATH, "//*[@id=\"screen6\"]/div[1]/div/p/span[3]/a")
        js = driver.execute_script
        js("arguments[0].scrollIntoView(true);", appointment)
        appointment.click()
        time.sleep(1.5)
        driver.find_element(By.ID, "app-proceed").click()
        time.sleep(5)
        driver.refresh()
        driver.find_element(By.ID, "switchMonth").click()

        # Cancel the appointment
        driver.find_element(By.XPATH,
                            "//*[@id=\"calendar\"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[2]/table/tbody/tr/td[6]/a/div/span").click()
        time.sleep(5)
        m_link = driver.find_element(By.XPATH,"//*[@id=\"meet-rec\"]/div/dl[8]/dd/a")
        Meeting_link = m_link.get_attribute('href')
        print("Meeting link : "+ Meeting_link)
        driver.find_element(By.XPATH, "//*[@id=\"meet-rec\"]/dl/dt/a/button").click()
        for windowHandle in driver.window_handles:
            if windowHandle != parentwindowhandle:
                driver.switch_to.window(windowHandle)
                break
        time.sleep(1)
        Cancel_Button = driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/form/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/a/button")
        Cancel_Button.click()
        print("Approval Pending Appointment Cancelled Successfully")
        time.sleep(1)
        driver.close()
        driver.switch_to.window(parentwindowhandle)
        driver.refresh()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)


    def test_08_Outlook(self):
        driver.switch_to.new_window()
        FirstCalendarLink = "https://imeetify.com/testpurplemeet/Outlook-ME"
        driver.get(FirstCalendarLink)
        Appointment(Ctype='outlook calendar', Fn='Outlooksync', Ln='Calendar', mail='sathishtest16@gmail.com')

        driver.switch_to.window(parentwindowhandle)
        # Check the slot is bloked in secound calendar
        driver.switch_to.new_window()
        SecoundCalendarLink = "https://imeetify.com/testpurplemeet/Outlook-CA"
        driver.get(SecoundCalendarLink)
        time.sleep(6)
        next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
        next.click()
        next.click()
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
        time.sleep(2)
        check = driver.find_element(By.ID, "10:00 AM")
        classAttributeValue = check.get_attribute("class")
        if "disabled-sec" in classAttributeValue:
            print("1. Outlook sync is  working fine")
            time.sleep(1.5)
            driver.close()
            driver.switch_to.window(parentwindowhandle)
            Reschdule(Ctype='Outlook calendar')
            driver.switch_to.new_window()
            driver.get(SecoundCalendarLink)
            time.sleep(8.5)
            next2 = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
            next2.click()
            next2.click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
            check3 = driver.find_element(By.ID, "10:00 AM")
            classAttributeValue3 = check3.get_attribute("class")
            if "disabled-sec" in classAttributeValue3:
                print("2. Old schedule not removed in other outlook sync imeetify calendar")
            else:
                print("2. Old schedule is removed in all outlook sync imeetify  calendar")
                check2 = driver.find_element(By.ID, "12:00 PM")
                classAttributeValue2 = check2.get_attribute("class")
                if "disabled-sec" in classAttributeValue2:
                    print("3. Reschedule outlook sync is working fine")
                    driver.close()
                    driver.switch_to.window(parentwindowhandle)
                    driver.refresh()
                    Cancel(Ctype='Outlook calendar ')
                    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
                    driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
                    time.sleep(5)
                else:
                    print("3. Outlook sync Reschdule is not working ")
        else:
            print("1. Outlook sync not working in other imeetify calendar's ")


    # Advanced , Availablity , Contact Form , RestrictTimeZone , PrivateLink
    def test_09_AACRP(self):
        restricted_link = driver.find_element(By.XPATH, "//*[@id=\"features\"]/div[11]/div/div[3]/div/descendant::a")
        link = restricted_link.get_attribute("href")
        driver.switch_to.new_window()
        driver.get(link)
        button = driver.find_element(By.ID, "countryid")
        if button.is_enabled():
            print("Dropdown is clickable Restrict Time Zone is not working")
            driver.quit()

        else:
            print("Dropdown is not clickable Restrict Time Zone is working")
            text = driver.find_element(By.XPATH, "//*[@id=\"co\"]")
            mytext = text.text
            print("This Message are description Below in the country dropdown : " + mytext)
            time.sleep(3)
        driver.close()
        driver.switch_to.window(parentwindowhandle)
        driver.find_element(By.XPATH, "//*[@id=\"features\"]/div[11]/div/div[4]/ul/li[3]/a").click()
        name = driver.find_element(By.ID, "calendarname")
        name.clear()
        name.send_keys("PrivateLink")

        # On the privatelink options
        time.sleep(1)
        driver.find_element(By.ID, "makeprivate").click()
        time.sleep(1)
        driver.find_element(By.ID, "btn-next").click()
        driver.find_element(By.XPATH, "//*[@id=\"availability\"]/div/div/div/div[2]/div/div/div[1]/ul/li[3]/a").click()
        # Advanced make the unavailable
        forwardbutton = driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[2]/div/button[2]")
        forwardbutton.click()

        # Make Unaavailable 12 to 16
        source_element = driver.find_element(By.XPATH,
                                             "//*[@id=\"calendar\"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[2]")
        target_element = driver.find_element(By.XPATH,
                                             "//*[@id=\"calendar\"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[5]")

        # Create an ActionChains object
        actions = ActionChains(driver)

        # Perform drag-and-drop action to select the date range
        actions.click_and_hold(source_element).move_to_element(target_element).click().release().perform()
        time.sleep(2.5)
        driver.find_element(By.XPATH, "//*[@id=\"monthly-calendar-event\"]/div/div/div[2]/div[3]/div/div[2]").click()
        driver.find_element(By.ID, "btn-On").click()

        driver.find_element(By.XPATH,
                            "//*[@id=\"skip-target\"]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/button[1]").click()

        time.sleep(8)

        driver.find_element(By.ID, "oldnameid").click()
        for windowHandle in driver.window_handles:
            if windowHandle != parentwindowhandle:
                driver.switch_to.window(windowHandle)
                break
        Private_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div")
        linktext = Private_element.text
        if "PrivateLink" in linktext:
            print("Privatecalendar is Not working")
        else:
            print("Privatecalendar is  working")
        time.sleep(3)
        driver.close()
        driver.switch_to.window(parentwindowhandle)
        restricted_Newlink = driver.find_element(By.XPATH, "//*[@id=\"features\"]/div[11]/div/div[3]/div/descendant::a")
        link2 = restricted_Newlink.get_attribute("href")
        driver.switch_to.new_window()
        driver.get(link2)
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]").click()
        time.sleep(3)
        one = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[3]/td[2]")
        oneclass = one.get_attribute("class")
        two = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[3]/td[3]")
        twoclass = two.get_attribute("class")
        three = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[3]/td[4]")
        threeclass = three.get_attribute("class")
        four = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[3]/td[5]")
        fourclass = four.get_attribute("class")
        if oneclass == "disabled day":
            True
        else:
            print("12th Date Unavailable is not working")
        if twoclass == "disabled day":
            True
        else:
            print("13th Date Unavailable is not working")
        if threeclass == "disabled day":
            True
        else:
            print("14th Date Unavailable is not working")
        if fourclass == "disabled day":
            True
        else:
            print("15th Date Unavailable is not working")

        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[1]").click()
        time.sleep(1.5)

        time.sleep(5)
        next = driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/thead/tr[2]/th[3]")
        next.click()
        next.click()
        driver.find_element(By.XPATH, "//*[@id=\"demo-2\"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div").click()
        ft = driver.find_element(By.ID, "10:00 AM")
        ft.click()
        time.sleep(1.2)
        button = driver.find_element(By.ID, "nextbtn")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(ft))
        button.click()
        time.sleep(1)
        driver.find_element(By.ID, "name").send_keys("Contact Form")
        driver.find_element(By.ID, "lastname").send_keys("Calendar")
        driver.find_element(By.ID, "email").send_keys("sathishtest16@gmail.com")
        driver.find_element(By.ID,"companyname").send_keys("selenium")
        driver.find_element(By.ID,"mobile").send_keys("243 2343 232")
        driver.find_element(By.ID,"terms_res").click()
        save_button = driver.find_element(By.ID, "btn_submit")
        js = driver.execute_script
        js("arguments[0].scrollIntoView(true);", save_button)
        time.sleep(3)
        driver.find_element(By.ID, "promotional_res").click()
        driver.find_element(By.ID,"singlefieldsinput1").send_keys("Automation Testing With Python")
        driver.find_element(By.ID,"radiooptionid-1-1").click()
        time.sleep(2.5)
        driver.find_element(By.ID, "btn_submit").click()
        time.sleep(8)
        driver.close()
        print("Contact Form  Appointment successfully")
        driver.switch_to.window(parentwindowhandle)

        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[1]/a").click()

        Cancel('Contact Form')

        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "//*[@id=\"sidebar\"]/div/div[2]/nav/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id=\"features\"]/div[11]/div/div[4]/ul/li[3]/a").click()
        name2 = driver.find_element(By.ID, "calendarname")
        name2.clear()
        name2.send_keys("Restrictzone")
        # On the privatelink options
        driver.find_element(By.ID, "makeprivate").click()
        driver.find_element(By.ID, "btn-next").click()
        driver.find_element(By.XPATH, "//*[@id=\"availability\"]/div/div/div/div[2]/div/div/div[1]/ul/li[3]/a").click()
        time.sleep(3)
        # Advanced make the unavailable
        driver.find_element(By.XPATH, "//*[@id=\"calendar\"]/div[1]/div[2]/div/button[2]").click()

        unavailable_tab = driver.find_element(By.CLASS_NAME, "fc-title")
        if unavailable_tab.is_enabled():
            for i in range(4):
                time.sleep(1)
                driver.find_element(By.CLASS_NAME, "fc-title").click()
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    "//*[@id=\"monthly-calendar-event\"]/div/div/div[2]/div[3]/div/div[2]").click()
                driver.find_element(By.ID, "btn-Off").click()
                time.sleep(2)
                i += 1

        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//*[@id=\"skip-target\"]/div/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/button[1]").click()
        time.sleep(5)
        driver.quit()




if __name__ == '__main__':
    unittest.main()
