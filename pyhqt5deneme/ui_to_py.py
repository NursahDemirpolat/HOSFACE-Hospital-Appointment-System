from PyQt5 import uic

with open('HastaAramaui.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('HastaArama.ui', fout)