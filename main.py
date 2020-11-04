import logging
import generator

import native_logger

# initialize once
native_logger.configure_rotating_logger('generator')

# initialize when you want to use
generator_logger = logging.getLogger('generator')
for i in range(10):
    generator_logger.warning(f'main.py : {generator.generate_uuid()}')
