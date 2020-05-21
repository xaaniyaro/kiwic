import re
import csv

class Input():
    example1 =  '''
                "Clouds are white."
                "Pittsburgh is beautiful."
                '''

    example2 = '''
                """Clouds,are,white."""
                """Pittsburg,is,beautiful."""
                '''


    def txtFile(self, filename):
        f = open(filename, "r")
        words = []
        for x in f:
            proc = re.sub(r'\W+', ' ', x)
            words.append(proc.lower().split())
        return words

    #output
    #[['clouds', 'are', 'white'], ['pittsburgh', 'is', 'beautiful']]

    def csvFile(self, filename):
        f = open(filename)
        csv_f = csv.reader(f)
        words = []
        finalWords = []
        for row in csv_f:
            proc = row[0].split(',')
            for i in proc:
                word = re.sub(r'\W+', '', i).lower()
                words.append(word)
            finalWords.append(words)
            words = []
        return finalWords

    #output
    #[['clouds', 'are', 'white'], ['pittsburgh', 'is', 'beautiful']]