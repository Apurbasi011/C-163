from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Fever_Report")
root.geometry("600x600")

question1_radioButton = StringVar(value = "0")

Question1 = Label(root, text = "Do You Have a Headache And a Sore Throat ?")
Question1.pack()
question1_r1 = Radiobutton(root, text = "yes", variable = question1_radioButton, value = "yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "no", variable = question1_radioButton, value = "no")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")

Question2 = Label(root, text = "Is Your Body Temperature High ?")
Question2.pack()
question2_r1 = Radiobutton(root, text = "yes", variable = question2_radioButton, value = "yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "no", variable = question2_radioButton, value = "no")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")

Question3 = Label(root, text = "Are There Any Symptoms Of Eye Redness ?")
Question3.pack()
question3_r1 = Radiobutton(root, text = "yes", variable = question3_radioButton, value = "yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "no", variable = question3_radioButton, value = "no")
question3_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get() == "yes":
        score = score + 20
        print(score)
        
    if question2_radioButton.get() == "yes":
        score = score + 20
        print(score)
        
    if question3_radioButton.get() == "yes" :
        score = score + 20
        print(score)    
    
    if score <= 20 : 
        messagebox.showinfo("Report", "You Don't Need To Visit a Doctor")
        
    elif score > 20 and score <= 40 : 
        messagebox.showinfo("Report", "You Might Perhaps Have To Visit a Doctor")
        
    else : 
        messagebox.showinfo("Report", "I Strongly Advise You To Visit a Doctor")
        
btn = Button(root, text = "Click Me", command = fever_score)
btn.pack()
root.mainloop()
    
