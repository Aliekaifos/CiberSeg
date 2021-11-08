# KEILA SOFIA CABALLERO RAMOS
# LLENADO DE FORMULARIO
# https://forms.office.com/r/S8Jy6Jsvmh
import pyautogui
import time
from faker import Faker
fake = Faker()

pregunta2 = ["Al infinito y mas alla", "No contaban con mi astucia"]

# PRIMER LLENADO
pyautogui.click(x=371, y=526, clicks=1)
print("DC")
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite(pregunta2[0])
print(pregunta2[0])
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('down')
print("9 AM")
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
mail = fake.email()
print(mail)
pyautogui.write(mail)
pyautogui.press('tab')
time.sleep(3)
# SCREEN
im = pyautogui.screenshot()
print(im)
im.save(r'ss1.png')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)

pyautogui.press('tab')

# SEGUNDO LLENADO
pyautogui.press('enter')

pyautogui.click(x=371, y=484, clicks=1)
print("MARVEL")
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite(pregunta2[1])
print(pregunta2[1])
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('down')
print("10 AM")
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
mail2 = fake.email()
print(mail2)
pyautogui.write(mail2)
pyautogui.press('tab')
time.sleep(3)
# SCREEN
im = pyautogui.screenshot()
print(im)
im.save(r'ss2.png')
time.sleep(3)
pyautogui.press('enter')
