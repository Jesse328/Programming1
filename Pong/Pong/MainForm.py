﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.RaiseDragEvent = System.Random()
        self.ballup = 0
        self.balld = 0
        self.flagleft = False
        self.flagright = False
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        self._lbltitle = System.Windows.Forms.Label()
        self._leftscore = System.Windows.Forms.Label()
        self._rightscore = System.Windows.Forms.Label()
        self._lblball = System.Windows.Forms.Label()
        self._lblleft = System.Windows.Forms.Label()
        self._lblright = System.Windows.Forms.Label()
        self._timerdummy = System.Windows.Forms.Timer(self._components)
        self._timerboolean = System.Windows.Forms.Timer(self._components)
        self._timerright = System.Windows.Forms.Timer(self._components)
        self._timerleft = System.Windows.Forms.Timer(self._components)
        self._timerball = System.Windows.Forms.Timer(self._components)
        self._timermulti = System.Windows.Forms.Timer(self._components)
        self.SuspendLayout()
        # 
        # lbltitle
        # 
        self._lbltitle.Font = System.Drawing.Font("Microsoft Tai Le", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._lbltitle.Location = System.Drawing.Point(12, 25)
        self._lbltitle.Name = "lbltitle"
        self._lbltitle.Size = System.Drawing.Size(958, 52)
        self._lbltitle.TabIndex = 0
        self._lbltitle.Text = "Please Enter to Start or M to start Multiplayer"
        self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # leftscore
        # 
        self._leftscore.Font = System.Drawing.Font("Microsoft Tai Le", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._leftscore.Location = System.Drawing.Point(168, 96)
        self._leftscore.Name = "leftscore"
        self._leftscore.Size = System.Drawing.Size(166, 109)
        self._leftscore.TabIndex = 1
        self._leftscore.Text = "0"
        # 
        # rightscore
        # 
        self._rightscore.Font = System.Drawing.Font("Microsoft Tai Le", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._rightscore.Location = System.Drawing.Point(734, 96)
        self._rightscore.Name = "rightscore"
        self._rightscore.Size = System.Drawing.Size(166, 109)
        self._rightscore.TabIndex = 2
        self._rightscore.Text = "0"
        # 
        # lblball
        # 
        self._lblball.BackColor = System.Drawing.Color.White
        self._lblball.Location = System.Drawing.Point(479, 304)
        self._lblball.Name = "lblball"
        self._lblball.Size = System.Drawing.Size(20, 20)
        self._lblball.TabIndex = 3
        self._lblball.Click += self.LblballClick
        # 
        # lblleft
        # 
        self._lblleft.BackColor = System.Drawing.Color.White
        self._lblleft.Location = System.Drawing.Point(12, 246)
        self._lblleft.Name = "lblleft"
        self._lblleft.Size = System.Drawing.Size(20, 100)
        self._lblleft.TabIndex = 4
        # 
        # lblright
        # 
        self._lblright.BackColor = System.Drawing.Color.White
        self._lblright.Location = System.Drawing.Point(950, 246)
        self._lblright.Name = "lblright"
        self._lblright.Size = System.Drawing.Size(20, 100)
        self._lblright.TabIndex = 5
        # 
        # timerright
        # 
        self._timerright.Interval = 20
        self._timerright.Tick += self.TimerrightTick
        # 
        # timerleft
        # 
        self._timerleft.Interval = 20
        self._timerleft.Tick += self.TimerleftTick
        # 
        # timerball
        # 
        self._timerball.Interval = 20
        self._timerball.Tick += self.TimerballTick
        # 
        # timermulti
        # 
        self._timermulti.Interval = 20
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(988, 607)
        self.Controls.Add(self._lblright)
        self.Controls.Add(self._lblleft)
        self.Controls.Add(self._lblball)
        self.Controls.Add(self._rightscore)
        self.Controls.Add(self._leftscore)
        self.Controls.Add(self._lbltitle)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.ForeColor = System.Drawing.Color.White
        self.Name = "MainForm"
        self.Text = "Pong"
        self.Load += self.MainFormLoad
        self.SizeChanged += self.MainFormSizeChanged
        self.KeyDown += self.MainFormKeyDown
        self.ResumeLayout(False)


    def TimerballTick(self, sender, e):
        ball = self._lblball
        lpdl = self._lblleft
        rpdl = self._lblright
        rscore = int(self._rightscore.Text)
        lscore = int(self._leftscore.Text)
        ball.Top += self.ballup
        ball.Left += 8 * self.balld
        
        if ball.Right >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
            self.balld = -1
            self.ballup = self.RaiseDragEvent.Next(-4, 5)
        elif ball.Left <= lpdl.Left and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
            self.balld = 1
            self.ballup = self.RaiseDragEvent.Next(-4, 5)
            
        if ball.Top <= 0:
            self.balld = -1
            self.Top += 5 * self.balld
        elif ball.Bottom >= self.Height:
            self.balld = 1
            self.Top += 5 * self.balld
            
        if ball.Top <= self.Top + 10:
            self.ballup = 1
        elif ball.Top >= self.Height - 50:
            self.ballup = -1
            
            
        # -
            
        if ball.Location.X <= 0 or ball.Location.X < lpdl.Left - 20:
               """ TODO: FINISH LEFT BOUNDARY """
               pass
    
        if ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top:
            lscore += 1
            self._leftscore.Text = str(lscore)
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
          
        """ TODO: FINISH RIGHT SCORE WIN CONDITION """
        
        if lscore == 10: #Left Win condition
            self._timerball.Enabled = False
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
            self.ballup = 0
            self._lbltitle.Text = "Left Player Wins! Press R to restart"
            self._lbltitle.Visible = True
            
        """ TODO: ? """
        if self.timerboolean.Enabled:
            lpdl.Top = ball.Top - 20
        pass
            

    def MainFormKeyDown(self, sender, e):
        tball  = self._timerball
        tdum   = self._timerdummy
        tbool  = self._timerboolean
        tmult  = self._timermulti
        tleft  = self._timerleft
        tright = self._timerright
        bl     = self._lblball
        lpdl   = self._lblleft
        rpdl   = self._lblright
        title  = self._lbltitle
        
        def reset():
            title.Visible = True
            title.Text = "Press Enter to start or M to start Multiplayer"
            self._leftscore.Text = "0"
            self._rightscore.Text = "0"
            tball.Enabled = False
            tdum.Enabled = False
            tbool.Enabled = False
            tmult.Enabled = False
            tleft.Enabled = False
            tright.Enabled = False
            bl.left = self.Width // 2
            bl.Top = self.Height // 2
            lpdl.Top = (self.Height // 2) - 50 + lpdl.Height
            rpdl.Top = (self.Height // 2) - 50 + rpdl.Height
            """ TODO: RESET SECRETS """
            bl.BackColor = Color.White
            
         if e.KeyCode == keys.R:
             reset()
             
             
         """ TODO: SECRET CONTROL """
         
         if e.KeyCode == Keys.Enter:
             tball.Enabled = True
             tdum.Enabled = True
             tbool.Enabled = not tmult.Enabled
             title.Visible = False
         if e.KeyCode == Keys.M:
             reset()
             title.Visible = True
             title.Text = "Use W and S to move the left paddle; hit Enter to start"
             tmult.Enabled = True
             
         if tdum.Enabled:
             if e.KeyCode == Keys.Up:
                 self.flagright = False
                 tright.Enabled = True
             elif e.KeyCode == Keys.Down:
                 self.flagright = True
                 tright.Enabled = True
                 
         """ TODO: FINISH MULTIPLAYER CONTROLS """
         if tmult.Enabled and tball.Enabled:
             if e.KeyCode == Keys.W:
                 pass
             elif e.KeyCode  == Keys.S:
                 pass
         pass
            

    def MainFormLoad(self, sender, e):
        """ TODO: ADD 3 NUIQUE SECRETS/CHEATS?EASTER EGGS
        IN TOTAL & FINISH MULTIPLAYER & SCOREBOARD & DUMMY AI """
        self.balld = 1
        self.ballup = self.RaiseDragEvent.Next(-4, 5)
        
    def pdlTick(self, pd1, flagd, tmr):
        if flagd == True:
            pd1.Top += 5
        else:
            pdl.Top <= 5
        if pdl.Top <= 10 or pdl.Bottom >= self.Height - 50:
            tmr.Enabled = False

    def TimerleftTick(self, sender, e):
        self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

    def TimerrightTick(self, sender, e):
        self.pdlTick(self._lblleft, self.flagright, self._timerright)

    def LblballClick(self, sender, e):
        self._lblball.BackColor = Color.Red
        self.BackColor = Color.Green #Form BG Color
        """ TODO:PUT MORE EASTER EGGS LATER """

    def MainFormSizeChanged(self, sender, e):
        self._lblright.Left = self.Width - 25 - self._lblright.Width
        self._rightscore.Left = self.Width - 75 - self._rightscore.Width
        self._lbltitle.Width = self.Width - 25
        self._lblball.Left = self.Width // 2
        self._lblball.Top = self.Height // 2