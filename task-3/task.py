import http.client
import json
from tkinter import *
import sys
import os
from tkinter import Tk,Button
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
root = Tk()
root.title("Сovid")
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/africa", headers=headers)
res = conn.getresponse()
data = res.read()
coron = data.decode("utf-8")
json = json.loads(coron)
text = Text(width=500, height=500, fg='#FFFFFF', bg='#8B008B', font=("Arial Bold", 13))
text.pack()
for i in range(10):
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[14])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[12])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[10])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[2])
Button(root, text="Restart(такая большая, что-бы видно было))", font=("Arial Bold", 23), command=restart_program, fg='#ffffff', bg='#041f3a',width=40, height=10,).place(x = 690, y = 400)
root.mainloop()
