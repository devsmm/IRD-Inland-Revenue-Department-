from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import datetime


class Ird_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x780+0+0")
        self.root.title("IRD -Inland Revenue Department")
        p1 = PhotoImage(file="gov.ico")
        root.iconphoto(True, p1)
        color = "#007fff"
        title = Label(self.root, text="IRD Tax Calculation System", bd=2, bg=color, foreground="white", relief=GROOVE,
                      font=("times new roman", 30, "bold"), pady=2)
        title.pack(fill=X)
        line = LabelFrame(self.root, bg=color)
        line.place(x=0, y=150, relwidth=1)
        #   -----------variables----------------
        self.name = StringVar()
        self.age = IntVar()
        self.address = StringVar()
        self.income = IntVar()
        self.maritalStatus = StringVar()
        self.diplomatic_employee = StringVar()
        self.gender = StringVar()
        self.insurance = StringVar()
        self.tax_income = None
        self.disability_status = StringVar()
        self.dateTime = datetime.datetime.now()
        # Details:
        customerDetails = LabelFrame(self.root, text="Customer Details", font=("Futura", 16, "bold"), bg=color,
                                     fg="white", borderwidth=0.5, relief=GROOVE, height=1300)
        customerDetails.place(x=10, y=210, relwidth=0.4, relheight=0.63)

        # ----for name-----

        cname_label = Label(customerDetails, text="Name", font=("Halvetica", 16, "bold"), bg=color,
                            fg="white")
        cname_label.grid(row=0, column=0, padx=20, pady=5)
        self.cname_text = Entry(customerDetails, textvariable=self.name, width=20, font="Halvetica", bd=2,
                                relief=SUNKEN)
        self.cname_text.grid(row=0, column=1, padx=10, pady=5)

        # ----for Address-----

        caddress_label = Label(customerDetails, text="Address", font=("Halvetica", 16, "bold"), bg=color,
                               fg="white")
        caddress_label.grid(row=1, column=0, padx=20, pady=5)
        self.caddress_text = Entry(customerDetails, textvariable=self.address, width=20, font="Halvetica", bd=2,
                                   relief=SUNKEN)
        self.caddress_text.grid(row=1, column=1, padx=10, pady=5)

        # ----for Age-----

        cage_label = Label(customerDetails, text="Age", font=("Halvetica", 16, "bold"), bg=color,
                           fg="white")
        cage_label.grid(row=2, column=0, padx=20, pady=5)
        self.cage_text = Entry(customerDetails, textvariable=self.age, width=20, font="Halvetica", bd=2, relief=SUNKEN)
        self.cage_text.grid(row=2, column=1, padx=10, pady=5)

        # ----for income-----

        cage_label = Label(customerDetails, text="Income", font=("Halvetica", 16, "bold"), bg=color,
                           fg="white")
        cage_label.grid(row=3, column=0, padx=20, pady=5)
        self.income_text = Entry(customerDetails, textvariable=self.income, width=20, font="Halvetica", bd=2,
                                 relief=SUNKEN)
        self.income_text.grid(row=3, column=1, padx=10, pady=5)

        #   ----------for marital status-------
        Label(customerDetails, text="Marital status", font=("Halvetica", 16, "bold"), bg=color,
              fg="white").grid(row=4, column=0, pady=5, padx=5)
        self.marriedButton = Radiobutton(customerDetails, text="Married", variable=self.maritalStatus, value="married",
                                         bg=color, width=10,
                                         font="Halvetica")
        self.marriedButton.grid(row=4, column=1, padx=6, pady=5)
        self.unmarriedButton = Radiobutton(customerDetails, text="Unmarried", variable=self.maritalStatus,
                                           value="unmarried", bg=color,
                                           width=10, font="Halvetica")
        self.unmarriedButton.grid(row=4, column=2, padx=10, pady=5)

        # ----for disability status----
        Label(customerDetails, text="Disability Status", font=("Halvetica", 16, "bold"), bg=color,
              fg="white").grid(row=6, column=0, pady=5, padx=5)
        self.disability_dropdown = OptionMenu(customerDetails, self.disability_status,
                                              "Natural Person", "Physically Disabled")
        self.disability_dropdown.grid(row=6, column=1, padx=6, pady=5)
        self.disability_status.set("choose the disability status")

        # -----for abroad worker-------
        Label(customerDetails, text="Diplomatic Worker Of Nepal Situated abroad?", font=("Halvetica", 16, "bold"),
              bg=color,
              fg="white").grid(row=7, columnspan=3, pady=5, padx=5)
        self.yesButton = Radiobutton(customerDetails, text="yes", variable=self.diplomatic_employee, value="yes",
                                     bg=color, width=10,
                                     font="Halvetica")
        self.yesButton.grid(row=8, column=0, padx=6, pady=5)
        self.noButton = Radiobutton(customerDetails, text="no", variable=self.diplomatic_employee, value="no",
                                    bg=color, width=10,
                                    font="Halvetica")
        self.noButton.grid(row=8, column=1, padx=6, pady=5)

        # ----gender-----
        Label(customerDetails, text="Gender", font=("Halvetica", 16, "bold"), bg=color,
              fg="white").grid(row=9, column=0, pady=5, padx=5)
        self.male = Radiobutton(customerDetails, text="Male", variable=self.gender, value="male",
                                bg=color, width=10,
                                font="Halvetica")
        self.male.grid(row=9, column=1, padx=6, pady=5)
        self.female = Radiobutton(customerDetails, text="Female", variable=self.gender,
                                  value="female", bg=color,
                                  width=10, font="Halvetica")
        self.female.grid(row=9, column=2, padx=10, pady=5)

        # -- insured-----
        Label(customerDetails, text="Insurance", font=("Halvetica", 16, "bold"), bg=color,
              fg="white").grid(row=10, column=0, pady=5, padx=5)
        self.insured = Radiobutton(customerDetails, text="Insured", variable=self.insurance, value="Insured",
                                   bg=color, width=10,
                                   font="Halvetica")
        self.insured.grid(row=10, column=1, padx=6, pady=5)
        self.uninsured = Radiobutton(customerDetails, text="Uninsured", variable=self.insurance,
                                     value="Uninsured", bg=color,
                                     width=10, font="Halvetica")
        self.uninsured.grid(row=10, column=2, padx=10, pady=5)

        #   -----for buttons-----
        submit_btn = Button(customerDetails, command=self.details, text="Submit", width=10, bd=2,
                            font=("Halvetica", 16, "bold"), borderwidth=1, fg="white", bg="#1AA7EC")
        submit_btn.grid(row=11, column=0, pady=1, padx=2)

        clear_btn = Button(customerDetails, command=self.clear, text="Clear", width=10,
                           font=("Halvetica", 16, "bold"), bd=2, fg="white", bg="RED")
        clear_btn.grid(row=11, column=1, pady=1, padx=2)

        #   ------for result area------
        resultArea = Frame(self.root, bd=10, relief=GROOVE, width=1300)
        resultArea.place(x=690, y=250, width=600, height=380)
        resultTitle = Label(resultArea, text="Tax Calculation", font=("Halvetica", 16, "bold"), bd=6, relief=GROOVE)
        resultTitle.pack(fill=X)
        scroll_y = Scrollbar(resultArea, orient=VERTICAL)
        self.textarea = Text(resultArea, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

    def calculateMarried(self, yearly_income):
        if yearly_income < 400000:
            tax_amount = yearly_income * 0.01

        elif yearly_income >= 400000 or yearly_income < 500000:
            tax_amount = 4500 + ((yearly_income - 400000) * 0.1)

        elif 500000 <= yearly_income < 700000:
            tax_amount = 14500 + ((yearly_income - 500000) * 0.2)

        elif 700000 <= yearly_income < 2000000:
            tax_amount = 54500 + ((yearly_income - 700000) * 0.3)

        else:
            tax_amount = 429500 + ((yearly_income - 2000000) * 0.36)
        return tax_amount

    def calculateUnmarried(self, yearly_income):
        if yearly_income < 400000:
            tax_amount = yearly_income * 0.01
        elif yearly_income >= 400000 or yearly_income < 500000:
            tax_amount = 4000 + ((yearly_income - 400000) * 0.1)
        elif 500000 <= yearly_income < 700000:
            tax_amount = 14000 + ((yearly_income - 500000) * 0.2)
        elif 700000 <= yearly_income < 2000000:
            tax_amount = 54000 + ((yearly_income - 700000) * 0.3)
        else:
            tax_amount = 444000 + ((yearly_income - 2000000) * 0.36)
        return tax_amount

    def calculateTax(self):
        if self.insurance.get() == "Insured":
            afterInsurance = (self.income.get() * 12) - 20000
        else:
            afterInsurance = self.income.get() * 12
        tax = None
        # -- for female with disabilities:
        if self.disability_status.get() == "Physically Disabled" and self.gender.get() == "female":
            if self.maritalStatus.get() == "married":
                if self.diplomatic_employee.get() == "yes":
                    # ---exceptions for disability and diplomatic employee:
                    tax = self.calculateMarried(afterInsurance) - (
                            0.1 * self.calculateMarried(afterInsurance) + 0.75 * self.calculateMarried(afterInsurance))
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateMarried(afterInsurance) - (
                            0.1 * self.calculateMarried(afterInsurance) + 0.5 * self.calculateMarried(
                        afterInsurance))
            if self.maritalStatus.get() == "unmarried":
                if self.diplomatic_employee.get() == "yes":
                    tax = self.calculateUnmarried(afterInsurance) - (
                            0.1 * self.calculateUnmarried(afterInsurance) + 0.75 * self.calculateUnmarried(
                        afterInsurance))
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateUnmarried(afterInsurance) - (
                            0.1 * self.calculateUnmarried(afterInsurance) + 0.5 * self.calculateUnmarried(
                        afterInsurance))

        # --for male with disabilities:
        if self.disability_status.get() == "Physically Disabled" and self.gender.get() == "male":
            if self.maritalStatus.get() == "married":
                # ---exceptions for disability and diplomatic employee:
                if self.diplomatic_employee.get() == "yes":
                    tax = self.calculateMarried(afterInsurance) - (0.75 * self.calculateMarried(afterInsurance))
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateMarried(afterInsurance) - 0.5 * self.calculateMarried(
                        afterInsurance)

            if self.maritalStatus.get() == "unmarried":
                if self.diplomatic_employee.get() == "yes":
                    tax = self.calculateUnmarried(afterInsurance) - (0.75 * self.calculateUnmarried(
                        afterInsurance))
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateUnmarried(afterInsurance) - 0.5 * self.calculateUnmarried(afterInsurance)

        # --for male with no disabilities:
        if self.disability_status.get() == "Natural Person" and self.gender.get() == "male":
            if self.maritalStatus.get() == "married":
                if self.diplomatic_employee.get() == "yes":
                    tax = self.calculateMarried(afterInsurance) - 0.75 * self.calculateMarried(afterInsurance)
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateMarried(afterInsurance)

            if self.maritalStatus.get() == "unmarried":
                if self.diplomatic_employee.get() == "yes":
                    tax = self.calculateUnmarried(afterInsurance) - 0.75 * self.calculateUnmarried(afterInsurance)
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateUnmarried(afterInsurance)

        # --for female with no disabilities:
        if self.disability_status.get() == "Natural Person" and self.gender.get() == "female":
            if self.maritalStatus.get() == "married":
                if self.diplomatic_employee.get() == "yes":
                    tax = self.calculateMarried(afterInsurance) - (
                            0.1 * self.calculateMarried(afterInsurance) + 0.75 * self.calculateMarried(
                        afterInsurance))
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateMarried(afterInsurance) - 0.1 * self.calculateMarried(afterInsurance)

            if self.maritalStatus.get() == "unmarried":
                if self.diplomatic_employee.get() == "yes":
                    tax = self.calculateUnmarried(afterInsurance) - (
                            0.75 * self.calculateUnmarried(afterInsurance) + 0.1 * self.calculateUnmarried(
                        afterInsurance))
                if self.diplomatic_employee.get() == "no":
                    tax = self.calculateUnmarried(afterInsurance) - self.calculateUnmarried(
                        afterInsurance) + 0.1 * self.calculateUnmarried(afterInsurance)
        return tax

    def useDb(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="ird"
        )

        myCursor = mydb.cursor()
        myCursor.execute("INSERT INTO tax_calculations (Name,Address,Age,Income,Marital_status,Disability_status,"
                         "Diplomatic_employee,Gender,Insurance,Tax_Income,date_time) VALUES('{}','{}', "
                         "{},{},'{}','{}','{}','{}','{}',{},'{}'); ".format(self.name.get(), self.address.get(),
                                                                            self.age.get(),
                                                                            self.income.get(), self.maritalStatus.get(),
                                                                            self.disability_status.get(),
                                                                            self.diplomatic_employee.get(),
                                                                            self.gender.get(), self.insurance.get(),
                                                                            self.tax_income, self.dateTime))
        mydb.commit()

    def giveInfo(self):
        popUp = Toplevel(self.root)
        popUp.title("Confirmation")
        popUp.geometry("300x150")
        Label(popUp, text="Data Stored Successfully!", height=4).pack()
        Button(popUp, command=popUp.destroy, text="Okay", bg="#00AB66", width=14, fg="LIGHT GREEN").pack()

    def details(self):
        self.tax_income = self.calculateTax()
        self.useDb()
        self.textarea.insert(END, "---------------------------------------------------------------------\n")
        self.textarea.insert(END, "\t\t Income Tax Calculation System\n")
        self.textarea.insert(END, "\t\t\tLazimpat,Kathmandu\n")
        self.textarea.insert(END, f"\t\tDatetime:{self.dateTime}\n")
        self.textarea.insert(END, "---------------------------------------------------------------------\n")
        self.textarea.insert(END, "\t\tWelcome to the Income Tax Calculation System\n")
        self.textarea.insert(END, "---------------------------------------------------------------------\n")
        self.textarea.insert(END, f"Name:{self.name.get()}\n")
        self.textarea.insert(END, f"Age:{self.age.get()}\n")
        self.textarea.insert(END, f"Address:{self.address.get()}\n")
        self.textarea.insert(END, f"Income:{self.income.get()}\n")
        self.textarea.insert(END, f"Disability status:{self.disability_status.get()}\n")
        self.textarea.insert(END, f"Diplomatic employed:{self.diplomatic_employee.get()}\n")
        self.textarea.insert(END, f"Marital status:{self.maritalStatus.get()}\n")
        self.textarea.insert(END, f"Gender:{self.gender.get()}\n")
        self.textarea.insert(END, f"Insurance:{self.insurance.get()}\n")
        self.textarea.insert(END, f"Tax Income:{self.tax_income}\n")
        self.giveInfo()

    def clear(self):
        self.cname_text.delete(0, END)
        self.cage_text.delete(0, END)
        self.caddress_text.delete(0, END)
        self.income_text.delete(0, END)
        self.unmarriedButton.deselect()
        self.marriedButton.deselect()
        self.income_text.delete(0, END)
        self.yesButton.deselect()
        self.noButton.deselect()
        self.male.deselect()
        self.female.deselect()
        self.uninsured.deselect()
        self.insured.deselect()


def main():
    root = Tk()
    irdApp = Ird_App(root)
    photoImage = ImageTk.PhotoImage(Image.open("C:/Users/Sm/Desktop/python db tutorials/ird.png"))
    photoLabel = Label(image=photoImage)
    photoLabel.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
