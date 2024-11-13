import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(70, 246)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(103, 58)
        self._button1.TabIndex = 0
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(239, 244)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(111, 59)
        self._button2.TabIndex = 1
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(428, 239)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(120, 63)
        self._button3.TabIndex = 2
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(46, 33)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(99, 41)
        self._label1.TabIndex = 3
        self._label1.Text = "length"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(46, 98)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 33)
        self._label2.TabIndex = 4
        self._label2.Text = "width"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Location = System.Drawing.Point(46, 156)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(109, 34)
        self._label3.TabIndex = 5
        self._label3.Text = "area"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(50, 210)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(95, 29)
        self._label4.TabIndex = 6
        self._label4.Text = "perimeter"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.Info
        self._label5.Location = System.Drawing.Point(238, 136)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(111, 44)
        self._label5.TabIndex = 7
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.Info
        self._label6.Location = System.Drawing.Point(233, 202)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(105, 37)
        self._label6.TabIndex = 8
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(219, 31)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(107, 20)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(219, 92)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(106, 20)
        self._textBox2.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(889, 306)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog52"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        length = int(self._textbox1.Text)
        width  = int(self._textbox2.Text)
        area   = length * width
        perim  =2 * length + 2 * width
        self._label3.Text = str(area)
        self._label4.Text = str(perim)
        # + - * / %     ** pow     // devide & round down
        # int (integer):a whole number,pos/neg
        #float (Floating-Point Number):any number w/ a decimal
        #str (String): a string of text

    def Button2Click(self, sender, e):
        self._textbox1.Text = ""
        self._textbox2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""