from app import main

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

if __name__ == "__main__":
    main.run()
