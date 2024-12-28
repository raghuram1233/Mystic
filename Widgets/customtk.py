import datetime
import time
from tkinter.constants import  *
import wikipedia
import webbrowser
import os
import customtkinter as tk
import requests
from bs4 import BeautifulSoup
from PIL import Image

#font
my_font = ("Comic Sans MS", 15,"bold")
font=('Roboto',10,'bold')

#colors
color=['black','red','yellow','blue','green','white']

qn=['q1','q2','q3','q4','q5','q6','q7','q8','q9']
qc = ['introduce yourself','time',"open vs",'play music','open google','open spotify']

fn=['f1','f2']
fc=['wikipedia','youtube']

cricket_on=False

#weather variables
APIKEY = '3b634812c1df51168e0bf159e60637e4'
lat='17.442120'
lon='78.281273'

BASE_URL=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}'
response = requests.get(BASE_URL).json()

icon_code=response['weather'][0]['icon']
desc=response['weather'][0]['description']
tem=response['main']['temp']
hum=response['main']['humidity']
tem= int(tem)-273

#checking time for greetings
def wishme(key):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        global greeting
        greeting = 'good morining!'
        print(greeting)
    elif hour>=12 and hour<18:
        greeting = 'good afternoon!'
        print(greeting)
    else:
        greeting = "good evening!"
        print(greeting)
    if key=='user':
        global startup_line
        startup_line = "i am Mystic. how may i help you"
        print(startup_line)
    elif key=='admin':
        startup_line = "hello sir tell me what to do"
        print(startup_line)
def maine():
    #checking user type
    if pwd=='wasd' or pwd == 'TrR':
        if pwd == 'wasd' :
            global access
            access = "Acess Granted As User"
            print(access)
            wishme('user')
            level = 'user'

        elif pwd == 'TrR' :
            access = "Acess Granted As Admin"
            print(access)
            wishme('admin')
            level='admin'

        if __name__ =="__main__" :

            #creating tkinter
            tk.set_appearance_mode("dark")
            tk.set_default_color_theme("blue")
            root = tk.CTk()
            win_width=root.winfo_screenwidth()
            win_height=root.winfo_screenheight()
            root.geometry("%dx%d" % (win_width, win_height))
            root.title("Mystic")

            x = 0

            root.rowconfigure(0,weight=1)
            root.rowconfigure(1,weight=12)
            root.columnconfigure(0,weight=7)
            root.columnconfigure(1,weight=1)

            intro_frame = tk.CTkFrame(root,width=1720,height=90,border_width=0)
            intro_frame.grid(column=0,row=0,sticky='nsew')

            main_frame = tk.CTkFrame(root,width=1720,height=990,border_width=0)
            main_frame.grid(column=0,row=1,sticky='nsew')

            widget_frame = tk.CTkFrame(root,width=200,height=1080,border_width=0)
            widget_frame.grid(column=1,row=0,sticky='nsew',rowspan=2)

            #creating startup lines
            text1 = tk.CTkLabel(intro_frame,text=greeting,font=my_font).place(x=0)
            text2 = tk.CTkLabel(intro_frame,text=startup_line,font=(my_font)).place(x=0,y=30)
            text4 = tk.CTkLabel(intro_frame,text=access,font=(my_font)).place(x=0,y=60)   

            """
            spotify_img=tk.PhotoImage(file="C:\\Users\\91960\\OneDrive\\Desktop\\TRR\\AI\\img\\spot.png")
            zoom_img=tk.PhotoImage(file="C:\\Users\\91960\\OneDrive\\Desktop\\TRR\\AI\\img\\zoo.png")
            file_img=tk.PhotoImage(file="C:\\Users\\91960\\OneDrive\\Desktop\\TRR\\AI\\img\\file.png")

            def unpack():
                spot.pack_forget()
                zoo.pack_forget()
                expl.pack_forget()
                close_btn.pack_forget()
                open_btn.pack(anchor=E)

            def spotify():
                path = "C:\\tm\\spotify.exe"
                os.startfile(path)
                unpack()

            def zoom():
                path = "C:\\tm\\Zoom.lnk"
                os.startfile(path)
                unpack()

            def file_explorer():
                path = "C:\\tm\\thisPC.lnk"
                os.startfile(path)
                unpack()



            spot=tk.CTkButton(root,bg='black',border='0',image=spotify_img,command=spotify)

            zoo=tk.CTkButton(root,bg='black',border='0',image=zoom_img,command=zoom)

            expl=tk.CTkButton(root,bg='black',border='0',image=file_img,command=file_explorer)



            open_arrow=tk.PhotoImage(file="C:\\Users\\91960\\OneDrive\\Desktop\\TRR\\AI\\img\\open_arrow.png")
            close_arrow=tk.PhotoImage(file="C:\\Users\\91960\\OneDrive\\Desktop\\TRR\\AI\\img\\close_arrow.png")

            def btnclose():
                    open_btn.configure(image=open_arrow)
                    open_btn.configure(command=btnopen)
                    unpack()

            def btnopen():
                    open_btn.configure(image=close_arrow)
                    open_btn.configure(command=btnclose)
                    open_btn.pack_forget()
                    spot.pack(padx=10,pady=10, side=tk.RIGHT,anchor=NE)
                    zoo.pack(padx=10,pady=10, side=tk.RIGHT,anchor=NE)
                    expl.pack(padx=10,pady=10, side=tk.RIGHT,anchor=NE)
                    close_btn.pack(side=tk.RIGHT,anchor=NE)

            close_btn=tk.CTkButton(root,bg='black',border='0',image=close_arrow,command=btnclose)

            open_btn = tk.CTkButton(root,border=0,image=open_arrow,command=btnopen)
            open_btn.pack(anchor=E)
            """

            #cricket
            score_lab=tk.CTkLabel(root,font=font)
            lead_status=tk.CTkLabel(root,font=font)

            def score_update():
                global cricket_on
                cricket_on=True

                URL='https://www.google.com/search?q=ind+vs+eng&oq=ind+vs+eng&aqs=chrome..69i57.3743j0j1&sourceid=chrome&ie=UTF-8#sie=m;/g/11qnlqpqqx;5;/m/021q23;cm;fp;1;;'

                headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

                page = requests.get(URL,headers=headers)

                soup = BeautifulSoup(page.content,'html.parser')

                score= soup.find(class_='imspo_mh_cricket__second-score imspo_mh_cricket__one-innings-column-with-overs').get_text()
                lead=soup.find(class_='imso_mh__score-txt imso-ani imspo_mh_cricket__summary-sentence').get_text()

                score_lab.configure(text=score)
                lead_status.configure(text=lead)
                root.update()
                score_lab.after(5000,score_update)

            '''

            #tile
            btn=tk.CTkButton(root,font=font,width=20)
            btn.pack(anchor=NE,padx='10',pady='10')

            def beg():
                    webbrowser.open('https://open.spotify.com/track/3Wrjm47oTz2sjIgck11l5e?si=b543a3d98d314747')
            def badboy():
                    webbrowser.open('https://open.spotify.com/track/0RE4crnT3jRms1xxVlEZx2?si=21137575ac8e447e')
            def makeumine():
                    webbrowser.open('https://open.spotify.com/track/5iFwAOB2TFkPJk8sMlxP8g?si=41f5317094504b37')

            def song1():
                    btn.configure(text='BEGGING')
                    btn.configure(command=beg)
                    root.after(3000,song2)
            def song2():
                    btn.configure(text='BAD BOY')
                    btn.configure(command=badboy)
                    root.after(3000,song3)
            def song3():
                    btn.configure(text='MAKE YOUR MINE')
                    btn.configure(command=makeumine)
                    root.after(3000,song1)

            if cricket_on==False:
                song1()

            '''

            #weather frame
            weather_frame=tk.CTkFrame(widget_frame,height=200,width=200,fg_color='#3B8489',border_width=10)
            weather_frame.grid(sticky='nsew')
            weather_frame.grid_propagate(False)

            weather_frame.columnconfigure(0,weight=1)
            weather_frame.columnconfigure(1,weight=1)
            weather_frame.rowconfigure(0,weight=2)
            weather_frame.rowconfigure(1,weight=1)
            weather_frame.rowconfigure(2,weight=1)

            icon = tk.CTkImage(dark_image=Image.open(f".\\weathericons\\{icon_code}.png"),light_image=Image.open(f".\\weathericons\\50d.png"),size=(100,100))
            iconlab=tk.CTkLabel(weather_frame,image=icon,text='',fg_color='transparent')
            iconlab.grid(row=0,column=0,sticky='nsew')

            tk.CTkLabel(weather_frame,text=f'{tem}°c',fg_color='transparent',font=my_font).grid(row=0,column=1,sticky='nsew')

            tk.CTkLabel(weather_frame,text=f'Humidity : {hum}%',font=my_font).grid(column=0,row=1,columnspan=2,sticky='nsew')

            tk.CTkLabel(weather_frame,text=f'{desc}',font=my_font).grid(column=0,row=2,columnspan=2,sticky='nsew')

            #removing CTklabels when full
            def destroyer():
                for i in main_frame.winfo_children():
                    i.destroy()
            root.update()

            while True:

                query = input()
                root.update()
                #checking no.of CTklabels
                if (x%17==0)  :
                    destroyer()

                #wakeword func
                if '' in query:
                    #response
                    tk.CTkLabel(main_frame,text='User Said: '+query,font=my_font).pack(anchor=NW)

                    #Quick Commands
                    for i  in range(0,len(qn)):
                        if qn[i]==query:
                            query=qc[i]

                    for i in range(0,len(fn)):
                        if fn[i] in query:
                            query = query.replace(fn[i],fc[i])

                    #logics
                    if 'wikipedia' in query:
                        tk.CTkLabel(main_frame,text='Searching Wikipedia...',font=my_font).pack(anchor=NW)
                        query = query.replace('wikipedia','')
                        results = wikipedia.summary(query,sentences=2)
                        tk.CTkLabel(main_frame,text=f'According to Wikipedia:{results}',font=my_font).pack(anchor=NW)                    
                        x=x+1

                    elif 'introduce yourself' in query:
                        if level == 'user':
                            tk.CTkLabel(main_frame,text="I Am Mystic & I Am An A.I \nAsk Me Anything",font=my_font).pack(anchor=NW)
                            x=x+1
                        elif level == 'admin':
                            tk.CTkLabel(main_frame,text="Hello Sir This Is Mystic Your Friend",font=my_font).pack(anchor=NW)
                            x=x+1

                    elif 'youtube' in query:
                        if 'search' in query:
                            query = query.replace('youtube search ','')
                            yt = (f"https://www.youtube.com/results?search_query={query}")
                            webbrowser.open(yt)
                            tk.CTkLabel(main_frame,text=f'Response: Results for {query}',font=my_font).pack(anchor=NW)
                            x=x+1

                        else :    
                            webbrowser.open("youtube.com")
                            tk.CTkLabel(main_frame,text='Response: YouTube Has Been Launched',font=my_font).pack(anchor=NW)
                            x=x+1

                    elif 'open google' in query:
                        webbrowser.open("google.com")
                        tk.CTkLabel(main_frame,text='Response: Brave Has Been Launched',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'play music' in query:
                        music_dir = 'C:\\tm\\new folder'
                        songs = os.listdir(music_dir)
                        z = int(input("Enter the song index"))
                        os.startfile(os.path.join(music_dir,songs[z]))
                        tk.CTkLabel(main_frame,text=f'Response: PLaying song{z}',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'anime' in query:
                        webbrowser.open("gogoanime.lol")
                        tk.CTkLabel(main_frame,text='Response: Website Has Been Launched',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'time' in query:
                        strtime = datetime.datetime.now().strftime("%H:%M:%S")
                        var = f"the time is {strtime}"
                        tk.CTkLabel(main_frame,text='Response: '+var,font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open vs' in query:
                        vspath = "C:\\tm\\Code.exe"
                        os.startfile(vspath)
                        tk.CTkLabel(main_frame,text='Response: vs code has been launched',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open brave' in query:
                        bravepath = "C:\\tm\\brave.exe"
                        os.startfile(bravepath)
                        tk.CTkLabel(main_frame,text='Response: Brave has been lanched ',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open chrome' in query:
                        chromepath = "C:\\tm\\chrome.exe"
                        os.startfile(chromepath)
                        tk.CTkLabel(main_frame,text='Response: Chrome has been lanched ',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open spotify' in query :
                        spotifypath = "C:\\tm\\spotify.exe"
                        os.startfile(spotifypath)
                        tk.CTkLabel(main_frame,text='Response: Spotify has been launched',font=my_font).pack(anchor=NW)
                        x=x+1

                    #for addition

                    elif '+' in query :
                        ab=[]

                        for a in query.split():
                            if a.isdigit():
                                ab.append(int(a))

                        y = 0

                        for p in range(0,len(ab)):
                            x = y + ab[p]
                            y = x

                        print(y) 

                    #for multiplication
                    elif 'into' in query :
                        ab=[]

                        for a in query.split():
                            if a.isdigit():
                                ab.append(int(a))

                        y = 1

                        for p in range(0,len(ab)):
                            x = y * ab[p]
                            y = x

                        print(y)

                    #for division
                    elif 'by' in query :
                        ab=[]

                        for a in query.split():
                            if a.isdigit():
                                ab.append(int(a))

                        y = ab[0]/ab[1]

                        print(y)

                    #for Substraction
                    elif '-' in query :
                        ab=[]

                        for a in query.split():
                            if a.isdigit():
                                ab.append(int(a))

                        y = ab[0]

                        for p in range(1,len(ab)):
                            x = y - ab[p]
                            y = x

                        print(y)

                    #songs
                    elif 'begging' in query :
                        spath = 'https://open.spotify.com/track/3Wrjm47oTz2sjIgck11l5e?si=ff73e53ccca1434e'
                        webbrowser.open(spath)
                        tk.CTkLabel(main_frame,text='Response: Bad Liar is being played',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'bad boy' in query :
                        s2path = 'https://open.spotify.com/track/0RE4crnT3jRms1xxVlEZx2?si=5c2abe9739ef4bf4'
                        webbrowser.open(s2path)
                        tk.CTkLabel(main_frame,text='Response: runaway is being played',font=my_font).pack(anchor=NW)
                        x=x+1

                    #opening folder
                    elif 'folder' in query :
                        folderpath = 'C:\\Users\\91960\\OneDrive\\Desktop\\TRR'
                        folderindex = int(input("Enter Your Folder Index"))
                        subfoldername = os.listdir(folderpath)[folderindex]
                        folderpath = folderpath + f'\\{subfoldername}'
                        os.startfile(folderpath)
                        tk.CTkLabel(main_frame,text='Response: Folder has been opened',font=my_font).pack(anchor=NW)
                        x=x+1

                    #opening zoom
                    elif 'open zoom' in query :
                        zoompath = 'C:\\Users\\91960\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                        os.startfile(zoompath)
                        tk.CTkLabel(main_frame,text='Response: Zoom has been launched',font=my_font).pack(anchor=NW)
                        x=x+1
                   

                    #writing notes
                    elif 'write' in query:
                        query=query.replace('write','')
                        with open('text\\notes.txt','a') as f:
                            f.write(query+'\n')
                        tk.CTkLabel(main_frame,text='Response: evrything is saved in notes',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'help'  in query:
                        print("Input          Result")
                        print("Wikipedia      Show You Data From Wiki")
                        print("Youtube        Shows The Results from Youtube")
                        print("Open Google    Opens Your Default Browser")
                        print("Play Music     Plays music from your Default Folder")
                        print("Anime          Opens Anime Website")
                        print("Time           tells u the current time")
                        print("Open App       opens the App specified")
                        print("folder path    opens the folderpath")
                        print("write          Evreything is saved in a txt file")
                        print("bgc color      changes the bg to the specific color")
                        print("refresh        reloads everything")
                        print("stop           closes the program")

                        tk.CTkLabel(main_frame,text='Input          Result',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='Wikipedia      Show You Data From Wiki',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='Youtube        Shows The Results from Youtube',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='Open Google    Opens Your Default Browser',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='Play Music     Plays music from your Default Folder',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='Anime          Opens Anime Website',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='Time           tells u the current time',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='Open App       opens the App specified',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='folder path    opens the folderpath',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='write          Evreything is saved in a txt file',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='bgc color      changes the bg to the specific color',font=my_font).pack(anchor=NW)
                        tk.CTkLabel(main_frame,text='stop           closes the program',font=my_font).pack(anchor=NW)
                        x+=11

                    #changing background color
                    elif 'bgc' in query:
                        query=query.replace("bgc",'')
                        query=query.replace(" ",'')
                        for i in color:
                                if query==i:
                                        root.configure(bg=i)
                                        root.update()

                    #refreshing total page
                    elif 'refresh' in query:
                        root.destroy()
                        maine()

                    #end
                    elif 'stop' in query :
                        tk.CTkLabel(main_frame,text='Response: Shutting Down In 5 Secdonds',font=my_font).pack(anchor=NW)
                        root.update()
                        time.sleep(1)
                        break

                    else:
                        tk.CTkLabel(main_frame,text='Response: no match',font=my_font).pack(anchor=NW)
                        with open('text\\error_log.txt','a') as f:
                            f.write(query + '\n')
                        root.update()

            
            
            root.mainloop()
count=0
while count < 4:
    pwd = input('Enter Your Acess Key: ')
    if pwd=='wasd' or pwd=='TrR':
        print('Access Granted')
        maine()
        break
    else:
        with open('text\\acess.txt','a') as f :
            f.write(f"Some One Tried To Acess With Key '{pwd}' \n")
        z=3-count
        print(f'Access denied. Try again.You Have {z}Chances')
        count += 1
