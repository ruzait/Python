from openpyxl import Workbook

# Create workbook
wb = Workbook()

# Create workSheet
sheet = wb.active

# value asiagn
sheet["A2"] = "Santra"
sheet["B1"] = "E-tech"

try:
    # Save
    wb.save(filename="example.xlsx")
except Exception as e:
    print(e)