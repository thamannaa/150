from tkinter import *
import random
root=Tk()
root.title("countries and capitals")
root.geometry("500x500")
enter_country=Entry(root)
enter_country.place(relx=0.5,rely=0.2,anchor=CENTER)
enter_capital=Entry(root)
enter_capital.place(relx=0.5,rely=0.3,anchor=CENTER)
display_country=Label(root)

display_capital=Label(root)
display_capital.place(relx=0.5,rely=0.6,anchor=CENTER)
random_country=Label(root)
random_country.place(relx=0.5,rely=0.8,anchor=CENTER)
random_capital=Label(root)
random_capital.place(relx=0.5,rely=0.9,anchor=CENTER)

country_list=[]
capital_list=[]
def country_citylist():
    country=enter_country.get()
    country_list.append(country)
    display_country["text"]="country name:"+str(country_list)
    
    capital=enter_capital.get()
    capital_list.append(capital)
    display_capital["text"]="capital name:"+str(capital_list)
    
def random_capital_city():
    length1=len(country_list)
    random_no1=random.randint(0,length1-1)
    random_coun=country_list[random_no1]
    random_country["text"]="random country"+str(random_coun)
    
    length2=len(capital_list)
    random_no2=random.randint(0,length2-1)
    random_cap=capital_list[random_no2]
    random_capital["text"]="random capital"+str(random_cap)

display_country.place(relx=0.5,rely=0.5,anchor=CENTER)
btn=Button(root,text="display country and city name",command=country_citylist,bg="Royal Blue",fg="white")
btn2=Button(root,text="random country and city",command=random_capital_city,bg="red",fg="black")
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
btn2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()
