import customtkinter as tk
from PIL import Image

wea = tk.CTk()
tk.set_appearance_mode("dark")
win_width=wea.winfo_screenwidth()
win_height=wea.winfo_screenheight()
wea.geometry("%dx%d" % (win_width, win_height))

wall = tk.CTkImage(dark_image=Image.open(f".\\bg_img\\wall2.png"),light_image=Image.open(f".\\bg_img\\wall2.png"),size=(100,100))
walli=tk.CTkLabel(wea,image=wall,text='',fg_color='transparent')
walli.place(x=0,y=0)

#wea.rowconfigure(0,weight=1)
#wea.rowconfigure(1,weight=10)
#wea.columnconfigure(0,weight=7)
#wea.columnconfigure(1,weight=1)

framered = tk.CTkFrame(wea,bg_color='red',fg_color='red',border_width=0,width=1720,height=90)
framered.grid(column=0,row=0,sticky='nsew')

frameblue = tk.CTkFrame(wea,bg_color='blue',fg_color='blue',border_width=0,width=1720,height=990)
frameblue.grid(column=0,row=1,sticky='nsew')

framegreen = tk.CTkFrame(wea,width=200,height=1080)
framegreen.grid(column=1,row=0,sticky='nsew',rowspan=2)

weather_frame = tk.CTkFrame(framegreen,height=200,width=200,fg_color="transparent",corner_radius=20,bg_color='pink')
weather_frame.grid()
weather_frame.grid_propagate(False)

weather_frame.columnconfigure(0,weight=1)
weather_frame.columnconfigure(1,weight=1)
weather_frame.rowconfigure(0,weight=2)
weather_frame.rowconfigure(1,weight=1)
weather_frame.rowconfigure(2,weight=1)

icon = tk.CTkImage(dark_image=Image.open(f".\\weathericons\\50d.png"),light_image=Image.open(f".\\weathericons\\50d.png"),size=(100,100))
iconlab=tk.CTkLabel(weather_frame,image=icon,text='',fg_color='transparent')
iconlab.grid(row=0,column=0,sticky='nsew')

temp = tk.CTkLabel(weather_frame,text=25,fg_color='transparent').grid(row=0,column=1,sticky='nsew')

humidity = tk.CTkLabel(weather_frame,text=f'Humidity : 50%').grid(column=0,row=1,columnspan=2,sticky='nsew')

description = tk.CTkLabel(weather_frame,text='haze').grid(column=0,row=2,columnspan=2,sticky='nsew')

wea.mainloop()