# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\rootbuilder\ui\rootbuilder_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RootBuilderMenu(object):
    def setupUi(self, RootBuilderMenu):
        RootBuilderMenu.setObjectName("RootBuilderMenu")
        RootBuilderMenu.resize(530, 458)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RootBuilderMenu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contentSplitter = QtWidgets.QSplitter(RootBuilderMenu)
        self.contentSplitter.setOrientation(QtCore.Qt.Vertical)
        self.contentSplitter.setObjectName("contentSplitter")
        self.topTabWidget = QtWidgets.QTabWidget(self.contentSplitter)
        self.topTabWidget.setObjectName("topTabWidget")
        self.modeTab = QtWidgets.QWidget()
        self.modeTab.setObjectName("modeTab")
        self.topTabWidget.addTab(self.modeTab, "")
        self.customModeTab = QtWidgets.QWidget()
        self.customModeTab.setObjectName("customModeTab")
        self.topTabWidget.addTab(self.customModeTab, "")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.topTabWidget.addTab(self.settingsTab, "")
        self.exclusionsTab = QtWidgets.QWidget()
        self.exclusionsTab.setObjectName("exclusionsTab")
        self.topTabWidget.addTab(self.exclusionsTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.topTabWidget.addTab(self.helpTab, "")
        self.btmTabWidget = QtWidgets.QTabWidget(self.contentSplitter)
        self.btmTabWidget.setObjectName("btmTabWidget")
        self.actionsTab = QtWidgets.QWidget()
        self.actionsTab.setObjectName("actionsTab")
        self.btmTabWidget.addTab(self.actionsTab, "")
        self.exportTab = QtWidgets.QWidget()
        self.exportTab.setObjectName("exportTab")
        self.btmTabWidget.addTab(self.exportTab, "")
        self.updateTab = QtWidgets.QWidget()
        self.updateTab.setObjectName("updateTab")
        self.btmTabWidget.addTab(self.updateTab, "")
        self.verticalLayout_2.addWidget(self.contentSplitter)

        self.retranslateUi(RootBuilderMenu)
        self.topTabWidget.setCurrentIndex(0)
        self.btmTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RootBuilderMenu)

    def retranslateUi(self, RootBuilderMenu):
        _translate = QtCore.QCoreApplication.translate
        RootBuilderMenu.setWindowTitle(_translate("RootBuilderMenu", "Form"))
        self.topTabWidget.setTabText(self.topTabWidget.indexOf(self.modeTab), _translate("RootBuilderMenu", "Mode"))
        self.topTabWidget.setTabText(self.topTabWidget.indexOf(self.customModeTab), _translate("RootBuilderMenu", "Custom"))
        self.topTabWidget.setTabText(self.topTabWidget.indexOf(self.settingsTab), _translate("RootBuilderMenu", "Settings"))
        self.topTabWidget.setTabText(self.topTabWidget.indexOf(self.exclusionsTab), _translate("RootBuilderMenu", "Exclusions"))
        self.topTabWidget.setTabText(self.topTabWidget.indexOf(self.helpTab), _translate("RootBuilderMenu", "Help"))
        self.btmTabWidget.setTabText(self.btmTabWidget.indexOf(self.actionsTab), _translate("RootBuilderMenu", "Actions"))
        self.btmTabWidget.setTabText(self.btmTabWidget.indexOf(self.exportTab), _translate("RootBuilderMenu", "Export"))
        self.btmTabWidget.setTabText(self.btmTabWidget.indexOf(self.updateTab), _translate("RootBuilderMenu", "Update"))
