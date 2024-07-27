# Problem

Quicko does not current support ICICI direct template. Thus we have to manually add the data to the quicko template, and the upload it to account capital gains.

# Idea

A python script to automate conversion of icici direct capital gains to quicko template.

**Note: only works for Stocks (not MF, bonds, etc)**

# How to use

1. Download trade-wise capital gain excel from ICICI direct.
2. The formal will be xls. Open in excel.
3. Remove all the useless details and just have the table with the header row and values.
4. Export the updated XLS as CSV using excel with the file name as icici.csv.
5. Download the quicko template xlsx and rename it to template.xlsx  
6. Run main.py
7. It will update the template.xlsx with the new Stocks.

# How to Contribute

_There are lot of scope for improvement, thus contributions are highly encouraged_

1. Raise a pull request explaining your changes.

