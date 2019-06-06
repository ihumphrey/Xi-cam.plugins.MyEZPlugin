from xicam.plugins import EZPlugin
from pyqtgraph import GradientWidget
from pyqtgraph.console import ConsoleWidget
# from qtpy.QtGui import QWidget

def my_cake():
    print('\nmy_cake called\n')
    MyEZPlugin.instance.centerwidget.runCmd("print('cake')")
    # print(cw().__dict__)
    # cw().runCmd("print('cake')")
    # useful to have @property method to do: MyEZPlugin.centerwidget.<method>()?

# try this
# -----------------------------------------
# center_widget = ConsoleWidget

# in my_cake()
#     center_widget.runCmd("print('cake')")

cake_action = [
    'cake_icon',
    'cake_function()'
    'cake_action_name'
]
toolbar_items = [['/Users/ian/repos/Xi-cam.gui/xicam/gui/static/icons/cake'
                  '.png',
                 my_cake, 'cake']]

cw = ConsoleWidget
# why does instantiating the console widget make the window detached?
MyEZPlugin = EZPlugin(name='MyEZPlugin',
                      toolbuttons=toolbar_items,
                      centerwidget=ConsoleWidget)
# MyEZPlugin = EZPlugin(name='MyEZPlugin',
#                       toolbuttons=toolbar_items,
#                       centerwidget=cw)