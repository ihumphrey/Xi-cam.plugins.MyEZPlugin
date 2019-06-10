from xicam.plugins import EZPlugin
from pyqtgraph import GradientWidget
from pyqtgraph.console import ConsoleWidget
import numpy as np
# from qtpy.QtGui import QWidget

def my_cake():
    plugin = MyEZPlugin.instance
    plugin.centerwidget.setImage(np.random.random((100, 100, 100)))

# try this
# -----------------------------------------
# center_widget = ConsoleWidget

# in my_cake()
#     center_widget.runCmd("print('cake')")


toolbar_items = [['/Users/ian/repos/Xi-cam.gui/xicam/gui/static/icons/cake'
                  '.png',
                 my_cake, 'cake']]
params = [
    {'name': 'x', 'value': 0.0, 'type': 'float'},
    {'name': 'y', 'value': 0.0, 'type': 'float'},
]
cw = ConsoleWidget
cw = None
# why does instantiating the console widget make the window detached?
MyEZPlugin = EZPlugin(name='MyEZPlugin',
                      toolbuttons=toolbar_items,
                      centerwidget=cw,
                      parameters=params)
# MyEZPlugin = EZPlugin(name='MyEZPlugin',
#                       toolbuttons=toolbar_items,
#                       centerwidget=cw)