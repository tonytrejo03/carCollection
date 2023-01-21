# Tony Trejo
# HW 11
# Collection for dream cars

import PySimpleGUI as sg

# classes and functions
class Cars:
    def __init__(self,make="",model="",year="",color=""):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return make,model,year,color
    
    # attempt to make the "manufactor" sort from alphabetically order


        
# main
layout = [[sg.Text("Dream Car Collection Tool")],
          [sg.Text("Manufacturer: "),sg.Input(key="make",size=(10,20))],
          [sg.Text("Model: "),sg.Input(key="model",size=(10,20))],
          [sg.Text("Year: "),sg.Input(key="year",size=(5,10)),sg.Text("Color: "),sg.Input(key="color",size=(5,10))],
          [sg.Button("OK"),sg.Button("Close"),sg.Button("Save to File")],
          [sg.Multiline(size=(30,30),key="summary")]]

win = sg.Window("Car Collection Tool",layout=layout)

text = ""
while True:
    event,data = win.read()
    if event == "OK":
        text = text + data["make"] + "\n"
        win["summary"].update(text)
        win["make"].update("")
        text = text + data["model"] + "\n"
        win["summary"].update(text)
        win["model"].update("")
        text = text + data["year"] + "\n"
        win["summary"].update(text)
        win["year"].update("")
        text = text + data["color"] + "\n"
        win["summary"].update(text)
        win["color"].update("")
        text = text + "\n"
    elif event == "Save to File":
        try:
            fname = sg.popup_get_text("Enter name of file:")
            fvar = open(fname,"w")
            fvar.write(text)
            fvar.close()
            sg.popup("The file was saved.")
        except:
            sg.popup("The file could not be saved.")
    elif event == "Close":
        win.close()
        break
        
