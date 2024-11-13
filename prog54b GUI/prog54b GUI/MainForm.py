import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(179, 38)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(115, 20)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(179, 97)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(113, 20)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(179, 156)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(115, 20)
        self._textBox3.TabIndex = 2
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(179, 213)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(118, 20)
        self._textBox4.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Info
        self._label1.Location = System.Drawing.Point(49, 38)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(90, 27)
        self._label1.TabIndex = 4
        self._label1.Text = "integers"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(798, 289)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "prog54b GUI"
        self.ResumeLayout(False)
        self.PerformLayout()

