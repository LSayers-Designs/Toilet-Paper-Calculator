"""
Program: gottp.py
Author: L-Sayers
Date Created: 5/3/2020
Date Completed: 5/3/2020
Last Revised: 5/3/2020
Description: Calculates toilet paper stash per household to determine if you are a hoarder
"""

from breezypythongui import EasyFrame 
import math

class gottp(EasyFrame):
	"""GUI style framework"""
	def __init__(self):
		EasyFrame.__init__(self, title = "2-Ply Toilet Paper Calculator for a Household", background = "cadetblue",width = 800, height = 400)
		#Labels for the window 
		self.addLabel(text = "Got Enough Toilet Paper?", row = 0, column = 0, columnspan = 100, sticky = "NSEW", background = "white", foreground = "darkcyan", font="bold")
		self.addLabel(text = "Number of adult women:", row = 1, column = 0, columnspan = 10, background = "cadetblue", foreground = "white", font="bold")
		self.addLabel(text = "Number of adult men:", row = 2, column = 0, columnspan = 10, background = "cadetblue", foreground = "white", font="bold")
		self.addLabel(text = "Number of children (11 years and under):", row = 3, column = 0, columnspan = 10, background = "cadetblue", foreground = "white", font="bold")
		self.addLabel(text = "How many rolls of toilet paper do you currently have in stock?", row = 4, column = 0, columnspan = 10, background = "cadetblue", foreground = "white", font="bold")
		self.addLabel(text = "How many sheets per roll in stock (see the packaging for details or otherwise guess)", row = 5, column = 0, columnspan = 10, background = "cadetblue", foreground = "white", font="bold")

		#and input area for data collection
		self.women = self.addIntegerField(value = 0, row = 1, column = 1, width = 10)
		self.men = self.addIntegerField(value = 0, row = 2, column = 1, width = 10)
		self.kid = self.addIntegerField(value = 0, row = 3, column = 1, width = 10)
		self.rolls = self.addIntegerField(value = 0, row = 4, column = 1, width = 10)
		self.sheets = self.addIntegerField(value = 0, row = 5, column = 1, width =10)
		
		#Output area and command button to calculate results and output data
		self.outputArea = self.addTextArea(text = " ", row = 7, column = 0, columnspan = 2, width = 5, height = 5)
		self.calculate = self.addButton(text = "Calculate", row = 6, column = 0, columnspan = 2, command = self.calculate)

	#Event handling and calculations
	def calculate(self):	
		#Modus Tollens
		p = 89
		q = 62
		r = 44

		#Get inputs
		female = self.women.getNumber()
		male = self.men.getNumber()
		kids = self.kid.getNumber()
		onhand = self.rolls.getNumber()
		sheetspr = self.sheets.getNumber()

		#Compute Inputs
		roll = str(sheetspr)
		rollph = str((sheetspr*2)/((p*female)+(q*male)+(r*kids)))
		rstock = str(((sheetspr*2)/((p*female)+(q*male)+(r*kids))) * onhand)
		facts = (((sheetspr*2)/((p*female)+(q*male)+(r*kids))) * onhand)
		

		#Additional Comment Statments
		if facts < 7:
			comment = ("You need to grab a 12 pack quick!")
		elif facts < 14:
			comment = ("You might want to purchase a few extra rolls just to be safe.")	
		elif facts < 28:
			comment = ("You are reasonably stocked.")
		elif facts < 56:
			comment = ("Wow! How much closet space do you have to store all that toilet paper?")
		else:
			comment = ("You should feel ashamed of yourself, you hoarder!!")

		if rollph == 1:
			days = ("day")	
		else:
			days = ("days")

		#Output Statements
		conclusion = ("A single " + roll + " sheet 2-ply roll of toilet paper will last your household " + rollph +" "+ days + ". \nYou currently have a " + rstock + " day supply. \n" + comment)
		
		
		#Append Results 
		self.outputArea.setText(conclusion)
	
"""Main function"""
def main():
	gottp().mainloop()
#global call to main
main()