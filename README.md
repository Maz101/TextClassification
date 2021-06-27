## Details:

In the `data` folder, you will find one `csv` file containing real text from medical trials scraped from ClinicalTrials.gov. Each row contains a `description` with text information about the trial and a corresponding `label` that identifies the disease or condition that it pertains to. There is an additional field `nctid` that describes the trial id that the row pertains to.

Provided with this repo is also a `main.py` file with a minimal [Flask](https://flask.palletsprojects.com/en/1.1.x/) demo. Once you have installed the `requirements.txt` in your python environment you will be able to run the main file by simply calling `python main.py` inside your directory. This should start the local server and you should be able to see `Hello World!` in your browser at `http://127.0.0.1:5000/`.

## The Task - Done

Your task is to use the data to make a model capable of predicting a specific label given an unseen trial description.

You may assume that descriptions passed will always be relevant to at least one of the labels.

You should treat the `description` column as your input (X) and the `label` column as the output category (y) that you are trying to predict.

The `label` distribution is the following:

| `label`                       | Number of Examples |
| ----------------------------- | :----------------: |
| Dementia                      |        368         |
| ALS                           |        368         |
| Obsessive Compulsive Disorder |        358         |
| Scoliosis                     |        335         |
| Parkinson’s Disease           |        330         |

The `description` column contains plain text that explains the trial in a short description.

Your model should then be served through the small [Flask](https://flask.palletsprojects.com/en/1.1.x/) file provided. Feel free to extend it or split the file as needed.

### Exploration

Exploratory model analysis and data analysis was done in the Notebook.

### Serving the solution through Flask

The model implemented will serve the solution through (`main.py`).

The API can be tested using the `test.py` file although it is important to make sure the server is running by calling `python main.py` in another terminal window.

