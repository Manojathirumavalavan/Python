class student:
    dept="CSE"
    def set_dim(self,name,marks):
        self.name=name
        self.marks=marks
        self.p=0
    def per(self):
        self.p=sum(self.marks)//3
    def display(self):
        self.per()
        print("1.NAME: ",self.name)
        print("2.SCORE: ",self.p)
        print("3.DEPT: ",student.dept)
        
manoja=student()
loubna=student()
rakshana=student()
manoja.set_dim("Mano",[40,50,60])
loubna.set_dim("Loubs",[45,55,65])
rakshana.set_dim("Raks",[30,60,70])
manoja.display()
loubna.display()
rakshana.display()