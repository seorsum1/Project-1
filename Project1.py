import sys
from PyQt5 import QtWidgets
from mainUI import Ui_mainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.cart = {"cookie": 0, "sandwich": 0, "water": 0}
        self.prices = {"cookie": 1.5, "sandwich": 4, "water": 1}

        self.shopButton.clicked.connect(self.show_cart)
        self.exitButton.clicked.connect(self.close_app)
        self.cartButton.clicked.connect(self.show_cart)
        self.cookieButton.clicked.connect(lambda: self.add_item("cookie"))
        self.sandwichButton.clicked.connect(lambda: self.add_item("sandwich"))
        self.waterButton.clicked.connect(lambda: self.add_item("water"))

    def close_app(self):
        self.close()

    def add_item(self, item):
        self.cart[item] += 1
        self.update_output_label()

    def show_cart(self):
        self.update_output_label()

    def update_output_label(self):
        output = []
        total_cost = 0

        for item, count in self.cart.items():
            if count > 0:
                cost = count * self.prices[item]
                output.append(f'({count}) {item.capitalize()} = ${cost:.2f}')
                total_cost += cost

        output.append('-' * 20)
        output.append(f'GRAND TOTAL = ${total_cost:.2f}')
        output.append('-' * 20)

        self.outputLabel.setText('\n'.join(output))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
