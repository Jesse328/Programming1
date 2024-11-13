import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(6, 8)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(131, 22)
        self._label1.TabIndex = 0
        self._label1.Text = "Sum of the series"
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Items.AddRange(System.Array[System.Object](
            ["3+6+9+12+15+18+21+24...+9663+9666+9669"]))
        self._listBox1.Location = System.Drawing.Point(18, 37)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(304, 290)
        self._listBox1.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(6, 387)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(110, 65)
        self._button1.TabIndex = 2
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(133, 387)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(112, 65)
        self._button2.TabIndex = 3
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(265, 387)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(104, 65)
        self._button3.TabIndex = 4
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Yellow
        self.ClientSize = System.Drawing.Size(423, 464)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog152a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        sum = 
        self.listBox1,Items.Add()
        for num in range(3,9666+3):
            num = 