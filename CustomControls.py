import wx
import wx.grid
import MyValidator
import Config

channels = [];
for i in range(0, Config.num_channels):
    channels.append(0.0);

ch_counter = 0
cht_counter = 0
    
sliders = []
slider_boxes = []




class ChannelSlider(wx.Slider):
    def __init__(self, parent, name, value, minValue, maxValue, pos, size, style):
        global ch_counter
        wx.Slider.__init__(self, parent, name, value, minValue, maxValue, pos, size, style)
        self.ch_num = ch_counter
        self.ch_override = False
        
        self.Bind(wx.EVT_SCROLL, self.OnScroll)    
        self.Bind(wx.EVT_SCROLL_THUMBTRACK, self.slider_mouse_down)
        self.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.slider_mouse_up)
        
        sliders.append(self)
        ch_counter += 1
        
    def slider_mouse_down(self, event):
        self.ch_override = True
#        print str(self.ch_num) + ": " + str(self.GetValue())
        if(self.ch_override == True):
            channels[self.ch_num] = self.GetValue()
        event.Skip() 
        
    def slider_mouse_up(self, event):
        self.ch_override = False
        event.Skip() 
        
        
    def OnScroll(self, event):
        print str(self.ch_num) + ": " + str(self.GetValue())
        if(self.ch_override == True):
            slider_boxes[self.ch_num].SetValue(str(self.GetValue()))
            channels[self.ch_num] = self.GetValue()
        
    def SetLevel(self, level):
        self.SetValue(level)
        
        
class ChannelText(wx.TextCtrl):
    def __init__(self, parent, id, value, pos, size, style, ch_num=0):
        #self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), wx.TE_CENTRE|wx.TE_NO_VSCROLL|wx.TE_PROCESS_ENTER 
        global cht_counter
        wx.TextCtrl.__init__(self, parent, id, value, pos, size, style, validator=MyValidator.CharValidator('digit'))
        self.ch_num = cht_counter
        self.ch_override = False
        slider_boxes.append(self)
        cht_counter += 1
        
        self.Bind(wx.EVT_CHAR, self.text_char)
        self.Bind(wx.EVT_SET_FOCUS, self.text_getfocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.text_killfocus)
        
    def text_char(self, event):
        print "char"
        key = event.GetKeyCode()
        print key 
        if key == 13:   #enter
            #do enter action
            self.update_channel_val(self.ch_num, int(self.Value))
            self.Parent.lxq_text.SetFocus()
            print key
        elif key == 9: #tab
            #do tab action
            self.update_channel_val(self.ch_num, int(self.Value))
            nextnum = self.ch_num + 1 if self.ch_num < 23 else 0
            nextstring = "0" + str(nextnum) if nextnum in range(0, 10) else str(nextnum)
            
            exec('self.Parent.ch_text' + nextstring + '.SetFocus()')
            print key
        event.Skip() 
    
    def update_channel_val(self, ch_num, value):
        sliders[ch_num].SetValue(value)
        channels[ch_num] = value
        
    def text_getfocus(self, event):
        print "getfocus"
        self.ch_override = True
        self.SelectAll()
        event.Skip() 
    
    def text_killfocus(self, event):
        print "killfocus"
        self.ch_override = False
        event.Skip() 

class GenericTable(wx.grid.PyGridTableBase):
    def __init__(self, data, rowLabels=None, colLabels=None):
        wx.grid.PyGridTableBase.__init__(self)
        self.data = data
        self.rowLabels = rowLabels
        self.colLabels = colLabels
        
    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]
        
    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]
        
    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        pass         

