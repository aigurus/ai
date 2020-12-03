# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:11:35 2020

@author: Amit
"""

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
Label:
    text:
        ('[b]Hello[/b][color=ff0033]kivy[/color]\\n'
        '[u]Hello[/u][color=ff0033]kivy[/color]\\n'
        '[i]Hello[/i][color=ff0033]kivy[/color]\\n'
        '[s]Hello[/s][color=ff0033]kivy[/color]\\n'
        
        )
    font_size:'45pt'
    markup:True
    
    ''')
   
class texttag(App):
    def build(self):
        return root
    
if __name__ =='__main__':
    texttag().run()

