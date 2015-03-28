import tornado.web
import sys

sys.path.append("F:\web\UIModules")

from ui_module_equipmentSelector import ui_module_equipmentSelector
from ui_module_componentSelector import ui_module_componentSelector

class equipmentSelectorUIModule(tornado.web.UIModule):
    def render(self):
        return ui_module_equipmentSelector()

class componentSelectorUIModule(tornado.web.UIModule):
    def render(self, eqID):
        return ui_module_componentSelector(eqID)