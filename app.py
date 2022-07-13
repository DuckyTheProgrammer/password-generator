from tkinter import *
import os
import random
from tkinter import messagebox

# vars
azUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
azLower = "abcdefghijklmnopqrstuvwxyz"

smbls = "!@#$%^&*()"
nums = "0123456789"

string = azUpper + azLower + smbls + nums
lenght = 16

pwdList = []


#genrating password function
def createPwd():

    generatePwdBtn.config(state="disabled", bg="grey", fg="white")

    password = "".join(random.sample(string, lenght))
    print("Your new password is: " + password)

    pwdList.append(password)

    pwdLabel = Label(frame, text=password, bg="white")
    pwdLabel.configure(font=("Helvetica",16,"bold"))
    pwdLabel.place(relx=0.065, rely=0.25)

    savePwdBtn.config(bg="#263D42", fg="white", state="normal")

#saving password function
def savePwd():
    generatePwdBtn.config(state="normal", bg="#263D42", fg="white")
    print(pwdList)

    with open('passwords.txt', 'w') as f:
        for pwd in pwdList:
            f.write(pwd + '\n')

    for item in frame.winfo_children():
        item.destroy()

    messagebox.showinfo(title="SUCCESS",message="Successfully saved your password in TXT File (passwords.txt)")

    savePwdBtn.config(bg="grey", fg="white", state="disabled")

#delete txt file function
def deletePwdFile():
    if os.path.isfile('passwords.txt'):
        os.remove('passwords.txt')
        pwdList.clear()
        messagebox.showinfo(title="SUCCESS",message="Successfully deleted TXT File (passwords.txt))")
    for item in frame.winfo_children():
            item.destroy()
    
    savePwdBtn.config(bg="grey", fg="white", state="disabled")
    
# ui

root = Tk() 
root.title("Password Generator")

canvas = Canvas(root, width=300, height=300, bg="#263D42")
canvas.pack()

titleLabel = Label(root, text="GENERATE PASSWORD AND SAVE", bg="#263D42", fg="white")
titleLabel.configure(font=("", 11, ""))
titleLabel.place(relx=0.085, rely=0.03)

frame = Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.65, relx=0.1, rely=0.1)

generatePwdBtn = Button(root, text="Generate Password",  bg="#263D42", fg="white", command=createPwd)
generatePwdBtn.pack()

savePwdBtn = Button(root, text="Save Password",  bg="grey", fg="white", command=savePwd, state="disabled")
savePwdBtn.pack()

deletePwdBtn = Button(root, text="Delete TXT File",  bg="#263D42", fg="white", command=deletePwdFile)
deletePwdBtn.pack()


root.mainloop()