# The PyPDF2 module allows you to work with PDF files in Python, including reading, writing, and manipulating them. 
# One of the most commonly used methods of this module is the PdfFileReader() method, which is used to read a PDF file. 
# Here's an example of how to use it:
import PyPDF2

# Open the PDF file
pdf_file = open('sample.pdf', 'rb')

# Create a PdfFileReader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Print the number of pages in the PDF file
print(pdf_reader.numPages)

# Close the PDF file
pdf_file.close()

# Another useful method of the PyPDF2 module is the PdfFileWriter() method, which is used to create a new PDF file or add pages to an existing one. 
# Here's an example of how to use it:
import PyPDF2

# Create a new PDF file
pdf_writer = PyPDF2.PdfFileWriter()

# Add a page to the PDF file
pdf_writer.addPage(pdf_reader.getPage(0))

# Save the PDF file
with open('new.pdf', 'wb') as pdf_file:
    pdf_writer.write(pdf_file)

# Next, let's take a look at the csv module. 
# This module allows you to work with CSV files in Python, including reading, writing, and manipulating them. One of the most commonly used methods of this module is the reader() method, which is used to read a CSV file. 
# Here's an example of how to use it:
import csv

# Open the CSV file
with open('sample.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Iterate over the rows in the CSV file
    for row in csv_reader:
        print(row)

# Another useful method of the csv module is the writer() method, which is used to write data to a CSV file. 
# Here's an example of how to use it:
import csv

# Create some data to write to the CSV file
data = [['Name', 'Age', 'City'], ['John', '30', 'New York'], ['Jane', '25', 'Chicago']]

# Open the CSV file
with open('new.csv', 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)
    
    # Write the data to the CSV file
    csv_writer.writerows(data)

# It is possible to use both the PyPDF2 and csv modules together to extract data from a PDF file and automatically fill it into a CSV file.
# Here's an example of how to do this:
import PyPDF2
import csv

# Open the PDF file
with open('sample.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    # Extract the text from the first page of the PDF file
    page = pdf_reader.getPage(0)
    pdf_text = page.extractText()

# Open the CSV file
with open('sample.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Split the PDF text by new lines
    lines = pdf_text.split('\n')
    for line in lines:
        # Split each line by commas
        fields = line.split(',')
        csv_writer.writerow(fields)