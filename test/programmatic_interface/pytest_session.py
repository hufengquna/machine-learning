"""@pytest_session

This module will test the following sessions:

  - data_new: stores supplied dataset into a SQL database.
  - data_append: appends supplied dataset to an already stored dataset in an
                 SQL database.
  - model_generate: generate an model by selecting a particular range of
                    dataset (session), and store it into a NoSQL cache.
  - model_predict: generate a prediction by selecting a particular cached
                   model from the NoSQL cache.

  Note: this module requires the installation of 'pytest':

      - pip install pytest

  Then, this script can be run as follows:

      - py.test session.py
      - py.test /somedirectory

  Note: pytest will recursively check subdirectories for python scripts, from
        the current working directory.

  Note: this module is recommended to be run from the directory containing the
        'pytest.ini', as the current working directory.

"""
import requests
import json
import os.path

data_new = 'http://localhost:5000/data_new/'
data_append = 'http://localhost:5000/data_append/'
model_generate = 'http://localhost:5000/model_generate/'
model_predict = 'http://localhost:5000/model_predict/'

headers = headers={'Content-Type': 'application/json'}

def get_sample_json():
    """@get_sample_json

    Get a sample json dataset.

    """

    json_dataset = None
    with open(os.path.join('..', 'interface', 'static', 'data', 'json', 'programmatic_interface', 'sample-1.json'), 'r') as json_file:
        json_dataset = json.load(json_file)
    return json.dumps(json_dataset)

def check_data_new():
    """@check_data_new

    This method tests the 'data_new' session.

    """

    assert requests.post(data_new, headers=headers, data=get_sample_json())

def check_data_append():
    """@check_data_append

    This method tests the 'data_append' session.

    """

    assert requests.post(data_append, headers=headers, data=get_sample_json())
