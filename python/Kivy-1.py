# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:16:14 2020

@author: Amit
"""

import kivy
kivy.require('1.9.0') # Kivy ver where the code has been tested!
from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text='Hello world')
if __name__ == '__main__':
    MyApp().run()
    

