from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import re
class ATM:
    def __init__(self,root):
        self.root = root
        self.root.title("ATM")
        self.root.geometry("300x200")
        self.attempt = 0
        self.Balance = 1000
        self.Main_Menu()

    def Main_Menu(self):
        self.Label_Login = Label(self.root,text="Welcome",font=("Arial",16,"bold italic"))
        self.Label_Login.pack()

        self.Menu_Seperator = ttk.Separator(self.root,orient=HORIZONTAL)
        self.Menu_Seperator.pack(padx=10,pady=10,fill="x")

        self.Withdraw_Button = Button(self.root,text="Withdraw",command=self.Withdraw)
        self.Withdraw_Button.pack()

        self.Balance_Button = Button(self.root,text="Show Balance",command=self.Show_Balance)
        self.Balance_Button.pack()

        self.Deposit_Button = Button(self.root,text="Deposit",command=self.Deposit)
        self.Deposit_Button.pack()

        self.Quit_Button = Button(self.root,text="Exit",command=lambda:self.root.quit())
        self.Quit_Button.pack()


    def Withdraw(self):
        self.Clean_Root()
        
        Order = Label(self.root,text="Enter the Amount")
        Order.pack()
        
        Input_Text = Text(self.root,height=1,width=11)
        Input_Text.pack()

        Enter_Button = Button(self.root,text="enter",width=5,height=2,command=lambda:self.Enter(Input_Text.get("1.0",END)))
        Enter_Button.pack()

        Back_Button = Button(self.root,text="back",width=5,height=2,command=self.Back)
        Back_Button.pack()

    def Enter(self,Amount):        
        try:
            Amount = float(Amount)
            if Amount <= 0:
                messagebox.showerror("error","you cannot enter zero and negatives")
                self.attempt += 1
                self.Withdraw()

            elif Amount > self.Balance:
                messagebox.showerror("error","you cannot enter this amount")
                self.attempt += 1
                self.Withdraw()

            else :
                self.Balance -= Amount
                messagebox.showinfo("successful","{} deducted from your account".format(Amount))
                self.Back()
        except ValueError:
            messagebox.showerror("ValueError","Cannot enter string")
            self.attempt += 1
            if self.attempt >= 3 :
                messagebox.showerror("Logging out","Session is closing..")
                self.root.quit()
            self.Withdraw()
            
    def Enter_Deposit(self,Amount):
        try:
            Amount = float(Amount)
            if Amount <= 0:
                messagebox.showerror("Error","Cannot enter negative or zero for deposit")
                self.attempt += 1
                self.Deposit()
            else :
                self.Balance += Amount
                messagebox.showinfo("Succeed",f"{Amount}deposited into your account")
                self.Back()
        except ValueError:
            messagebox.showerror("Error","Enter a digit ")
            self.Deposit()
            self.attempt += 1
            if self.attempt >= 3:
                messagebox.showerror("Logging out","Session is closing..")
                self.root.quit()

    def Back(self):                     
        self.Clean_Root()
        self.Main_Menu()
    def Deposit(self):
        self.Clean_Root()

        Order = Label(self.root,text="Enter the Amount")
        Order.pack()

        Deposit_Amount = Text(self.root,height=1,width=11)
        Deposit_Amount.pack()

        Enter_Deposit = Button(self.root,text="Enter",command=lambda:self.Enter_Deposit(Deposit_Amount.get("1.0",END)))
        Enter_Deposit.pack()

        Back_Button = Button(self.root,text="back",command=self.Back,width=5,height=2)
        Back_Button.pack(pady=10)

    def Show_Balance(self):              
        self.Clean_Root()
        label1 = Label(self.root,text="Account Details",font=("Arial",14,"italic"))
        label1.pack()
        
        seperate = ttk.Separator(self.root,orient=HORIZONTAL)
        seperate.pack(padx=10,pady=10,fill="x")

        label2 = Label(self.root,text="balance : {}".format(self.Balance),font=("Arial",16,"bold italic"))
        label2.pack()

        Back_Button = Button(self.root,text="back",width=5,height=2,command=self.Back)
        Back_Button.pack(pady=20)

    def Clean_Root(self):                
        for i in self.root.winfo_children():
            i.destroy()

if __name__ == "__main__":
    root = Tk()
    ATM(root)
    root.mainloop()

