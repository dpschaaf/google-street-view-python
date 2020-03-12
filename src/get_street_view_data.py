import requests
import json

from constants import STREET_IAMGE_KEY, STREET_METADATA_URL, STREET_IMAGE_URL, IMAGE_SIZE, FOV

API_KEY = STREET_IAMGE_KEY

def extract_street_view_metadata(address_or_latlng):
    location = address_or_latlng
    endpoint = f"{STREET_METADATA_URL}?size={IMAGE_SIZE}&fov={FOV}&location={location}&key={API_KEY}"
    res = requests.get(endpoint)
    return res.json()


def extract_street_view_image_url(address_or_latlng):
    location = address_or_latlng
    endpoint = f"{STREET_IMAGE_URL}?size={IMAGE_SIZE}&fov={FOV}&location={location}&key={API_KEY}"
    return endpoint
