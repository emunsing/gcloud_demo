import thirdparty
import numpy as np
import click
import logging

CA_ZIP_RANGE = (90001, 96162)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--n', default=10, help='Number of random addresses to generate.')
def request_ramdom_addresses(n):
    """
    Request random addresses from the third-party API.
    """
    for i in range(n):
        zipcode = np.random.randint(*CA_ZIP_RANGE)
        lat, lon = thirdparty.get_lat_long(zipcode)
        logging.warning(f"Zipcode: {zipcode}, Lat: {lat}, Lon: {lon}")

if __name__ == '__main__':
    cli()