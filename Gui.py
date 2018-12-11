import kivy

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

main_manager = ScreenManager()
main_manager.add_widget(PlayerStats(name='player_stats'))
main_manager.add_widget(Inventory(name='inventory'))
main_manager.add_widget((Menu(name='menu')))

class GuiApp(App):

    def build(self):
        return main_manager

if __name__ == '__main__':
    GuiApp().run()