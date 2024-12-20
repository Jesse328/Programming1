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
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(29, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(220, 63)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Three TestScores"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(37, 72)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(128, 52)
        self._label2.TabIndex = 1
        self._label2.Text = "score 1:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(37, 124)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(128, 52)
        self._label3.TabIndex = 2
        self._label3.Text = "score 2:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(37, 176)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(128, 52)
        self._label4.TabIndex = 3
        self._label4.Text = "score 3:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(37, 228)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(128, 52)
        self._label5.TabIndex = 4
        self._label5.Text = "Average:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(147, 88)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(126, 21)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(147, 140)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(125, 21)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(146, 192)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(126, 21)
        self._textBox3.TabIndex = 7
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(146, 247)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(126, 31)
        self._label6.TabIndex = 8
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(37, 384)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(107, 48)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate average"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(166, 363)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(105, 42)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(168, 424)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(105, 40)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(348, 474)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg198ScoreAvg"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        decScore1 = 0.0
        decScore2 = 0.0
        decScore3 = 0.0
        decAverage = 0.0
        
        decScore1 = float(self._textBox1.Text)
        decScore2 = float(self._textBox2.Text)
        decScore3 = float(self._textBox3.Text)
        
        decAverage = (decScore1 + decScore2 + decScore3) / 3
        self._label6.Text = str(round(decAverage, 2))
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label6.text = ""

    def Button3Click(self, sender, e):
        Application.Exit()