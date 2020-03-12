import requests
import os
from get_geocoding_data import get_geocoding_data, get_formatted_address, get_zip_code
from get_street_view_data import extract_street_view_image_url

from constants import DOWNLOADED_DIR, DOWNLOADED_EXTENSION, DEFAULT_IMAGE_DIR


def get_default_image():
    print("using default image")
    return DEFAULT_IMAGE_DIR, "Currently Using Local Default Image"


def download_image(src, desc):
    try:
        img_data = requests.get(src).content
        with open(desc, 'wb') as handler:
            handler.write(img_data)
    except:
        pass


def get_image_url(address):

    geocode_res = get_geocoding_data(address)
    if geocode_res['status'] != 'OK':
        return get_default_image()

    zip_code = get_zip_code(geocode_res)
    if zip_code == None:
        return get_default_image()

    image_url = extract_street_view_image_url(address)

    file_name = f"{zip_code}-{address}"
    full_image_path = f"{DOWNLOADED_DIR}{file_name}{DOWNLOADED_EXTENSION}"
    file_existing = os.path.isfile(full_image_path)
    os.makedirs(DOWNLOADED_DIR, exist_ok=True)

    if file_existing == False:
        print("downloading image")
        download_image(image_url, full_image_path)
    else:
        print("image existing")
    print("src: ", image_url)
    print("des: ", full_image_path)
    return full_image_path, image_url
