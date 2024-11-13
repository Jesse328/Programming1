import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(4, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(359, 212)
        self._listBox1.TabIndex = 0
        self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._button1.Location = System.Drawing.Point(4, 246)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(92, 52)
        self._button1.TabIndex = 1
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._button2.Location = System.Drawing.Point(145, 246)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(92, 50)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._button3.Location = System.Drawing.Point(286, 246)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(92, 48)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(434, 326)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog162b"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "Year\t\tPopulation (in mil.)"
        self._listBox1.Items.Add(heading)
        pop = 243
        four year in range(1990,2016):
             line = str(year) + "\t\t" + str(int(pop))
             self._listBox1.Items.Add(line)
             pop *=1.029

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()

    