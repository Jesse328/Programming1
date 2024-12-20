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
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label3 = System.Windows.Forms.Label()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(58, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(279, 53)
        self._label1.TabIndex = 0
        self._label1.Text = "Radio Button Check Box Demo"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(45, 72)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(101, 42)
        self._label2.TabIndex = 1
        self._label2.Text = "Radio Buttons"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(45, 131)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(117, 42)
        self._radioButton1.TabIndex = 2
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Choice1"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(45, 189)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(117, 42)
        self._radioButton2.TabIndex = 3
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Choice2"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(45, 251)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(117, 42)
        self._radioButton3.TabIndex = 4
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Choice3"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(200, 77)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(137, 32)
        self._label3.TabIndex = 5
        self._label3.Text = "Check boxes"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # radioButton4
        # 
        self._radioButton4.Location = System.Drawing.Point(220, 251)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(117, 42)
        self._radioButton4.TabIndex = 6
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Choice1"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # radioButton5
        # 
        self._radioButton5.Location = System.Drawing.Point(220, 189)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(117, 42)
        self._radioButton5.TabIndex = 7
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "Choice5"
        self._radioButton5.UseVisualStyleBackColor = True
        # 
        # radioButton6
        # 
        self._radioButton6.Location = System.Drawing.Point(220, 131)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(117, 42)
        self._radioButton6.TabIndex = 8
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "Choice1"
        self._radioButton6.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(45, 350)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(85, 50)
        self._button1.TabIndex = 9
        self._button1.Text = "OK"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(220, 350)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(81, 50)
        self._button2.TabIndex = 10
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(425, 453)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._radioButton6)
        self.Controls.Add(self._radioButton5)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg247Radio"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        strMessage = ""
        
        if self.radioButton1.Checked == True:
            strMessage = "You selected Choice 1"
        elif self.radioButton2.Checked == True:
            strMessage = "You selected Choice 2"
        elif self.radioButton3.Checked == True:
            strMessage = "You selected Choice 3"
        
        if self.radioButton4.Checked == True:
            strMessage += " and Choice 4"
        elif self.radioButton5.Checked == True:
            strMessage += " and Choice 5"
        elif self.radioButton6.Checked == True:
            strMessage += " and Choice 6"
            
        MessageBox.Show(strMessage)

    def Button2Click(self, sender, e):
        Application.Exit()