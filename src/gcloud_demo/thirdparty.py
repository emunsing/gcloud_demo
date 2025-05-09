import os
import attr
import requests
import logging

GMAPS_API_KEY = os.getenv('GOOGLE_API_KEY')
ADDRESS_VALIDATION_URL = f'https://addressvalidation.googleapis.com/v1:validateAddress?key={GMAPS_API_KEY}'

@attr.s(auto_attribs=True, kw_only=True)
class Address:
    street_address: str = '' # Street address, e.g. "111 Main Street"
    city: str = '' #
    state: str = '' # state
    postal_code: str = '' # Zip code
    country: str = 'US'
    latitude: float = None # Latitude
    longitude: float = None

def validate_address(addr: Address) -> [Address, None]:
    """
    Accepts an address as a dictionary, returns updated address, latitude, and longitude.
    Adapted from https://github.com/emunsing/turfcutter
    """
    # Structure the address for the API request
    address = {
        "address": {
            "regionCode": addr.country,
            "postalCode": addr.postal_code,
            "administrativeArea": addr.state,
            "locality": addr.city,
            "addressLines": [addr.street_address]
        }
    }

    # Send request to Address Validation API
    response = requests.post(ADDRESS_VALIDATION_URL, json=address)
    result = response.json()

    if 'result' in result and 'geocode' in result['result']:
        validated_address = result['result']['address']
        try:
            corrected_address = Address(
                street_address=validated_address['postalAddress']['addressLines'][0],
                city=validated_address['postalAddress']['locality'],
                state=validated_address['postalAddress']['administrativeArea'],
                postal_code=validated_address['postalAddress']['postalCode'],
                country=validated_address['postalAddress']['regionCode'],
                latitude=result['result']['geocode']['location']['latitude'],
                longitude=result['result']['geocode']['location']['longitude']
            )
            return corrected_address
        except KeyError as e:
            logging.warning(f"Key error: {e}")
            return None
    else:
        logging.warning("Error:", result.get("error", "Unknown error"))
        return None