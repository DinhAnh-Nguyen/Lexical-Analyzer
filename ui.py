from tkinter import *
import tkinter as tk

from analyzer import LexicalAnalyzer

class AnalyzerWindow(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		#set the layout method to pack
		self.pack()

		#create variables
		title = "Lexical Analyzer"

		helpText = "This program is a small Lexical Analyzer. \nInput your " \
		"code in the left textbox and then hit Analyze. The result will be in the right textbox" \
		"\nThe text boxes can be resized via the handle in the middle"

		self.defaultInputString = "input <- [5, 8, 12, 4, 10]" \
		"\ncount <- 0" \
		"\ntotal <- 0" \
		"\nfor x in input do" \
		"\n	count <- count + 1" \
		"\n	total <- total + x " \
		"\naverage <- total / count"

		self.stringResult = tk.StringVar()
		self.stringResult.set("Click Analyze!")
		
		self.backgroundColour = master["background"]

		#create widgets
		self.labelTitle = tk.Label(text=helpText)
		self.labelTitle.pack()
		self.labelTitle.configure(background=self.backgroundColour)

		# create a pane to hold the two textareas that can be resized
		# via a handle in the middle
		self.paned = tk.PanedWindow(master, orient=tk.HORIZONTAL, sashrelief=tk.RIDGE, sashwidth=10)
		#flat, groove, raised, ridge, solid, or sunken
		self.paned.pack(fill=tk.BOTH, expand=True)
		self.paned.configure(background=self.backgroundColour)

		#create the two text areas with the pane as their parent
		self.textInput = tk.Text(self.paned, height = 15, width = 40)
		self.textInput.insert(INSERT, self.defaultInputString)
		self.textInput.config(font=("Courier", 10), background="khaki")

		self.textResult = tk.Text(self.paned, height=15, width = 40)
		self.textResult.insert(INSERT, self.stringResult.get())

		self.textResult.tag_configure("EVEN", background="medium spring green")
		self.textResult.tag_configure("ODD", background="pale green")
		self.textResult.tag_configure("ERROR", background="yellow2")
		self.textResult.config(font=("Courier", 10), background="pale green")
		
		#add the children to the pane
		self.paned.add(self.textInput)
		self.paned.add(self.textResult)

		#create the buttons
		self.buttonAnalyze = tk.Button(text = "Analyze!", command = self.analyze)
		self.buttonAnalyze.pack()
		self.buttonAnalyze.configure(background=self.backgroundColour)
		
		self.buttonExample = tk.Button(text = "Insert default code", command = self.setExampleInput)
		self.buttonExample.pack()
		self.buttonExample.configure(background=self.backgroundColour)

	def setExampleInput(self):
		self.textInput.delete(1.0, END)
		self.textInput.insert(INSERT, self.defaultInputString)

	#function to be called when clicking analyze
	def analyze(self, event = None):
		analyzer = LexicalAnalyzer()
		result = analyzer.lex(self.textInput.get(1.0, END))
		self.textResult.delete(1.0, END)

		if not isinstance(result, str):
			# if its a valid result, then iterate through it in order to make it readable
			for idx, token in enumerate(result):
				kind, value = token
				value = value.replace("\n", "\\n").replace("\t", "\\t")
				line = f"{kind:<10} : {value}\n"
				tag_name = "EVEN" if idx % 2 else "ODD"
				self.textResult.insert(tk.END, line, (tag_name))
		else:
			self.textResult.insert(INSERT, result, ("ERROR"))

root = tk.Tk()
root.minsize(400, 300)
# root.resizable(False, False)
root.title("Lexical Analyzer")
root.configure(background="azure3")

analyzer = AnalyzerWindow(root)
analyzer.mainloop()