import csv, time
from get_street_view_data import extract_street_view_metadata
from metadata_processor import metadata_processor
from constants import SRC_FILE_URL, DES_FILE_URL
from spreadsheet_processor import append_headings, get_street_head_positions, check_blank_row, get_full_address_from_heading_pos


src_file = open(SRC_FILE_URL)
des_file = open(DES_FILE_URL, 'w')

csv_reader_object = csv.reader(src_file)
csv_writer_object = csv.writer(des_file)

print(f"\nReading data from {SRC_FILE_URL}...\n")
time.sleep(1)

# get head itemšs
header = next(csv_reader_object)

address_pos = get_street_head_positions(header)
append_headings(header, csv_writer_object)
status_pos = header.index('Status')

cnt = 0

print("\n\n--------------------------------------------------")
print("Data Processing\n")
time.sleep(1)

for row in csv_reader_object:
    print("--------------------------------------------------")

    # curren data
    total_data = row
    cnt += 1

    is_blank = check_blank_row(row, cnt, status_pos, csv_writer_object, address_pos)
    if is_blank == True:
        continue

    full_address = get_full_address_from_heading_pos(row, address_pos)
    print(f"No {cnt}: {full_address}")

    # get street view data
    street_view_data = extract_street_view_metadata(full_address)

    # get status metadata
    status = street_view_data['status']
    total_data.append(status)


    # get image data
    image_data = metadata_processor(full_address, status)

    print("\n" * 2)
    try:
        downloaded_url = image_data[0]
        google_img_url = image_data[1]
    except:
        total_data[status_pos] = 'ERROR'
        print(f"Error Cannot get addresses, Please check again {cnt + 1} th row in the origin CSV data...\n\n\n")
        csv_writer_object.writerow(total_data)
        continue

    total_data.append(downloaded_url)
    total_data.append(google_img_url)

    # save row
    csv_writer_object.writerow(total_data)

print("end")

src_file.close()
des_file.close()
