"""i18n Library"""
import lib.utils as utils
import io
from os import path
import json

class I18n:
    lang = 'en'
    tokens = []
    path = './i18n/'

    def __init__(self, lang):
        """Constructor"""
        if not path.exists(self.path):
            utils.create_dir(self.path)
        self.set_lang(lang)

    def _file(self):
        """Return a file name with reaspective path"""
        return self.path + self.lang + ".json"

    def set_lang(self, lang):
        """Set the language"""
        if utils.is_string(lang):
            self.lang = lang
            print("Creating " + self._file() + " file...")

            # Writing file
            if not path.exists(self._file()):
                print(self._file())
                with io.open(self._file(), "w+") as output:
                    json.dump({}, output)

    def translate(self, token):
        if not self.tokens:
            # Reading i18n file
            with open(self._file()) as data_file:
                data_loaded = json.load(data_file)
                self.tokens = data_loaded

        if token in self.tokens:
            return self.tokens[token]
        else:
            return False
