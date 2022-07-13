from tkinter import *
from selenium import webdriver

 

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('800x600')


def credentials():
    global txt1, txt2
    lbl1 = Label(window, text="Username:")
    lbl1.grid(column=1, row=0)
    lbl2 = Label(window, text="Password:")
    lbl2.grid(column=1, row=2)
    txt1 = Entry(window, width=60)
    txt1.focus()
    txt1.grid(column=1, row=1)
    txt2 = Entry(window, width=60)
    txt2.grid(column=1, row=3)
    credsbutton.grid_forget()
    connectbutton.grid_forget()

    def save():
        global txt1, txt2
        u = txt1.get()
        p = txt2.get()
        file1 = open('creds.txt', 'w')
        file1.write(u)
        file1.write("\n")
        file1.write(p)
        savebutton.grid_forget()
        connectbutton.grid_forget()

    def connect():
        save()
        browser = webdriver.Firefox()
        browser.get("http://www.facebook.com")

        file = open("creds.txt", "r")
        lines = file.readlines()

        username = browser.find_element("id", "email")
        username.send_keys(lines[0])
        password = browser.find_element("id", "pass")
        password.send_keys(lines[1])
        submit = browser.find_element("name", "login")

        submit.click()

        connectbutton.grid_forget()

    savebutton = Button(window, text="Save & Connect",
                        command=save and connect)
    savebutton.grid(column=4, row=4)


credsbutton = Button(window, text="Enter Credentials", command=credentials)
credsbutton.grid(column=1, row=1)


def directconnect():
    browser = webdriver.Firefox()
    browser.get("http://www.facebook.com")

    file = open("creds.txt", "r")
    lines = file.readlines()

    username = browser.find_element("id", "email")
    username.send_keys(lines[0])
    password = browser.find_element("id", "pass")
    password.send_keys(lines[1])
    submit = browser.find_element("name", "login")
    submit.click()


connectbutton = Button(window, text="Connect", command=directconnect)
connectbutton.grid(column=1, row=2)


window.mainloop()
