import sys
from PyQt5 import QtWidgets
from mainUI import Ui_mainWindow
from typing import Dict

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)
        self.cart: Dict[str, int] = {"cookie": 0, "sandwich": 0, "water": 0}
        self.prices: Dict[str, float] = {"cookie": 1.5, "sandwich": 4, "water": 1}

        self.hide_shop_items()

        self.shopButton.clicked.connect(self.show_shop_items)
        self.doneButton.clicked.connect(self.hide_shop_items)
        self.cartButton.clicked.connect(self.show_cart)
        self.resetButton.clicked.connect(self.reset_cart)
        self.cookieButton.clicked.connect(lambda: self.add_item("cookie"))
        self.sandwichButton.clicked.connect(lambda: self.add_item("sandwich"))
        self.waterButton.clicked.connect(lambda: self.add_item("water"))

    def add_item(self, item: str) -> None:
        """
        Add an item and quantity to the cart and update the output label.

        Args:
            item (str): The item to be added to the cart.
        """
        item_quantity = f'{item}Quantity'
        quantity = getattr(self, item_quantity).toPlainText()
        try:
            if quantity.isdigit():
                quantity = int(quantity)
                self.cart[item] += quantity
                if self.cart[item] == 1:
                    self.outputLabel.setText(f"{self.cart[item]} {item.capitalize()} in cart")
                elif item == 'sandwich':
                    self.outputLabel.setText(f"{self.cart[item]} {item.capitalize()}es in cart")
                else:
                    self.outputLabel.setText(f"{self.cart[item]} {item.capitalize()}s in cart")
            else:
                raise ValueError
        except(ValueError):
            self.outputLabel.setText('Error, Enter Integers Only!')
        self.outputLabel.repaint()

    def show_cart(self) -> None:
        """
        Update the output label to display the cart contents.
        """
        self.update_output_label()

    def reset_cart(self) -> None:
        """
        Reset the cart and update the output label.
        """
        self.cart = {"cookie": 0, "sandwich": 0, "water": 0}
        self.update_output_label()

    def show_shop_items(self) -> None:
        """
        Show shop items and their respective buttons and labels.
        """
        self.shopButton.setVisible(False)
        self.cartButton.setVisible(False)
        self.cookieButton.setVisible(True)
        self.sandwichButton.setVisible(True)
        self.waterButton.setVisible(True)
        self.cookieQuantity.setVisible(True)
        self.sandwichQuantity.setVisible(True)
        self.waterQuantity.setVisible(True)
        self.cookieLabel.setVisible(True)
        self.sandwichLabel.setVisible(True)
        self.waterLabel.setVisible(True)
        self.doneButton.setVisible(True)
        self.outputLabel.setText("")
        self.outputLabel.repaint()

    def hide_shop_items(self) -> None:
        """
        Hide shop items and their respective buttons and labels.
        """
        self.shopButton.setVisible(True)
        self.cartButton.setVisible(True)
        self.cookieButton.setVisible(False)
        self.sandwichButton.setVisible(False)
        self.waterButton.setVisible(False)
        self.cookieQuantity.setVisible(False)
        self.sandwichQuantity.setVisible(False)
        self.waterQuantity.setVisible(False)
        self.cookieLabel.setVisible(False)
        self.sandwichLabel.setVisible(False)
        self.waterLabel.setVisible(False)
        self.doneButton.setVisible(False)
        self.outputLabel.setText("")
        self.outputLabel.repaint()

    def update_output_label(self) -> None:
        """Update the output label with the current cart contents and total cost."""
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
    