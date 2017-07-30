import logging
import sys

from darkskypy import DarkSkyPy

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(level=logging.CRITICAL)
logging.getLogger("chardet").setLevel(level=logging.CRITICAL)
logging.getLogger("darkskypy").setLevel(level=logging.DEBUG)

log = logging.getLogger(__name__)


def main():
    darksky = DarkSkyPy(sys.argv[1])
    # weather = darksky.weather(-34.9286, 138.5999)
    darksky.latitude = 12.3
    darksky.longitude = -32.1
    print(darksky.url)
    darksky._extend = True
    print(darksky.url)
    pass


if __name__ == "__main__":
    main()
