import datetime
import time
from tkinter.constants import  *
import wikipedia
import webbrowser
import os
import tkinter as tk
import requests
from bs4 import BeautifulSoup

#font
my_font = ("Comic Sans MS", 10,"bold")
font=('Roboto',10,'bold')

#colors
color=['black','red','yellow','blue','green','white']

qn=['q1','q2','q3','q4','q5','q6','q7','q8','q9']
qc = ['introduce yourself','time',"open vs",'play music','open google','open spotify']

fn=['f1','f2']
fc=['wikipedia','youtube']

cricket_on=False

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
            root = tk.Tk()
            width=root.winfo_screenwidth()
            height=root.winfo_screenheight()
            root.geometry("%dx%d" % (width, height))
            root.title("Mystic")
            root.config(bg='#000000')

            x = 0


            can2 = tk.Canvas(root,width=1920,height=955,bg='#000000',highlightthickness=0)
            can2.place(x=0,y=125)

            #creating startup lines
            text1 = tk.Label(root,text=greeting,font=(my_font),fg='#2E8B57',bg='#000000').place(x=0)
            text2 = tk.Label(root,text=startup_line,font=(my_font),fg='#2E8B57',bg='#000000').place(x=0,y=30)
            text4 = tk.Label(root,text=access,font=(my_font),fg='#2E8B57',bg='#000000').place(x=0,y=60)   

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



            spot=tk.Button(root,bg='black',border='0',image=spotify_img,command=spotify,activebackground='black')

            zoo=tk.Button(root,bg='black',border='0',image=zoom_img,command=zoom,activebackground='black')

            expl=tk.Button(root,bg='black',border='0',image=file_img,command=file_explorer,activebackground='black')



            open_arrow=tk.PhotoImage(file="C:\\Users\\91960\\OneDrive\\Desktop\\TRR\\AI\\img\\open_arrow.png")
            close_arrow=tk.PhotoImage(file="C:\\Users\\91960\\OneDrive\\Desktop\\TRR\\AI\\img\\close_arrow.png")

            def btnclose():
                    open_btn.config(image=open_arrow)
                    open_btn.config(command=btnopen)
                    unpack()

            def btnopen():
                    open_btn.config(image=close_arrow)
                    open_btn.config(command=btnclose)
                    open_btn.pack_forget()
                    spot.pack(padx=10,pady=10, side=tk.RIGHT,anchor=NE)
                    zoo.pack(padx=10,pady=10, side=tk.RIGHT,anchor=NE)
                    expl.pack(padx=10,pady=10, side=tk.RIGHT,anchor=NE)
                    close_btn.pack(side=tk.RIGHT,anchor=NE)

            close_btn=tk.Button(root,bg='black',border='0',image=close_arrow,command=btnclose,activebackground='black')

            open_btn = tk.Button(root,border=0,image=open_arrow,command=btnopen)
            open_btn.pack(anchor=E)
            """

            #cricket
            score_lab=tk.Label(root,bg='black',fg='white',font=font)
            lead_status=tk.Label(root,bg='black',fg='white',font=font)

            def score_update():
                global cricket_on
                cricket_on=True

                URL='https://www.google.com/search?q=ind+vs+eng&oq=ind+vs+eng&aqs=chrome..69i57.3743j0j1&sourceid=chrome&ie=UTF-8#sie=m;/g/11qnlqpqqx;5;/m/021q23;cm;fp;1;;'

                headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

                page = requests.get(URL,headers=headers)

                soup = BeautifulSoup(page.content,'html.parser')

                score= soup.find(class_='imspo_mh_cricket__second-score imspo_mh_cricket__one-innings-column-with-overs').get_text()
                lead=soup.find(class_='imso_mh__score-txt imso-ani imspo_mh_cricket__summary-sentence').get_text()

                score_lab.config(text=score)
                lead_status.config(text=lead)
                root.update()
                score_lab.after(5000,score_update)

            #tile
            btn=tk.Button(root,bg='black',activebackground='black',font=font,fg='#ffffff',width='20')
            btn.pack(anchor=NE,padx='10',pady='10')

            lab=tk.Label(root,bg='black',font=font,fg='#ffffff')
            lab.pack(anchor=NE,padx='10',pady='10')

            def beg():
                    webbrowser.open('https://open.spotify.com/track/3Wrjm47oTz2sjIgck11l5e?si=b543a3d98d314747')
                    lab.config(text='BEGGING')
            def badboy():
                    webbrowser.open('https://open.spotify.com/track/0RE4crnT3jRms1xxVlEZx2?si=21137575ac8e447e')
                    lab.config(text='BAD BOY')
            def makeumine():
                    webbrowser.open('https://open.spotify.com/track/5iFwAOB2TFkPJk8sMlxP8g?si=41f5317094504b37')
                    lab.config(text='MAKE YOU MINE')

            def song1():
                    btn.config(text='BEGGING')
                    btn.config(command=beg)
                    root.after(3000,song2)
            def song2():
                    btn.config(text='BAD BOY')
                    btn.config(command=badboy)
                    root.after(3000,song3)
            def song3():
                    btn.config(text='MAKE YOUR MINE')
                    btn.config(command=makeumine)
                    root.after(3000,song1)

            if cricket_on==False:
                song1()

            #removing labels when full
            def destroyer():
                for i in can2.winfo_children():
                    i.destroy()


            while True:
                query = input()
                root.update()
                #checking no.of labels
                if (x%17==0)  :
                    destroyer()

                #wakeword func
                if '' in query:
                    #response
                    tk.Label(can2,text='User Said: '+query,bg='#000000',fg='#2E8B57',font=my_font).pack(anchor=NW)

                    #Quick Commands
                    for i  in range(0,len(qn)):
                        if qn[i]==query:
                            query=qc[i]

                    for i in range(0,len(fn)):
                        if fn[i] in query:
                            query = query.replace(fn[i],fc[i])

                    #logics
                    if 'wikipedia' in query:
                        tk.Label(can2,text='Searching Wikipedia...',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        query = query.replace('wikipedia','')
                        results = wikipedia.summary(query,sentences=2)
                        tk.Label(can2,text=f'According to Wikipedia:{results}',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)                    
                        x=x+1

                    elif 'introduce yourself' in query:
                        if level == 'user':
                            tk.Label(can2,text="I Am Mystic & I Am An A.I \nAsk Me Anything",fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                            x=x+1
                        elif level == 'admin':
                            tk.Label(can2,text="Hello Sir This Is Mystic Your Friend",fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                            x=x+1

                    elif 'youtube' in query:
                        if 'search' in query:
                            query = query.replace('youtube search ','')
                            yt = (f"https://www.youtube.com/results?search_query={query}")
                            webbrowser.open(yt)
                            tk.Label(can2,text=f'Response: Results for {query}',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                            x=x+1

                        else :    
                            webbrowser.open("youtube.com")
                            tk.Label(can2,text='Response: YouTube Has Been Luanched',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                            x=x+1

                    elif 'open google' in query:
                        webbrowser.open("google.com")
                        tk.Label(can2,text='Response: Brave Has Been Launched',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'play music' in query:
                        music_dir = 'C:\\tm\\new folder'
                        songs = os.listdir(music_dir)
                        z = int(input("Enter the song index"))
                        os.startfile(os.path.join(music_dir,songs[z]))
                        tk.Label(can2,text=f'Response: PLaying song{z}',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'anime' in query:
                        webbrowser.open("gogoanime.lol")
                        tk.Label(can2,text='Response: Website Has Been Launched',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'time' in query:
                        strtime = datetime.datetime.now().strftime("%H:%M:%S")
                        var = f"the time is {strtime}"
                        tk.Label(can2,text='Response: '+var,fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open vs' in query:
                        vspath = "C:\\tm\\Code.exe"
                        os.startfile(vspath)
                        tk.Label(can2,text='Response: vs code has been launched',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open brave' in query:
                        bravepath = "C:\\tm\\brave.exe"
                        os.startfile(bravepath)
                        tk.Label(can2,text='Response: Brave has been lanched ',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open chrome' in query:
                        chromepath = "C:\\tm\\chrome.exe"
                        os.startfile(chromepath)
                        tk.Label(can2,text='Response: Chrome has been lanched ',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'open spotify' in query :
                        spotifypath = "C:\\tm\\spotify.exe"
                        os.startfile(spotifypath)
                        tk.Label(can2,text='Response: Spotify has been launched',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
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
                        tk.Label(can2,text='Response: Bad Liar is being played',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    elif 'bad boy' in query :
                        s2path = 'https://open.spotify.com/track/0RE4crnT3jRms1xxVlEZx2?si=5c2abe9739ef4bf4'
                        webbrowser.open(s2path)
                        tk.Label(can2,text='Response: runaway is being played',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    #opening folder
                    elif 'folder' in query :
                        folderpath = 'C:\\Users\\91960\\OneDrive\\Desktop\\TRR'
                        folderindex = int(input("Enter Your Folder Index"))
                        subfoldername = os.listdir(folderpath)[folderindex]
                        folderpath = folderpath + f'\\{subfoldername}'
                        os.startfile(folderpath)
                        tk.Label(can2,text='Response: Folder has been opened',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    #opening zoom
                    elif 'open zoom' in query :
                        zoompath = 'C:\\Users\\91960\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                        os.startfile(zoompath)
                        tk.Label(can2,text='Response: Zoom has been launched',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x=x+1

                    #cricket score
                    elif 'cricket' in query :
                        lab.pack_forget()
                        btn.pack_forget()
                        score_lab.pack(anchor=NE,padx='10',pady='10')
                        lead_status.pack(anchor=NE,padx='10',pady='10')
                        score_update()

                    #song    
                    elif 'songs' in query :
                        score_lab.pack_forget()
                        lead_status.pack_forget()
                        lab.pack(anchor=NE,padx='10',pady='10')
                        btn.pack(anchor=NE,padx='10',pady='10')

                    #writing notes
                    elif 'write' in query:
                        query=query.replace('write','')
                        with open('text\\notes.txt','a') as f:
                            f.write(query+'\n')
                        tk.Label(can2,text='Response: evrything is saved in notes',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
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

                        tk.Label(can2,text='Input          Result',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='Wikipedia      Show You Data From Wiki',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='Youtube        Shows The Results from Youtube',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='Open Google    Opens Your Default Browser',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='Play Music     Plays music from your Default Folder',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='Anime          Opens Anime Website',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='Time           tells u the current time',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='Open App       opens the App specified',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='folder path    opens the folderpath',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='write          Evreything is saved in a txt file',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='bgc color      changes the bg to the specific color',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        tk.Label(can2,text='stop           closes the program',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        x+=11

                    #changing background color
                    elif 'bgc' in query:
                        query=query.replace("bgc",'')
                        query=query.replace(" ",'')
                        for i in color:
                                if query==i:
                                        root.config(bg=i)
                                        root.update()

                    #refreshing total page
                    elif 'refresh' in query:
                        root.destroy()
                        maine()

                    #end
                    elif 'stop' in query :
                        tk.Label(can2,text='Response: Shutting Down In 5 Secdonds',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        root.update()
                        time.sleep(1)
                        break

                    else:
                        tk.Label(can2,text='Response: no match',fg='#2E8B57',bg='#000000',font=my_font).pack(anchor=NW)
                        root.update()
            
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
