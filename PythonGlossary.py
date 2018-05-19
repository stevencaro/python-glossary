
from random import choice
import json
import re

class PythonGlossary():

    def __init__(self):
        glossary_file = 'python-glossary-requests.json'

        with open (glossary_file, 'r') as gloss:
            self.glossary = json.load(gloss)

    def show(self, entry):
        print('''\
{0[term]}

    {0[gloss]}'''.format(entry))

    def rand(self):
        entry = choice(self.glossary)
        self.show(entry)

    def search(self, search_str):
        results = []
        for entry in self.glossary:

            regex = re.compile(search_str, re.IGNORECASE)
            match = re.search(regex, entry['term'])

            if match:
                results.append( entry )

        for res in results:
            self.show(res)
            if len(results) > 1:
                print('-' * 80 )

