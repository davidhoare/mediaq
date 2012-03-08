"""Subclass of MainFrameBase, which is generated by wxFormBuilder."""from configobj import ConfigObjimport wximport CustomControlsimport Guiimport threadingimport timeimport OutputBasic# Implementing MainFrameBaseclass MediaQMainFrameBase(Gui.MainFrameBase):        def __init__(self, parent):        Gui.MainFrameBase.__init__(self, parent)                self.config = self.ReadConfig()                #Init variables         self.channels = CustomControls.channels        self.sliders = CustomControls.sliders        self.slider_boxes = CustomControls.slider_boxes                data = (("A", "B"),         ("C", "D"),         ("E", "F"),         ("G", "G"),        ("F", "F"),         ("Q", "Q"))                    colLabels = ("Last", "First")        rowLabels = ("1", "2", "3", "4", "5", "6", "7", "8", "9")                self.lx_table = CustomControls.GenericTable(data, rowLabels, colLabels)                self.lx_grid.SetTable(self.lx_table, True)        print "table value: " + str(self.lx_table.GetValue(1,1))                #'output' variables        self.output_chan = []        for i in range(0, int(self.config['num_channels'])):            self.output_chan.append(0.0);                self.dmx = [];        for i in range(0, 512):            self.dmx.append(0)                                self.display_update_enabled = True        self.output_enabled = True                 self.master_level = 100                        self.Bind(wx.EVT_CLOSE, self.OnClose)                t1 = threading.Thread(target=self.update_display)        t1.daemon = True        t1.start()                t2 = threading.Thread(target=self.update_output_chan)        t2.daemon = True        t2.start()                t3 = threading.Thread(target=self.output_to_dmx)        t3.daemon = True        t3.start()                self.enable_output()                def OnClose(self, event):#        dlg = wx.MessageDialog(self, "Do you really want to close this application?", "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)#        result = dlg.ShowModal()#        dlg.Destroy()#        if result == wx.ID_OK:#            self.display_update_enabled         = False        self.Destroy()            def update_output_chan(self):        while self.output_enabled:            #set the channel values based on cue values, and master            master_percent = self.master_level/100.0            for c in range(0, int(self.config['num_channels'])):                self.output_chan[c] = self.channels[c] * master_percent                            time.sleep(0.1)                def output_to_dmx(self):        #TODO: patch system        #but for now, we'll just do 1 to 1 for the first 24 chan        while self.output_enabled:            for c in range(0, len(self.output_chan)):                self.dmx[c] = self.output_chan[c]            if(self.config['output_type'] == "basic"):                OutputBasic.SetDMX(self.dmx)            time.sleep(0.1)                def enable_output(self):        if(self.config['output_type'] == "basic"):            OutputBasic.enable()    def update_display(self):#        print "config output type: " + self.config['output_type']         while self.display_update_enabled        :            for c in range(0, int(self.config['num_channels'])):                ch_val =  self.output_chan[c]                if(self.sliders[c].ch_override == False):                    self.sliders[c].SetLevel(ch_val)                if(self.slider_boxes[c].ch_override == False):                    self.slider_boxes[c].SetValue(str(int(ch_val)))                self.master_text.Value = str(int(self.master_level))            time.sleep(0.01)            #control surface events--------------------------------    def master_scroll(self, event):        self.master_level = event.GetPosition()        #menu events--------------------------------        def m_mniOpenClick(self, event):        # TODO: Implement m_mniOpenClick        pass        def m_mniSaveClick(self, event):        # TODO: Implement m_mniSaveClick        pass        def m_mniExitClick(self, event):        self.OnClose(event)        pass        def m_mniAboutClick(self, event):        # TODO: Implement m_mniAboutClick        pass    # configFile functions -------------------------------------    def SaveConfig(self):        config = ConfigObj()        config.filename = "conf.ini"        #        config['num_channels'] = "24"                config.write()        def ReadConfig(self):        config = ConfigObj("conf.ini")        return config