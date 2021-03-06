from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.init"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
       json = result.json()
       #  (city,country,temp_fahrenheit,weather)
       city = json["name"]
       country = json["sys"]["country"]
       temp_kelvin = json['main']['temp']
       temp_celsius = temp_kelvin - 273.15
       temp_fahrenheit = (temp_kelvin - 273.15)*9/5+32
       icon= json["weather"][0]["icon"]

       weather = json["weather"][0]["main"]
       final = [city,country,temp_celsius,temp_fahrenheit,weather,icon]
       return final

    else:
        return None





def search():

    city = city_text.get()
    weather = get_weather(city)



    # print(weather_state)

    if weather:
        location_lbl["text"] = '{},{}'.format(weather[0], weather[1])
        temp_lbl["text"]= '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl["text"] = weather[4]
        weather_image = (weather[5])
        # my_img = ImageTk.PhotoImage(Image.open("weather_icon//" + weather_image + ".png"))
        # img_label = Label(app,image=my_img)
        # img_label.pack()
        # img_label["image"]=my_img.show()
        # create the canvas, size in pixels
        canvas = Canvas(width=300, height=200, bg='black')

        # pack the canvas into a frame/form
        canvas.pack(expand=YES, fill=BOTH)

        # load the .gif image file
        gif1 = PhotoImage(file="weather_icon//" + weather_image + ".png")

        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        canvas.create_image(50, 10, image=gif1, anchor=NW)
        mainloop()
        




    else:
        messagebox.showerror("error,""cannot find city {}".format(city))


app = Tk()
app.title("weather app")
app.geometry("600x350")
app.iconbitmap('icon.ico')
app.config(bg='azure1')


city_text = StringVar()
city_entry = Entry(app, textvariable = city_text,bg='azure1')
city_entry.pack()

search_btn = Button(app, text="search button",font=('bold',10), width=13,command=search,bg='aquamarine4',fg="gray1")
search_btn.pack()

location_lbl = Label(app,text='',font=('calibri bold',20),bg='azure1')
location_lbl.pack()



temp_lbl = Label(app, text ="",font=('calibri bold',12),bg='azure1')
temp_lbl.pack()

weather_lbl = Label(app,text ="",font=('calibri bold',12),bg='azure1')
weather_lbl.pack()
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    my_label.config(text=hour + ":" + minute + ":" + second)
    my_labe2.config(text=day)
    my_label.after(1000, clock)


def update():
    my_label.config(text="new text")


my_label = Label(app, text="", font=("Helvetica", 18),bg="azure1",fg="black")
my_label.pack()

my_labe2 = Label(app, text="", font=("Helvetica", 12))
my_labe2.pack()
clock()

app.mainloop()
