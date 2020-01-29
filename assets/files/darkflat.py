#! /usr/bin/env python

from qtpy.QtGui import QPalette, QColor
from qtpy import QtCore


WHITE =     QColor(255, 255, 255)
BLACK =     QColor(0, 0, 0)
RED =       QColor(255, 0, 0)
PRIMARY =   QColor(53, 53, 53)
SECONDARY = QColor(35, 35, 35)
TERTIARY =  QColor(42, 130, 218)


def css_rgb(color, a=False):
    """Get a CSS `rgb` or `rgba` string from a `QtGui.QColor`."""
    return ("rgba({}, {}, {}, {})" if a else "rgb({}, {}, {})").format(*color.getRgb())


class QDarkPalette():
    """Dark palette for a Qt application meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        # Set all the colors based on the constants in globals       
        palette=QPalette()     
        palette.setColor(QPalette.Window,          PRIMARY)
        palette.setColor(QPalette.WindowText,      WHITE)
        palette.setColor(QPalette.Base,            SECONDARY)
        palette.setColor(QPalette.AlternateBase,   PRIMARY)
        palette.setColor(QPalette.ToolTipBase,     WHITE)
        palette.setColor(QPalette.ToolTipText,     WHITE)
        palette.setColor(QPalette.Text,            WHITE)
        palette.setColor(QPalette.Button,          PRIMARY)
        palette.setColor(QPalette.ButtonText,      WHITE)
        palette.setColor(QPalette.BrightText,      RED)
        palette.setColor(QPalette.Link,            TERTIARY)
        palette.setColor(QPalette.Highlight,       TERTIARY)
        palette.setColor(QPalette.HighlightedText, BLACK)


        palette.setColor(QPalette.Disabled, QPalette.Text, QtCore.Qt.darkGray)
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QtCore.Qt.darkGray)
        
        self.palette=palette
        
    @staticmethod
    def set_stylesheet(app):
        """Static method to set the tooltip stylesheet to a `QtWidgets.QApplication`."""
        app.setStyleSheet("QToolTip {{"
                          "color: {white};"
                          "background-color: {tertiary};"
                          "border: 1px solid {white};"
                          "}}".format(white=css_rgb(WHITE), tertiary=css_rgb(TERTIARY)))

    def set_app(self, app):
        """Set the Fusion theme and this palette to a `QtWidgets.QApplication`."""
        app.setStyle("Fusion")
        app.setPalette(self.palette)
        self.set_stylesheet(app)