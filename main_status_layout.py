from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QLabel
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtCore import Qt
from user_dict import user_dict, user_dict_fields, random_names
from main_backend import main
from LogWindow import LogWindow
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import logging
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #MainWindow.setStyleSheet(stylesheet)
        self.receivers = 0
        self.transmitters = 0
        self.receiver_list = []
        self.transmitter_list =[]

        self.log_window = LogWindow()
        
        font = QtGui.QFont("Arial", 10, QtGui.QFont.Weight.Bold)  # Set font to Arial, size 12, bold
        QtWidgets.QApplication.setFont(font)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 700)
        MainWindow.setMinimumSize(QtCore.QSize(598, 498))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.summ_layout_container_h = QtWidgets.QHBoxLayout()
        self.summ_layout_container_h.setObjectName("summ_layout_container_h")
        self.form_layou_summ_1 = QtWidgets.QFormLayout()
        self.form_layou_summ_1.setObjectName("form_layou_summ_1")
        self.ChannelLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ChannelLabel.setObjectName("ChannelLabel")
        self.form_layou_summ_1.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.ChannelLabel)
        self.TXModeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TXModeLabel.setObjectName("TXModeLabel")
        self.form_layou_summ_1.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.TXModeLabel)
        self.TRLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TRLabel.setObjectName("TRLabel")
        self.form_layou_summ_1.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.TRLabel)
        self.NameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NameLabel.setObjectName("NameLabel")
        self.form_layou_summ_1.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.NameLabel)
        self.NameAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NameAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.NameAnsLabel.setLineWidth(3)
        self.NameAnsLabel.setObjectName("NameAnsLabel")
        self.form_layou_summ_1.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NameAnsLabel)
        self.ChannelAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ChannelAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ChannelAnsLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.ChannelAnsLabel.setLineWidth(3)
        self.ChannelAnsLabel.setObjectName("ChannelAnsLabel")
        self.form_layou_summ_1.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ChannelAnsLabel)
        self.TXModeAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TXModeAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TXModeAnsLabel.setLineWidth(3)
        self.TXModeAnsLabel.setObjectName("TXModeAnsLabel")
        self.form_layou_summ_1.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.TXModeAnsLabel)
        self.TRAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TRAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TRAnsLabel.setLineWidth(3)
        self.TRAnsLabel.setObjectName("TRAnsLabel")
        self.form_layou_summ_1.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.TRAnsLabel)
        self.summ_layout_container_h.addLayout(self.form_layou_summ_1)
        self.form_layout_summ_2 = QtWidgets.QFormLayout()
        self.form_layout_summ_2.setObjectName("form_layout_summ_2")
        self.IPLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.IPLabel.setObjectName("IPLabel")
        self.form_layout_summ_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.IPLabel)
        self.LocationLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.LocationLabel.setObjectName("LocationLabel")
        self.form_layout_summ_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LocationLabel)
        self.ProtocolLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ProtocolLabel.setObjectName("ProtocolLabel")
        self.form_layout_summ_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.ProtocolLabel)
        self.ActivityLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ActivityLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.ActivityLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.ActivityLabel.setObjectName("ActivityLabel")
        self.form_layout_summ_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.ActivityLabel)
        self.IPAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.IPAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.IPAnsLabel.setLineWidth(3)
        self.IPAnsLabel.setObjectName("IPAnsLabel")
        self.form_layout_summ_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.IPAnsLabel)
        self.LocationAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.LocationAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.LocationAnsLabel.setLineWidth(3)
        self.LocationAnsLabel.setObjectName("LocationAnsLabel")
        self.form_layout_summ_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.LocationAnsLabel)
        self.ProtocolAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ProtocolAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ProtocolAnsLabel.setLineWidth(3)
        self.ProtocolAnsLabel.setObjectName("ProtocolAnsLabel")
        self.form_layout_summ_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ProtocolAnsLabel)
        self.ActivityAnsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.ActivityAnsLabel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ActivityAnsLabel.setLineWidth(3)
        self.ActivityAnsLabel.setObjectName("ActivityAnsLabel")
        self.form_layout_summ_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ActivityAnsLabel)
        self.summ_layout_container_h.addLayout(self.form_layout_summ_2)
        self.gridLayout.addLayout(self.summ_layout_container_h, 3, 1, 1, 1)

        ## Btns
        self.button_container_h = QtWidgets.QHBoxLayout()
        self.button_container_h.setContentsMargins(40, -1, 40, -1)
        self.button_container_h.setObjectName("button_container_h")


        
        self.add_transmitter_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_transmitter_btn.setObjectName("add_transmitter_btn")
        self.add_transmitter_btn.clicked.connect(self.add_transmitter)
        self.button_container_h.addWidget(self.add_transmitter_btn)

        self.add_receiver_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_receiver_btn.setObjectName("add_receiver_btn")
        self.add_receiver_btn.clicked.connect(self.add_receiver)
        
        self.button_container_h.addWidget(self.add_receiver_btn)

        self.start_simulation_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_simulation_btn.setObjectName("start_simulation_btn")
        self.start_simulation_btn.clicked.connect(self.start_simulation)
        self.button_container_h.addWidget(self.start_simulation_btn)
        self.stop_simulation_btn = QtWidgets.QPushButton(parent=self.centralwidget)


        self.stop_simulation_btn.setObjectName("stop_simulation_btn")
        self.button_container_h.addWidget(self.stop_simulation_btn)
        self.gridLayout.addLayout(self.button_container_h, 0, 1, 1, 1)


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabbed_window = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabbed_window.setMinimumSize(QtCore.QSize(393, 277))
        self.tabbed_window.setObjectName("tabbed_window")
        self.topology_tab = QtWidgets.QWidget()
        self.topology_tab.setObjectName("topology_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.topology_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")

        ## Graphics
        self.topology_layout = QGraphicsScene()
        self.topology_layout.setObjectName("topology_layout")
        self.topology_view = QGraphicsView(self.topology_layout)
        self.topology_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.gridLayout_2.addWidget(self.topology_view, 0, 0, 1, 1)
        self.tabbed_window.addTab(self.topology_tab, "")


        #self.status_tab = QtWidgets.QWidget()
        #self.status_tab.setObjectName("status_tab")
        #self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.status_tab)
        #self.verticalLayout_2.setObjectName("verticalLayout_2")
        #self.status_tab_form = QtWidgets.QFormLayout()
        #self.status_tab_form.setObjectName("status_tab_form")
        #self.verticalLayout_2.addLayout(self.status_tab_form)
        #self.tabbed_window.addTab(self.status_tab, "")
        self.result_tab = QtWidgets.QWidget()
        self.result_tab.setObjectName("result_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.result_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.result_tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 552, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.results_tab_form = QtWidgets.QFormLayout()
        self.results_tab_form.setObjectName("results_tab_form")
        self.verticalLayout_3.addLayout(self.results_tab_form)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tabbed_window.addTab(self.result_tab, "")
        self.logs_tab = QtWidgets.QWidget()
        self.logs_tab.setObjectName("logs_tab")
        self.logs = QtWidgets.QVBoxLayout(self.logs_tab)
        self.logs.setObjectName("logs")
        self.logs_tab_form = QtWidgets.QFormLayout()
        self.logs_tab_form.setObjectName("logs_tab_form")
        self.logs.addLayout(self.logs_tab_form)
        self.tabbed_window.addTab(self.logs_tab, "")
        self.horizontalLayout.addWidget(self.tabbed_window)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")

        ## User List Column
        self.user_list_container_v = QtWidgets.QVBoxLayout(self.widget)
        self.user_list_container_v.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.user_list_container_v.setSpacing(10)
        self.user_list_container_v.setObjectName("user_list_container_v")
        self.user_list_label = QtWidgets.QLabel(parent=self.widget)
        self.user_list_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.user_list_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.user_list_label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.user_list_label.setLineWidth(1)
        self.user_list_label.setObjectName("user_list_label")
        self.user_list_container_v.addWidget(self.user_list_label)
        self.user_list_form_layout = QtWidgets.QFormLayout()
        self.user_list_form_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.user_list_form_layout.setObjectName("user_list_form_layout")
        self.user_list_container_v.addLayout(self.user_list_form_layout)
        self.eve_check_box = QtWidgets.QCheckBox(parent=self.widget)
        self.eve_check_box.setCheckable(True)
        self.eve_check_box.setChecked(False)
        self.eve_check_box.setObjectName("eve_check_box")
        self.user_list_container_v.addWidget(self.eve_check_box)
        self.bits_combo_box = QtWidgets.QComboBox(parent=self.widget)
        self.bits_combo_box.setMaxVisibleItems(5)
        self.bits_combo_box.setObjectName("bits_combo_box")
        self.bits_combo_box.addItem("")
        self.bits_combo_box.addItem("")
        self.bits_combo_box.addItem("")
        self.bits_combo_box.addItem("")
        self.user_list_container_v.addWidget(self.bits_combo_box)
        self.protocol_combo_box = QtWidgets.QComboBox(parent=self.widget)
        self.protocol_combo_box.setObjectName("protocol_combo_box")
        self.protocol_combo_box.addItem("")
        self.protocol_combo_box.addItem("")
        self.user_list_container_v.addWidget(self.protocol_combo_box)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(174, 16777215))
        self.label.setObjectName("label")
        self.user_list_container_v.addWidget(self.label)
        self.repetition_slider = QtWidgets.QSlider(parent=self.widget)
        self.repetition_slider.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.repetition_slider.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.repetition_slider.setMaximum(5000)
        self.repetition_slider.setSingleStep(200)
        self.repetition_slider.setPageStep(500)
        self.repetition_slider.setProperty("value", 100)
        self.repetition_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.repetition_slider.setInvertedAppearance(False)
        self.repetition_slider.setInvertedControls(False)
        self.repetition_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.repetition_slider.setObjectName("repetition_slider")
        self.user_list_container_v.addWidget(self.repetition_slider)
        self.gridLayout.addWidget(self.widget, 0, 0, 4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ## hard coding the name and ip address feild to not leave initially empty
        self.user_list_form_layout.addRow(f"User   ", QLabel("I.P Address   "))

        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(parent=self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menusimulation = QtWidgets.QMenu(parent=self.menubar)
        self.menusimulation.setObjectName("menusimulation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_FIle = QtGui.QAction(parent=MainWindow)
        self.actionNew_FIle.setObjectName("actionNew_FIle")
        self.actionOpen_File = QtGui.QAction(parent=MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_File = QtGui.QAction(parent=MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExport = QtGui.QAction(parent=MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionCopy = QtGui.QAction(parent=MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtGui.QAction(parent=MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtGui.QAction(parent=MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind_All = QtGui.QAction(parent=MainWindow)
        self.actionFind_All.setObjectName("actionFind_All")
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPapers = QtGui.QAction(parent=MainWindow)
        self.actionPapers.setObjectName("actionPapers")
        self.actionResources = QtGui.QAction(parent=MainWindow)
        self.actionResources.setObjectName("actionResources")
        self.actionUser_manual = QtGui.QAction(parent=MainWindow)
        self.actionUser_manual.setObjectName("actionUser_manual")
        self.actionRun = QtGui.QAction(parent=MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionDebug = QtGui.QAction(parent=MainWindow)
        self.actionDebug.setObjectName("actionDebug")
        self.actionLogs = QtGui.QAction(parent=MainWindow)
        self.actionLogs.setObjectName("actionLogs")
        self.menuFIle.addAction(self.actionNew_FIle)
        self.menuFIle.addAction(self.actionOpen_File)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionSave_File)
        self.menuFIle.addAction(self.actionSave_As)
        self.menuFIle.addAction(self.actionExport)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionFind_All)
        self.menuHelp.addAction(self.actionPapers)
        self.menuHelp.addAction(self.actionResources)
        self.menuHelp.addAction(self.actionUser_manual)
        self.menusimulation.addAction(self.actionRun)
        self.menusimulation.addAction(self.actionDebug)
        self.menusimulation.addAction(self.actionLogs)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menusimulation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabbed_window.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QKD"))
        self.ChannelLabel.setText(_translate("MainWindow", "Channel"))
        self.TXModeLabel.setText(_translate("MainWindow", "TXMode"))
        self.TRLabel.setText(_translate("MainWindow", "T/R"))
        self.NameLabel.setText(_translate("MainWindow", "Name"))
        self.NameAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.ChannelAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.TXModeAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.TRAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.IPLabel.setText(_translate("MainWindow", "I.P"))
        self.LocationLabel.setText(_translate("MainWindow", "Location"))
        self.ProtocolLabel.setText(_translate("MainWindow", "Protocol"))
        self.ActivityLabel.setText(_translate("MainWindow", "Activity"))
        self.IPAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.LocationAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.ProtocolAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.ActivityAnsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.add_receiver_btn.setText(_translate("MainWindow", "Receiver"))
        self.add_transmitter_btn.setText(_translate("MainWindow", "Transmitter"))
        self.start_simulation_btn.setText(_translate("MainWindow", "Start Sim"))
        self.stop_simulation_btn.setText(_translate("MainWindow", "Stop Sim"))
        self.tabbed_window.setTabText(self.tabbed_window.indexOf(self.topology_tab), _translate("MainWindow", "Topology"))
        #self.tabbed_window.setTabText(self.tabbed_window.indexOf(self.status_tab), _translate("MainWindow", "Status"))
        self.tabbed_window.setTabText(self.tabbed_window.indexOf(self.result_tab), _translate("MainWindow", "Result"))
        self.tabbed_window.setTabText(self.tabbed_window.indexOf(self.logs_tab), _translate("MainWindow", "Logs"))

        self.user_list_label.setText(_translate("MainWindow", "Users Connected"))
        self.eve_check_box.setText(_translate("MainWindow", "Evesdropper"))
        self.bits_combo_box.setPlaceholderText(_translate("MainWindow", "Key Size(Bits)"))
        self.bits_combo_box.setItemText(0, _translate("MainWindow", "8"))
        self.bits_combo_box.setItemText(1, _translate("MainWindow", "16"))
        self.bits_combo_box.setItemText(2, _translate("MainWindow", "32"))
        self.bits_combo_box.setItemText(3, _translate("MainWindow", "64"))
        self.protocol_combo_box.setPlaceholderText(_translate("MainWindow", "Protocol"))
        self.protocol_combo_box.setItemText(0, _translate("MainWindow", "Differential Phase Shift (DPS)"))
        self.protocol_combo_box.setItemText(1, _translate("MainWindow", "Coherence One Way (COW)"))
        self.label.setText(_translate("MainWindow", "Repetitions :"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menusimulation.setTitle(_translate("MainWindow", "Run"))
        self.actionNew_FIle.setText(_translate("MainWindow", "New FIle"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionFind_All.setText(_translate("MainWindow", "Find All"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionPapers.setText(_translate("MainWindow", "Papers"))
        self.actionResources.setText(_translate("MainWindow", "Resources"))
        self.actionUser_manual.setText(_translate("MainWindow", "User manual"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
        self.actionLogs.setText(_translate("MainWindow", "Logs"))

    def add_receiver(self):
        try:
            
            pixmap = QtGui.QPixmap("./receiver.png")
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            item.setScale(0.25)
                
            text_item = QtWidgets.QGraphicsTextItem(f"‎Bob{self.receivers+1}/R{self.receivers+1}")
            text_item.setDefaultTextColor(QtCore.Qt.GlobalColor.black)
            text_item.setFont(QtGui.QFont("Arial", 10))

            text_item.setPos(0, item.pixmap().height() * 0.25)
            group = QtWidgets.QGraphicsItemGroup()
            group.addToGroup(item)
            group.addToGroup(text_item)


            group.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
            group.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges)
            group.setPos(100, 100)
            
            group.setData(0,f"receiver{self.receivers + 1}")
            group.mousePressEvent = lambda event, group=group: self.on_ellipse_clicked(event, group)
            self.receiver_list.append(group)
            self.add_users("receiver")
            
        except Exception as e:
            print(e)

    
    def add_transmitter(self):
        try:
            if self.transmitters < 1:
                t = 1
                pixmap = QtGui.QPixmap("./transmitter.png")
                item = QtWidgets.QGraphicsPixmapItem(pixmap)
                item.setScale(0.25)
                
                text_item = QtWidgets.QGraphicsTextItem(f"‎Alice{self.transmitters+1}/T{self.transmitters + 1}")
                text_item.setDefaultTextColor(QtCore.Qt.GlobalColor.black)
                text_item.setFont(QtGui.QFont("Arial", 10))

                text_item.setPos(0, item.pixmap().height() * 0.25)
                group = QtWidgets.QGraphicsItemGroup()
                group.addToGroup(item)
                group.addToGroup(text_item)


                group.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
                group.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges)
                group.setPos(100, 100)
            
                group.setData(0,f"transmitter{self.transmitters + 1}")
                group.mousePressEvent = lambda event, group=group: self.on_ellipse_clicked(event, group)
                self.transmitter_list.append(group)
                #self.all_users.append(item)
                self.add_users("transmitter")
                t += 1
            else:
                pass
        except Exception as e:
            print(e)

    def set_form_data(self,name):

        self.NameAnsLabel.setText(user_dict[name]['Name'])
        self.ChannelAnsLabel.setText(user_dict[name]['Channel'])
        self.TXModeAnsLabel.setText(user_dict[name]['Mode'])
        self.TRAnsLabel.setText(user_dict[name]['TR'])
        self.IPAnsLabel.setText(user_dict[name]['I.P Address'])
        self.LocationAnsLabel.setText(user_dict[name]['Location'])
        self.ProtocolAnsLabel.setText(user_dict[name]['Protocol'])
        self.ActivityAnsLabel.setText(user_dict[name]['Activity'])
        
    def on_ellipse_clicked(self, event, ellipse):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            name = ellipse.data(0)
            try:
                self.set_form_data(name)

            except Exception as e:
                print(e)


                
    def add_users(self, bit):
        # self.user_list_form_layout is the one I need to use
        self.add_to_json(bit)
        if bit == "receiver":
            self.receivers += 1
            self.user_list_form_layout.addRow(user_dict[f"receiver{self.receivers}"]["Name"] , QLabel(user_dict[f"receiver{self.receivers}"]["I.P Address"]))
            self.set_form_data(f"{bit}{self.receivers}")
        elif bit == "transmitter":
            self.transmitters += 1
            self.user_list_form_layout.addRow(user_dict[f"transmitter{self.transmitters}"]["Name"] , QLabel(user_dict[f"transmitter{self.transmitters}"]["I.P Address"]))
            self.set_form_data(f"{bit}{self.transmitters}")
        print(user_dict)
        self.draw()
        
    def generate_random_ip(self):
        return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"


    def add_to_json(self, bit):
        try:
            print("Starting add_to_json")
            user = {
                'Name': f"Alice{self.transmitters + 1}" if bit == "transmitter" else f"Bob{self.receivers + 1}" ,
                'I.P Address': self.generate_random_ip(),
                'Location': random.choice([
                    'Balanagar', 'Shadnagar', 'Jeedimetla']),
                'Protocol': self.protocol_combo_box.currentText(),
                'Channel': 'Classical' if bit == 'receiver' else 'Quantum',
                'Mode': 'Free Space Based',
                'Activity': 'Running',
                'TR': bit
            }
            print("User  data:", user, "\n\n")
            if bit == "receiver":
                user_dict[f"{bit}{self.receivers + 1}"] = user
            elif bit == "transmitter":
                user_dict[f"{bit}{self.transmitters + 1}"] = user
            print("User  dictionary after adding:", user_dict)
        except Exception as e:
            print(f"Error in add_to_json: {e}")
                

    def start_simulation(self):
        try:
            
            ## need to create log file with time stamp and be done
            
            self.log_window.clear_log()
            bits_value = int(self.bits_combo_box.currentText())
            if "DPS" in self.protocol_combo_box.currentText():
                protocol_value = 2
            elif "COW" in self.protocol_combo_box.currentText():
                protocol_value = 1

                
            eve_bool = self.eve_check_box.isChecked()
            rep_slider_value = self.repetition_slider.value()

            #### Need to start a loop trhough for all the recievers
            bob_list = []

            alice_basis = [np.random.randint(0, 2) for _ in range(bits_value)]
            alice_state = [np.random.randint(0, 2) for _ in range(bits_value)]
            for i in range(len(self.receiver_list)):
                bob_basis = [np.random.randint(0, 2) for _ in range(bits_value)]
                bob_list.append(main(alice_basis, alice_state, bob_basis, bits_value, eve_bool, rep_slider_value, protocol_value))
            
            for i in bob_list:
                self.show_results(i[0])

            self.results_tab_form.addRow(f"Alice Basis", QLabel(f": {bob_list[0][3][0]}"))
            self.results_tab_form.addRow(f"Alice bits", QLabel(f": {bob_list[0][3][2]}"))

            for i, v in enumerate(bob_list):
                self.results_tab_form.addRow(f"matchkey", QLabel(f": {v[1]}"))
                self.results_tab_form.addRow(f"mismatchkey", QLabel(f": {v[2]}"))
                self.results_tab_form.addRow(f"Bob Basis {i+1}", QLabel(f": {v[3][1]}"))
                self.plot_create([int(v[1]),int(v[2])], f"Bob{i+1}")
                pixmap = QPixmap("graphs/image.png")  # Replace with your image path

                image_label = QLabel()
                image_label.setPixmap(pixmap)
                self.results_tab_form.addRow(image_label)

            self.create_ext_log_file(bob_list)
            
        except Exception as e:
            print(e)
            
    def plot_create(self, values, filename):
        labels = ['Match Keys', 'Mismatch Keys']
        plt.bar(labels, values, color=['blue', 'orange'])

        plt.ylabel('Key Match Rate')
        plt.title('QKD Key Rate')
        plt.savefig(f'graphs/{filename}.png')
        plt.close()
        
    def create_ext_log_file(self,bob_list):
        filename = "__".join(time.asctime().split()).replace(":","_")
        self.logs_tab_form.addRow(time.asctime(), QLabel("Successfully logged result, check logs folder for more details"))
        file = open(f"logs/{filename}.txt", "a", encoding='utf-8')

        for objs in user_dict.keys():
            file.write(str(user_dict[objs]))
            file.write("\n")
        for i in bob_list:
            
            if self.eve_check_box.isChecked():
                file.write('\nalice eve circuit\n')
                file.write(i[0][0])
                file.write('\neve bob circuit\n')
                file.write(i[0][1])
                file.write('\n')
            else:
                file.write('\n')
                file.write(i[0][0])
                file.write('\n')
            file.write('matchkey : ')
            file.write(str(i[1]))
            file.write('\n')
            file.write('mismatchkey : ')
            file.write(str(i[2]))
            file.write('\n')
            for line in i[3]:
                file.write(line)
                file.write('\n')
            
            
        file.close()
        
            
            

    def show_results(self,sm):
        self.log_window.show()
        if self.eve_check_box.isChecked():
            self.log_window.add_log(" alice eve circuit\n\n")
            self.log_window.add_log(sm[0])
            self.log_window.add_log('\n\neve bob circuit \n\n')
            self.log_window.add_log(sm[1])
            self.log_window.add_log('\n\n')
        else:
            
            for i in sm:
                print("no eve")
                
                self.log_window.add_log(i)
                self.log_window.add_log('\n')

        self.log_window.add_log("Executed Successfully.")
            

##########################################################################
    def connecting_lines(self):
        if self.receivers > 0 and self.transmitters > 0:
            for i in self.receiver_list:
                for j in self.transmitter_list:
                    self.draw_line(i,j)

    def draw_line(self, item1, item2):
        pos1 = item1.pos() + QtCore.QPointF(item1.boundingRect().width() / 2, item1.boundingRect().height() / 2)
        pos2 = item2.pos() + QtCore.QPointF(item2.boundingRect().width() / 2, item2.boundingRect().height() / 2)
        
        line_item = QtWidgets.QGraphicsLineItem(QtCore.QLineF(pos1, pos2))
        line_item.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.red, 2))
        item1.setData(1, line_item)
        item2.setData(1,line_item)
        self.topology_layout.addItem(line_item)

        self.update_line(item1, item2, line_item)

    def update_line(self, item1, item2, line_item):
        pos1 = item1.pos() + QtCore.QPointF(item1.boundingRect().width() / 2, item1.boundingRect().height() / 2)
        pos2 = item2.pos() + QtCore.QPointF(item2.boundingRect().width() / 2, item2.boundingRect().height() / 2)

        line_item.setLine(QtCore.QLineF(pos1, pos2))

    def itemChange(self, item, change, value):
        if change == QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            line_item = item.data(1)
            if line_item:
                self.update_line(line_item)
        
    def draw(self):
        for i in self.receiver_list:
            self.topology_layout.addItem(i)
        for i in self.transmitter_list:
            self.topology_layout.addItem(i)
        #self.connecting_lines()
##################################################################        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
