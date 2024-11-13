import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(37, 19)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(105, 27)
        self._label1.TabIndex = 0
        self._label1.Text = "variable1"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(37, 89)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(113, 26)
        self._label2.TabIndex = 1
        self._label2.Text = "variable2"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Location = System.Drawing.Point(40, 151)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(102, 25)
        self._label3.TabIndex = 2
        self._label3.Text = "variable3"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label4.Location = System.Drawing.Point(41, 224)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(109, 28)
        self._label4.TabIndex = 3
        self._label4.Text = "variable4"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(336, 14)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(121, 43)
        self._button1.TabIndex = 4
        self._button1.Text = "sum"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(341, 84)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(116, 41)
        self._button2.TabIndex = 5
        self._button2.Text = "average"
        self._button2.UseVisualStyleBackColor = True
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(194, 26)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(114, 20)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(194, 95)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(111, 20)
        self._textBox2.TabIndex = 7
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(194, 156)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(111, 20)
        self._textBox3.TabIndex = 8
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(194, 229)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(111, 20)
        self._textBox4.TabIndex = 9
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.Info
        self._label5.Location = System.Drawing.Point(511, 19)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(93, 38)
        self._label5.TabIndex = 10
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.Info
        self._label6.Location = System.Drawing.Point(511, 89)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(95, 36)
        self._label6.TabIndex = 11
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(344, 188)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(112, 54)
        self._button3.TabIndex = 12
        self._button3.Text = "calculate"
        self._button3.UseVisualStyleBackColor = True
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(505, 193)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(88, 48)
        self._button4.TabIndex = 13
        self._button4.Text = "clear"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.Location = System.Drawing.Point(651, 184)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(87, 58)
        self._button5.TabIndex = 14
        self._button5.Text = "exit"
        self._button5.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(775, 261)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button3Click(self, sender, e):
        variable1 = int(self._textbox1.Text)
        variable2 = int(self._textbox2.Text)
        variable3 = int(self._textbox3.Text)
        variable4 = int(self._textbox4.Text)
        sum       = variable1 + variable2 + variable3 + variable4
        average   = sum / 4
        self._label5.Text = str(sum)
        self._label6.Text = str(average)
        # + - * / %     ** pow     // devide & round down
        # int (integer):a whole number,pos/neg
        #float (Floating-Point Number):any number w/ a decimal
        #str (String): a string of text
        
        

    def Button4Click(self, sender, e):
        self._label5.Text = ""
        self._label6.Text = ""