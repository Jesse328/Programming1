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
        self._label6 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label9 = System.Windows.Forms.Label()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label10 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label17 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self._label20 = System.Windows.Forms.Label()
        self._label21 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(172, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(197, 48)
        self._label1.TabIndex = 0
        self._label1.Text = "Highlander Hotel"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(246, 57)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(112, 29)
        self._label2.TabIndex = 1
        self._label2.Text = "Today's Date:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(285, 96)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(84, 31)
        self._label3.TabIndex = 2
        self._label3.Text = "Time:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label4.Location = System.Drawing.Point(32, 146)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(125, 33)
        self._label4.TabIndex = 3
        self._label4.Text = "Room information"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(75, 196)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(68, 21)
        self._label5.TabIndex = 4
        self._label5.Text = "Nights:"
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(55, 232)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(88, 20)
        self._label6.TabIndex = 5
        self._label6.Text = "Nighty charge:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(149, 193)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(83, 21)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(149, 231)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(83, 21)
        self._textBox2.TabIndex = 7
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label7.Location = System.Drawing.Point(285, 141)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(105, 38)
        self._label7.TabIndex = 8
        self._label7.Text = "Addtional charges"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(282, 196)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(107, 30)
        self._label8.TabIndex = 9
        self._label8.Text = "Room service:"
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(377, 196)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(83, 21)
        self._textBox3.TabIndex = 10
        # 
        # label9
        # 
        self._label9.Location = System.Drawing.Point(277, 226)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(92, 26)
        self._label9.TabIndex = 11
        self._label9.Text = "Telephone:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(377, 229)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(83, 21)
        self._textBox4.TabIndex = 12
        # 
        # label10
        # 
        self._label10.Location = System.Drawing.Point(282, 265)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(75, 23)
        self._label10.TabIndex = 13
        self._label10.Text = "Mac:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(377, 265)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(83, 21)
        self._textBox5.TabIndex = 14
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._label11.Location = System.Drawing.Point(32, 303)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(125, 29)
        self._label11.TabIndex = 15
        self._label11.Text = "Total Charges"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.Location = System.Drawing.Point(172, 343)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(115, 21)
        self._label12.TabIndex = 16
        self._label12.Text = "Addtional Charges:"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label13
        # 
        self._label13.Location = System.Drawing.Point(172, 377)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(115, 21)
        self._label13.TabIndex = 17
        self._label13.Text = "Subtotal:"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label14
        # 
        self._label14.Location = System.Drawing.Point(172, 311)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(115, 21)
        self._label14.TabIndex = 18
        self._label14.Text = "Room Charges:"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label15
        # 
        self._label15.Location = System.Drawing.Point(172, 451)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(115, 21)
        self._label15.TabIndex = 19
        self._label15.Text = "Total Charges:"
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label16
        # 
        self._label16.Location = System.Drawing.Point(172, 413)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(115, 21)
        self._label16.TabIndex = 20
        self._label16.Text = "Tax:"
        self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(32, 476)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(132, 61)
        self._button1.TabIndex = 26
        self._button1.Text = "calculate Charges"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(196, 478)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(128, 57)
        self._button2.TabIndex = 27
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(365, 481)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(120, 50)
        self._button3.TabIndex = 28
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.White
        self._label17.Location = System.Drawing.Point(287, 310)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(101, 21)
        self._label17.TabIndex = 29
        self._label17.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.White
        self._label18.Location = System.Drawing.Point(293, 343)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(96, 20)
        self._label18.TabIndex = 30
        self._label18.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.Color.White
        self._label19.Location = System.Drawing.Point(292, 380)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(95, 17)
        self._label19.TabIndex = 31
        # 
        # label20
        # 
        self._label20.BackColor = System.Drawing.Color.White
        self._label20.Location = System.Drawing.Point(292, 413)
        self._label20.Name = "label20"
        self._label20.Size = System.Drawing.Size(95, 17)
        self._label20.TabIndex = 32
        # 
        # label21
        # 
        self._label21.BackColor = System.Drawing.Color.White
        self._label21.Location = System.Drawing.Point(292, 451)
        self._label21.Name = "label21"
        self._label21.Size = System.Drawing.Size(95, 17)
        self._label21.TabIndex = 33
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(557, 541)
        self.Controls.Add(self._label21)
        self.Controls.Add(self._label20)
        self.Controls.Add(self._label19)
        self.Controls.Add(self._label18)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Room Charge Calculate"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


  

    def MainFormLoad(self, sender, e):
        self._label2.Text = date.today().strftime("%10, %15 %12, %18")
        self._label2.text = time.strftime("%5:%10:%12 %15")

    def Button1Click(self, sender, e):           
        decRoomCharges = 0.0
        decAddCharges = 0.0
        decSubtotal = 0.0
        decTax = 0.0
        decTotal = 0.0
        decTAX_RATE = 0.08
       
            decAddCharges = float(self._textBox3.Text) +  float(self._textBox4.Text) +  float(self._textBox5.Text)
            self._label18.Text = str(round(decAddCharges, 2))
            
        
            MessageBox.Show("Room Service, Telephone, and Misc. must be numbers", "Error")
            
            decRoomCharges = float(self._textBox1.Text) +  float(self._textBox2.Text)
            self._label17.Text = str(round(decRoomCharges, 2))
 
            MessageBox.Show("Nights and Nightly Charge must be numbers", "Error")
            
            decSubtotal = decRoomCharge + decAddcharges
            self._label19.Text = str(round(decRoomCharges, 2))
            
            decTax = decSubtital * decTAX.RATE
            self._label20.Text = str(round(decTax, 2))
            
            decTotal = decSubtital + decTax
            self._label21.Text = ste(round(decTotal, 2))
            
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._label17.Text = ""
        self._label18.Text = ""
        self._label19.Text = ""
        self._label20.Text = ""
        self._label21.Text = ""
        
    
    def Button3Click(self, sender, e):
        Application.Exit()