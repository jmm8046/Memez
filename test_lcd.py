import I2D_LCD_Driver
import requests
from time import *
website =  "http://api.icndb.com/jokes/random?"

mylcd= I2D_LCD_Driver.lcd()
while True:
    response = requests.get(website)
    data = response.json()
    str_pad = " "*16
    mystring = data["value"]["joke"]
    mystring = str_pad +mystring
    for i in range (0,len(mystring)):
        lcd_text = mystring[i:(i+16)]
        mylcd.lcd_display_string(lcd_text,1)
        sleep(0.2)
        mylcd.lcd_display_string(str_pad,1)
