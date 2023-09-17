from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital management Software")
        self.root.geometry("1540x800+0+0")

        
        self.Nameoftables=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.StorageAdvice=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()



        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="+ HOSPITAL MANAGEMENT SOFTWARE +",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # =========================== Data Fram ==============================================
        Datafram=Frame(self.root,bd=20,relief=RIDGE)
        Datafram.place(x=0,y=130,width=1530,height=400)

        DataframLeft=LabelFrame(Datafram,bd=10,relief=RIDGE,padx=10,
                                        font=("time new roman",12,"bold"),text="Patient Information")
        DataframLeft.place(x=0,y=5,width=980,height=350)

        DataframRight=LabelFrame(Datafram,bd=10,relief=RIDGE,padx=10,
                                        font=("time new roman",12,"bold"),text="Prescription")
        DataframRight.place(x=990,y=5,width=460,height=350)

        # ================================= Button Frame ========================   
 
        Buttonfram=Frame(self.root,bd=20,relief=RIDGE)
        Buttonfram.place(x=0,y=530,width=1530,height=70)

        # ================================= Details Frame ========================   
   
        Detailsfram=Frame(self.root,bd=20,relief=RIDGE)
        Detailsfram.place(x=0,y=600,width=1530,height=190)

        #====================================DataFrameLeft ===================================

        lblNameTablet=Label(DataframLeft,text="Names OF Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(DataframLeft,textvariable=self.Nameoftables,state="readonly",
                                                        font=("arial",12,"bold"),width=33)
        comNameTablet["values"]=("Nice","Corona Vacacina","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataframLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.Numberoftablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)
      
        lblDailyDose=Label(DataframLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)
      
        lblSideEffect=Label(DataframLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)
        
        lblNhsNumber=Label(DataframLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)


       
        # ========================== DataFrame Right ====================================
        self.txtPrescription=Text(DataframRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        #============================Buttons ===============================================
        
        btntxtPrescriptionData=Button(Buttonfram,command=self.iprectioption,text="Prescription ",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btntxtPrescriptionData.grid(row=0,column=0)
        
        btntxtPrescriptionData=Button(Buttonfram,text="Prescription Data",command=self.iPrescription_data,font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btntxtPrescriptionData.grid(row=0,column=1)


        btntUpdate=Button(Buttonfram,command=self.update_data,text="Update",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btntUpdate.grid(row=0,column=2)


        btnDelete=Button(Buttonfram,command=self.idelete,text="Delete",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnDelete.grid(row=0,column=3)


        btnClear=Button(Buttonfram,command=self.clear,text="Clear",font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonfram,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnExit.grid(row=0,column=5)

        # ================================== Table ===================================
        # ======================Scrolbar ========================
        scroll_x=ttk.Scrollbar(Detailsfram,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsfram,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsfram,columns=("Nameoftables","ref","dose","nooftablets","lot","issuedate",
                                      "expdate","dailydose","sideEfect","FurtherInformation","DrivingUsingMachine","storage","HowToUseMedication","PatientId","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack( side = BOTTOM, fill = X )
        scroll_y.pack( side = RIGHT, fill = Y )

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Nameoftables",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No.")         
        self.hospital_table.heading("dose",text="Dose")         
        self.hospital_table.heading("nooftablets",text="No Of Tablets")         
        self.hospital_table.heading("lot",text="Lot")         
        self.hospital_table.heading("issuedate",text="Issue Date")         
        self.hospital_table.heading("expdate",text="Exp Date")         
        self.hospital_table.heading("dailydose",text="Daily Dose")  
        self.hospital_table.heading("sideEfect",text="Side Eff.")
        self.hospital_table.heading("FurtherInformation",text="Further Info")
        self.hospital_table.heading("DrivingUsingMachine",text="Blood pres.")
        self.hospital_table.heading("storage",text="Storage") 
        self.hospital_table.heading("HowToUseMedication",text="Medication")
        self.hospital_table.heading("PatientId",text="PatientId")        
        self.hospital_table.heading("nhsnumber",text="NHS Number") 
        self.hospital_table.heading("pname",text="Patient Name")         
        self.hospital_table.heading("dob",text="DOB")         
        self.hospital_table.heading("address",text="Address")         
       
        self.hospital_table["show"]="headings"       



        self.hospital_table.column("Nameoftables",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("sideEfect",width=100)
        self.hospital_table.column("FurtherInformation",width=100)
        self.hospital_table.column("DrivingUsingMachine",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("HowToUseMedication",width=100) 
        self.hospital_table.column("PatientId",width=100)         
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()
        
     # ====================================Functinality Declartion ========================================================
    def iPrescription_data(self):
        if self.Nameoftables.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftables.get(),
                                                                                                                    self.ref.get(),
                                                                                                                    self.Dose.get(),
                                                                                                                    self.Numberoftablets.get(),
                                                                                                                    self.Lot.get(),
                                                                                                                    self.Issuedate.get(),
                                                                                                                    self.ExpDate.get(),
                                                                                                                    self.DailyDose.get(),
                                                                                                                    self.sideEfect.get(),
                                                                                                                    self.FurtherInformation.get(),
                                                                                                                    self.DrivingUsingMachine.get(),
                                                                                                                    self.StorageAdvice.get(),
                                                                                                                    self.HowToUseMedication.get(),
                                                                                                                    self.PatientId.get(),
                                                                                                                    self.nhsNumber.get(),
                                                                                                                    self.PatientName.get(),
                                                                                                                    self.DateOfBirth.get(),
                                                                                                                    self.PatientAddress.get()))
            conn.commit()
            conn.close() 
            self.fatch_data()
            messagebox.showinfo("Success","Record has ben inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftables=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,sideEfect=%s,FurtherInformation=%s,DrivingUsingMachine=%s,storage=%s,HowToUseMedication=%s,Patientid=%s,nhsnumber=%s,PatientName=%s,DateOfBirth=%s,patientaddress=%s where Reference_No=%s",(self.Nameoftables.get(),
                                                                                                                                                                                                                                                                                                                                self.Dose.get(),
                                                                                                                                                                                                                                                                                                                                self.Numberoftablets.get(),
                                                                                                                                                                                                                                                                                                                                self.Lot.get(),
                                                                                                                                                                                                                                                                                                                                self.Issuedate.get(),
                                                                                                                                                                                                                                                                                                                                self.ExpDate.get(),
                                                                                                                                                                                                                                                                                                                                self.DailyDose.get(),
                                                                                                                                                                                                                                                                                                                                self.sideEfect.get(),
                                                                                                                                                                                                                                                                                                                                self.FurtherInformation.get(),
                                                                                                                                                                                                                                                                                                                                self.DrivingUsingMachine.get(),
                                                                                                                                                                                                                                                                                                                                self.StorageAdvice.get(),
                                                                                                                                                                                                                                                                                                                                self.HowToUseMedication.get(),
                                                                                                                                                                                                                                                                                                                                self.PatientId.get(),
                                                                                                                                                                                                                                                                                                                                self.nhsNumber.get(),
                                                                                                                                                                                                                                                                                                                                self.PatientName.get(),
                                                                                                                                                                                                                                                                                                                                self.DateOfBirth.get(),
                                                                                                                                                                                                                                                                                                                                self.PatientAddress.get(),
                                                                                                                                                                                                                                                                                                                                self.ref.get(),
                                                                                                                                                                                                                                                                                                                                 ))
        conn.commit()
        self.fatch_data()
        conn.close() 
        messagebox.showinfo("Success","Record has ben Updating")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                             self.hospital_table.insert("",END,values=row)
            conn.commit()
        conn.close()

    def get_cursor(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftables.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Numberoftablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.sideEfect.set(row[8])
        self.FurtherInformation.set(row[9])
        self.DrivingUsingMachine.set(row[10])
        self.StorageAdvice.set(row[11])
        self.HowToUseMedication.set(row[12])
        self.PatientId.set(row[13])
        self.nhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DateOfBirth.set(row[16])
        self.PatientAddress.set(row[17])

    def iprectioption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftables.get() + "\n")
        self.txtPrescription.insert(END,"Reference No.:\t\t\t"+self.ref.get() + "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get() + "\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.Numberoftablets.get() + "\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"Issuedate:\t\t\t"+self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END,"Expired Date:\t\t\t"+self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEfect.get() + "\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END,"Medication:\t\t\t"+self.HowToUseMedication.get() + "\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get() + "\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"Date Of Birth:\t\t\t"+self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get() + "\n")


    def idelete(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="Mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been Deleted Successfuly")


    def clear(self):
        self.Nameoftables.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.DrivingUsingMachine.set("")
        self.StorageAdvice.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")


    def iExit(self):
        iExit=messagebox.askyesno("Hospital Managemtnt Softwaer","Confirm You Want To Exit")
        if iExit>0:
            root.destroy()
            return

root = Tk()
obj =Hospital(root)
root.mainloop()




