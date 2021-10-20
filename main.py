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
root.geometry('1000x800')
# Font Section=====================================================================

font_1 = ('Roboto Condenser',14)



#End Font Section=====================================================================


frame_matrix_grid = Frame(root,width=80,height=80,bg='white')
frame_matrix_grid.place(x=115,y=150)

#Entry Section (grid layout)====================================================

matrix_entry_1 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_1.grid(row=1,column=1,padx=10,pady=30)

matrix_entry_2 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_2.grid(row=1,column=2,padx=10,pady=30)

matrix_entry_3 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_3.grid(row=1,column=3,padx=10,pady=30)

matrix_entry_4 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_4.grid(row=1,column=4,padx=10,pady=30)

matrix_entry_5 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_5.grid(row=1,column=5,padx=10,pady=30)

matrix_entry_6 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_6.grid(row=1,column=6,padx=10,pady=30)

matrix_entry_7 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_7.grid(row=2,column=1,padx=10,pady=30)

matrix_entry_8 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_8.grid(row=2,column=2,padx=10,pady=30)

matrix_entry_9 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_9.grid(row=2,column=3,padx=10,pady=30)

matrix_entry_10 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_10.grid(row=2,column=4,padx=10,pady=30)

matrix_entry_11 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_11.grid(row=2,column=5,padx=10,pady=30)

matrix_entry_12 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_12.grid(row=2,column=6,padx=10,pady=30)

matrix_entry_13 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_13.grid(row=3,column=1,padx=10,pady=30)

matrix_entry_14 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_14.grid(row=3,column=2,padx=10,pady=30)

matrix_entry_15 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_15.grid(row=3,column=3,padx=10,pady=30)

matrix_entry_16 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_16.grid(row=3,column=4,padx=10,pady=30)

matrix_entry_17 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_17.grid(row=3,column=5,padx=10,pady=30)

matrix_entry_18 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_18.grid(row=3,column=6,padx=10,pady=30)

matrix_entry_19 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_19.grid(row=4,column=1,padx=10,pady=30)

matrix_entry_20 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_20.grid(row=4,column=2,padx=10,pady=30)

matrix_entry_21 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_21.grid(row=4,column=3,padx=10,pady=30)

matrix_entry_22 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_22.grid(row=4,column=4,padx=10,pady=30)

matrix_entry_23 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_23.grid(row=4,column=5,padx=10,pady=30)

matrix_entry_24 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_24.grid(row=4,column=6,padx=10,pady=30)

matrix_entry_25 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_25.grid(row=5,column=1,padx=10,pady=30)

matrix_entry_26 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_26.grid(row=5,column=2,padx=10,pady=30)

matrix_entry_27 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_27.grid(row=5,column=3,padx=10,pady=30)

matrix_entry_28 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_28.grid(row=5,column=4,padx=10,pady=30)

matrix_entry_29 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_29.grid(row=5,column=5,padx=10,pady=30)

matrix_entry_30 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_30.grid(row=5,column=6,padx=10,pady=30)


matrix_entry_31 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_31.grid(row=6,column=1,padx=10,pady=30)

matrix_entry_32 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_32.grid(row=6,column=2,padx=10,pady=30)

matrix_entry_33 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_33.grid(row=6,column=3,padx=10,pady=30)

matrix_entry_34 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_34.grid(row=6,column=4,padx=10,pady=30)

matrix_entry_35 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_35.grid(row=6,column=5,padx=10,pady=30)

matrix_entry_36 = Entry(frame_matrix_grid,font=font_1,width=8)
matrix_entry_36.grid(row=6,column=6,padx=10,pady=30)



#End Entry Section (grid layout)====================================================

#Button Section=============================================================

button_solve= Button(root,text="Solve",font=font_1,command= matrix_composition)
button_solve.place(x=470,y=700)

#End Button Section=============================================================

label_copyright = Label(root, text='2021 Leonardo Ramazzotti')
label_copyright.place(x=700,y=780)

root.mainloop()