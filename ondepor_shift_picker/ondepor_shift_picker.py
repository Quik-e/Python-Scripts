# By Quik-e
# Este programa se encarga de conseguir el segundo turno (10:30) para boxeo en CUBA dentro de dos dias. El programa va a correr como chronjob Lunes, Miercoles y Sábado en la hora que abran los turnos de la app ONDEPOR

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import datetime, time, os, wget

Week = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

weekend = ("Sábado", "Domingo")

# Get which day of the week is today
date = (datetime.datetime.today()+datetime.timedelta(days = 2)).date()
weekDay = Week[date.weekday()]
print("Sacando turno para", weekDay, date)
if weekDay in weekend:
    print("No shifts on weekends!")
    exit()

# Specify driver
chrometab = webdriver.Chrome(os.getcwd()+"\\chromedrivers\\chromedriver.exe") # Windows

# Automating process
chrometab.get("https://www.ondepor.com/")

# Logging in
loginForm = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="area-login"]/div/a[1]'))).click() # Click button to get login form
email = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.ID, 'loginform-email')))
passw = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.ID, 'loginform-password')))
email.clear() # Clearing fields just in case
passw.clear()
email.send_keys("USERNAME")
passw.send_keys("PASSWORD")
loginButton = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.ID, 'login'))).click()

# Picking the second shift two days from now
calButton = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar_board_icon_576"]'))).click()
nextButton = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar_club_576"]/div[1]/a[2]'))).click()
time.sleep(2)
nextButton2 = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar_club_576"]/div[1]/a[2]'))).click()
time.sleep(2)
webWeekDay = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar_club_576"]/div[1]'))).text.split(' ',1)[0].capitalize() # Get weekday (splitting it from date) of shift to make sure it's the right day
shiftStatus = WebDriverWait(chrometab,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="scroller-576"]/ul/li[2]/div[2]/button'))).text # Get shift status to see if it is full or not
print(webWeekDay, shiftStatus)
if weekDay == webWeekDay  and shiftStatus == "ANOTARME":
    signUpButton = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="scroller-576"]/ul/li[2]/div[2]/button'))).click()
    acceptTermsButton = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="reservar"]/div[2]/div[4]/div[2]/div/div/input'))).click()
    getReservationButton = WebDriverWait(chrometab,10).until(EC.element_to_be_clickable((By.ID, 'btn_submit'))).click()
elif weekDay != webWeekDay:
    print("Wrong weekday!")
elif shiftStatus == "COMPLETO":
    print("Shift is full!")
elif shiftStatus == "PROXIMAMENTE":
    print("Shift not open yet!")
chrometab.close()
