#recreating student project by combining GUI using tkinter
import tkinter as tk
from tkinter import messagebox

user_id="Sakthivel_@4714"
status=False
userprompt="please enter user id:"

window=tk.Tk()
window.title("Student mark analyzer")
window.geometry("200x200")
window.configure(bg="white")
label1=tk.Label(window,
               text="This is student mark analyser record",
               bg="white",
               font=("arial",25),
               fg="dark green")
entry_box=tk.Entry(window,
                 width=45,
                 fg="dark green",
                 font=("arial",10),
                 bg="white",
                 bd=2,
                 relief="sunken",
                 )

def Userid_Check():
    global status
    if entry_box.get()==userprompt+user_id:
        messagebox.showinfo("Success","correct user id")
        label2=tk.Label(window,
                text="Go to python ide and continue with pandas!",
                font=("arial",22),
                fg="dark green",
                bg="white")
        label2.pack(pady=150)
        status=True
    else:
        messagebox.showerror("error","wrong user id. Try again")
        entry_box.delete(0,tk.END)#clears the box
        entry_box.insert(0,userprompt)
        status=False      
button=tk.Button(window,
                 text="Enter",
                 width=10,
                 font=("arial",10),
                 fg="dark green",
                 bg="white",
                 state="normal",
                 activeforeground="dark green",
                 activebackground="white",
                 command=Userid_Check,              
             )
label1.pack()

entry_box.pack(padx=30,pady=65)
entry_box.insert(0,userprompt)
button.pack(padx=0,pady=0)
window.mainloop()

print("welcome to students marks record!")
response=input("""choose(1/2/3):
1.Show a sample
2.create new one like sample
3.create a new data frame on your own
""")
while ~status:
    try:
        is_integer=False
        option=int(response)
        if option>3 or option<1:
            is_integer=True
            raise ValueError("invalid input(choice is not in the range)")
        else:
            print(f"valid input and you choosed : {int(response)}")
            break
    except ValueError as e:
        if not is_integer:
            print(f"ValueError Raised!:{e}")
        else:
            print(e)
        print("choose any one above (integer format)")
        response=input("Re-enter crtly:")
    else:
        status=~status

#pandas section of student mark analyser
import pandas as pd
import numpy as np
from collections import defaultdict

def Sample(data = {
    "Name": ["Sakthi", "Anu", "Ravi", "Meena", "Kumar"],
    "Roll No": [101, 102, 103, 104, 105],
    "Physics": [85, 78, 92, 74, 81],
    "Chemistry": [90, 83, 86, 79, 80],
    "Maths": [95, 88, 91, 80, 84]}): #default argument
    df=DataFrame(data) # data frame with default index value
# Calculating Total Marks
    df["Total"] = df[["Physics", "Chemistry", "Maths"]].sum(axis=1)
#  Calculating Cutoff ((Math/2) + (Phy/4) + (Chem/4))
    df["Cutoff"] = df["Maths"] / 2 + df["Physics"] / 4 + df["Chemistry"] / 4

 # Highest and Lowest marks among the 3 subjects
    df["High Mark"] = df[["Physics", "Chemistry", "Maths"]].max(axis=1)
    df["Low Mark"] = df[["Physics", "Chemistry", "Maths"]].min(axis=1)

# Mean of 3 subjects
    df["Mean"] = df[["Physics", "Chemistry", "Maths"]].mean(axis=1)

#  Assign Ranks based on Total Marks (descending)
    df["Rank"] = df["Total"].rank(ascending=False, method="min").astype(int)
    df = df.sort_values(by="Rank")

# Format rank as Rank1, Rank2, etc.
    df["Rank"] = df["Rank"].apply(lambda x: f"Rank{x}")

# final DataFrame
    return (df.reset_index(drop=True))#it actuall does not have name as argument instead it create all the cloumn name that are dropped already while using apply function
col_lst=["Name","Rollno","Physics","Chemistry","Maths"]
match option:
    case 1:
        print(Sample())
    case 2:
        data_dict=defaultdict(list)
        no_of_std=int(input("Enter the no of students:"))
        for i in range(no_of_std):
            for col in col_lst:
                ans=input(f"Enter {col}{i}:")
                if col==col_lst[0]:
                    while True:
                        if  re.fullmatch(r'^[A-Za-z\s]+$],ans):
                            data_dict[col].append(ans)
                            break
                        else:
                            print("invalid name")
                else:
                    while True:
                        try:
                            integer=int(ans)
                        except ValueError as e:
                            print("Value error raised :",e)
                            try:
                                ans=input(f"Enter a valid {col}: ")
                        else:
                            data_dict[col].append(integer)
                            break
            print("\n","Next student")
        print(Sample(data_dict))
    case _:
        print("oops something went wrong")
