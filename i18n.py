import lib.utils as utils
import io
from os import path
import json

class I18n:
    lang = 'en'
    tokens = []
    path = './i18n/'

    def __init__(self, lang):
        """Set a lang"""

        # print('Config tokens on file in ' + self.path + ' <selected language>.json ')
        if not path.exists(self.path):
            utils.create_dir(self.path)

        self.set_lang(lang)

    def _file(self):
        return self.path + self.lang + ".json"

    def set_lang(self, lang):
        if utils.is_string(lang):
            self.lang = lang
            print("Creating " + self._file() + " file...")

            # Writing file
            if not path.exists(self._file()):
                print(self._file())
                with io.open(self._file(), "w+") as output:
                    json.dump({}, output)

    def translante(self, token):
        if not self.tokens:
            # Reading i18n file
            with open(self._file()) as data_file:
                data_loaded = json.load(data_file)
                self.tokens = data_loaded
                # print(data_loaded)

        if token in self.tokens:
            return self.tokens[token]
        else:
            return False
