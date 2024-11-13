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
        self._listBox1.Items.AddRange(System.Array[System.Object](
            ["1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20"]))
        self._listBox1.Location = System.Drawing.Point(109, 82)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(317, 134)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Yellow
        self._button1.Location = System.Drawing.Point(34, 269)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(129, 69)
        self._button1.TabIndex = 1
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Yellow
        self._button2.Location = System.Drawing.Point(206, 269)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(128, 68)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Yellow
        self._button3.Location = System.Drawing.Point(379, 269)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(126, 67)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(561, 444)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122h"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading = "number\t\tSquare\t\tSquare Root\t\tCube\t\4th Root"
        self.listBox1,Items.Add(heading)
        for num in range (1,20+1):
            nsqrd = num ** 2
            nsqrt = math.sqrt(num)
            nc    = num ** 3
            n4tht = math.sqrt(num) ** 2
        

    def Button2Click(self, sender, e):
        self.listBox1,Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()