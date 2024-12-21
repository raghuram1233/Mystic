from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
import time
import wikipedia
import webbrowser
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    path = os.path.join(base_path, relative_path)
    path = path.replace('\\','/')
    return path


#colors
color=['black','red','yellow','blue','green','white']

qn=['q1','q2','q3','q4','q5','q6','q7','q8','q9']
qc = ['introduce yourself','time',"open vs",'play music','open google','open spotify']

fn=['f1','f2']
fc=['wikipedia','youtube']

class ScrollLabel(QtWidgets.QScrollArea):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QtWidgets.QScrollArea.__init__(self, *args, **kwargs)
        
        # making widget resizable
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
 
        # making qwidget object
        content = QtWidgets.QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QtWidgets.QVBoxLayout(content)
 
        # creating label
        self.label = QtWidgets.QLabel(content)
        self.label.setStyleSheet('color:rgb(238,236,239);')
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        # setting alignment to the text
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)
 
    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

class Ui_LoginWindow(object):
    def __init__(self):
        self.count = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        QtGui.QFontDatabase.addApplicationFont("Resources/Inspiration_Regular.ttf")
        font_family = 'Inspiration'
        custom_font = QtGui.QFont(font_family)

        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(33, 37, 41);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #LoginPage Code
        self.Login = QtWidgets.QFrame(self.centralwidget)
        self.Login.setEnabled(True)
        self.Login.setGeometry(QtCore.QRect(350, 150, 500, 300))
        self.Login.setStyleSheet("background-color: rgb(52, 58, 64);\n"
"border-radius : 57px;")
        self.Login.setObjectName("Login")
        self.Enter_label = QtWidgets.QLabel(self.Login)
        self.Enter_label.setGeometry(QtCore.QRect(100, 50, 300, 95))

        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)

        custom_font.setPointSize(40)
        self.Enter_label.setFont(custom_font)
        self.Enter_label.setStyleSheet("color: rgb(233, 236, 239);")
        self.Enter_label.setObjectName("Enter_label")
        self.key_enter = QtWidgets.QPushButton(self.Login)
        self.key_enter.setGeometry(QtCore.QRect(371, 190, 94, 54))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.key_enter.setFont(font)
        self.key_enter.setStyleSheet("border-radius : 20px;\n"
"color: rgb(233, 236, 239);\n"
"background-color: rgb(73, 80, 87);")
        self.key_enter.setObjectName("key_enter")
        self.key_input = QtWidgets.QLineEdit(self.Login)
        self.key_input.setEnabled(True)
        self.key_input.setGeometry(QtCore.QRect(50, 190, 300, 54))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.key_input.setFont(font)
        self.key_input.setStyleSheet("border-radius : 20px;\n"
"background-color: rgb(73, 80, 87);\n"
"padding-left: 5px;")
        self.key_input.setText("")
        self.key_input.setObjectName("key_input")
        self.key_input.setFocus()
        self.no_of_chances = QtWidgets.QLabel(self.Login)
        self.no_of_chances.setGeometry(QtCore.QRect(60, 250, 405, 30))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(8)
        font.setKerning(True)
        self.no_of_chances.setFont(font)
        self.no_of_chances.setStyleSheet("color:rgb(238,236,239);")
        self.no_of_chances.setText("")
        self.no_of_chances.setObjectName("no_of_chances")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.key_enter.clicked.connect(self.login)
        self.key_input.returnPressed.connect(self.login)


        #MainPage code
        self.legend = QtWidgets.QFrame(self.centralwidget)
        self.legend.resize(1200,600)
        self.legend.hide()
        self.statusbar.setVisible(False)
        self.sidebar_frame = QtWidgets.QFrame(self.legend)
        self.sidebar_frame.setGeometry(QtCore.QRect(0, 0, 70, 600))
        self.sidebar_frame.setStyleSheet("background-color: rgb(52, 58, 64);")
        self.sidebar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar_frame.setObjectName("sidebar_frame")

        self.Ai_frame = QtWidgets.QFrame(self.legend)
        self.Ai_frame.setGeometry(QtCore.QRect(70, 0, 1130, 600))
        self.Ai_frame.setStyleSheet("background-color: rgb(33, 37, 41);")
        self.Ai_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ai_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Ai_frame.setObjectName("Ai_frame")

        self.Apps_frame = QtWidgets.QFrame(self.legend)
        self.Apps_frame.setGeometry(QtCore.QRect(70, 0, 1130, 600))
        self.Apps_frame.setStyleSheet("background-color: rgb(33, 37, 41);")
        self.Apps_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Apps_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Apps_frame.setObjectName("Apps_frame")
        self.Apps_frame.hide()

        self.settings_frame = QtWidgets.QFrame(self.legend)
        self.settings_frame.setGeometry(QtCore.QRect(70, 0, 1130, 600))
        self.settings_frame.setStyleSheet("background-color: rgb(33, 37, 41);")
        self.settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_frame.setObjectName("settings_frame")
        self.settings_frame.hide()

        self.Ai_Button = QtWidgets.QPushButton(self.sidebar_frame)
        self.Ai_Button.setGeometry(17, 15, 35, 35)
        self.Ai_Button.setStyleSheet(f"background-image : url({resource_path('Resources/img/home.png')}); border-radius:0")
        self.Ai_Button.setText("")
        self.Ai_Button.clicked.connect(self.Ai_display)
        self.Ai_Button.setObjectName("Ai_Button")

        self.apps_btn = QtWidgets.QPushButton(self.sidebar_frame)
        self.apps_btn.setGeometry(QtCore.QRect(18, 100, 35, 35))
        self.apps_btn.setStyleSheet(f"background-image : url({resource_path('Resources/img/app_grid.png')}); border-radius:0")
        self.apps_btn.setText("")
        self.apps_btn.clicked.connect(self.App_display)
        self.apps_btn.setObjectName("apps_btn")

        self.pushButton_3 = QtWidgets.QPushButton(self.sidebar_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 185, 40, 40))
        self.pushButton_3.setStyleSheet("border-radius : 10px;background-color: rgb(73, 80, 87);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.settings_btn = QtWidgets.QPushButton(self.sidebar_frame)
        self.settings_btn.setGeometry(QtCore.QRect(15,545,40,40))
        self.settings_btn.setStyleSheet(f"background-image : url({resource_path('Resources/img/settings_icon.png')}); border-radius:0")
        self.settings_btn.setText('')
        self.settings_btn.clicked.connect(self.settings_display)
        self.settings_btn.setObjectName("settings_btn")

        search_field_font = QtGui.QFont()
        search_field_font.setPointSize(17)
        self.search_field = QtWidgets.QLineEdit(self.Ai_frame)
        self.search_field.setFont(search_field_font)
        self.search_field.setGeometry(QtCore.QRect(250,530,600,50))
        self.search_field.setStyleSheet("border-radius:20px;background-color: rgb(108,117,125); padding-left:5px;")
        self.search_field.setObjectName("search_field")

        self.search_btn = QtWidgets.QPushButton(self.Ai_frame)
        self.search_btn.setGeometry(QtCore.QRect(865,530,50,50))
        self.search_btn.setStyleSheet(f"border-radius:20;background-color: rgb(108,117,125);  background-image : url({resource_path('Resources/img/arrow_right.png')});background-repeat: no-repeat; background-position: center;   ")
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.msgsent)
        self.search_field.returnPressed.connect(self.msgsent)

        self.text_area = QtWidgets.QScrollArea(self.Ai_frame)
        self.text_area.setGeometry(165,0,800,500)
        self.text_area.setStyleSheet("border:0; ")
        self.text_area.setObjectName("text_frame")
 
        self.scroll_label = ScrollLabel(self.text_area)
        self.chat = ''
        self.scroll_label.setText(self.chat)
        self.scroll_label.setGeometry(0,0,800, 500)

        self.app_grid_frame = QtWidgets.QFrame(self.Apps_frame)
        self.app_grid_frame.setGeometry(70,65,990,470)
        self.app_grid_frame.setStyleSheet("background-color: rgb(52,58,64);border-radius: 40px;")
        self.app_grid_frame.setObjectName("app_grid_frame")
        self.app_grid_layout = QtWidgets.QGridLayout()
        self.app_grid_frame.setLayout(self.app_grid_layout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)       



    def login(self):
        if self.count != 3:
            pwd = self.key_input.text()
            self.key_input.setText('')
            if pwd=='wasd' or pwd=='TrR':
                hour = int(datetime.datetime.now().hour)
                if pwd=='wasd':
                    self.power = 'user'
                else:
                    self.power = 'admin'

                if hour>=0 and hour<12:
                    self.chat+='good morining!'
                elif hour>=12 and hour<18:
                    self.chat+='good afternoon!'
                else:
                    self.chat+="good evening!"

                if self.power=='user':
                    self.chat+='\n'+"i am Mystic. how may i help you"

                elif self.power=='admin':
                    self.chat+='\n'+"hello sir tell me what to do"

                self.no_of_chances.setText('Access Granted')
                self.Login.deleteLater()
                self.legend.show()
                self.scroll_label.setText(self.chat)
                self.search_field.setFocus()

            else:
                z=3-self.count
                self.no_of_chances.setText(f'Access denied. Try again.You Have {z}Chances')
                self.count += 1
        else:
            MainWindow.close()

    def msgsent(self):
        if(self.search_field.text()!=''):
            self.chat+='\nMe :' + (self.search_field.text())
            self.scroll_label.setText(self.chat)
            self.airesponse(self.search_field.text())
            self.search_field.setFocus()

    def airesponse(self,query):
        self.search_field.setText('')
        self.chat+='\n'+'Response : '

        #Quick Commands
        for i  in range(0,len(qn)):
            if qn[i]==query:
                query=qc[i]

        for i in range(0,len(fn)):
            if fn[i] in query:
                query = query.replace(fn[i],fc[i])
        

        #logics

        if 'wikipedia' in query:
            self.chat+='Searching Wikipedia...'
            query = query.replace('wikipedia','')
            try:
                results = wikipedia.summary(query,sentences=2)
            except:
                results = f'{query} is Not Found'
            self.chat+=f'According to Wikipedia:{results}'

        elif 'introduce yourself' in query:
            if self.power == 'user':
                self.chat+='I Am Mystic & I Am An A.I \nAsk Me Anything'
            
            elif self.power == 'admin':
                self.chat+='Hello Sir This Is Mystic Your Friend'
                        
        elif 'youtube' in query:
            if 'search' in query:
                query = query.replace('youtube search ','')
                yt = (f"https://www.youtube.com/results?search_query={query}")
                webbrowser.open(yt)
                self.chat+=f'Results for {query}'
            
            else :    
                webbrowser.open("youtube.com")
                self.chat+='YouTube Has Been Launched'
                        

        elif 'open google' in query:
            webbrowser.open("google.com")
            self.chat+=' Brave Has Been Launched'

        elif 'anime' in query:
            webbrowser.open("https://animesuge.to/home")
            self.chat+=' Website Has Been Launched'
        
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var = f"the time is {strtime}"
            self.chat+=var

        elif 'add path' in query:
            query=query.replace('add path','')
            query=query.replace(' ','')
            app_ = open(resource_path('C:\\TRR\\TRR\\AI\\Resources\\text\\app_path.txt'),'a')
            app_.write('\n' + query)
            self.chat+='Application Has Been Added.'

        elif 'remove path' in query:
            query=query.replace('remove path','')
            query=query.replace(' ','')
            
            self.chat+='Application Has Been Removed.'
        
            with open(resource_path("Resources\\text\\app_path.txt"), "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != query:
                        f.write(i)
                f.truncate()

        #writing notes
        elif 'write' in query:
            query=query.replace('write','')
            with open(resource_path('text\\notes.txt'),'a') as f:
                f.write(query+'\n')
            
            self.chat+='evrything is saved in notes'
                    

        elif 'help'  in query:
            self.chat+="\nInput          Result\n"
            self.chat+="Wikipedia      Show You Data From Wiki\n"
            self.chat+="Youtube        Shows The Results from Youtube\n"
            self.chat+="Open Google    Opens Your Default Browser\n"
            self.chat+="Play Music     Plays music from your Default Folder\n"
            self.chat+="Anime          Opens Anime Website\n"
            self.chat+="Time           tells u the current time\n"
            self.chat+="Open App       opens the App specified\n"
            self.chat+="folder path    opens the folderpath\n"
            self.chat+="write          Evreything is saved in a txt file\n"
            self.chat+="bgc color      changes the bg to the specific color\n"
            self.chat+="refresh        reloads everything\n"
            self.chat+="stop           closes the program\n"

        #refreshing total page
        elif 'refresh' in query:
            self.chat = ''

        #end   
        elif 'stop' in query :
            QtWidgets.QApplication.quit()
        
        else:
            try:
                self.chat+= f'\n {eval(self.search_field.text())}'
            except:
                self.chat+='no match'

        self.scroll_label.setText(self.chat)

    def App_display(self):
        self.Ai_frame.hide()
        self.settings_frame.hide()
        self.Apps_frame.show()
        self.Refresh_grid_apps()

    def Ai_display(self):
        self.Apps_frame.hide()
        self.settings_frame.hide()
        self.Ai_frame.show()
        self.search_field.setFocus()

    def settings_display(self):
        self.Ai_frame.hide()
        self.Apps_frame.hide()
        self.settings_frame.show()

    def get_file_icon(self,path):
        fin = QtCore.QFileInfo(path)
        qq = QtWidgets.QFileIconProvider()
        ic = qq.icon(fin)
        return ic

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Enter_label.setText(_translate("MainWindow", "Enter Your Key"))
        self.key_enter.setText(_translate("MainWindow", "Enter"))

    def Refresh_grid_apps(self):
        app_text_path = open(resource_path('C:\\TRR\\TRR\\AI\\Resources\\text\\app_path.txt'),'r')
        app_paths_list = app_text_path.readlines()
        app_paths_list = [i.replace('\n','') for i in app_paths_list]
        if len(app_paths_list)>21:
            no_of_apps = 21
        else:
            no_of_apps = len(app_paths_list)    

        while self.app_grid_layout.count():
            child = self.app_grid_layout.takeAt(0)
            if child.widget():
              child.widget().deleteLater()

        for app_no in range(no_of_apps):
            self.app_grid_layout.addWidget(QtWidgets.QPushButton(),int(app_no/7),app_no%7)
            self.app_grid_layout.itemAt(app_no).widget().setStyleSheet("border: 0;")
            self.app_grid_layout.itemAt(app_no).widget().setFixedHeight(50)
            self.app_grid_layout.itemAt(app_no).widget().setFixedWidth(50)
            self.app_grid_layout.itemAt(app_no).widget().setIcon(self.get_file_icon(resource_path(app_paths_list[app_no])))
            self.app_grid_layout.itemAt(app_no).widget().setIconSize(QtCore.QSize(35,35))


        for app_no in range(no_of_apps):
            self.app_grid_layout.itemAt(app_no).widget().clicked.connect(lambda _, i=app_no: os.startfile(app_paths_list[i]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())