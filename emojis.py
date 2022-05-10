"""
@author: cucumberpeel

enables common emoji keyboard shortcuts

"""

import emoji

class Emoji():
    def __init__(self):
        self.shortcuts = {':)': u'\U0001f642', ';)': u'\U0001f609', ':D': u'\U0001f600', ":')": u'\U0001f972', ':P': u'\U0001f61b', \
        '^_^': u'\U0001f60a', ':(': u'\U0001f641', '>:(': u'\U0001f621', ':|': u'\U0001f610', '-_-': u'\U0001f611', 'B)': u'\U0001f60E', \
        ':/': u'\U0001F615', ':o': u'\U0001f62e', ":'(": u'\U0001f622', 'T_T': u'\U0001f62d', '<3': u'\U0001f90d'}

    """list all available shortcuts"""
    def get_all_shortcuts(self):
        print("-" * 20)
        print("Available emoji shortcuts:")
        for text, uni in self.shortcuts:
            print(f"{text} --> {uni}")
        print("-" * 20)

    """emoji shortcut to unicode"""
    def emojify_msg(self, msg):
        words = msg.split()
        for i in range(len(words)):
            if words[i] in self.shortcuts.keys():
                words[i] = self.shortcuts[words[i]]
        return ' '.join(words)

    """unicode to emoji shortcut"""
    def demojify_msg(self, msg):
        words = msg.split()
        for i in range(len(words)):
            if words[i] in self.shortcuts.values():
                words[i] = list(self.shortcuts.keys())[i]
        return ' '.join(words)
