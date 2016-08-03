"""This module handles getting images from databroker

"""

from databroker import DataBroker as db, get_table, get_images


class DBHandler:
    def __init__(self, data_dict, key_list):
        self.key_list = key_list
        self.data_dict = data_dict

    def get_data(self, header_id=None):
        """This method gets image data from a databroker header

        Parameters
        ----------
        header_id : int or str (optional)
            The id of the header, can be a uid, scan ID, or a slice such as -1
            if header_id is none the method defaults to db[-1]

        """


    def get_header(self, header_id=None):
        """This method fetches a databroker header

        header_id : int or str (optional)
            The id of the header, can be a uid, scan ID, or a slice such as -1
            if header_id is none the method defaults to db[-1]

        """