import random
import sys
from PyQt5 import uic
import io
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QPainter
from math import sin, cos, pi
g = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>644</width>
    <height>522</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="jmak">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>жмяк</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(g)
        uic.loadUi(f, self)
        self.resize(1000, 1000)
        self.do_paint = False
        self.n = 1
        self.x = 0
        self.y = 0
        self.jmak.clicked.connect(self.krug)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            if self.n == 1:
                self.krug()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def krug(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        size = random.randint(20, 100)
        self.qp.setBrush(color)
        self.qp.drawEllipse(int(self.x - size / 2), int(self.y - size / 2), size, size)
