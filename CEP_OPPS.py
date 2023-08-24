Product_List = [['Fruits & Vegetables', 'mango.png', 'Mango Sindhri Box', '675', '3000 gm'], ['Fruits & Vegetables', 'banana.png', 'Banana', '99', '6 unit'], ['Fruits & Vegetables', 'melon.png', 'Melon', '229', '2000 gm'], ['Fruits & Vegetables', 'peach.png', 'Peach', '229', '1000 gm'], ['Fruits & Vegetables', 'tomato.png', 'Tomato', '89', '1000 gm'], ['Fruits & Vegetables', 'onion.png', 'Onion', '95', '1000 gm'], ['Fruits & Vegetables', 'cucumber.png', 'Cucumber', '32', '500 gm'], ['Fruits & Vegetables', 'garlic.png', 'Garlic', '79', '250 gm'], ['Fruits & Vegetables', 'chilli.png', 'Green Chilli', '35', '250 gm'], ['Fruits & Vegetables', 'ginger.png', 'Ginger', '69', '250 gm'], ['Personal Care', 'soap.png', 'Soap', '199', '1 unit'], ['Personal Care', 'shampoo.png', 'Shampoo', '359', '200 bar'], ['Personal Care', 'toothpaste.png', 'Toothpaste', '349', '250 ml'], ['Personal Care', 'handwash.png', 'Hand Wash', '489', '350 gm'], ['Personal Care', 'showergel.png', 'Shower Gel', '479', '300 ml'], ['Personal Care', 'facewash.jpg', 'Face Wash', '489', '150 ml'], ['Personal Care', 'haircomb.png', 'Hair Comb', '749', '1 unit'], ['Personal Care', 'conditioner.png', 'Hair Conditioner', '589', '120 ml'], ['Personal Care', 'bodyspray.png', 'Body Spray', '579', '100 ml'], ['Personal Care', 'haircolor.png', 'Hair Color', '889', '1 unit'], ['Fresh Meat', 'chickenkarahicut.png', 'Chicken Karahi Cut', '489', '900 gm'], ['Fresh Meat', 'chickenkarahicut.png', 'Chicken Mince', '359', '500 gm'], ['Fresh Meat', 'chickenkarahicut.png', 'Chicken Breast', '749', '1 kg'], ['Fresh Meat', 'chickenkarahicut.png', 'Chicken Biryani Cut', '489', '900 gm'], ['Fresh Meat', 'chickenkarahicut.png', 'Whole Chicken', '479', '1 unit'], ['Fresh Meat', 'chickenkarahicut.png', 'Chicken Korma Cut', '489', '900 gm'], ['Fresh Meat', 'chickenkarahicut.png', 'Beef Karahi Cut', '749', '900 gm'], ['Fresh Meat', 'chickenkarahicut.png', 'Beef Mince', '589', '500 gm'], ['Fresh Meat', 'chickenkarahicut.png', 'Beef Korma Cut', '979', '1 kg'], ['Fresh Meat', 'chickenkarahicut.png', 'Beef Biryani Cut', '889', '900 gm'], ['Fish & Seafood', 'rahufish.png', 'Rahu Fish', '649', '1 kg'], ['Fish & Seafood', 'rahufish.png', 'Sole fish', '729', '500 gm'], ['Fish & Seafood', 'rahufish.png', 'Tuna', '489', '1 kg'], ['Fish & Seafood', 'rahufish.png', 'Surmai', '359', '700 gm'], ['Fish & Seafood', 'rahufish.png', 'Black Pomfret', '749', '700 gm'], ['Fish & Seafood', 'rahufish.png', 'Mushka', '489', '500 gm'], ['Fish & Seafood', 'rahufish.png', 'King Fish', '479', '1 kg'], ['Fish & Seafood', 'rahufish.png', 'Dangri', '589', '700 gm'], ['Fish & Seafood', 'rahufish.png', 'White Pomfret', '979', '700 gm'], ['Fish & Seafood', 'rahufish.png', 'Trout', '889', '1 kg']]
# Prolst=[]
# for i in Product_List:
#     x=[]
#     if "C:/Users/Maria/Desktop/card/" in i[1]:
#         x.append(i[0])
#         x.append(i[1][28:])
#         x.append(i[2])
#         x.append(i[3])
#         x.append(i[4])
#         Prolst.append(x)
#
# print(Prolst)
class First_Name_Error(Exception):
    pass
class Last_Name_Error(Exception):
    pass
class Email_Error(Exception):
    pass
class Password_Error(Exception):
    pass
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image

class MainPage:
    TotalPrice=0
    def frontpage(self):
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        Label(self.Canvas_Area, text=f"Hi {obj.user_name}!", bg="white",fg="red", font="times 15").place(x=15, y=28)
        Label(self.Canvas_Area, text="WELCOME TO AIUH SHOPPING STORE", bg="white", fg="black",font="times 22 bold").place(x=235, y=20)
        Label(self.Canvas_Area, text="Search Product", bg="white", font="times 15").place(x=165, y=84)
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1020x850")
        self.root.title("Grocery Store")
        self.root.config(background="white")
        self.root.resizable(False,False)
        self.f1 = Frame(self.root, width=1020, height=850, bg="black")
        self.f1.place(x=0, y=0)
        self.pic = Image.open(r"mainpagepic.png")
        self.pic = self.pic.resize((1016, 716), Image.Resampling.LANCZOS)
        self.pic = ImageTk.PhotoImage(self.pic)
        Label(self.f1, image=self.pic).place(x=0, y=0)
        self.main_frame2 = Frame(self.f1, width=700, height=500, bg="black")
        self.main_frame2.place(x=150, y=120)
        self.main_frame3 = Frame(self.f1, width=700, height=500, bg="black")
        self.main_frame = Frame(self.f1, width=700, height=500, bg="black")
        self.main_frame.place(x=150, y=120)

        self.frame1 = Frame(self.root, background="white")
        self.frame2 = Frame(self.root, background="white")
        self.frame3 = Frame(self.root, background="white")
        self.frame4 = Frame(self.root, background="white",width=500)
        self.frame5 = Frame(self.root, background="white",width=500)
        self.frame6 = Frame(self.root, background="white",width=500)
        self.frame7 = Frame(self.root, background="white",width=1000)
        self.frame8 = Frame(self.root, background="white",width=1000)
        #Canvas Area
        self.Canvas_Area = Canvas(self.frame1, width=1200, height=120, bg="white",background="white",highlightthickness=0)
        self.Canvas_Area.grid(row=0, sticky=W)
        self.Canvas_Area2 = Canvas(self.frame7, width=1200,height=700, bg="white",background="white",highlightthickness=0)
        self.Canvas_Area2.grid(row=0, sticky=W)

        # self.frame5.pack()
        # self.frame6.pack()
        # self.frame7.pack(side=LEFT)
    def ordered_check(self):
        if self.ordered_price==True:
            self.frame7.forget()
            del int_page.frame7
            self.frame7 = Frame(self.root, background="white", width=1000)
            int_page.frame8.pack()
            Label(int_page.Canvas_Area, text=len(Products.cart_list) - len(self.order_list), bg="white",fg="red").place(x=990, y=10,width=25)
            Label(int_page.frame8, text="Order Details:", bg="white",font="times 18 bold").pack()
            self.Order_Detail_List=[]
            self.Order_Detail_List.append(obj.user_email_signin_val.get())

            for i in self.order_list:
                if i in Products.cart_list:
                    Products.cart_list.remove(i)
                    self.Order_Detail_List.append(i)
                Label(int_page.frame8,text=f"Product Name: {i.product_name}\t  |Rs. {i.product_price}",bg="white",font="times 13").pack()
            with open("OrderDetails.txt", "a+") as f:
                f.write(str(self.Order_Detail_List))
    def total_price(self):
        self.order_list=[]
        MainPage.TotalPrice = 0
        for i in Products.cart_list:
            if i.Checkbutton_Val.get()==1:
                self.order_list.append(i)
                MainPage.TotalPrice+=int(i.product_price)*i.no
        self.buy_now["text"]=f"Total Price: Rs. {MainPage.TotalPrice}/="
    def order_messagebox(self):
        self.total_price()
        if MainPage.TotalPrice==0:
            tmsg.showinfo("Invalid Order!","Please select the product first!")
        else:
            self.ordered_price = tmsg.askyesno("Confirm Order!", "Are you sure you want to buy this ?")
            self.ordered_check()

    def product_remover(self):
        self.removed_product_list = []
        for i in Products.cart_list:
            if i.Checkbutton_Val.get() == 1:
                self.removed_product_list.append(i)
        for j in self.removed_product_list:
            Products.cart_list.remove(j)
        Label(int_page.Canvas_Area, text=len(Products.cart_list), bg="white",
                      fg="red").place(x=990, y=10, width=25)

        self.cart_button()

    def cart_button(self):
        int_page.frame6.forget()
        int_page.frame2.forget()
        int_page.frame3.forget()
        int_page.frame8.forget()
        # self.frame7 = Frame(self.root, background="white", width=1000)
        # self.frame7.forget()
        # self.frame7 = Frame(self.root, background="white", width=1000)
        self.frame7.pack(side=LEFT, anchor=NW)
        self.Canvas_Area2 = Canvas(self.frame7, width=1200, height=700, bg="white", background="white",highlightthickness=0)
        self.Canvas_Area2.grid(row=0, sticky=W)
        int_page.frame8.pack()
        c=0
        count = 0

        Label(int_page.Canvas_Area2,text="View Cart",font="times 18 bold",bg="white").place(x=450,y=c+3)
        def add_quant(i):
            def add():
                i.no += 1
                i.label["text"] = i.no
                print(i.product_name)
            return add
        def sub_quant(i):
            def sub():
                if i.no<=1:
                    i.no=1
                else:
                    i.no -= 1
                    i.label["text"] = i.no
                    print(i.product_name)
            return sub
        for i in Products.cart_list:
            c+=28
            count+=1
            if count==1:
                Label(int_page.Canvas_Area2, text="S. No.", bg="white",font="times 12 bold").place(x=20, y=c, anchor=NW)
                Label(int_page.Canvas_Area2, text=f"Product Names", bg="white",font="times 12 bold").place(x=350, y=c,anchor=NW)
                Label(int_page.Canvas_Area2, text=f"Price", bg="white",font="times 12 bold").place(x=785, y=c,anchor=NW)
                Label(int_page.Canvas_Area2, text=f"Quantity", bg="white",font="times 12 bold").place(x=910, y=c,anchor=NW)
                int_page.Canvas_Area2.create_line(0,60,1200,60)
                int_page.Canvas_Area2.create_line(80,35,80,700)
                int_page.Canvas_Area2.create_line(880,35,880,700)
                int_page.Canvas_Area2.create_line(740,35,740,700)
            Label(int_page.Canvas_Area2,text=f"{count}",bg="white").place(x=30,y=c+40,anchor=NW)
            Label(int_page.Canvas_Area2,text=f"Rs. {i.product_price}",bg="white").place(x=785,y=c+40,anchor=NW)
            i.Checkbutton_Val = IntVar()
            i.checkButton = Checkbutton(int_page.Canvas_Area2,text =f"{i.product_name}",bg="white",variable=i.Checkbutton_Val,onvalue = 1,offvalue = 0,height = 0)
            i.checkButton.place(x=100,y=c+40,anchor=NW)
            int_page.Canvas_Area2.create_line(0, c+65, 1200, c+65)
            i.label=Label(int_page.Canvas_Area2,text=i.no,bg="white")
            i.add_quantity_button=Button(int_page.Canvas_Area2,activebackground="red",text="+",bg="white",command=add_quant(i),height=1)
            i.sub_quantity_button=Button(int_page.Canvas_Area2,activebackground="red",text="-",bg="white",command=sub_quant(i),height=1)
            i.sub_quantity_button.place(x=860+50,y=c+39)
            i.label.place(x=880+50,y=c+40)
            i.add_quantity_button.place(x=900+50,y=c+39)

        self.buy_now = Button(int_page.Canvas_Area2, activebackground="red", text="Total Price: Rs. 0/=",
                              command=self.total_price,
                              bg="white", font="times 15 bold", relief="ridge", border=3)
        self.buy_now.place(x=20, y=520)
        self.place_order = Button(int_page.Canvas_Area2, text="Place Order", command=self.order_messagebox, fg="red",bg="white", activebackground="red", font="times 20 bold", relief="ridge", border=3)
        self.place_order.place(x=428, y=510)
        self.remove_product = Button(int_page.Canvas_Area2, text="Remove Product", command=self.product_remover,fg="black",bg="white", activebackground="red", font="times 15 bold", relief="ridge", border=3)
        self.remove_product.place(x=838,y=520)








    def FindProduct(self):
        int_page.frame6.forget()
        del int_page.frame6
        self.frame6 = Frame(self.root, background="white", width=500)
        self.frame6.forget()
        # self.frame7 = Frame(int_page.root, background="white", width=500)
        self.frame7.forget()
        self.frame8.forget()
        self.search_obj = SearchProduct()
    def Search_Box(self):
        self.Product_Value = StringVar()
        self.Product_Entry = Entry(self.Canvas_Area, textvariable=self.Product_Value, width=70, relief="solid",font="Times 15",highlightthickness=1,borderwidth=0,foreground="grey",selectbackground="red")
        self.Product_Entry.config(highlightbackground ="red", highlightcolor="red")
        self.Product_Entry.place(x=295,y=85)
        # search button
        self.openImage=Image.open(r"searchbox.png")
        self.resizedimage=self.openImage.resize((35,26),Image.Resampling.LANCZOS)
        self.searchImage=ImageTk.PhotoImage(self.resizedimage)
        self.Button_Search = Button(self.Canvas_Area,bg="white",image=self.searchImage,highlightcolor="red",borderwidth=False,relief="flat",command=self.FindProduct)
        self.Button_Search.place(x=963,y=84)
        # category box button
        self.categories = PhotoImage(file=r"catogories.png")
        self.categoriesPhoto = self.categories.subsample(9, 9)
        self.categories_button=Button(self.Canvas_Area,command=category_button,text="Categories",font="times 15",bg="white",image=self.categoriesPhoto,compound=LEFT,highlightthickness=2,borderwidth=1,relief="flat")
        self.categories_button.place(x=12,y=80)
        # shoping cart button
        self.cart=PhotoImage(file=r"shoppingcart.png")
        self.shoppingcartPhoto=self.cart.subsample(10,10)
        self.shoppingcartButton= Button(self.Canvas_Area,command=self.cart_button,image=self.shoppingcartPhoto,bg="white",borderwidth=0,relief="flat")
        self.shoppingcartButton.place(x=962,y=24)
class Account:
    with open("ACCOUNT_DETAILS.txt", "r+") as f:
        r = f.readlines()
        lst = []
        for i in r:
            i = i.strip()
            x = i.split(";")
            lst.append(x)
    print(lst)
    def accountdetailssaver(self):
        if self.user_shipping_address_val.get()=="" or self.user_city_val.get()=="" or self.user_state_val.get()=="" or self.user_phone_no_val.get()=="" or len(self.user_phone_no_val.get())!=11  or not self.user_phone_no_val.get().isdigit():
            if self.user_shipping_address_val.get()=="":
                Label(int_page.main_frame3, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(x=570 - 150+168, y=250 - 120)
            if self.user_city_val.get()=="":
                Label(int_page.main_frame3, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(x=570 - 150+32,y=330 - 120)
            if self.user_state_val.get()=="":
                Label(int_page.main_frame3, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(x=700 - 150+40, y=330 - 120)
            if self.user_phone_no_val=="" or len(self.user_phone_no_val.get())!=11  or not self.user_phone_no_val.get().isdigit():
                Label(int_page.main_frame3, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(x=570 - 150+115, y=410 - 120)
            return





        with open("ACCOUNT_DETAILS.txt", "a+") as f:
            f.write(f"{self.user_email_val.get()};{self.user_password_val.get()};{self.user_first_name_val.get()};{self.user_last_name_val.get()};{self.user_phone_no_val.get()};{self.user_shipping_address_val.get()};{self.user_city_val.get()};{self.user_state_val.get()};")
            f.seek(0)
        self.user_name=self.user_first_name_val.get()
        self.accountsignin()

    def accountchecker(self):

        for i in Account.lst:
            print(i[0],i[1])
            if i[0]==f"{self.user_email_signin_val.get()}" and i[1]==f"{self.user_password_signin_val.get()}":
                self.user_name = i[2]
                self.accountsignin()
            elif i[0]!=f"{self.user_email_signin_val.get()}" or i[1]!=f"{self.user_password_signin_val.get()}":
                Label(int_page.main_frame2, text="invalid email or password*", font=("yu gothic ui", 8, "bold"), fg="red", bg="black").place(x=645 - 150, y=303 - 150)
    def accountsignin(self):
        print("Email :",self.user_email_val.get())
        print("Password :",self.user_password_val.get())
        int_page.f1.place_forget()
        int_page.main_frame2.place_forget()
        int_page.frontpage()
        int_page.Search_Box()
        cat1 = Catogeries("Fruits & Vegetables", "frt.png")
        cat2 = Catogeries("Personal Care", "personalcare.png")
        cat3 = Catogeries("Fresh Meat", "freshmeat.png")
        cat4 = Catogeries("Fish & Seafood", "fish.png")
        cat5 = Catogeries("Grocery", "grocery.png")
        cat6 = Catogeries("Beverages", "beverages.png")
        cat7 = Catogeries("Bakery & Dairy", "bakeryitem.png")
        cat1.pic_categories()
        cat2.pic_categories()
        cat3.pic_categories()
        cat4.pic_categories()
        cat5.pic_categories()
        cat6.pic_categories()
        cat7.pic_categories()
        Catogeries.row_no = 0
        Catogeries.column_no = 0
        dict["pro1"].Label_Top_Selling()
        Catogeries.column_no = 1
        dict["pro" + str(i)].pic_product()
        Catogeries.column_no = 2
        dict["pro15"].pic_product()
        Catogeries.column_no = 3
        dict["pro10"].pic_product()
        Catogeries.column_no = 4
        dict["pro5"].pic_product()
        Catogeries.column_no = 5
        dict["pro19"].pic_product()
        Catogeries.column_no = 0
    def accountsignup(self):
        print("First Name :",self.user_first_name_val.get())
        print("Last Name :",self.user_last_name_val.get())
        print("Email :",self.user_email_val.get())
        print("Password :",self.user_password_val.get())
        for i in Account.lst:
            if i[0] == self.user_email_val.get():
                Label(int_page.main_frame, text="Already Exist*", font=("yu gothic ui", 8, "bold"), fg="red",bg="black").place(x=730 - 150, y=335  - 120)
                return self.signup()
        if self.user_first_name_val.get()=="" or self.user_password_val.get()=="" or self.user_last_name_val.get()=="" or "@" not in self.user_email_val.get() or "." not in self.user_email_val.get():
            try:
                if self.user_first_name_val.get() == "":
                    raise First_Name_Error
                # return

            except First_Name_Error:
                Label(int_page.main_frame, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(
                    x=570 - 150 + 80, y=250 - 120)
                # return
            try:
                if self.user_last_name_val.get() == "":
                    raise Last_Name_Error
                # return
            except Last_Name_Error:
                Label(int_page.main_frame, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(
                    x=700 - 150 + 78, y=250 - 120)
                # return
            try:
                if self.user_email_val.get() == "" or "@" not in self.user_email_val.get() or "." not in self.user_email_val.get():
                    raise Email_Error
                # return

            except Email_Error:
                Label(int_page.main_frame, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(
                    x=570 - 150 + 40, y=300 + 30 - 120)
                # return

            try:

                if self.user_password_val.get() == "":
                    raise Password_Error
                return

            except Password_Error:
                Label(int_page.main_frame, text="*", font=("yu gothic ui", 12, "bold"), fg="red", bg="black").place(
                    x=570 - 150 + 70, y=380 + 30 - 120)
                return

        int_page.main_frame.place_forget()
        int_page.main_frame3.place(x=150, y=120)
        Label(int_page.main_frame3, text="Creating Your Account", bg="black", fg="white",font=("yu gothic ui", 15, "bold")).place(x=580 - 150, y=200 - 120)
        Label(int_page.main_frame3, text="Add Shipping Address", font=("yu gothic ui", 12, "bold"), fg="grey", bg="black").place(x=570 - 150, y=250 - 120)
        self.user_shipping_address_val = StringVar()
        self.user_shipping_address = Entry(int_page.main_frame3, width=32, font="Helvetica 10", border=0, bg="black",selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_shipping_address_val).place(x=570 + 3-150, y=280-120)
        can_area7 = Canvas(int_page.main_frame3, width=230, height=1.4, bg="grey", highlightthickness=0).place(x=570 + 3-150,y=300-120)

        Label(int_page.main_frame3, text="City", font=("yu gothic ui", 12, "bold"), fg="grey",bg="black").place(x=570 - 150,y=330 - 120)
        self.user_city_val = StringVar()
        self.user_city = Entry(int_page.main_frame3, width=14, font="Helvetica 10", border=0, bg="black",selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_city_val).place(x=570 + 3 - 150,y=360 - 120)
        can_area7 = Canvas(int_page.main_frame3, width=100, height=1.4, bg="grey", highlightthickness=0).place(x=570 + 3 - 150, y=380 - 120)

        Label(int_page.main_frame3, text="State", font=("yu gothic ui", 12, "bold"), fg="grey",bg="black").place(x=700 - 150, y=330 - 120)
        self.user_state_val = StringVar()
        self.user_state = Entry(int_page.main_frame3, width=14, font="Helvetica 10", border=0, bg="black", selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_state_val).place(x=700 + 3 - 150,y=360 - 120)
        can_area8 = Canvas(int_page.main_frame3, width=100, height=1.4, bg="grey", highlightthickness=0).place(x=700 + 3 - 150, y=380 - 120)

        Label(int_page.main_frame3, text="Phone Number", font=("yu gothic ui", 12, "bold"), fg="grey",bg="black").place(x=570 - 150, y=410 - 120)
        self.user_phone_no_val = StringVar()
        self.user_phone_no = Entry(int_page.main_frame3, width=32, font="Helvetica 10",validate="focus", border=0, bg="black",selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_phone_no_val).place(x=570 + 3 - 150,y=440 - 120)
        can_area7 = Canvas(int_page.main_frame3, width=230, height=1.4, bg="grey", highlightthickness=0).place(x=570 + 3 - 150, y=460 - 120)

        self.mainpageloginpic = Image.open(r"login.png")
        self.mainpageloginpic = self.mainpageloginpic.resize((90, 23), Image.Resampling.LANCZOS)
        self.mainpageloginpic = ImageTk.PhotoImage(self.mainpageloginpic)
        self.mainpageloginbutton = Button(int_page.main_frame3, image=self.mainpageloginpic, bg="black",highlightthickness=0, border=0, background="black",command=self.accountdetailssaver,activebackground="black").place(x=640 - 150, y=520 - 150)

    def signup(self):
        int_page.main_frame2.place_forget()
        int_page.main_frame.place(x=150, y=120)
        self.welcome_label=Label(int_page.f1,text="WELCOME",font=("yu gothic ui",20,"bold"),fg="white",bg="black")
        self.welcome_label.place(x=300,y=150)
        self.mainpageuserpic=Image.open(r"user.png")
        self.mainpageuserpic = self.mainpageuserpic.resize((50, 50), Image.Resampling.LANCZOS)
        self.mainpageuserpic = ImageTk.PhotoImage(self.mainpageuserpic)
        self.mainpageuserpiclabel=Label(int_page.f1, image=self.mainpageuserpic,bg="black")
        self.mainpageuserpiclabel.place(x=660, y=150)
        self.mainpagecartpic = Image.open(r"mainpagecart.png")
        self.mainpagecartpic = self.mainpagecartpic.resize((300, 250), Image.Resampling.LANCZOS)
        self.mainpagecartpic = ImageTk.PhotoImage(self.mainpagecartpic)
        self.mainpagecartpiclabel=Label(int_page.f1, image=self.mainpagecartpic, bg="black")
        self.mainpagecartpiclabel.place(x=210, y=230)
        # Create New Account
        Label(int_page.main_frame, text="Create Your Account", bg="black", fg="white",font=("yu gothic ui", 15, "bold")).place(x=590-150, y=200-120)
        self.user_first_name_val = StringVar()
        self.user_last_name_val = StringVar()
        self.user_email_val = StringVar()
        self.user_password_val = StringVar()
        Label(int_page.main_frame, text="First Name", font=("yu gothic ui", 12, "bold"), fg="grey", bg="black").place(x=570-150, y=250-120)
        self.user_first_name = Entry(int_page.main_frame, width=14, font="Helvetica 10", border=0, bg="black",selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_first_name_val).place(x=570 + 3-150, y=280-120)
        Label(int_page.main_frame, text="Last Name", font=("yu gothic ui", 12, "bold"), fg="grey", bg="black").place(x=700-150,y=250-120)
        self.user_last_name = Entry(int_page.main_frame, width=14, font="Helvetica 10", border=0, bg="black",selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_last_name_val).place(x=700 + 3-150, y=280-120)
        Label(int_page.main_frame, text="Email", font=("yu gothic ui", 12, "bold"), fg="grey", bg="black").place(x=570-150, y=300 + 30-120)
        self.user_email = Entry(int_page.main_frame, width=32, font="Helvetica 10", border=0, bg="black",selectforeground="white", selectbackground="red", foreground="white", textvariable=self.user_email_val).place(x=570 + 3-150, y=330 + 30-120)
        Label(int_page.main_frame, text="Password", font=("yu gothic ui", 12, "bold"), fg="grey", bg="black").place(x=570-150, y=380 + 30-120)
        self.user_password = Entry(int_page.main_frame, show="*", width=32, font="Helvetica 10", border=0, bg="black",fg="grey", selectforeground="white", selectbackground="red", foreground="white", textvariable=self.user_password_val).place(x=570 + 3-150, y=410 + 30-120)
        self.can_area1 = Canvas(int_page.main_frame, width=100, height=1.4, bg="grey", highlightthickness=0).place(x=570 + 3-150, y=300-120)
        can_area2 = Canvas(int_page.main_frame, width=100, height=1.4, bg="grey", highlightthickness=0).place(x=700 + 3-150, y=300-120)
        can_area3 = Canvas(int_page.main_frame, width=230, height=1.4, bg="grey", highlightthickness=0).place(x=570 + 3-150, y=350 + 30-120)
        can_area4 = Canvas(int_page.main_frame, width=230, height=1.4, bg="grey", highlightthickness=0).place(x=570 + 3-150,y=430 + 30-120)
        self.mainpagecreateaccountpic = Image.open(r"createaccount.png")
        self.mainpagecreateaccountpic = self.mainpagecreateaccountpic.resize((190, 23), Image.Resampling.LANCZOS)
        self.mainpagecreateaccountpic = ImageTk.PhotoImage(self.mainpagecreateaccountpic)
        self.mainpagecreateaccountbutton = Button(int_page.main_frame, image=self.mainpagecreateaccountpic, bg="black",highlightthickness=0, border=0, background="black",command=self.accountsignup, activebackground="black").place(x=593-150, y=490-120)
        self.already_have_account = Button(int_page.main_frame,text="Already have an account?",font=("yu gothic ui", 10, "bold"), fg="red", bg="black", border=0, activebackground="black", activeforeground="grey",command=self.signin).place(x=607-150, y=529-120)
    def signin(self):
        int_page.main_frame.place_forget()
        int_page.main_frame2.place(x=150, y=120)
        self.user_email_signin_val = StringVar()
        self.user_password_signin_val = StringVar()
        Label(int_page.main_frame2, text="Log In", bg="black", fg="white", font=("yu gothic ui", 15, "bold")).place(x=593-88, y=200-120)
        Label(int_page.main_frame2, text="Email", font=("yu gothic ui", 12, "bold"), fg="grey", bg="black").place(x=570-150,y=300-150)
        self.user_email = Entry(int_page.main_frame2, width=30, font="Helvetica 10", border=0, bg="black",selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_email_signin_val).place(x=570-150, y=330-150)
        Label(int_page.main_frame2, text="Password", font=("yu gothic ui", 12, "bold"), fg="grey", bg="black").place(x=570-150,y=380-150)
        self.user_password = Entry(int_page.main_frame2, show="*", width=30, font="Helvetica 10", border=0, bg="black",fg="grey", selectforeground="white", selectbackground="red", foreground="white",textvariable=self.user_password_signin_val).place(x=570-150, y=410-150)
        can_area5 = Canvas(int_page.main_frame2, width=215, height=1.4, bg="grey", highlightthickness=0).place(x=570-150, y=350-150)
        can_area6 = Canvas(int_page.main_frame2, width=215, height=1.4, bg="grey", highlightthickness=0).place(x=570-150, y=430-150)
        self.mainpageloginpic = Image.open(r"login.png")
        self.mainpageloginpic = self.mainpageloginpic.resize((90, 23), Image.Resampling.LANCZOS)
        self.mainpageloginpic = ImageTk.PhotoImage(self.mainpageloginpic)
        self.mainpageloginbutton = Button(int_page.main_frame2, image=self.mainpageloginpic, bg="black",highlightthickness=0, border=0, background="black", command=self.accountchecker,activebackground="black").place(x=633-150, y=460-150)
        self.create_a_new_account = Button(int_page.main_frame2, text="Create a new account",font=("yu gothic ui", 10, "bold"), fg="red", bg="black", border=0,activebackground="black", activeforeground="grey",command=self.signup).place(x=604-145, y=500-150)

# root.mainloop()
class SearchProduct:
    count=0
    def __init__(self):
        SearchProduct.count+=1
        int_page.frame3.forget()
        int_page.frame4.forget()
        int_page.frame5.forget()
        int_page.frame2.forget()
        int_page.frame7.forget()
        int_page.frame6.pack()
        print(int_page.Product_Value.get())
        r = 0
        Catogeries.row_no = 0
        Catogeries.column_no = 0
        count=0
        if len(int_page.Product_Value.get())!=0:
            for i in range(len(Product_List)):
                for j in range(len(Product_List[i][2])):
                    if dict["pro" + str(i)].product_name[j].lower() == int_page.Product_Value.get()[j].lower():
                        if len(int_page.Product_Value.get()) == (j + 1):
                            dict["pro" + str(i)].pic_product()
                            count += 1
                            Catogeries.column_no += 1
                            if Catogeries.column_no >= 5:
                                Catogeries.column_no = 0
                            if r >= 4:
                                Catogeries.row_no = 1
                            r += 1

                            break
                        else:
                            pass
                    else:
                        break
        Catogeries.row_no=0
        if count==0 or len(int_page.Product_Value.get())==0:
            Label(int_page.frame6, text="Product Not Found!", font="times 12", bg="white", fg="red").grid()

def category_button():
    int_page.frame6.forget()
    # int_page.frame7= Frame(int_page.root, background="white", width=500)
    int_page.frame7.forget()
    int_page.frame8.forget()
    int_page.frame2.pack()
class Catogeries:
    row_no=0
    column_no=0
    count=0
    def __init__(self,category_name,category_pic_path):
        self.category_path="r"+f'"{category_pic_path}"'
        self.category_name=category_name
    def CategoryDisplayer(self):
        Catogeries.count+=1
        if Catogeries.count>=1:
            int_page.frame6.forget()
            del int_page.frame6
            int_page.frame6 = Frame(int_page.root, background="white", width=500)
            int_page.frame6.pack()
        int_page.frame2.forget()
        int_page.frame3.forget()
        int_page.frame4.forget()
        r=0
        for i in range(len(dict)):
            if self.category_name == dict["pro"+str(i)].category_name:
                dict["pro"+str(i)].pic_product()
                Catogeries.column_no+=1
                if Catogeries.column_no>=5:
                    Catogeries.column_no=0
                if r>=4:
                    Catogeries.row_no=1
                r+=1
        Catogeries.row_no=0
    def pic_categories(self):
        self.category = Image.open(eval(self.category_path))
        self.categoryresized = self.category.resize((109, 100), Image.Resampling.LANCZOS)
        self.categoryimage = ImageTk.PhotoImage(self.categoryresized)
        self.categorybutton = Button(int_page.frame2,command=self.CategoryDisplayer,text=self.category_name,compound=TOP,font="Times 12",bg="white",fg="grey", image=self.categoryimage, relief="solid",borderwidth=0)
        self.categorybutton.pack(anchor=NW,side=LEFT,pady=15,padx=16)
class Products(Catogeries):
    cart_list=[]
    no=1
    def AddToCart(self):
        print(self.category_name)
        print(self.product_name)
        print(self.product_price)
        # Products.cart_list.append([self.product_name,self.product_price])
        Products.cart_list.append(self)
        Products.cart_list = list(set(Products.cart_list))
        Label(int_page.Canvas_Area,text=len(Products.cart_list),bg="white",fg="red").place(x=990,y=10,width=25)
    def Label_Top_Selling(self):
        LabelTopSelling=Label(int_page.frame3, text="Top Selling Product",bg="white",font="times 18 bold")
        LabelTopSelling.pack(pady=12)
    def __init__(self,category_name,category_pic_path,product_name,price,weight,units_sold,stock):
        super().__init__(category_name,category_pic_path)
        self.product_path =  f'r"{category_pic_path}"'
        self.product_name = product_name
        self.product_price=price
        self.product_units_sold=units_sold
        self.product_stock=stock
        self.product_weight=weight
    def pic_product(self):
        self.product = Image.open(eval(self.product_path))
        self.productresized = self.product.resize((165, 140), Image.Resampling.LANCZOS)
        self.productimage = ImageTk.PhotoImage(self.productresized)
        self.border = LabelFrame(int_page.frame6, bd=2, bg="grey", relief=FLAT,width=110,height=100)
        int_page.frame6.pack()
        self.border.grid(padx=15, pady=5,row=Catogeries.row_no,column=Catogeries.column_no)
        self.productbutton = Button(self.border,text=f"{self.product_name}\n{self.product_weight}\nRs. {self.product_price}", compound=TOP, font="Times 13 bold",bg="white", fg="black", image=self.productimage, relief="solid", borderwidth=0)
        self.productbutton.pack(ipady=8)
        self.cartbutton = Button(self.border,command=self.AddToCart,text="ADD TO CART", font="Times 12 bold", bg="Red", fg="black",width=18,relief="solid", borderwidth=0)
        self.cartbutton.pack(ipady=8)
int_page=MainPage()
obj=Account()
obj.signup()
dict={}
for i in range(len(Product_List)):
    dict["pro"+str(i)]=Products(Product_List[i][0],Product_List[i][1],Product_List[i][2],Product_List[i][3],Product_List[i][4],0,0)
int_page.root.mainloop()
