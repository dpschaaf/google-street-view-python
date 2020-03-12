from API_KEY import GEOCODE_API_KEY, STREET_IAMGE_KEY
# Test Files

SRC_FILE_URL = 'assets/csv/src.csv'
DES_FILE_URL = 'assets/csv/des.csv'

# Google Map Geocoding

GEOCODE_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"


# Google Map Street View

STREET_METADATA_URL = "https://maps.googleapis.com/maps/api/streetview/metadata"
STREET_IMAGE_URL = "https://maps.googleapis.com/maps/api/streetview"

API_KEY = STREET_IAMGE_KEY
IMAGE_SIZE = '600x400'
FOV = 70


# Default Download Format

DOWNLOADED_DIR = 'assets/downloads/'
DOWNLOADED_EXTENSION = '.jpg'
DEFAULT_IMAGE_DIR = 'assets/default.png'

# Table Header

ADDRESS_INF_HEADERS = ['Image Street',
                       'Image City', 'Image State', 'Image Zip']
APPEND_HEADERS = ['Status', 'Location', 'URL']
