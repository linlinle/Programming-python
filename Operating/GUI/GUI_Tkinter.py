from tkinter import *
import tkinter.messagebox as mb

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()#把Widget加入到父容器中
		self.createWidgets()
		
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()#grid()可以实现更复杂的布局。
		self.alertButton = Button(self,text='hello',command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		mb.showinfo('Message','hello,%s'%name)
		
app = Application()
# 设置窗口标题:
app.master.title('hello world')
# 主消息循环:
app.mainloop()