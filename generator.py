import logging
import uuid


def generate_uuid():
    generator_logger = logging.getLogger('generator')
    str_uuid = str(uuid.uuid4())
    generator_logger.warning(f'generator.py : {str_uuid}')
    return str_uuid