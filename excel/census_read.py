#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for 
# each county.

import openpyxl
import pprint

def main():
    print('Opening workbook...')
    
    # Load the workbook and select the appropriate sheet
    wb = openpyxl.load_workbook('census_pop_data.xlsx')
    sheet = wb['Population by Census Tract']
    county_data = {}

    # Fill in county_data with each county's population and tracts
    print('Reading rows...')
    for row in sheet.iter_rows(min_row=2, values_only=True):
        state, county, pop = row[1], row[2], row[3]

        # Make sure the key for this state exists
        county_data.setdefault(state, {})
        # Make sure the key for this county in this state exists
        county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

        # Each row represents one census tract, so increment by one
        county_data[state][county]['tracts'] += 1
        # Increase the county pop by the pop in this census tract
        county_data[state][county]['pop'] += int(pop)

    # Open a new text file and write the contents of county_data to it
    print('Writing results...')
    with open('census_pop_data.py', 'w') as result_file:
        result_file.write('allData = ' + pprint.pformat(county_data))
    
    print('Done.')

if __name__ == '__main__':
    main()
