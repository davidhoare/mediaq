import sys
print(sys.version)

import wx
from MediaQMainFrameBase import MediaQMainFrameBase

class MediaQ(wx.App):
    def OnInit(self):
        self.m_frame = MediaQMainFrameBase(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = MediaQ(0)
app.MainLoop()
