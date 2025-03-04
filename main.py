import requests
import tkinter as tk

#Aaita El Jabal
#Beit Yahoun
#Bint Jbeil
#Beirut

days = 5
city = "Aaita El Jabal"

window = tk.Tk()
window.title("API Weather")
window.geometry("400x250")

#city = tk.Entry(window, width=30)
#city.pack(pady=10)
#days = tk.Entry(window, width=5)
#days.pack(pady=10)
screen = tk.Listbox(window, width=50, height=10)
screen.pack(pady=10)

#print(days)

url = f"https://api.weatherapi.com/v1/forecast.json?key=1589a80a8580487cb32202758252802&q={city}&days={days}&aqi=no&alerts=no"
api_key = "1589a80a8580487cb32202758252802"

response = requests.get(url)

#print(response)
response.raise_for_status()
data = response.json()

#for w in range(days):
    #new_data = data["forecast"]["forecastday"][w]["date"]
    #weather = data["forecast"]["forecastday"][w]["day"]["avgtemp_c"]
    #print(f"{new_data} / {weather}C\n")

def Weather():
    screen.delete(0, tk.END)
    for w in range(days):
        new_data = data["forecast"]["forecastday"][w]["date"]
        weather = data["forecast"]["forecastday"][w]["day"]["avgtemp_c"]
        result = f"{new_data} / {weather}C\n"
        screen.insert(tk.END, result)
        #print(f"{new_data} / {weather}C\n")

show = tk.Button(window, width=30, text="Weather", command=Weather)
show.pack(pady=10)

print(response)

window.mainloop()