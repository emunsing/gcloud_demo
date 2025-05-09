import thirdparty
import numpy as np
import click
import logging

CA_ZIP_RANGE = (90001, 96162)

# A set of randomly generated but vetted zip codes which contain main street
ZIPCODES_WITH_MAIN_STREET = ["90242", "96054", "91361", "91566", "91880", "93723", "92545",
                             "92064", "90003", "94042", "92119", "90061", "92806", "93319",
                             "92410", "92990", "90519", "92793", "93105", "92662", "91244",
                             "93649", "91364" ]

@click.group()
def cli():
    pass


@cli.command()
@click.option('--n', default=100, help='Number of random addresses to generate.')
@click.option('--random-zip', is_flag=True, help='Generate random addresses.')
def request_ramdom_addresses(n, random_zip):
    """
    Request random addresses from the third-party API.
    """
    for i in range(n):
        if random_zip:
            zip_code = np.random.randint(*CA_ZIP_RANGE)
        else:
            zip_code = np.random.choice(ZIPCODES_WITH_MAIN_STREET)
        address_request = thirdparty.Address(postal_code=str(zip_code),
                                             street_address=f"{np.random.randint(1, 100)} Main St"
                                             )
        updated_address = thirdparty.validate_address(address_request)
        if updated_address is None:
            continue
        if address_request.postal_code not in updated_address.postal_code:
            logging.warning(f"Street address does not exist in zip {address_request.postal_code}")
        else:
            logging.warning(f"{updated_address.street_address}, {updated_address.city} {updated_address.postal_code}: {updated_address.latitude}, {updated_address.longitude}")

if __name__ == '__main__':
    cli()