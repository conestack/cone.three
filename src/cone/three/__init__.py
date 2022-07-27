from cone.app import main_hook
from cone.three.browser import configure_resources
import logging


logger = logging.getLogger('cone.three')


@main_hook
def initialize_three(config, global_config, settings):
    # application startup initialization

    # static resources
    configure_resources(settings)

    # scan browser package
    config.scan('cone.three.browser')
