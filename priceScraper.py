import csv
from requests_html import HTMLSession

# The following getAmazonPrice function is adapted from the code shown in the following video: https://www.youtube.com/watch?v=WcPNlnsNZyY
def getAmazonPrice(list):

    for row in list:
        if row[0] == "items":
            continue
        session = HTMLSession()
        amazonUrl = row[2]
        itemInfo = session.get(amazonUrl)
        itemInfo.html.render(sleep=1)
        row[0] = itemInfo.html.xpath('//*[@id="productTitle"]', first=True).text

        try:
            row[1] = itemInfo.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
        except:
            row[1] = "N/A"

    # print(list)

# Reads file named "itemPrices.csv" and creates a new list with the existing info
# itemPrices.csv should have three columns, and the first row should be "items,prices,url"
# Any row after that should be formatted like the following example: ",,https://www.amazon.com/PlayStation-DualSense-Wireless-Controller-Midnight-5/dp/B094WL86N5/ref=sr_1_6?keywords=ps5&qid=1636487722&sr=8-6"
# Items and prices cells should be an empty, and url cells should contain the URL of the item you want to price scrape on Amazon
# The following CSV read is adapted from Roy learns to code's answer on StackOverflow: https://stackoverflow.com/questions/3699927/writing-to-a-particular-cell-using-csv-module-in-python

print("Reading itemsPrices.csv...")
with open('itemPrices.csv', 'r+') as itemPrices:
    reader = csv.reader(itemPrices)

    itemList = list(reader)
    itemPrices.close()

# print(itemList)

print("Retrieving item names and prices...")
getAmazonPrice(itemList)

# Writes new info into the existing CSV and modifies items and prices cells
# The following CSV read is adapted from Roy learns to code's answer on StackOverflow: https://stackoverflow.com/questions/3699927/writing-to-a-particular-cell-using-csv-module-in-python
print("Modifying itemPrices.csv with item names and prices...")
with open('itemPrices.csv', 'w', newline='') as newItemPrices:
    writer = csv.writer(newItemPrices)
    writer.writerows(itemList)
    newItemPrices.close()

print("Finished!")