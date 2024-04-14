""" zid_project1.py

"""
import json
import os
import tempfile
from random import sample

import toolkit_config as cfg

from yf_example1 import tic

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
ROOTDIR = os.path.join('C:','Users','amin9','toolkit','toolkit')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')

# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {'Volume':14 , 'Date':11, 'Adj Close':19 , 'Close': 10, 'Open': 6, 'High': 20}


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
    Each non-empty line of the file is guaranteed to have the following format:

    "XXXX"="YYYY"

    where:
        - XXXX represents an exchange.
        - YYYY represents a ticker.

    This function should return a dictionary, where each key is a properly formatted
    ticker, and each value the properly formatted exchange corresponding to the ticker.

    Parameters
    ----------
    pth : str
        Full path to the location of the TICKERS.txt file.

    Returns
    -------
    dict
        A dictionary with format {<tic> : <exchange>} where
            - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
            - Each value (<exchange>) is a string containing the exchange for this ticker.

    Notes
    -----
    The keys and values of the dictionary returned must conform with the following rules:
        - All characters are in lower case
        - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
        - No spaces
        - No empty tickers or exchanges

    """
    # <COMPLETE THIS PART>
    ticker_dict = {}
    with open(pth, 'r') as file:
        for line in file:
            ticker_and_exchange = line.strip().split('.')
            if len(ticker_and_exchange) == 2:
                exchange, ticker = ticker_and_exchange
                ticker_dict[ticker.strip()] = exchange.strip()  #scaler.com
    return ticker_dict

def test_get_tics():   #stackoverflow.com
    temp_dir = tempfile.gettempdir()
    test_this_code = os.path.join(temp_dir, 'TICKER.txt')

test_data ="""NASDAQ"="INTC"
"NYSE"="ABBV"
"NASDAQ"="FB"""

with open(test_this_code, 'y') as temp_file:
        temp_file.write(sample.data.strip())  #scaler.com

result = get_tics(test_this_code)

expected_result ={
    "INTC": "NASDAQ",
    "ABBV": "NYSE",
    "FB": "NASDAQ"
}

#verifying results
if result == expected_result:
        print("Test passed successfully.")
else:
        print("Test failed.")
    #deleting temp file
os.remove(test_this_code)
# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(tic):
    """ Returns a list with the lines of the ".dat" file containing the stock
    price information for the ticker `tic`.


    Parameters
    ----------
    tic : str
        Ticker symbol, in lower case.

    Returns
    -------
    list
        A list with the lines of the ".dat" file for this `tic`. Each element
        is a line in the file, without newline characters (e.g. '\n')


    Hints (optional)
    ----------------
    - Create a variable with the location of the relevant file using the `os`
      module, the `DATDIR` constant, and f-strings.

    """
    # IMPORTANT: The answer to this question should NOT include full paths
    # like "C:\\Users...". There should be no forward or backslashes.
    # <COMPLETE THIS PART>
file_pathway = os.path.join(DATDIR, f"{tic}.dat")
line = []
with open (file_pathway, 'r') as file:
    line = [lines.strip() for lines in file.readlines()]
    #return line



# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """Returns the information contained in a line of a ".dat" file as a
    dictionary, where each key is a column name and each value is a string
    with the value for that column.

    This line will be split according to the field width in `COLWIDTHS`
    of each column in `COLUMNS`.

    Parameters
    ----------
    line : str
        A line from ".dat" file, without any newline characters

    Returns
    -------
    dict
        A dictionary with format {<col> : <value>} where
        - Each key (<col>) is a column in `COLUMNS` (as a string)
        - Each value (<value>) is a string containing the correct value for
          this column.

    Hints (optional)
    ----------------
    - Your solution should include the constants `COLUMNS` and `COLWIDTHS`
    - For each line in the file, extract the correct value for each column
      sequentially.

    """
    # <COMPLETE THIS PART>
def line_to_dict(line):
    COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']
    COLWIDTHS = {'Volume': 14, 'Date': 11, 'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}

    begin = 0
    line_data = {}

    for col in COLUMNS:
        width = COLWIDTHS[col]

        value = line[begin:begin+width].strip()

        line_data[col] = value

        begin += width
    return line_data
print(line_to_dict())

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst=None):
    """Verifies if the tickers provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        tic_exchange_dic : dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If tickers_lst is not None, raise an Exception if any of the below rules are violated:
            1. tickers_lst is an empty list.

            2. tickers_lst contains a ticker that does not correspond to a key tic_exchange_dic

               Example:
               If tic_exchange_dic is {'tsm':'nyse', 'aal':'nasdaq'},
               tickers_lst = ['aal', 'Tsm'] would raise an Exception because
               'Tsm' is not a key of tic_exchange_dic.

    """
    # <COMPLETE THIS PART>
    if tickers_lst is not None:
        pass

    if not tickers_lst:
        raise Exception ('tickers_list is an empty list')
    for ticker in tickers_lst:
        if tickers_lst.lower() not in tic_exchange_dic:
            raise Exception (f'The Ticker {ticker} is not similar to any key in tic_exchange_dic')

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_cols(col_lst=None):
    """Verifies if the column names provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        col_lst : list, optional
            A list containing column names (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If col_lst is not None, raise an Exception if any of the below rules are violated:
            1. col_lst is an empty list.

            2. col_lst contains a column that is not found in `COLUMNS`.

               Example:
               If COLUMNS = ['Close', 'Date'],
               col_lst = ['close'] would raise an Exception because 'close' is not found in `COLUMNS`

    """
    # <COMPLETE THIS PART>

def verify_cols(col_lst=None, ticker_number_1=None):
    if ticker_number_1 is not None:
        if not ticker_number_1:
            raise Exception (f"Ticker is empty")
        for ticker in ticker_number_1:
            if ticker.lower() not in col_lst:
                raise Exception (f"Ticker '{ticker}' does not correspond with a key in col_1st")


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """Returns a dictionary containing the data for the tickers specified in tickers_lst.
        An Exception is raised if any of the tickers provided in tickers_lst or any of the
        column names provided in col_lst are invalid.

        Parameters
        ----------
        tic_exchange_dic: dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings)

        col_lst : list, optional
            A list containing column names (as strings)

        Returns
        -------
        dict
            A dictionary with format {<tic> : <data>} where
            - Each key (<tic>) is a ticker in tickers_lst (as a string)
            - Each value (<data>) is a dictionary with format
                {
                    'exchange': <tic_exchange>,
                    'data': [<dict_0>, <dict_1>, ..., <dict_n>]
                }
              where
                - <tic_exchange> refers to the exchange that <tic> belongs to in lower case.
                - <dict_0> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[0]),
                  but that only contains the columns listed in col_lst
                - <dict_n> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[-1]),
                  but that only contains the columns listed in col_lst

        Notes
        -----
        - Please refer to the assessment description for an example of what the returned dictionary should look like.
        - If tickers_lst is None, the dictionary returned should contain the data for
          all tickers found in tic_exchange_dic.
        - If col_lst is None, <dict_0>, <dict_1>, ... should contain all the columns found in `COLUMNS`

        Hints (optional)
        ----------------
        - To check if tickers_lst contains any invalid tickers, you can call `verify_tickers`
        - To check if col_lst contains any invalid column names, you can call `verify_cols`
        - This function should call the `read_dat` and `line_to_dict` functions

    """
    # <COMPLETE THIS PART>

    if col_lst is not None:
        verify_cols(col_lst)
    if tickers_lst is not None:
        verify_tickers(tickers_lst)
    if tickers_lst is not None:
        verify_tickers(tic_exchange_dic)
    if tickers_lst is None:
        tickers_lst = list(tic_exchange_dic)

result = {}
for ticker in tickers_lst:
        tic_exchange_dic = tic_exchange_dic.lower()
        ticker_content = read_dat()
        sorting_data = {k:'v' for k, v in line_to_dict(line).items()}

        result[ticker] = {tic_exchange_dic : 'exchange',
        sorting_data : 'data'}

print(data_dict)



# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """Saves the data found in the data_dict dictionary into a
        JSON file whose name is specified by pth.

        Parameters
        ----------
        data_dict: dict
            A dictionary returned by the `create_data_dict` function

        pth : str
            The complete path to the output JSON file. This is where the file with
            the data will be saved.


        Returns
        -------
        None
            This function does not return anything

    """
    # <COMPLETE THIS PART>
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    json_data = json.dumps(data_dict, indent = 4)
    with open(pth, 'w') as file:
        file.write(json_data)
print(f'Data saved to {json_pth}')


    # ----------------------------------------------------------------------------
#    Please put your answers for the last question here:
# ----------------------------------------------------------------------------

#1 -It is good to configure at the beginning is because for the following:
    #1) ROOTDIR allows the below code to be portable because it establishes a central reference point
    #for the project, allowing the project to run from other devices
    #2) DATDIR is a dedicated path handling method that creates paths to data files and by creating
    # at the beginning, it ensures that processing files can be easily located
    #3) TICPATH - adding path allows python to run smoothly while maintaining errors.

#
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#  Uncomment the statements below to call the test and/or main functions.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Test functions
    # _test_get_tics()
    # _test_read_dat()
    # _test_line_to_dict()
    # _test_create_data_dict()
    # _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
    pass





