
### pypi and pip
# python modules download (https://pypi.org/)
# allows you tu search like(https://yelp.com)

# Package for working with excel spreadsheet (https://pypi.org/openpyxl)
# to install: pip install openpyxl
# done in pycharm

import openpyxl as xl
from openpyxl.chart import BarChart, Reference


wb = xl.load_workbook("newDeliveryPrice.xlsx")  # Loading the workbook
sheet = wb["Sheet1"] # Accessing a particular sheet
cell = sheet["a1"] # Accessing a cell

# NOW PLOT A GRAPH OF YOUR WORK
# using the File of the transaction, update the address by deducting 100 from all delivery
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row,5)
    updated_price = cell.value - 100
    updated_price_cell = sheet.cell(row, 6)
    updated_price_cell.value = updated_price

values = Reference(sheet,
          min_row=2,
          max_row=sheet.max_row,
          min_col=5,
          max_col=5)
chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, 'f2')
wb.save("newDeliveryPrice.xlsx")


# Challenge:
# Refactor your code so that it can be reusable for automating different kind of files


# ORGANIZE CODE AND PLACE FUNCTIONS WHERE NEED BE
import openpyxl as xl
from openpyxl.chart import BarChart, Reference

def process_workbook(filename):
    wb = xl.load_workbook(filename)  # Loading File
    sheet = wb["sheet1"]

    for row in range(2, sheet.max_row + 1):
        cell = sheet.cell(row,5)
        updated_price = cell.value - 100
        updated_price_cell = sheet.cell(row, 6)
        updated_price_cell.value = updated_price

    values = Reference(sheet,
                min_row=2,
                max_row=sheet.max_row,
                min_col=5,
                max_col=5)
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'f2')
    wb.save(filename)




# complete package topic 


# import the files

import openpyxl as xl
from openpyxl.chart import BarChart, Reference


wb = xl.load_workbook("newDeliveryPrice.xlsx")  # Loading the workbook
sheet = wb["Sheet1"] # Accessing a particular sheet
cell = sheet["a1"] # Accessing a cell
print(cell.value)
cell1 = sheet.cell(1, 1) # cell printing using sheet
print(cell1.value)

print(sheet.max_row) # checks for the total number of rows in a spreadsheet

#iterate and print all the values
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    print(cell.value)


# print values for column 1
for column in range(1,sheet.max_column + 1):
    cell = sheet.cell(column, 1)
    print(cell.value)

# add a new File with a price drop of 12% and place the values in a new cell

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row,3)
    corrected_price = cell.value * 0.12
    corrected_price_cell = sheet.cell(row, 4)
    corrected_price_cell.value = corrected_price

wb.save('newTransactions.xlsx')

# using the File of the transaction, update the address by deducting 100 from all delivery
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row,5)
    updated_price = cell.value - 100
    updated_price_cell = sheet.cell(row, 6)
    updated_price_cell.value = updated_price

wb.save("newDeliveryPrice.xlsx")



# NOW PLOT A GRAPH OF YOUR WORK
# using the File of the transaction, update the address by deducting 100 from all delivery
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row,5)
    updated_price = cell.value - 100
    updated_price_cell = sheet.cell(row, 6)
    updated_price_cell.value = updated_price

values = Reference(sheet,
          min_row=2,
          max_row=sheet.max_row,
          min_col=5,
          max_col=5)
chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, 'f2')
wb.save("newDeliveryPrice.xlsx")




# ORGANIZE CODE AND PLACE FUNCTIONS WHERE NEED BE
import openpyxl as xl
from openpyxl.chart import BarChart, Reference

def process_workbook(filename):
    wb = xl.load_workbook(filename)  # Loading File
    sheet = wb["sheet1"]

    for row in range(2, sheet.max_row + 1):
        cell = sheet.cell(row,5)
        updated_price = cell.value - 100
        updated_price_cell = sheet.cell(row, 6)
        updated_price_cell.value = updated_price

    values = Reference(sheet,
                min_row=2,
                max_row=sheet.max_row,
                min_col=5,
                max_col=5)
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'f2')
    wb.save(filename)



# Machine Learning with Python
