from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class KeyDown(App):
    def build(self):
        Window.bind(on_key_down=self.key_action)
        return Widget()

    def key_action(self, *args):
        print("got a key event: %s" % list(args))


if __name__ == '__main__':
    KeyDown().run()