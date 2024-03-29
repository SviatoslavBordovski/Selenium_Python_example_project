from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from ohrm.Pages.loginPage import LoginPage
from ohrm.Pages.homePage import HomePage
from ohrm.Pages.createUserPage import CreateUser
#from ohrm.Tests.signIn_signOut_positiveTest import positiveSignIn <--- we need that test if needed to run it before the created in this file
#from ohrm.Tests.signIn_signOut_negativeTest import negativeSignIn <--- we need that test if needed to run it before the created in this file
from selenium.webdriver.common.keys import Keys

class userManagement(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/incognito/Downloads/drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
 
    def test_3_createValidUser(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
 
        #Login to HRM system
        newUser = LoginPage(driver)
        newUser.enter_username('Admin')
        newUser.enter_password('admin123')
        newUser.click_login()
        
        #Creation of new user
        newUser = CreateUser(driver)
        newUser.adminSection_click()
        newUser.addUser_click()
        newUser.userRole()
        newUser.newEmployeeName('Hello World 2000')
        newUser.newUsername('Superuser30')
        newUser.status_enabled()
        newUser.new_user_password('Superuser2020!')
        newUser.new_user_confirm_password('Superuser2020!')
        newUser.click_save_user()
        time.sleep(3) #Time for checking a confirmation link during test execution
        
        #Confirmation link that should be verified after successful user addition
        confirmationLink = 'https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers'
        
        if driver.current_url == confirmationLink:
            print(confirmationLink + ' / New user was created successfully!')
        else:
            self.fail('Fix me, geeez!')
        
        #Logout from OrangeHRM system
        newUser = HomePage(driver)
        newUser.click_welcome()
        newUser.click_logout()
        
    @classmethod #Browser close and driver quit
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/incognito/Downloads/everything/projects/reports'))
