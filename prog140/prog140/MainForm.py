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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(12, 68)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(111, 59)
        self._label1.TabIndex = 0
        self._label1.Text = "Number 1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 156)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(124, 51)
        self._label2.TabIndex = 1
        self._label2.Text = "Operation"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 247)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(111, 57)
        self._label3.TabIndex = 2
        self._label3.Text = "Number 2:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(12, 345)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(111, 48)
        self._label4.TabIndex = 3
        self._label4.Text = "Result:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(100, 87)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(110, 21)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(100, 265)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(110, 21)
        self._textBox2.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(275, 42)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(50, 40)
        self._button1.TabIndex = 6
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(341, 42)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(49, 40)
        self._button2.TabIndex = 7
        self._button2.Text = "-"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(411, 42)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(51, 40)
        self._button3.TabIndex = 8
        self._button3.Text = "="
        self._button3.UseVisualStyleBackColor = True
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(275, 97)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(50, 40)
        self._button4.TabIndex = 9
        self._button4.Text = "^"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.Location = System.Drawing.Point(341, 97)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(49, 40)
        self._button5.TabIndex = 10
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._button6.Location = System.Drawing.Point(411, 97)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(51, 40)
        self._button6.TabIndex = 11
        self._button6.Text = "//"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.Location = System.Drawing.Point(335, 147)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(60, 39)
        self._button7.TabIndex = 12
        self._button7.Text = "MOD"
        self._button7.UseVisualStyleBackColor = True
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.Location = System.Drawing.Point(307, 247)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(116, 36)
        self._button8.TabIndex = 13
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = True
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.Location = System.Drawing.Point(308, 309)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(115, 36)
        self._button9.TabIndex = 14
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = True
        self._button9.Click += self.Button9Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(100, 362)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(110, 25)
        self._label5.TabIndex = 15
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(497, 474)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog140"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        db1Result = 0.0
        self._label2.Text = "+"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        db1Result = num1 + num2
        self._label5.Text = db1Result

    def Button2Click(self, sender, e):
        db1Result = 0.0
        self._label2.Text = "-"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        db1Result = num1 - num2
        self._label5.Text = db1Result

    def Button4Click(self, sender, e):
        db1Result = 0.0
        self._label2.Text = "^"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        db1Result = num1 * num2
        self._label5.Text = db1Result
       

    def Button5Click(self, sender, e):
        db1Result = 0.0
        self._label2.Text = "/"
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        db1Result = num1 / num2
        self._label5.Text = db1Result
        

    def Button6Click(self, sender, e):
        intResult = 0.0
        self._label2.Text = "//"
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        intResult = num1 // num2
        self._label5.Text = db1Result

    def Button7Click(self, sender, e):
        if num1 < num2:
            db1Result = 0.0
            self._label2.Text = "Mod"
        db1Result = float(self._textBox1.Text) - float(self._textBox2.Text)
        self._label5.Text = db1Result
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)

    def Button8Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label5.Text = ""

    def Button9Click(self, sender, e):
        Application.Exit()