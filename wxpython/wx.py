# 目前wxpython不支持python3.10及以上版本
import wx
app = wx.App()
# 创建一个应用程序对象
app = wx.App()

# 创建一个主窗口
frm = wx.Frame(None, title='第一个wx程序',size=(300,200))
# 显示窗口    
frm.Show()
# 进入主循环
app.MainLoop()