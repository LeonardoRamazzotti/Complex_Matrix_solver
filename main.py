from tkinter import *
import math
import cmath
import numpy

def det_solve(matrice):
    res = round(numpy.linalg.det(matrice),2)
    print(res)
    return res     

def matrix_composition():
    r1c1 = matrix_entry_1.get()
    r1c2 = matrix_entry_2.get()
    r1c3 = matrix_entry_3.get()
    r1c4 = matrix_entry_4.get()
    r1c5 = matrix_entry_5.get()
    r1c6 = matrix_entry_6.get()
    r2c1 = matrix_entry_7.get()
    r2c2 = matrix_entry_8.get()
    r2c3 = matrix_entry_9.get()
    r2c4 = matrix_entry_10.get()
    r2c5 = matrix_entry_11.get()
    r2c6 = matrix_entry_12.get()
    r3c1 = matrix_entry_13.get()
    r3c2 = matrix_entry_14.get()
    r3c3 = matrix_entry_15.get()
    r3c4 = matrix_entry_16.get()
    r3c5 = matrix_entry_17.get()
    r3c6 = matrix_entry_18.get()
    r4c1 = matrix_entry_19.get()
    r4c2 = matrix_entry_20.get()
    r4c3 = matrix_entry_21.get()
    r4c4 = matrix_entry_22.get()
    r4c5 = matrix_entry_23.get()
    r4c6 = matrix_entry_24.get()
    r5c1 = matrix_entry_25.get()
    r5c2 = matrix_entry_26.get()
    r5c3 = matrix_entry_27.get()
    r5c4 = matrix_entry_28.get()
    r5c5 = matrix_entry_29.get()
    r5c6 = matrix_entry_30.get()
    r6c1 = matrix_entry_31.get()
    r6c2 = matrix_entry_32.get()
    r6c3 = matrix_entry_33.get()
    r6c4 = matrix_entry_34.get()
    r6c5 = matrix_entry_35.get()
    r6c6 = matrix_entry_36.get()

    list_matrix = [[r1c1,r1c2,r1c3,r1c4,r1c5,r1c6],[r2c1,r2c2,r2c3,r2c4,r2c5,r2c6],[r3c1,r3c2,r3c3,r3c4,r3c5,r3c6],[r4c1,r4c2,r4c3,r4c4,r4c5,r4c6],[r5c1,r5c2,r5c3,r5c4,r5c5,r5c6],[r6c1,r6c2,r6c3,r6c4,r6c5,r6c6]]
    
    
    
    for row in list_matrix:
        for index, element in enumerate(row):
            if len(element) > 0:
            
                row[index] = complex(element)
            #else :
            #    row[index] = 0
           
    for row in list_matrix:
        i=0
        while i <len(row):
            
             if row[i] == '':
                row.pop(i)
                
             else:   
                 i+=1
                 
    while i < len(list_matrix):
        if len(list_matrix[i]) == 0:
            
            list_matrix.pop(i)
        else:
            i+=1
            
                
    matrix = numpy.array(list_matrix)
    
    label_matrix = Label(root,text = matrix) # manca il posizionamento 
    
    determinante = det_solve(matrix)
    
    result_label = Label(root,text=determinante, font = font_1)
    result_label.place(x=650,y=700)
    

root = Tk()
root.title('Matrix Solver')
root.geometry('720x800')
root.resizable(False, False)
# Font Section=====================================================================

font_1 = ('Roboto Condenser',12)



#End Font Section=====================================================================
#Image Section =======================================================================

bg_image = PhotoImage(file = 'bg.png')
solve = PhotoImage(file='solve.png')


#End Image Section =======================================================================

bg_label = Label(root,image = bg_image)
bg_label.pack()


#Entry Section (grid layout)====================================================

matrix_entry_1 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_1.place(x=55,y=121)

matrix_entry_2 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_2.place(x=164,y=121)

matrix_entry_3 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_3.place(x=273,y=121)

matrix_entry_4 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_4.place(x=382,y=121)

matrix_entry_5 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_5.place(x=491,y=121)

matrix_entry_6 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_6.place(x=600,y=121)

matrix_entry_7 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_7.place(x=55,y=168)

matrix_entry_8 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_8.place(x=164,y=168)

matrix_entry_9 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_9.place(x=273,y=168)

matrix_entry_10 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_10.place(x=382,y=168)

matrix_entry_11 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_11.place(x=491,y=168)

matrix_entry_12 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_12.place(x=600,y=168)

matrix_entry_13 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_13.place(x=55,y=216)

matrix_entry_14 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_14.place(x=164,y=216)

matrix_entry_15 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_15.place(x=273,y=216)

matrix_entry_16 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_16.place(x=382,y=216)

matrix_entry_17 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_17.place(x=491,y=216)

matrix_entry_18 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_18.place(x=600,y=216)

matrix_entry_19 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_19.place(x=55,y=264)

matrix_entry_20 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_20.place(x=164,y=264)

matrix_entry_21 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_21.place(x=273,y=264)

matrix_entry_22 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_22.place(x=382,y=264)

matrix_entry_23 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_23.place(x=491,y=264)

matrix_entry_24 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_24.place(x=600,y=264)

matrix_entry_25 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_25.place(x=55,y=312)

matrix_entry_26 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_26.place(x=164,y=312)

matrix_entry_27 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_27.place(x=273,y=312)

matrix_entry_28 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_28.place(x=382,y=312)

matrix_entry_29 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_29.place(x=491,y=312)

matrix_entry_30 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_30.place(x=600,y=312)

matrix_entry_31 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_31.place(x=55,y=360)

matrix_entry_32 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_32.place(x=164,y=360)

matrix_entry_33 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_33.place(x=273,y=360)

matrix_entry_34 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_34.place(x=382,y=360)

matrix_entry_35 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_35.place(x=491,y=360)

matrix_entry_36 = Entry(root,font=font_1,width=6,bg='#ECE8E8' ,highlightthickness = 0,borderwidth=0,selectbackground='white')
matrix_entry_36.place(x=600,y=360)


#End Entry Section (grid layout)====================================================

#Button Section=============================================================

button_solve= Button(root,image=solve,font=font_1,bg='#FFFFFF',command= matrix_composition,highlightthickness = 0,borderwidth=0,activebackground='#FFFFFF')
button_solve.place(x=518,y=31)

#End Button Section=============================================================

label_copyright = Label(root, text='2021 Leonardo Ramazzotti')
label_copyright.place(x=700,y=780)


root.mainloop()