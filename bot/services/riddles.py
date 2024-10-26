import logging
from json import JSONDecodeError

import requests

from ..settings import settings

logger = logging.getLogger(__name__)

REQUEST_SETTINGS = settings.REQUEST_SETTINGS.to_dict()
REQUEST_SETTINGS['cert'] = tuple(REQUEST_SETTINGS.get('cert', []))


class RiddleService:
    BASE_URL = settings.BASE_RIDDLES_API_URL
    DEFAULT_REQUEST_SETTINGS = REQUEST_SETTINGS
    
    @classmethod
    def get_riddle(cls):
        try:
            response = requests.get(cls.BASE_URL, **cls.DEFAULT_REQUEST_SETTINGS)

            if not response.ok:
                logger.warning(f'Did not retrieve requested resource.  Reason: Received "{response.status_code}: {response.reason}"')

                return

            return response.json()

        except requests.RequestException as e:
            logger.error(f'Did not retrieve requested stats.  Reason: Encountered a Request Error.  Error: {e}')
            logger.debug('Traceback: ', exc_info=e)

            return
        
        except JSONDecodeError as e:
            logger.error(f'Did not process requested resource.  Reason: Could not JSON decode response data.  Error: {e}')
            logger.debug('Traceback: ', exc_info=e)

            return
