import os
import time
from constants import APPEND_HEADERS, ADDRESS_INF_HEADERS

def check_blank_row(row, cnt, status_pos, writer, address_pos):
    # checking blank row
    is_blank_row = False
    for pos in address_pos:
        if not row[pos]:
            is_blank_row = True
            break

    if is_blank_row == True:
        print(f"Incomplete Address, Please check again {cnt + 1} th row in the origin CSV data...\n\n\n")
        row.insert(status_pos, 'ERROR')
        writer.writerow(row)
        time.sleep(1)

    return is_blank_row

def get_full_address_from_heading_pos(row, address_pos):
    address = []

    # get address
    for col in address_pos:
        address.append(row[col])

    # full joined address
    full_address = ', '.join(address)
    return full_address

def get_street_head_positions(header):
    positions = []

    print("--------------------------------------------------")
    print("Checking Address Information Headings...\n")
    time.sleep(1)

    for idx, head_item in enumerate(ADDRESS_INF_HEADERS):
        print(f"No {idx + 1}: checking '{head_item}'")
        time.sleep(1)

        pos = idx + 1
        try:
            pos = header.index(head_item)
            print(f"Column: {pos + 1}(1 based index)\n")
        except ValueError:
            print(
                f"Error, Please check if there is {head_item} heading in the first line\n")
            pass
        positions.append(pos)

    print(f"address information headings indexes: {positions}\n\n")
    return positions


def append_headings(header, writer):
    print("--------------------------------------------------")
    print("Appending Header Columns to the origin\n")
    time.sleep(1)

    for head_item in APPEND_HEADERS:
        if head_item not in header:
            print(f"appending '{head_item}'")
            time.sleep(1)
            header.append(head_item)
    writer.writerow(header)
