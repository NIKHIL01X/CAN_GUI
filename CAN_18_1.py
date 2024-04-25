import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Displays Screen To Enter The N0. Of Messages
canFileName = input("Enter a new CAN file name : ")
try:
    with open(f"{canFileName}.txt", 'a') as file:
        print()
    print(f"File Created Successfully :  {canFileName}.txt ")
    print(" ")
    current_directory = os.getcwd()
    print(f"Path of the CAN file created : {os.path.join(current_directory, canFileName)}.txt")
    print(" ")
except:
    print("There was a problem creating CAN txt file")
    quit()

noOfMsgss = int(input("Enter the number of total messages : "))
noOfMsgs = noOfMsgss+1
print(" ")
print(f"Total no. of messages in file ({canFileName}.txt) = {noOfMsgss}")
print(" ")



with open(f"{canFileName}.txt", "a") as f:
    openingBrackets = '{'
    f.write("\n")
    f.write(f"{openingBrackets}\n")

global signalCount
signalCount = 0
for msg in range(1, noOfMsgs):

    # Displays Screen To Enter CAN Details
    class Screen2(tk.Tk):

        def __init__(self, columns=9, column_names=[]):
            super().__init__()
            self.columns = columns
            self.column_names = column_names
            self.geometry("900x430")
            self.title("CAN")
            self.configure(bg="#101010")


            frame = tk.Frame(self)
            frame.configure(bg="#101010")
            frame.pack()

            fgColor = "WHITE"
            bgColor = "#101010"


            # m = int(msgs.get())
            # global ii
            # for ii in range(0, noOfMsgs):
            label = tk.Label(self, text=f"Msg : {msg }")
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.pack(pady=35)
            # print(i)

            # for i in m:
            #     # label = tk.Label(self, text=f"Msg : {int(i)}")
            #     # label.pack()
            #     print(i)

            # row_headers = ["CANID", "idType", "DLC", "TriggerType", "Period", "dir", "NoOfSignals", "msgtype",
            #                "useNwIDExt"]
            row_headers = ["CANID", "DLC", "PERIOD", "NoOfSignals", "idType", "TriggerType", "dir", "msgtype",
                          "useNwIDExt"]
            # for i in range(columns):
            #     label = tk.Label(frame, text=row_headers[i])
            #     label.grid(row=0, column=i)

            # row_headers = []

            #CANID
            d = 0
            fgColor= "WHITE"
            bgColor = "#101010"
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)

            global canId
            canId = tk.Entry(frame)
            canId.grid(row=d, column=2)


            #idType
            d = 4
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global idType
            global idType2
            idType = tk.Button(frame, text="  sid  ", command=self.id)
            idType2 = tk.Button(frame, text=" xid ", command=self.id2)
            # idType = tk.Entry(frame)
            idType.grid(row=d, column = 2)
            idType2.grid(row=d, column = 3)

            #DLC
            d = 1
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global dlc
            dlc = tk.Entry(frame)
            dlc.grid(row=d, column=2)

            #TriggerType
            d = 5
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global triggerType
            global triggerType2
            # triggerType = tk.Entry(frame)
            triggerType = tk.Button(frame, text="Type1", command=self.trigger1)
            triggerType2 = tk.Button(frame, text="Type2", command=self.trigger2)
            triggerType.grid(row=d, column=2)
            triggerType2.grid(row=d,column=3)

            #Period
            d = 2
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global period
            period = tk.Entry(frame)
            period.grid(row=d, column=2)

            #dir
            d = 6
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global dir
            global dir2
            # dir = tk.Entry(frame)
            dir = tk.Button(frame, text="Tx", command=self.tx)
            dir2 = tk.Button(frame, text="Rx", command=self.rx)
            dir.grid(row=d, column=2)
            dir2.grid(row=d, column=3)

            #NoOfSignals
            d = 3
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global noofSignals
            noofSignals = tk.Entry(frame)
            noofSignals.grid(row=d, column=2)

            #msgType
            d = 7
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global msgType
            global msgType2
            # msgType = tk.Entry(frame)
            msgType = tk.Button(frame, text="bitfield", command=self.msgtype1)
            msgType2 = tk.Button(frame, text="bytefield", command=self.msgtype2)
            msgType.grid(row=d, column=2)
            msgType2.grid(row=d, column=3)

            # useNwIDExt
            d = 8
            label = tk.Label(frame, text=row_headers[d], font=('Arial', 14))
            label.config(fg=fgColor)
            label.configure(bg=bgColor)
            label.grid(row=d, column=1, rowspan=1)
            global usenwIdext
            global usenwIdext2
            # usenwIdext = tk.Entry(frame)
            usenwIdext = tk.Button(frame, text="enable", command=self.enable)
            usenwIdext2 = tk.Button(frame, text="disable", command=self.disable)
            usenwIdext.grid(row=d, column=2)
            usenwIdext2.grid(row=d, column=3)

            self.button = tk.Button(self, text="Next",command= self.add_to_txt)
            self.button.pack(pady=30)
        #   self.button.pack(pady=50)
        #idTypes
        def id(self):
            global idT
            if idType:
                idType2.config(bg="SystemButtonFace")
                idT = "sid"
                idType.config(bg="red")
        def id2(self):
            global idT
            if idType2:
                idType.config(bg="SystemButtonFace")
                idT = "xid"
                idType2.config(bg="red")
        #Tx, Rx - DIR
        def tx(self):
            global txrx
            if dir:
                dir2.config(bg="SystemButtonFace")
                txrx = "Tx"
                dir.config(bg="red")
        def rx(self):
            global txrx
            if dir2:
                dir.config(bg="SystemButtonFace")
                txrx = "Rx"
                dir2.config(bg="red")

        #TriggerTypes
        def trigger1(self):
            global trigger
            if triggerType:
                triggerType2.config(bg="SystemButtonFace")
                trigger = "Type1"
                triggerType.config(bg="red")
        def trigger2(self):
            global trigger
            if triggerType2:
                triggerType.config(bg="SystemButtonFace")
                trigger = "Type2"
                triggerType2.config(bg="red")
        #Message Type - bittype  bytetype
        def msgtype1(self):
            global msgtype
            if msgType:
                msgType2.config(bg="SystemButtonFace")
                msgtype = "bitfield"
                msgType.config(bg="red")
        def msgtype2(self):
            global msgtype
            if msgType2:
                msgType.config(bg="SystemButtonFace")
                msgtype = "bytefield"
                msgType2.config(bg="red")
        #UseNwidext - enable  disable
        def enable(self):
            global useN
            if usenwIdext:
                usenwIdext2.config(bg="SystemButtonFace")
                useN = "enable"
                usenwIdext.config(bg="red")
        def disable(self):
            global useN
            if usenwIdext2:
                usenwIdext.config(bg="SystemButtonFace")
                useN = "diable"
                usenwIdext2.config(bg="red")
        #DataType - int, unit,float, bool
        # def int(self):
        #     global datatype
        #     if usenwIdext:
        #         useN = "enable"
        # def unit(self):
        #     global useN
        #     if usenwIdext2:
        #         useN = "diable"
        #
        # def float(self):
        #     global useN
        #     if usenwIdext:
        #         useN = "enable"
        #
        # def bool(self):
        #     global useN
        #     if usenwIdext2:
        #         useN = "diable"

        def add_to_txt(self):
            # msgss = msgs.get()
            # msgss = msg
            try:
                signal = int(noofSignals.get())
                if signal <= 64:
                    global canid
                    canid = canId.get()
                    # idtype = idType.get()
                    # Sid = sid.get()
                    Dlc = dlc.get()
                    # triggertype = triggerType.get()
                    Period = period.get()
                    # Dir = dir.get()
                    noofsignals = noofSignals.get()
                    # msgtype = msgType.get()
                    # useNwidext = usenwIdext.get()

                    bracket = '{'
                    bracketclose = '},'

                    # if canId and noofSignals:
                    if canid and noofsignals:
                        format = (
                            # "msginfo{msgss}"
                            f'      "msgInfo{msg}" :{bracket} "canId":{canid}, "idType":"{idT}", "dlc":{Dlc}, "triggerType":"{trigger}", "period":{Period}, "dir":"{txrx}", "noOfSignals":{noofsignals}, "msgType":"{msgtype}", "useNwIdExt":"{useN}"{bracketclose}')
                        print(format)
                        try:
                            openbracket = '{'
                            with open(f"{canFileName}.txt", "a") as f:
                                # a = f.write(f"{openbracket}\n")
                                # if a:
                                #     f.write(" ")
                                #     f.write(f"{format}\n")
                                # else:
                                #    # f.write(f"{openbracket}")
                                #    f.write(" ")
                                #    f.write(f"{format}\n")
                                f.write("\n")
                                f.write(f"{format}\n")

                            # self.done_popup()
                            screen = Screen3()
                            Screen2.destroy(self)
                            # Display the second window.
                            screen.mainloop()
                            # self.done_popup()
                        except:
                            self.error_popup()
                            self.destroy()
                            # print("Error!")
                    else :
                        self.fill_all_field()
                else:
                    self.greater_than()
            except:
                self.fill_all_field()
        # Function To Switch To Signal Entry Screen
        # def go_to_screen_3(self):
        #     screen = Screen3()
        #     Screen2.destroy(self)
        #     # Display the second window.
        #     screen.mainloop()


        #     # Create a new instance of the second window.
            # self.destroy()

        def done_popup(self):
            # Create a Toplevel widget.
            popup = tk.Toplevel(self)

            # Create a label to display the popup message.

            label = tk.Label(popup, text="Saved to txt file")
            label.pack()

            # Display the popup window.
            popup.mainloop()
        def greater_than(self):
            # Create a Toplevel widget.
            popup = tk.Toplevel(self)
            popup.geometry("500x100")
            # Create a label to display the popup message.
            label = tk.Label(popup, text="Invalid Entry : Max number of signals = 64", font=("Arial", 14))
            label.pack()
            # Display the popup window.
            popup.mainloop()
        def error_popup(self):
            # Create a Toplevel widget.
            popup = tk.Toplevel(self)

            # Create a label to display the popup message.

            label = tk.Label(popup, text="There was an error saving the data to text file")
            label.pack()

            # Display the popup window.
            popup.mainloop()

        def fill_all_field(self):  # This code is to show popup when the name of the signal is same.
            # Create a Toplevel widget.
            popup = tk.Toplevel(self)
            popup.geometry("500x100")

            # Create a label to display the popup message.

            label = tk.Label(popup, text="Fill all the given fields.", font="Arial, 20")
            # label = tk.Label(popup, text="CANID and No. Of Signals ", font="Arial, 20")
            label.pack()

            # Display the popup window.
            popup.mainloop()

    # Displays Screen To Enter Signal Values
    class Screen3(tk.Tk):
        def __init__(self, columns=9, column_names=[]):
            super().__init__()
            self.columns = columns
            self.column_names = column_names
            self.title("Create rows")
            self.geometry("1200x500")
            self.title("Signals")
            # self.configure(bg="#2A2A2E")

            frame = Frame(self)
            frame.pack(fill=BOTH, expand=1)

            #Verticle Scroll Bar CODE - Start
            my_canvas = Canvas(frame)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=2) #original expand value = 1

            my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            second_frame = Frame(my_canvas)

            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
            # Verticle Scroll Bar CODE - END




            global signals
            signals = int(noofSignals.get())
            global num_entries
            num_entries = signals


            global col_names
            col_names = ["XID", "xidIndex", "StartBit", "Length", "Endianness", "sf", "offSet", "dataType"]


            # signals = int(input("Enter Number Of Signals : "))
            # num_entries = signals
            global num_columns
            num_columns = len(col_names)

            # Labels for column names and entry widgets
            for d, col_name in enumerate(col_names):
                label = tk.Label(second_frame, text=col_name, font=('Arial', 14))
                label.grid(row=0, column=d * 2, columnspan=2)

            # A list to store entry widgets
            global entry_widgets
            entry_widgets = [[None] * num_columns for _ in range(num_entries)]

            # Entry Widgets
            for i in range(num_entries):
                # print(i)
                tk.Label(second_frame, text=f"Signal: {i + 1}").grid(row=i + 1)
                # tk.Label(frame, text=f"Signal: {totalSignal}").grid(row=i + 1)
                for j in range(num_columns):
                    # tk.Label(root, text=f"Signal: {i + 1}, Column {j + 1}:").grid(row=i, column=2 * j)
                    entry = tk.Entry(second_frame)
                    entry.grid(row=i + 1, column=2 * j + 1)
                    entry_widgets[i][j] = entry


            print_button = tk.Button(second_frame, text="Done", command=self.process_data)
            print_button.grid(row=num_entries + 5, columnspan=num_columns * 2 +1)
        def process_data(self):
            global i
            data = [[] for _ in range(num_entries)]
            bracketClose = '},'
            bracketEnd = '}'
            for i in range(num_entries):
                for j in range(num_columns):
                    entry_value = entry_widgets[i][j].get()
                    null = "null"
                    if j == 0:
                        # data[i].append(f"{entry_value}")
                        # data[i].append(f'"{entry_value}"')
                        data[i].append(f'"xid" :{int(entry_value) if entry_value.isdigit() else null}')
                    elif j == 1:
                        data[i].append(f'"xidIndex" :{int(entry_value) if entry_value.isdigit() else null}')
                    elif j == 2:
                        data[i].append(f'"startBit" :{int(entry_value) if entry_value.isdigit() else null}')
                    elif j == 3:
                        data[i].append(f'"length" :{int(entry_value) if entry_value.isdigit() else null}')
                    elif j == 4:
                        if "m" in entry_value or "M" in entry_value:
                            # data[i].append(f'"endianness" :"{entry_value}"')
                            data[i].append('"endianness" :"Motorola"')
                        elif "i" in entry_value or "I" in entry_value:
                            data[i].append('"endianness" :"Intel"')
                    elif j == 5:
                        data[i].append(f'"sf" :{int(entry_value) if entry_value.isdigit() else null}')
                    elif j == 6:
                        data[i].append(f'"offset" :{int(entry_value) if entry_value.isdigit() else null}')
                    elif j == 7:
                        if i + 1 == signals:
                            if msg+1 == noOfMsgs:
                                data[i].append(f'"dataType" :"{entry_value}"{bracketEnd}')
                            else:
                                data[i].append(f'"dataType" :"{entry_value}"{bracketClose}')
                        else:
                            data[i].append(f'"dataType" :"{entry_value}"{bracketClose}')

            for i, row in enumerate(data):
                bracket = '{'
                # print(f"Row {i + 1}: {row}")
                # print(str(row)[1:-1])
                # print(f"Row {i + 1}: [{', '.join(row)}]")
                # signalinfo = f'"signalInfo{i+1}"'
                global signalCount
                signalinfo = f'"signalInfo{signalCount + 1}"'
                signalCount += 1
                # print(f"{signalinfo} {i + 1}: {', '.join(map(str,  row))}")
                # signalFormat = f"{signalinfo} : canId:{can} {', '.join(map(str, row))}"
                signalFormat = f"{signalinfo} : {bracket} canId :{canid}, {', '.join(map(str, row))}"
                print(signalFormat)
                try:
                    openbracket = '{'
                    with open(f"{canFileName}.txt", "a") as f:
                        # a = f.write(f"{openbracket}\n")
                        # if a:
                        f.write(f"      {signalFormat}\n")
                        # else:
                        #     f.write(f"{openbracket}")
                        #     f.write(f"{format}\n")
                except:
                    print("There was an error saving the entered data to the .txt file")
            # self.mainloop()
            self.destroy()


    if __name__ == '__main__':
        app = Screen2()
        app.mainloop()
with open(f"{canFileName}.txt", "a") as f:
    # a = f.write(f"{openbracket}\n")
    # if a:
    #     f.write(" ")
    #     f.write(f"{format}\n")
    # else:
    #    # f.write(f"{openbracket}")
    #    f.write(" ")
    #    f.write(f"{format}\n")
    closingBrackets = '}'
    f.write("\n")
    f.write(f"{closingBrackets}\n")