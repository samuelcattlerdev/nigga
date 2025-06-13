import wx

class Crear_ventana(wx.Frame):
    def _init_(self):
        wx.Frame._init_(self, None, -1, title = "Medidor Ambiental", size = (400, 375),style = wx.DEFEAULT_FRAME_STYLE)

app = wx.App()
window = Crear_ventana()
window.Show()
app.MainLoop()
