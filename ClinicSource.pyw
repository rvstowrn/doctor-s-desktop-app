import sqlite3
from tkinter import *
from tkinter import messagebox
import tempfile
import win32api
import win32print

conn = sqlite3.connect("clinic.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS clinic (name TEXT,date TEXT,age TEXT,sex TEXT,disease TEXT,prescription TEXT,side TEXT)")
conn.commit()


def search():
  n=name_text.get()
  d=date_text.get()
  di=disease_text.get()
  cur.execute("SELECT * FROM clinic WHERE name=? OR date=? OR disease=?", (n,d,di))
  rows = cur.fetchall()
  #e0.insert('end',rows[0][0])
  e1.insert('end',rows[0][1])
  e2.insert('end',rows[0][2])
  e3.insert('end',rows[0][3])
  e4.insert('end',rows[0][4])  
  s=rows[0][5]
  str=s.split('|',20)
  try:
     e5.insert('end',str[0])
     e6.insert('end',str[1])
     e7.insert('end',str[2])
     e8.insert('end',str[3])
     e9.insert('end',str[4])
     e10.insert('end',str[5])
     e11.insert('end',str[6])
     e12.insert('end',str[7])
     e13.insert('end',str[8])
     e14.insert('end',str[9])
     e15.insert('end',str[10])
     e16.insert('end',str[11])
     e17.insert('end',str[12])
     e18.insert('end',str[13])
  finally:
     s=rows[0][6]
     str=s.split('|',20)
     e19.insert('end',str[0])
     e20.insert('end',str[1])
     e21.insert('end',str[2])
     e22.insert('end',str[3])

  
def insert():
  n=name_text.get()
  d=date_text.get()
  a=age_text.get()
  s=sex_text.get()
  di=disease_text.get()
  p1=prescription_text1.get()
  p2=prescription_text2.get() 
  p3=prescription_text3.get()
  p4=prescription_text4.get()
  p5=prescription_text5.get()
  p6=prescription_text6.get()
  p7=prescription_text7.get()
  p8=prescription_text8.get()
  p9=prescription_text9.get()
  p10=prescription_text10.get()
  p11=prescription_text11.get()
  p12=prescription_text12.get()
  p13=prescription_text13.get()
  p14=prescription_text14.get()
  s1=side_text1.get()
  s2=side_text2.get()
  s3=side_text3.get()
  s4=side_text4.get()
  p=p1+'|'+p2+'|'+p3+'|'+p4+'|'+p5+'|'+p6+'|'+p7+'|'+p8+'|'+p9+'|'+p10+'|'+p11+'|'+p12+'|'+p13+'|'+p14
  sn=s1+'|'+s2+'|'+s3+'|'+s4
  cur.execute("INSERT INTO clinic VALUES (?,?,?,?,?,?,?)", (n,d,a,s,di,p,sn))
  conn.commit()
  e0.delete(0, 'end')
  e1.delete(0, 'end')
  e2.delete(0, 'end')
  e3.delete(0, 'end')
  e4.delete(0, 'end')
  e5.delete(0, 'end')
  e6.delete(0, 'end')
  e7.delete(0, 'end')
  e8.delete(0, 'end')
  e9.delete(0, 'end')
  e10.delete(0, 'end')
  e11.delete(0, 'end')
  e12.delete(0, 'end')
  e13.delete(0, 'end')
  e14.delete(0, 'end')
  e15.delete(0, 'end')
  e16.delete(0, 'end')
  e17.delete(0, 'end')
  e18.delete(0, 'end')
  e19.delete(0, 'end')
  e20.delete(0, 'end')
  e21.delete(0, 'end')
  e22.delete(0, 'end')
        
def update():
  n=name_text.get()
  d=date_text.get()
  a=age_text.get()
  s=sex_text.get()
  di=disease_text.get()
  p1=prescription_text1.get()
  p2=prescription_text2.get() 
  p3=prescription_text3.get()
  p4=prescription_text4.get()
  p5=prescription_text5.get()
  p6=prescription_text6.get()
  p7=prescription_text7.get()
  p8=prescription_text8.get()
  p9=prescription_text9.get()
  p10=prescription_text10.get()
  p11=prescription_text11.get()
  p12=prescription_text12.get()
  p13=prescription_text13.get()
  p14=prescription_text14.get()
  s1=side_text1.get()
  s2=side_text2.get()
  s3=side_text3.get()
  s4=side_text4.get()
  p=p1+'|'+p2+'|'+p3+'|'+p4+'|'+p5+'|'+p6+'|'+p7+'|'+p8+'|'+p9+'|'+p10+'|'+p11+'|'+p12+'|'+p13+'|'+p14
  sn=s1+'|'+s2+'|'+s3+'|'+s4
  cur.execute("UPDATE clinic SET date=?,age=?,sex=?,disease=?,prescription=?,side=? WHERE name=?", (d,a,s,di,p,sn,n))
  conn.commit()
  e0.delete(0, 'end')
  e1.delete(0, 'end')
  e2.delete(0, 'end')
  e3.delete(0, 'end')
  e4.delete(0, 'end')
  e5.delete(0, 'end')
  e6.delete(0, 'end')
  e7.delete(0, 'end')
  e8.delete(0, 'end')
  e9.delete(0, 'end')
  e10.delete(0, 'end')
  e11.delete(0, 'end')
  e12.delete(0, 'end')
  e13.delete(0, 'end')
  e14.delete(0, 'end')
  e15.delete(0, 'end')
  e16.delete(0, 'end')
  e17.delete(0, 'end')
  e18.delete(0, 'end')
  e19.delete(0, 'end')
  e20.delete(0, 'end')
  e21.delete(0, 'end')
  e22.delete(0, 'end')

def delete():
  n=name_text.get()
  d=date_text.get()
  cur.execute("DELETE FROM clinic WHERE name=? OR date=?", (n, d))
  conn.commit()
  e0.delete(0, 'end')
  e1.delete(0, 'end')
  e2.delete(0, 'end')
  e3.delete(0, 'end')
  e4.delete(0, 'end')
  e5.delete(0, 'end')
  e6.delete(0, 'end')
  e7.delete(0, 'end')
  e8.delete(0, 'end')
  e9.delete(0, 'end')
  e10.delete(0, 'end')
  e11.delete(0, 'end')
  e12.delete(0, 'end')
  e13.delete(0, 'end')
  e14.delete(0, 'end')
  e15.delete(0, 'end')
  e16.delete(0, 'end')
  e17.delete(0, 'end')
  e18.delete(0, 'end')
  e19.delete(0, 'end')
  e20.delete(0, 'end')
  e21.delete(0, 'end')
  e22.delete(0, 'end')
  
def printrn1():
  n=name_text.get()
  fname=n+'-A4.html'
  f = open(fname,'w')
  d=date_text.get()
  a=age_text.get()
  s=sex_text.get()
  di=disease_text.get()
  p1=prescription_text1.get()
  p2=prescription_text2.get() 
  p3=prescription_text3.get()
  p4=prescription_text4.get()
  p5=prescription_text5.get()
  p6=prescription_text6.get()
  p7=prescription_text7.get()
  p8=prescription_text8.get()
  p9=prescription_text9.get()
  p10=prescription_text10.get()
  p11=prescription_text11.get()
  p12=prescription_text12.get()
  p13=prescription_text13.get()
  p14=prescription_text14.get()
  if len(p1)!=0:
     if p1[1]!='.':  
        p1="  "+p1
  if len(p2)!=0:
     if p2[1]!='.' :
        p2="  "+p2
  if len(p3)!=0:
     if p3[1]!='.': 
        p3="  "+p3
  if len(p4)!=0:
     if p4[1]!='.': 
        p4="  "+p4
  if len(p5)!=0:
     if p5[1]!='.': 
        p5="  "+p5
  if len(p6)!=0:
     if p6[1]!='.': 
        p6="  "+p6
  if len(p7)!=0:
     if p7[1]!='.': 
        p7="  "+p7
  if len(p8)!=0:
     if p8[1]!='.': 
        p8="  "+p8
  if len(p9)!=0:
     if p9[1]!='.': 
        p9="  "+p9
  if len(p10)!=0:
     if p10[1]!='.': 
        p10="  "+p10
  if len(p11)!=0:
     if p11[1]!='.': 
        p11="  "+p11
  if len(p12)!=0:
     if p12[1]!='.':
        p12="  "+p12
  if len(p13)!=0:
     if p13[1]!='.': 
        p13="  "+p13
  if len(p14)!=0:
     if p14[1]!='.': 
        p14="  "+p14
   
    
  n=n[::-1]
  n1='{:>22}'.format(n)
  n=n1[::-1]
  s1=side_text1.get()
  s1=s1[::-1]
  s2=side_text2.get()
  s2=s2[::-1]
  s3=side_text3.get()
  s3=s3[::-1]
  s4=side_text4.get()
  s4=s4[::-1]
  s11='{:>15}'.format(s1)
  s1=s11[::-1]
  s22='{:>15}'.format(s2)
  s2=s22[::-1]
  s33='{:>15}'.format(s3)
  s3=s33[::-1]              
  s44='{:>15}'.format(s4)
  s4=s44[::-1]
  s5="""               """
  s6="""        """
  message =""" <!DOCTYPE html>
  <html>
  <head>
  <title>new</title>
  <style type="text/css">
  html,body
  {
    font-size: 150%;
    font-family: cursive;
    color: blue;
  }
  .ee
  {
    font-size: 200%;
  }
  .dark
  {
    font-weight: bold;
  }
  .b
  {
    border: solid 3px;
  }
  .bb
  {
   font-size: 160%;
   font-weight:bold;
  }
  .data
  {
  font-size: 170%;
  font-weight: bold;
  }
  </style>
  </head>
  <body>
  <pre>
                                 <span class="b"> I Treat He Cures </span>


   <span class='ee'> Dr S.K. Das</span>                               <span class='bb'>VERMA HOMOEO CLINIC</span>      
              D.H.M.S.(BU),                               MIG-54,Hanuman Nagar 
     M.D.E.H.(KNP),ND(LKO),                               Kankarbagh,Patna -800020  
   Experienced in chronic &                                               
      complicated diseases,                               CONSULTING HOURS
    Regd:Central council of                               9.00 A.M. to 12.00 P.M.
     Homoeopathy(New Delhi)                               5.30 P.M. to 08.30 P.M.
                                                          Contact No-
   <span class='ee'>Dr D.C.Verma</span>                               9835050075
              D.B.M.S.(Cal)                               9771417464
                                                         <span class="dark"> Sunday Closed</span>
  
        <p id='data'>"""+s5+s6+"""Name:"""+n+s6+"""Age:"""+a+"""  Sex:"""+s+"""</p> 


                        <img src='rx.png' width=2%>
                       
  """+s1+"""          """+p1+"""
  """+s2+"""          """+p2+"""
  """+s3+"""          """+p3+"""
  """+s4+"""          """+p4+"""
  """+s5+"""          """+p5+"""
  """+s5+"""          """+p6+"""
  """+s5+"""          """+p7+"""
  """+s5+"""          """+p8+"""
  """+s5+"""          """+p9+"""
  """+s5+"""          """+p10+"""
  """+s5+"""          """+p11+"""
  """+s5+"""          """+p12+"""
  """+s5+"""          """+p13+"""
  """+s5+"""          """+p14+"""
  </pre>
  </body>
  </html>"""
  f.write(message)
  f.close()
  '''
  n=name_text.get()
  d=date_text.get()
  p=e3.get("1.0",'end')
  s="\t\t\tI Treat He Cures\nDr.S.K. Das\t\tVerma Homeo clinicmg\n"+"\n\n\n\n"+n+"\n\n"+d+"\t\t" + p
  filename = tempfile.mktemp (".txt")
  open (filename, "w").write (s)
  win32api.ShellExecute (
  0,
  "printto",
  filename,
  '"%s"' % win32print.GetDefaultPrinter (),
  ".",
  0
  )'''

def printrn2():
  n=name_text.get()
  fname=n+'-A5.html'
  f = open(fname,'w')
  d=date_text.get()
  a=age_text.get()
  s=sex_text.get()
  di=disease_text.get()
  p1=prescription_text1.get()
  p2=prescription_text2.get() 
  p3=prescription_text3.get()
  p4=prescription_text4.get()
  p5=prescription_text5.get()
  p6=prescription_text6.get()
  p7=prescription_text7.get()
  p8=prescription_text8.get()
  p9=prescription_text9.get()
  p10=prescription_text10.get()
  p11=prescription_text11.get()
  p12=prescription_text12.get()
  p13=prescription_text13.get()
  p14=prescription_text14.get()
  if len(p1)!=0:
     if p1[1]!='.':  
        p1="  "+p1
  if len(p2)!=0:
     if p2[1]!='.' :
        p2="  "+p2
  if len(p3)!=0:
     if p3[1]!='.': 
        p3="  "+p3
  if len(p4)!=0:
     if p4[1]!='.': 
        p4="  "+p4
  if len(p5)!=0:
     if p5[1]!='.': 
        p5="  "+p5
  if len(p6)!=0:
     if p6[1]!='.': 
        p6="  "+p6
  if len(p7)!=0:
     if p7[1]!='.': 
        p7="  "+p7
  if len(p8)!=0:
     if p8[1]!='.': 
        p8="  "+p8
  if len(p9)!=0:
     if p9[1]!='.': 
        p9="  "+p9
  if len(p10)!=0:
     if p10[1]!='.': 
        p10="  "+p10
  if len(p11)!=0:
     if p11[1]!='.': 
        p11="  "+p11
  if len(p12)!=0:
     if p12[1]!='.':
        p12="  "+p12
  if len(p13)!=0:
     if p13[1]!='.': 
        p13="  "+p13
  if len(p14)!=0:
     if p14[1]!='.': 
        p14="  "+p14
    
  n=n[::-1]
  n1='{:>17}'.format(n)
  n=n1[::-1]
  s1=side_text1.get()
  s1=s1[::-1]
  s2=side_text2.get()
  s2=s2[::-1]
  s3=side_text3.get()
  s3=s3[::-1]
  s4=side_text4.get()
  s4=s4[::-1]
  s11='{:>15}'.format(s1)
  s1=s11[::-1]
  s22='{:>15}'.format(s2)
  s2=s22[::-1]
  s33='{:>15}'.format(s3)
  s3=s33[::-1]              
  s44='{:>15}'.format(s4)
  s4=s44[::-1]
  s5="""               """
  s6="""        """
  message =""" <!DOCTYPE html>
  <html>
  <head>
  <title>new</title>
  <style type="text/css">
  html,body
  {
    font-size: 100%;
    font-family: cursive;
    color: blue;
  }
  .ee
  {
    font-size: 200%;
  }
  .dark
  {
    font-weight: bold;
  }
  .b
  {
    border: solid 3px;
  }
  .bb
  {
   font-size: 160%;
   font-weight:bold;
  }
  .data
  {
  font-size: 170%;
  }
  </style>
  </head>
  <body>
  <pre>
                                 <span class="b"> I Treat He Cures </span>


   <span class='ee'> Dr S.K. Das</span>                               <span class='bb'>VERMA HOMOEO CLINIC</span>      
              D.H.M.S.(BU),                               MIG-54,Hanuman Nagar 
     M.D.E.H.(KNP),ND(LKO),                               Kankarbagh,Patna -800020  
   Experienced in chronic &                                               
      complicated diseases,                               CONSULTING HOURS
    Regd:Central council of                               9.00 A.M. to 12.00 P.M.
     Homoeopathy(New Delhi)                               5.30 P.M. to 08.30 P.M.
                                                          Contact No-
   <span class='ee'>Dr D.C.Verma</span>                               9835050075
              D.B.M.S.(Cal)                               9771417464
                                                         <span class="dark"> Sunday Closed</span>
  <pre class='data'>
            Name:"""+n+"""Age:"""+a+"""  Sex:"""+s+"""


                <img src='rx.png' width=3%>
                       
  """+s1+""" """+p1+"""
  """+s2+""" """+p2+"""
  """+s3+""" """+p3+"""
  """+s4+""" """+p4+"""
  """+s5+""" """+p5+"""
  """+s5+""" """+p6+"""
  """+s5+""" """+p7+"""
  """+s5+""" """+p8+"""
  """+s5+""" """+p9+"""
  """+s5+""" """+p10+"""
  """+s5+""" """+p11+"""
  """+s5+""" """+p12+"""
  """+s5+""" """+p13+"""
  """+s5+""" """+p14+"""       
  </pre>    
  </pre>
  </body>
  </html>"""
  f.write(message)
  f.close()
  '''
  n=name_text.get()
  d=date_text.get()
  p=e3.get("1.0",'end')
  s="\t\t\tI Treat He Cures\nDr.S.K. Das\t\tVerma Homeo clinicmg\n"+"\n\n\n\n"+n+"\n\n"+d+"\t\t" + p
  filename = tempfile.mktemp (".txt")
  open (filename, "w").write (s)
  win32api.ShellExecute (
  0,
  "printto",
  filename,
  '"%s"' % win32print.GetDefaultPrinter (),
  ".",
  0
  )'''


window = Tk()
window.title("Clinic Manager")
window.geometry('680x400')
l1 = Label(window, text="Name")
l2 = Label(window, text="Date")
l3 = Label(window, text="Age")
l4 = Label(window, text="Sex")
l5 = Label(window, text="Disease")
l6 = Label(window, text="Prescription")
l7 = Label(window, text="Side Note")
l8 = Label(window, text="Possible")
l9 = Label(window, text="Operations")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)
l5.grid(row=4, column=0)
l6.grid(row=0, column=2)
l7.grid(row=0, column=4)
l8.grid(row=14,column=0)
l9.grid(row=15,column=0)

name_text = StringVar()
e0 = Entry(window, textvariable=name_text)
e0.grid(row=0, column=1)

date_text = StringVar()
e1 = Entry(window, textvariable=date_text)
e1.grid(row=1, column=1)

age_text = StringVar()
e2 = Entry(window, textvariable=age_text)
e2.grid(row=2, column=1)

sex_text = StringVar()
e3 = Entry(window, textvariable=sex_text)
e3.grid(row=3, column=1)

disease_text = StringVar()
e4 = Entry(window, textvariable=disease_text)
e4.grid(row=4, column=1)

prescription_text1 = StringVar()
e5 = Entry(window, textvariable=prescription_text1)
e5.grid(row=0, column=3)

prescription_text2 = StringVar()
e6 = Entry(window, textvariable=prescription_text2)
e6.grid(row=1, column=3)

prescription_text3 = StringVar()
e7 = Entry(window, textvariable=prescription_text3)
e7.grid(row=2, column=3)

prescription_text4 = StringVar()
e8 = Entry(window, textvariable=prescription_text4)
e8.grid(row=3, column=3)

prescription_text5 = StringVar()
e9 = Entry(window, textvariable=prescription_text5)
e9.grid(row=4, column=3)

prescription_text6 = StringVar()
e10 = Entry(window, textvariable=prescription_text6)
e10.grid(row=5, column=3)

prescription_text7 = StringVar()
e11 = Entry(window, textvariable=prescription_text7)
e11.grid(row=6, column=3)

prescription_text8 = StringVar()
e12 = Entry(window, textvariable=prescription_text8)
e12.grid(row=7, column=3)

prescription_text9 = StringVar()
e13 = Entry(window, textvariable=prescription_text9)
e13.grid(row=8, column=3)

prescription_text10 = StringVar()
e14 = Entry(window, textvariable=prescription_text10)
e14.grid(row=9, column=3)

prescription_text11 = StringVar()
e15 = Entry(window, textvariable=prescription_text11)
e15.grid(row=10, column=3)

prescription_text12 = StringVar()
e16 = Entry(window, textvariable=prescription_text12)
e16.grid(row=11, column=3)

prescription_text13 = StringVar()
e17 = Entry(window, textvariable=prescription_text13)
e17.grid(row=12, column=3)

prescription_text14 = StringVar()
e18 = Entry(window, textvariable=prescription_text14)
e18.grid(row=13, column=3)

side_text1 = StringVar()
e19 = Entry(window, textvariable=side_text1)
e19.grid(row=0, column=5)

side_text2 = StringVar()
e20 = Entry(window, textvariable=side_text2)
e20.grid(row=1, column=5)

side_text3 = StringVar()
e21 = Entry(window, textvariable=side_text3)
e21.grid(row=2, column=5)

side_text4 = StringVar()
e22 = Entry(window, textvariable=side_text4)
e22.grid(row=3, column=5)

b1 = Button(window, text="Search", width=12, command=search)
b1.grid(row=16, column=0)

b2 = Button(window, text="Add", width=12, command=insert)
b2.grid(row=16, column=1)

b3 = Button(window, text="Update", width=12, command=update)
b3.grid(row=16, column=2)

b4 = Button(window, text="Delete", width=12, command=delete)
b4.grid(row=16, column=3)

b5 = Button(window, text="Create A4", width=12, command=printrn1)
b5.grid(row=16, column=4)

b6 = Button(window, text="Create A5", width=12, command=printrn2)
b6.grid(row=16, column=5)



window.mainloop()
