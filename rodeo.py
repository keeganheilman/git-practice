# import re

def rename_rodeo_columns(columns):
    #ends_with_data_expression = re.compile('Data\s*$')
    columns = [column.lower().replace(' data', '').replace(' ', '_') for column in columns]
    #columns = [re.replace(ends_with_data_expression, '', column) for column in columns]
    return columns



if __name__ == '__main__':
    # Create a list of exmple original column names
    original = [
        'Participant Count Data',
        'Rodeo Clown Count',
        'Hats Visible',
        'Cost Data',
    ]

    # Get the corrected column names
    corrected = rename_rodeo_columns(original)

    # Print a table to compare original and corrected names
    print('Original                  Corrected')
    print('--------                  ---------')
    for o, c in zip(original, corrected):
        print(f'{o:<25} {c:<25}')
