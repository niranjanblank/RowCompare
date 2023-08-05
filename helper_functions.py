import pandas as pd

def find_common_elements_in_row(table):

    num_of_rows = len(table)

    common_elements_dict = dict()

    # loop over each row
    for i in range(num_of_rows):
        # common elements in a row with respect to other rows
        common_elements = []
        # for comparing with every other row
        for j in range(num_of_rows):
            # to avoid comparing with itself
            if i != j:
                # find common elements between rows
                # performs intersection between rows to get common elements
                common = set(table[i]) & set(table[j])
                # if common elements are greater than 3 then adding to the list
                if len(common) >= 3:
                    common_values = ",".join([str(x) for x in list(common)])
                    data_to_append = {f'Common With {str(j+1)}': common_values}
                    common_elements.append(data_to_append)
        common_elements_dict[f'Ticket {i + 1}'] = common_elements

    return common_elements_dict