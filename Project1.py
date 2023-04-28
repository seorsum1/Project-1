import sys
from PyQt5 import QtWidgets
from mainUI import Ui_mainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.cart = {"cookie": 0, "sandwich": 0, "water": 0}
        self.prices = {"cookie": 1.5, "sandwich": 4, "water": 1}

        self.init_visibility()

        self.shopButton.clicked.connect(self.show_shop_items)
        self.doneButton.clicked.connect(self.hide_shop_items)
        self.cartButton.clicked.connect(self.show_cart)
        self.resetButton.clicked.connect(self.reset_cart)
        self.cookieButton.clicked.connect(lambda: self.add_item("cookie"))
        self.sandwichButton.clicked.connect(lambda: self.add_item("sandwich"))
        self.waterButton.clicked.connect(lambda: self.add_item("water"))

    def init_visibility(self):
        self.cookieButton.setVisible(False)
        self.sandwichButton.setVisible(False)
        self.waterButton.setVisible(False)
        self.cookieLabel.setVisible(False)
        self.sandwichLabel.setVisible(False)
        self.waterLabel.setVisible(False)
        self.doneButton.setVisible(False)

    def close_app(self):
        self.close()

    def add_item(self, item):
        self.cart[item] += 1
        if self.cart[item] == 1:
            self.outputLabel.setText(f"Added {self.cart[item]} {item.capitalize()}")
        elif item == 'sandwich':
            self.outputLabel.setText(f"Added {self.cart[item]} {item.capitalize()}es")
        else:
            self.outputLabel.setText(f"Added {self.cart[item]} {item.capitalize()}s")
        self.outputLabel.repaint()

    def show_cart(self):
        self.update_output_label()

    def reset_cart(self):
        self.cart = {"cookie": 0, "sandwich": 0, "water": 0}
        self.update_output_label()

    def show_shop_items(self):
        self.shopButton.setVisible(False)
        self.cartButton.setVisible(False)
        self.cookieButton.setVisible(True)
        self.sandwichButton.setVisible(True)
        self.waterButton.setVisible(True)
        self.cookieLabel.setVisible(True)
        self.sandwichLabel.setVisible(True)
        self.waterLabel.setVisible(True)
        self.doneButton.setVisible(True)
        self.outputLabel.setText("")
        self.outputLabel.repaint()

    def hide_shop_items(self):
        self.shopButton.setVisible(True)
        self.cartButton.setVisible(True)
        self.cookieButton.setVisible(False)
        self.sandwichButton.setVisible(False)
        self.waterButton.setVisible(False)
        self.cookieLabel.setVisible(False)
        self.sandwichLabel.setVisible(False)
        self.waterLabel.setVisible(False)
        self.doneButton.setVisible(False)
        self.outputLabel.setText("")
        self.outputLabel.repaint()

    def update_output_label(self):
        output = []
        total_cost = 0

        for item, count in self.cart.items():
            if count > 0:
                cost = count * self.prices[item]
                output.append(f'{item.capitalize()} ({count})= ${cost:.2f}')
                total_cost += cost

        if output:
            output.append(f'\nGRAND TOTAL = ${total_cost:.2f}')
        else:
            output.append('Cart empty!')

        self.outputLabel.setText('\n'.join(output))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
