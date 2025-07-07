## python student mark analyser program using modules 
import pandas as pd
import numpy as np
import string
from word2number import  w2n
from collections import defaultdict
import re#regex module
import shutil
data_dict=defaultdict(list)# creates a dictionary whose values are list
keys_lst=["Name","Physics","Chemistry","Maths"]
subjects=keys_lst[1:]
try:
    sample=input("Enter the no of students:")#storing the value whatever
    no_of_std=int(sample)# converting into integer
except Exception:
    while True:
        try:
            try:
                no_of_std=w2n.word_to_num(sample)
            except Exception:
                print("Give the input crtly:")   
                error=1/0
            else:
                break
        except Exception :
            try:
                sample=input("Enter the no of students:")
                no_of_std=int(sample)
            except Exception:
                try:
                    no_of_std=w2n.word_to_num(sample)
                except Exception:
                    continue
                else:
                    break
            else:
                break         
        else:
            break           
for i in range(no_of_std):
    for key in keys_lst:
        try:
            if key in subjects:
                data=float(input(f"Enter {key}:"))# if they give string then it will raise value error
            else:
                data=input(f"Enter {key}:")#this wont cause any error
        except ValueError:
            while True:
                try:
                    data=float(input(f"Enter a valid {key} mark:"))
                except ValueError:
                    continue
                else:
                    break
        data_dict[key].append(data)   # it assigns the input to the dictionary value 
    print()   #creates a gap btw students info in the output
data=data_dict.copy()   #copies the dictionary
ind_lst=list(string.ascii_lowercase)   #string a-z for custom indexing
df=pd.DataFrame(data,index=ind_lst[0:no_of_std])   #data frame
names_lst=list(df["Name"])   #list of names
for name in range(len(names_lst)):
    old_name=names_lst[name]
    mod_str=re.sub(r"\s+", "", old_name)   #this removes all the empty spaces
    while True: 
        if not bool(re.fullmatch(r"[A-Za-z]+",mod_str)):
            new_name=input(f"{names_lst[name]} is not a valid name enter crtly:")
            new_name=re.sub(r"\s","",new_name)
            mod_str=new_name
        else:
            df["Name"]=df["Name"].replace(old_name,mod_str)   #works finely and swaps the value even if it already crt
            break          
#print(df)   #perfectly replaced the names
df.drop_duplicates(subset="Name",keep="first",inplace=True)
#print(df)   #duplicates removed data frame

# to check whether the student has crt mark out off 100
valid=(df[subjects]>=0) &( df[subjects]<=100)
for index,row in valid.iterrows():
    if not row.all():
        name=df.loc[index,"Name"]  #name of student those who have invalid marks
        for subject in subjects:
            if not row[subject]:
                print()
                print(f"{name} has Invalid mark in {subject}")
                while True:
                    mark=float(input(f"Re-enter {subject} mark crtly:"))
                    if 0<=mark<101:
                        df.at[index,subject]=mark
                        break
                    else:
                        print("wrong input!")   
#print(df)#works finely
#adding a new column called cutoff 
df["Cutoff"]=df.apply(lambda mark:((mark["Physics"]+mark["Chemistry"])/2)+mark["Maths"],axis=1)  #column wise accessing values and doing operation
#print(df) dataframe after adding cutoff column
df["Mean"]=df.apply(lambda mark:round((mark["Physics"]+mark["Chemistry"]+mark["Maths"])/len(subjects),2),axis=1)
#print(df) dataframe after adding mean column

#creating a numpy array
def Get_Round(row):
    status_lst=list(df["Result"])
    x=row["Cutoff"]
    for status in status_lst:
        if status:
            if x>=179:
                return "Round1"
            elif 125<=x<179:
                return "Round2"
        else:
            return "Not eligible"
def Status(row):
    for subject in subjects:
        if row[subject]<35:
            return False
    return True #else part no needed
        
df["Result"]=df.apply(Status,axis=1)
df["Round"]=df.apply(Get_Round,axis=1)
#replacing true as pass and false as fail using apply()
df["Result"]=df["Result"].apply(lambda x:"pass" if x else "Fail")
print(df)



