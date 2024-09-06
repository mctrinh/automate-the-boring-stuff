import openpyxl

def update_prices(workbook_path, sheet_name, price_updates, output_path):
    # Load the workbook and select the sheet
    wb = openpyxl.load_workbook(workbook_path)
    sheet = wb[sheet_name]  # Updated method for accessing sheet
    
    # Loop through the rows and update the prices
    print('Updating prices...')
    for row in sheet.iter_rows(min_row=2, max_col=2, values_only=False):  # Iterate over rows, only the first two columns
        produce_name = row[0].value
        if produce_name in price_updates:
            row[1].value = price_updates[produce_name]
    
    # Save the updated workbook
    wb.save(output_path)
    print(f'Updated sales data saved to {output_path}')

# Define the produce types and their updated prices
PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}

# Run the function to update prices
update_prices('excel_sales.xlsx', 'Sheet', PRICE_UPDATES, 'excel_sales_updated.xlsx')
