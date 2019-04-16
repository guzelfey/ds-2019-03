import logging
import requests


logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def scrap_process(self, storage):

        url = 'https://bioinfo-abcc.ncifcrf.gov/totem/results_template3.php?q=Treg+cancer&q_op=AND&rows=3000&wt=json'

        response = requests.get(url)

        if not response.ok:
            logger.error(response.text)
            # then continue process, or retry, or fix your code

        else:
            # Note: here json can be used as response.json
            data = response.text

            # save scrapped objects here
            storage.write_data([data.replace('\n', '')])
