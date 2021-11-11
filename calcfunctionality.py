from PyQt5 import QtWidgets, uic, QtGui
import subprocess
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
    row1 = float(calcform.quantity.text()) * float(calcform.price.text())
    row2 = float(calcform.quantity_2.text()) * float(calcform.price_2.text())
    row3 = float(calcform.quantity_3.text()) * float(calcform.price_3.text())
    row4 = float(calcform.quantity_4.text()) * float(calcform.price_4.text())
    row5 = float(calcform.quantity_5.text()) * float(calcform.price_5.text())
    row6 = float(calcform.quantity_6.text()) * float(calcform.price_6.text())
    row7 = float(calcform.quantity_7.text()) * float(calcform.price_7.text())
    row8 = float(calcform.quantity_8.text()) * float(calcform.price_8.text())
    row9 = float(calcform.quantity_9.text()) * float(calcform.price_9.text())
    row10 = float(calcform.quantity_10.text()) * float(calcform.price_10.text())

    prodprice = float(calcform.productprice.text())
    result = "$" + str(prodprice-(row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9 + row10))
    calcform.label_12.setText(result)

def populateFields(component_name, price_name):

    with open('itemPrices.csv', 'r')as f:
        data = csv.reader(f)
        entries = []
        for row in data:
            entries.append(row)
        product = entries[1][0]
        price = entries[1][1].lstrip('$')
    component_name.setText(str(product))
    price_name.setText(str(price))
    f.close()

def writeLinkToRow(component_name):

    with open('itemPrices.csv', 'w', newline='')as f:
        writer = csv.writer(f)
        writer.writerows([["items", "prices", "url"],["","",component_name.text()]])
    f.close()

    subprocess.run(['python','priceScraper.py'])

def componententer(comp_number):                #Text box call functionality

    if comp_number == 1:
        writeLinkToRow(calcform.component)
        populateFields(calcform.component, calcform.price)

    elif comp_number == 2:
        writeLinkToRow(calcform.component_2)
        populateFields(calcform.component_2, calcform.price_2)

    elif comp_number == 3:
        writeLinkToRow(calcform.component_3)
        populateFields(calcform.component_3, calcform.price_3)

    # elif comp_number == 4:
    #
    # elif comp_number == 5:
    #
    # elif comp_number == 6:
    #
    # elif comp_number == 7:
    #
    # elif comp_number == 8:
    #
    # elif comp_number == 9:
    #
    # elif comp_number == 10:


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




