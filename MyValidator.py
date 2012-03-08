import wx
import string

########################################################################
class CharValidator(wx.PyValidator):
    ''' Validates data as it is entered into the text controls. '''

    #----------------------------------------------------------------------
    def __init__(self, flag):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)

    #----------------------------------------------------------------------
    def Clone(self):
        '''Required Validator method'''
        return CharValidator(self.flag)

    #----------------------------------------------------------------------
    def Validate(self, win):
        return True

    #----------------------------------------------------------------------
    def TransferToWindow(self):
        return True

    #----------------------------------------------------------------------
    def TransferFromWindow(self):
        return True

    #----------------------------------------------------------------------
    def OnChar(self, event):
        keycode = int(event.GetKeyCode())
        if keycode < 256:
#            print keycode
            key = chr(keycode)
            specialkeys = [chr(13), chr(9)]
            #print key
            if self.flag == 'alpha' and key in string.letters:
                event.Skip()
            if self.flag == 'digit' and (key in string.digits or key in specialkeys):
                event.Skip()
        return

########################################################################