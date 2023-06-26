from pyowm import OWM
from pyowm.utils.config import get_default_config
from PIL import ImageTk, Image
from customtkinter import *
from datetime import datetime

k = 0
def return_text():
    city.delete(0, END)

def change_theme():
    global k
    if k==0:
        set_appearance_mode("light")
        k+=1
    else:
        set_appearance_mode("dark")
        k-=1
def check_weather(*args):
    place = city.get()
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('2cbb0cc3f81c7d2ba1b18bb0247513c1', config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    det = w.detailed_status
    sp = w.wind()["speed"]
    hum = w.humidity
    pr = w.pressure.get('press')

    ans = 'Температура ' + str(temp) + ' °C'
    det_st = 'Состояние неба ' + str(det)
    sp_w = 'Скорость '+str(sp) +'м/с'
    hum_w = 'Влажность ' + str(hum) + '%'
    pr_w = 'Давление ' + str(pr)

    temperature.configure(text=ans)
    sky.configure(text=det_st)
    speed_wind.configure(text=sp_w)
    humidity.configure(text=hum_w)
    pressure.configure(text=pr_w)

    img_yasno = Image.open("ясно.png")
    photoImg_yasno = ImageTk.PhotoImage(img_yasno)
    img_pas = Image.open("пасмурно.png")
    photoImg_pas = ImageTk.PhotoImage(img_pas)
    img_per = Image.open("пер_обл.png")
    photoImg_per = ImageTk.PhotoImage(img_per)
    img_obls = Image.open("облачно_с_прояснениями.png")
    photoImg_obls = ImageTk.PhotoImage(img_obls)
    img_rain = Image.open("дождь.png")
    photoImg_rain = ImageTk.PhotoImage(img_rain)

    img_gr = Image.open("гроза.png")
    photoImg_gr = ImageTk.PhotoImage(img_gr)

    if det=="ясно":

        label = CTkLabel(root, image=photoImg_yasno, text="")
        label.place(x=20, y=285)
    elif det=="пасмурно":
        label = CTkLabel(root, image=photoImg_pas, text="")
        label.place(x=20, y=285)
    elif det=="переменная облачность":
        label = CTkLabel(root, image=photoImg_per, text="")
        label.place(x=20, y=285)
    elif det=="облачно с прояснениями":
        label = CTkLabel(root, image=photoImg_obls, text="")
        label.place(x=20, y=285)
    elif det=="небольшой дождь" or det=="дождь":
        label = CTkLabel(root, image=photoImg_rain, text="")
        label.place(x=20, y=285)
    elif det=="гроза":
        label = CTkLabel(root, image=photoImg_gr, text="")
        label.place(x=20, y=285)
    else:
        label = CTkLabel(root, text="")
root = CTk()
root.resizable(False, False)
root.geometry("300x380")
set_appearance_mode("dark")
root.title("Прогноз погоды")

root.iconbitmap("иконка_1.ico")

city = CTkEntry(root, placeholder_text="Город:")
city.place(x=5, y=10)
city.configure(width=230)

img = Image.open("return.png")
photoImg = ImageTk.PhotoImage(img)
btn_return = CTkButton(root, image=photoImg, width=25, height=25, text="", command=return_text)
btn_return.place(x=250, y=10)

img_w = Image.open("launch.png")
photoImg_w = ImageTk.PhotoImage(img_w)
weather_check = CTkButton(root, image=photoImg_w, width=25, height=25, text="", command=check_weather)
weather_check.place(x=5, y=50)

img_d = Image.open("display.png")
photoImg_d = ImageTk.PhotoImage(img_d)
change = CTkButton(root, image=photoImg_d, width=25, height=25, text="", command=change_theme)
change.place(x=250, y=340)

time = datetime.now()
text = time.strftime("Дата: %d.%m.%Y")
text1 = time.strftime("Время: %H:%M")
lbl_data = CTkLabel(root, text=text,font=CTkFont(size=14, weight="bold"))
lbl_data.place(x = 180,y = 50)


lbl_time = CTkLabel(root, text=text1,font=CTkFont(size=14, weight="bold"))
lbl_time.place(x = 180,y = 75)

wind = CTkLabel(root, text = "Ветер",font=CTkFont(size=14, weight="bold"))
wind.place(x = 20, y = 100)

speed_wind = CTkLabel(root, text = "Скорость __ м/с")

speed_wind.place(x = 20, y = 125)

barometr = CTkLabel(root, text = "Барометр",font=CTkFont(size=14, weight="bold"))
barometr.place(x = 20, y = 150)

temperature = CTkLabel(root, text = "Температура  °C")
temperature.place(x = 20, y = 175)

humidity = CTkLabel(root, text = "Влажность ")
humidity.place(x = 20, y = 200)

pressure = CTkLabel(root, text = "Давление")
pressure.place(x = 20,y = 225)

sky = CTkLabel(root, text = "Состояние неба", font=CTkFont(size=14, weight="bold"))
sky.place(x = 20,y = 250)

root.bind('<Return>', check_weather)
# root.bind('')

root.mainloop()