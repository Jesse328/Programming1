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
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Location = System.Drawing.Point(67, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(102, 33)
        self._label1.TabIndex = 0
        self._label1.Text = "length"
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Menu
        self._label2.Location = System.Drawing.Point(67, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(102, 34)
        self._label2.TabIndex = 1
        self._label2.Text = "width"
        self._label2.Click += self.Label2Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkRed
        self._label3.Location = System.Drawing.Point(228, 95)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(130, 50)
        self._label3.TabIndex = 2
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.Window
        self._label5.Location = System.Drawing.Point(67, 95)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(95, 50)
        self._label5.TabIndex = 4
        self._label5.Text = "area"
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.Window
        self._label6.Location = System.Drawing.Point(67, 164)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(96, 45)
        self._label6.TabIndex = 5
        self._label6.Text = "perimeter"
        self._label6.Click += self.Label6Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.HotTrack
        self._button1.Location = System.Drawing.Point(73, 224)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(89, 58)
        self._button1.TabIndex = 6
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.Info
        self._button2.Location = System.Drawing.Point(228, 224)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(105, 58)
        self._button2.TabIndex = 7
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.InactiveBorder
        self._button3.Location = System.Drawing.Point(408, 224)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(108, 58)
        self._button3.TabIndex = 8
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(219, 22)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(139, 20)
        self._textBox1.TabIndex = 9
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Red
        self._label4.Location = System.Drawing.Point(228, 164)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(130, 57)
        self._label4.TabIndex = 10
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(219, 66)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(139, 20)
        self._textBox2.TabIndex = 11
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.MenuHighlight
        self.ClientSize = System.Drawing.Size(685, 294)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog52a"
        self.Load += self.MainFormLoad
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

    

    