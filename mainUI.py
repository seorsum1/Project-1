from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(500, 750)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(500, 750))
        mainWindow.setMaximumSize(QtCore.QSize(500, 750))
        
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(175, 30, 150, 30))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.mainLabel.setFont(font)
        self.mainLabel.setScaledContents(False)
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        
        self.shopButton = QtWidgets.QPushButton(self.centralwidget)
        self.shopButton.setGeometry(QtCore.QRect(200, 150, 100, 40))
        self.shopButton.setObjectName("shopButton")
        
        self.doneButton = QtWidgets.QPushButton(self.centralwidget)
        self.doneButton.setGeometry(QtCore.QRect(375, 645, 100, 40))
        self.doneButton.setObjectName("doneButton")
        
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(25, 645, 100, 40))
        self.resetButton.setObjectName("resetButton")
        
        self.cartButton = QtWidgets.QPushButton(self.centralwidget)
        self.cartButton.setGeometry(QtCore.QRect(200, 250, 100, 40))
        self.cartButton.setObjectName("cartButton")
        
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(50, 475, 400, 150))
        self.outputLabel.setObjectName("outputLabel")
        
        self.cookieQuantity = QtWidgets.QTextEdit(self.centralwidget)
        self.cookieQuantity.setGeometry(QtCore.QRect(270, 150, 60, 40))
        self.cookieQuantity.setFont(font)
        self.cookieQuantity.setObjectName("cookieQuantity")
        
        self.sandwichQuantity = QtWidgets.QTextEdit(self.centralwidget)
        self.sandwichQuantity.setGeometry(QtCore.QRect(270, 250, 60, 40))
        self.sandwichQuantity.setFont(font)
        self.sandwichQuantity.setObjectName("sandwichQuantity")
        
        self.waterQuantity = QtWidgets.QTextEdit(self.centralwidget)
        self.waterQuantity.setGeometry(QtCore.QRect(270, 350, 60, 40))
        self.waterQuantity.setFont(font)
        self.waterQuantity.setObjectName("waterQuantity")
        
        self.cookieButton = QtWidgets.QPushButton(self.centralwidget)
        self.cookieButton.setGeometry(QtCore.QRect(350, 150, 100, 40))
        self.cookieButton.setObjectName("cookieButton")
        
        self.sandwichButton = QtWidgets.QPushButton(self.centralwidget)
        self.sandwichButton.setGeometry(QtCore.QRect(350, 250, 100, 40))
        self.sandwichButton.setObjectName("sandwichButton")
        
        self.waterButton = QtWidgets.QPushButton(self.centralwidget)
        self.waterButton.setGeometry(QtCore.QRect(350, 350, 100, 40))
        self.waterButton.setObjectName("waterButton")
        
        font.setPointSize(12)
        
        self.cookieLabel = QtWidgets.QLabel(self.centralwidget)
        self.cookieLabel.setGeometry(QtCore.QRect(40, 150, 130, 40))
        self.cookieLabel.setFont(font)
        self.cookieLabel.setObjectName("cookieLabel")
        
        self.sandwichLabel = QtWidgets.QLabel(self.centralwidget)
        self.sandwichLabel.setGeometry(QtCore.QRect(40, 250, 150, 40))
        self.sandwichLabel.setFont(font)
        self.sandwichLabel.setObjectName("sandwichLabel")
        
        self.waterLabel = QtWidgets.QLabel(self.centralwidget)
        self.waterLabel.setGeometry(QtCore.QRect(40, 350, 150, 40))
        self.waterLabel.setFont(font)
        self.waterLabel.setObjectName("waterLabel")
        
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Michael\'s Shop"))
        self.mainLabel.setText(_translate("mainWindow", "Main Menu"))
        self.shopButton.setText(_translate("mainWindow", "Shop!"))
        self.doneButton.setText(_translate("mainWindow", "Done"))
        self.resetButton.setText(_translate("mainWindow", "Reset Cart"))
        self.cartButton.setText(_translate("mainWindow", "View Cart"))
        self.outputLabel.setText(_translate("mainWindow", ""))
        self.cookieQuantity.setText(_translate("mainWindow", '1'))
        self.sandwichQuantity.setText(_translate("mainWindow", '1'))
        self.waterQuantity.setText(_translate("mainWindow", '1'))
        self.cookieButton.setText(_translate("mainWindow", "Add to cart"))
        self.sandwichButton.setText(_translate("mainWindow", "Add to cart"))
        self.waterButton.setText(_translate("mainWindow", "Add to cart"))
        self.cookieLabel.setText(_translate("mainWindow", "Cookie - $1.50 ea"))
        self.sandwichLabel.setText(_translate("mainWindow", "Sandwich - $1.50 ea"))
        self.waterLabel.setText(_translate("mainWindow", "Water - $1.50 ea"))
