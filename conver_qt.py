# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:29:15 2021

@author: jmaeda
"""
from PyQt5 import uic

# Qt Designerの出力ファイルを読み取りモードでオープン
fin = open('qt_MainWindowUI.ui', 'r', encoding='utf-8')
# Python形式ファイルを書き込みモードでオープン
fout = open('qt_MainWindowUI.py', 'w', encoding='utf-8')
# コンバート開始
uic.compileUi(fin, fout)
# ２つのファイルをクロース
fin.close()
fout.close()
