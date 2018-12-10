from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

gui_source = ''

with open('./Kivy/gui.kv') as file:
    for line in file:
        gui_source += line

Builder.load_string(gui_source)

class PlayerStats(Screen):
    pass

class Inventory(Screen):
    pass

class Menu(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widget(PlayerStats(name='player_stats'))
screen_manager.add_widget(Inventory(name='inventory'))
screen_manager.add_widget(Menu(name='menu'))

class GuiApp(App):

    def build(self):
        return screen_manager

gui_app = GuiApp
gui_app.run