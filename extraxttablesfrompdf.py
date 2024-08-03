import tabula
import pandas as pd

# Read PDF
tables = tabula.read_pdf('BluePlus_Rates.pdf', pages='all', multiple_tables=True)

# Print extracted tables
for i, table in enumerate(tables):
    print(f"Table {i}")
    print(table)

# Create a Pandas Excel writer
writer = pd.ExcelWriter('extracted_tables.xlsx', engine='xlsxwriter')

# Write each table to a different sheet in the Excel file
for i, table in enumerate(tables):
    table.to_excel(writer, sheet_name=f'Table_{i}', index=False)

# Save the Excel file
writer.close()
