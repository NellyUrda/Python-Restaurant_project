import tkinter.messagebox
from tkinter import *


def exit():
    window.destroy()

# we store all the items and prices from menu in dictionarys
pasta = {'fusilli': 4.20, 'penne rigate': 4.20, 'tagliatele': 4.20, 'spaghetti': 4.20}
salsa = {'aglio e olio': 5.0, 'arrabiata': 5.1, 'pesto': 3.5, 'carbonara': 4.5}
dessert = {'icecream  ': 3.0, 'tiramisu': 4.3}
beverage = {'tea': 2.0, 'coffee': 2.5, 'wine': 3.0}

item1 = item2 = item3 = item4 = 0

# Pay button
# choose the items from menu and calculate the total price to pay
def pay():
    for (key, value) in pasta.items():
        if key == pasta_choice.get():
            global item1  
            item1 = value
    for (key, value) in salsa.items():
        if key == salsa_choice.get():
            global item2
            item2 = value
    for (key, value) in dessert.items():
        if key == dessert_choice.get():
            global item3
            item3 = value
    for (key, value) in beverage.items():
        if key == beverage_choice.get():
            global item4
            item4 = value
    tkinter.messagebox.showinfo(message="Total to pay: " + str(item1 + item2 + item3 + item4))

# GUI for menu page
window = Tk()

window.geometry("730x400")
window.config(bg="gray") 

title_label = Label(window,
                    text="Italian restaurant",
                    font=("Ariel", 18, "bold"),
                    fg="white",
                    bg="black",
                    activebackground="gray")
title_label.place(x=200, y=0, width=300, height=40)

pasta_label = Label(window,
                    text="PASTA type",
                    font=("Ariel", 12, "bold"),
                    fg="black",
                    bg="gray",
                    activebackground="gray")
pasta_label.place(x=50, y=50, width=150, height=30)

salsa_label = Label(window,
                    text="SALSA type",
                    font=("Ariel", 12, "bold"),
                    fg="black",
                    bg="gray",
                    activebackground="gray")
salsa_label.place(x=220, y=50, width=150, height=30)

dessert_label = Label(window,
                      text="DESSERT",
                      font=("Ariel", 12, "bold"),
                      fg="black",
                      bg="gray",
                      activebackground="gray")
dessert_label.place(x=380, y=50, width=150, height=30)

beverage_label = Label(window,
                       text="BEVERAGE",
                       font=("Ariel", 12, "bold"),
                       fg="black",
                       bg="gray",
                       activebackground="gray")
beverage_label.place(x=530, y=50, width=150, height=30)

pasta_choice = StringVar(value=" ") 
fusilli_rb = Radiobutton(window,
                         text="fusilli",
                         variable=pasta_choice,
                         value="fusilli",
                         font=("Ariel", 12),
                         bg="#dbde97")
fusilli_rb.place(x=50, y=90, width=150, height=30)

penne_rigate_rb = Radiobutton(window,
                              text="penne rigate",
                              variable=pasta_choice,
                              value="penne rigate",
                              font=("Ariel", 12),
                              bg="#dbde97")
penne_rigate_rb.place(x=50, y=140, width=150, height=30)

tagliatele_rb = Radiobutton(window,
                            text="tagliatele",
                            variable=pasta_choice,
                            value="tagliatele",
                            font=("Ariel", 12),
                            bg="#dbde97")
tagliatele_rb.place(x=50, y=190, width=150, height=30)

spaghete_rb = Radiobutton(window,
                          text="spaghetti",
                          variable=pasta_choice,
                          value="spaghetti",
                          font=("Ariel", 12),
                          bg="#dbde97")
spaghete_rb.place(x=50, y=240, width=150, height=30)

salsa_choice = StringVar(value=" ")
aglio_olio_rb = Radiobutton(window,
                            text="aglio e olio",
                            variable=salsa_choice,
                            value="aglio e olio",
                            font=("Ariel", 12),
                            bg="#e3d9ac")
aglio_olio_rb.place(x=220, y=90, width=150, height=30)

arrabiata_rb = Radiobutton(window,
                           text="arrabiata",
                           variable=salsa_choice,
                           value="arrabiata",
                           font=("Ariel", 12),
                           bg="#b81119")
arrabiata_rb.place(x=220, y=140, width=150, height=30)

pesto_rb = Radiobutton(window,
                       text="pesto",
                       variable=salsa_choice,
                       value="pesto",
                       font=("Ariel", 12),
                       bg="#4c8c58")
pesto_rb.place(x=220, y=190, width=150, height=30)

carbonara_rb = Radiobutton(window,
                           text="carbonara",
                           variable=salsa_choice,
                           value="carbonara",
                           font=("Ariel", 12),
                           bg="#9c4706")
carbonara_rb.place(x=220, y=240, width=150, height=30)

dessert_choice = StringVar(value=" ")
icecream_rb = Radiobutton(window,
                          text="icecream",
                          variable=dessert_choice,
                          value="icecream",
                          font=("Ariel", 12),
                          bg="#dbde97")
icecream_rb.place(x=390, y=90, width=150, height=30)

tiramisu_rb = Radiobutton(window,
                          text="tiramisu",
                          variable=dessert_choice,
                          value="tiramisu",
                          font=("Ariel", 12),
                          bg="#dbde97", fg="black")
tiramisu_rb.place(x=390, y=140, width=150, height=30)

beverage_choice = StringVar(value=" ")
tea_rb = Radiobutton(window,
                     text="tea",
                     variable=beverage_choice,
                     value="tea",
                     font=("Ariel", 12),
                     bg="#dbde97")
tea_rb.place(x=560, y=90, width=150, height=30)

coffee_rb = Radiobutton(window,
                        text="coffee",
                        variable=beverage_choice,
                        value="coffee",
                        font=("Ariel", 12),
                        bg="#dbde97",
                        fg="black")
coffee_rb.place(x=560, y=140, width=150, height=30)

wine_rb = Radiobutton(window,
                      text="wine",
                      variable=beverage_choice,
                      value="wine",
                      font=("Ariel", 12),
                      bg="#dbde97")
wine_rb.place(x=560, y=190, width=150, height=30)

pay_button = Button(window,
                    text="Pay",
                    font=("Ariel", 12, "bold"),
                    fg="white",
                    bg="black",
                    activebackground="black",
                    activeforeground="white",
                    command=pay)
pay_button.place(x=250, y=320, width=120, height=40)

exit_button = Button(window,
                     text="Exit",
                     font=("Ariel", 12, "bold"),
                     fg="white",
                     bg="black",
                     activebackground="black",
                     activeforeground="white",
                     command=exit)
exit_button.place(x=400, y=320, width=120, height=40)

window.mainloop()
