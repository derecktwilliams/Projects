import tkinter as tk
from tkinter import *
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ' &appid=c6c307cde6a88f19555e6e6472afbff1'
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    final_info = condition + '\n' + str(temp) + ' °C'
    final_data = '\n' + 'Max Temp: ' + str(max_temp) + '\n' + 'Min Temp: ' + str(min_temp) + '\n' + 'Humidity: ' + str(humidity) +'\n' 'Wind ' + str(wind) + 'mph'
    label1.config(text = final_info)
    label2.config(text = final_data)

#deletes text on click
def click(*args):
    textfield.delete(0, 'end')


canvas = tk.Tk()
canvas.geometry("700x700")
canvas.title("WeatherApp")

f = ("poppins", 15, "bold")
t = ('poppins', 35, 'bold')

textfield = tk.Entry(canvas, font = t)
textfield.insert(0, "Enter Text")
textfield.bind("<Button-1>", click)
textfield.pack(pady = 20)
textfield.focus()


textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()


canvas.mainloop()
