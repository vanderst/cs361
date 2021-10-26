from PyQt5 import QtWidgets, uic, QtGui
import csv

app = QtWidgets.QApplication([])
mainmenu = uic.loadUi("main.ui")
calcform = uic.loadUi("calcform.ui")

def profilebuttonclick():   #opens profile
    calcform.exec()
    calcform.show()

def saveprofile():                  #Saves profile
    calcform.label_2.setText(calcform.lineEdit.text())
    mainmenu.pushButton.setText(calcform.lineEdit.text())

def backtoprofile():                                    #Back button functionality
    calcform.close()
    mainmenu.show()

def calculateprofit():                                  #Calculation functionality
    row1 = int(calcform.quantity.text()) * int(calcform.price.text())
    row2 = int(calcform.quantity_2.text()) * int(calcform.price_2.text())
    row3 = int(calcform.quantity_3.text()) * int(calcform.price_3.text())
    row4 = int(calcform.quantity_4.text()) * int(calcform.price_4.text())
    row5 = int(calcform.quantity_5.text()) * int(calcform.price_5.text())
    row6 = int(calcform.quantity_6.text()) * int(calcform.price_6.text())
    row7 = int(calcform.quantity_7.text()) * int(calcform.price_7.text())
    row8 = int(calcform.quantity_8.text()) * int(calcform.price_8.text())
    row9 = int(calcform.quantity_9.text()) * int(calcform.price_9.text())
    row10 = int(calcform.quantity_10.text()) * int(calcform.price_10.text())

    prodprice = int(calcform.productprice.text())
    result = str(prodprice-(row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9 + row10))
    calcform.label_12.setText(result)


def componententer(comp_number):                #Text box call functionality

    with open('dummydata.csv', 'rt')as f:
        data = csv.reader(f)
        entries = []
        for row in data:
            entries.append(row)
        product = entries[0][0]
        price = entries[0][1]

    if comp_number == 1:
        calcform.price.setText(str(price))
        calcform.component.setText(str(product))

    elif comp_number == 2:
        calcform.price_2.setText(str(price))
        calcform.component_2.setText(str(product))

    elif comp_number == 3:
        calcform.price_3.setText(str(price))
        calcform.component_3.setText(str(product))

    elif comp_number == 4:
        calcform.price_4.setText(str(price))
        calcform.component_4.setText(str(product))

    elif comp_number == 5:
        calcform.price_5.setText(str(price))
        calcform.component_5.setText(str(product))

    elif comp_number == 6:
        calcform.price_6.setText(str(price))
        calcform.component_6.setText(str(product))

    elif comp_number == 7:
        calcform.price_7.setText(str(price))
        calcform.component_7.setText(str(product))

    elif comp_number == 8:
        calcform.price_8.setText(str(price))
        calcform.component_8.setText(str(product))

    elif comp_number == 9:
        calcform.price_10.setText(str(price))
        calcform.component_9.setText(str(product))

    elif comp_number == 10:
        calcform.price_9.setText(str(price))
        calcform.component_10.setText(str(product))
    calcform.exec()
    calcform.show()


# Button Actions
mainmenu.pushButton.clicked.connect(profilebuttonclick)
mainmenu.pushButton_2.clicked.connect(profilebuttonclick)
mainmenu.pushButton_3.clicked.connect(profilebuttonclick)
mainmenu.pushButton_4.clicked.connect(profilebuttonclick)
mainmenu.pushButton_5.clicked.connect(profilebuttonclick)
mainmenu.pushButton_6.clicked.connect(profilebuttonclick)
mainmenu.pushButton_7.clicked.connect(profilebuttonclick)
mainmenu.pushButton_8.clicked.connect(profilebuttonclick)
mainmenu.pushButton_9.clicked.connect(profilebuttonclick)


calcform.component.returnPressed.connect(lambda : componententer(1))
calcform.component_2.returnPressed.connect(lambda: componententer(2))
calcform.component_3.returnPressed.connect(lambda: componententer(3))
calcform.component_4.returnPressed.connect(lambda: componententer(4))
calcform.component_5.returnPressed.connect(lambda: componententer(5))
calcform.component_6.returnPressed.connect(lambda: componententer(6))
calcform.component_7.returnPressed.connect(lambda: componententer(7))
calcform.component_8.returnPressed.connect(lambda: componententer(8))
calcform.component_9.returnPressed.connect(lambda: componententer(9))
calcform.component_10.returnPressed.connect(lambda: componententer(10))


calcform.pushButton_3.clicked.connect(calculateprofit)
calcform.pushButton_4.clicked.connect(saveprofile)
calcform.pushButton.clicked.connect(backtoprofile)

mainmenu.show()
app.exec_()


