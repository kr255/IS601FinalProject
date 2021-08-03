"""App entry point."""
import logging
import sys
from finalapp import create_app

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
stream_handler.stream = sys.stdout
print(sys.path)

app = create_app()
#
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)