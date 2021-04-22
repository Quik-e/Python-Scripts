from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import datetime, time, os, wget

def getInfo():
    #steamCheater = input("Please enter Steam Cheater's account link: ")
    steamCheater = "https://steamcommunity.com/profiles/76561199113929200"
    return steamCheater

class ReportBot():
    def __init__(self, email = "",steamID = "", password = ""):
        self.email = email
        self.steamID = steamID
        self.password = password
        self.loggedin = False
        self.chrometab = webdriver.Chrome(os.getcwd()+"\\chromedrivers\\chromedriver.exe") # Windows

    def steam_login(self):
        print(f"Logging in as BOT {self.steamID}")
        try:
            self.chrometab.get("https://steamcommunity.com/login/home/?goto=") #Open chrometab for Steam Login
            if(self.steamID == "" or self.password == ""): raise LoginDataError
            # Locate and load username and password
            username = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.ID, 'input_username')))
            password = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.ID, 'input_password')))
            username.clear()
            password.clear()
            username.send_keys(self.steamID)
            password.send_keys(self.password)
            submitButton = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_btn_signin > button'))).click()
            if(WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.ID, 'subHead'))).text == "Welcome to The Steam Community"):
                print("Login successful")
                self.loggedin = True
            else:
                raise loginError
        except LoginDataError:
            print("loginDataError: Please check username and password")
            self.chrometab.close()
        except loginError:
            print("Login Error")
            self.chrometab.close()
    
    def report_cheater(self, chLink = ""):
        while(chLink == ""):
            chLink = input(r"Please insert the cheater's steamlink: ")
            if ("steamcommunity.com/profiles" not in chLink): chLink = ""
        if(self.loggedin == False): self.steam_login()
        print("Reporting player")
        self.chrometab.get(chLink) # Go to cheater's steam profile
        actionButton = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.ID, 'profile_action_dropdown_link'))).click()
        reportButton = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="profile_action_dropdown"]/div[9]/a[2]'))).click()
        chInGametButton = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="step_content"]/div[6]'))).click()
        reportButton2 = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.ID, 'report_button'))).click()
        cheatComments = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.ID, 'report_txt_input')))
        cheatComments.clear()
        cheatComments.send_keys("Mucho Wallhack aca")
        selectGameButton = WebDriverWait(self.chrometab, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select_recently_played"]/div[@data-appid="730"]'))).click()
        #submitReport = WebDriverWait(self.chrometab, 10). until(EC.element_to_be_clickable((By.ID,'btn_submit_report'))).click()

if(__name__ == '__main__'):
    bot = ReportBot("", "workinprogress_gg", "wip1234566")
    bot.steam_login()
    bot.report_cheater("https://steamcommunity.com/profiles/76561199113929200")