import pytesseract
import openpyxl


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try:
  # Load the image and perform OCR on it
  image = "1.jpeg"
  text = pytesseract.image_to_string(image)

  # Split the OCR text into lines
  lines = text.split("\n")

  # Create a new workbook and add a sheet to it
  workbook = openpyxl.Workbook()
  sheet = workbook.active

  # Write the extracted information to the sheet
  for i, line in enumerate(lines):
    sheet.cell(row=i+1, column=1).value = line

  # Save the workbook to a file
  workbook.save("output.xlsx")

except Exception as e:
  # Handle any exceptions that may occur
  print(f"An error occurred: {e}")
