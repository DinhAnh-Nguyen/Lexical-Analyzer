import ctypes
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

		self.testStringOne = "input <- [5, 8, 12, 4, 10]" \
		"\ncount <- 0" \
		"\ntotal <- 0" \
		"\nfor x in input do" \
		"\n\tcount <- count + 1" \
		"\n\ttotal <- total + x " \
		"\naverage <- total / count"

		self.testStringTwo = "one <- FALSE" \
		"\ntwo <- TRUE" \
		"\nif one IS NOT two do" \
		"\n\ttwo <- 10 >= 11" \
		"\n\tone <- 10 <= 10" \
		"\ntwo IS one" \
		"\ntwo IS NOT one"

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
		self.textInput.insert(tk.INSERT, self.testStringOne)
		self.textInput.config(font=("Courier", 10), background="khaki")

		self.textResult = tk.Text(self.paned, height=15, width = 40)
		self.textResult.insert(tk.INSERT, self.stringResult.get())

		self.textResult.tag_configure("EVEN", background="medium spring green")
		self.textResult.tag_configure("ODD", background="pale green")
		self.textResult.tag_configure("ERROR", background="yellow2")
		self.textResult.config(font=("Courier", 10), background="pale green")
		
		#add the children to the pane
		self.paned.add(self.textInput)
		self.paned.add(self.textResult)

		#create a frame so the buttons can be side by side
		self.frameButtons = tk.Frame()
		self.frameButtons.pack()

		#create the buttons
		self.buttonAnalyze = tk.Button(self.frameButtons, text = "Analyze!", command = self.analyze)
		self.buttonAnalyze.pack(side='left')
		self.buttonAnalyze.configure(background=self.backgroundColour)
		
		self.buttonExample = tk.Button(self.frameButtons, text = "Insert example 1", command = lambda: self.setExampleInput(1))
		self.buttonExample.pack(side='left')
		self.buttonExample.configure(background=self.backgroundColour)

		self.buttonExampleTwo = tk.Button(self.frameButtons, text = 'Insert example 2', command= lambda: self.setExampleInput(2))
		self.buttonExampleTwo.pack(side='left')
		self.buttonExampleTwo.config(background=self.backgroundColour)

	def setExampleInput(self, exampleIdx):
		self.textInput.delete(1.0, tk.END)
		match exampleIdx:
			case 1:
				self.textInput.insert(tk.INSERT, self.testStringOne)
				return
			case 2:
				self.textInput.insert(tk.INSERT, self.testStringTwo)
				return

	#function to be called when clicking analyze
	def analyze(self):
		analyzer = LexicalAnalyzer()
		result = analyzer.lex(self.textInput.get(1.0, tk.END))
		self.textResult.delete(1.0, tk.END)

		if not isinstance(result, str):
			# if its a valid result, then iterate through it in order to make it readable
			for idx, token in enumerate(result):
				kind, value = token
				value = value.replace("\n", "\\n").replace("\t", "\\t")
				line = f"{kind:<10} : {value}\n"
				tag_name = "EVEN" if idx % 2 else "ODD"
				self.textResult.insert(tk.END, line, (tag_name))
		else:
			self.textResult.insert(tk.INSERT, result, ("ERROR"))

root = tk.Tk()
root.minsize(400, 300)
root.title("Lexical Analyzer")
root.configure(background="azure3")

#make it less blurry on windows
try:
	ctypes.windll.shcore.SetProcessDpiAwareness(1) # type: ignore # 1 for System DPI Aware, 2 for Per Monitor DPI Aware
except AttributeError:
	pass # Not all Windows versions support this

analyzer = AnalyzerWindow(root)
analyzer.mainloop()