"""This module handles getting images from databroker

"""

from databroker import DataBroker as db, get_images
import numpy as np


class DBHandler:
    def __init__(self, data_dict, key_list):
        self.key_list = key_list
        self.data_dict = data_dict

    def get_data(self, header_id=-1,
                 check_new_data=True, img_field_auto=True, img_field=None):
        """This method gets image data from a databroker header

        Parameters
        ----------
        header_id : int or str (optional)
            The id of the header, can be a uid, scan ID, or a slice such as -1
            if header_id is none the method defaults to db[-1]

        img_name : str (optional)
            the name of the image in question


        """
        header = self.get_header(header_id)
        if img_field_auto and (img_field is None):
            img_field_name = [key for key in header.descriptors[0]['data_keys']
                              if key.endswith('_image')[0]]
        else:
            img_field_name = img_field
        img_data = np.asarray(get_images(header, img_field_name).get_frame(0))
        uid = header['start']['uid']

        if self.is_new_data(uid) and check_new_data:
            return uid, img_data
        elif check_new_data is False:
            return uid, img_data
        else:
            return None

    def get_header(self, header_id=-1):
        """This method fetches a databroker header

        Parameters
        ----------

        header_id : int or str (optional)
            The id of the header, can be a uid, scan ID, or a slice such as -1
            if header_id defaults to db[-1]

        Returns
        -------
        Databroker Header


        """
        header = db[header_id]
        return header

    def is_new_data(self, uid):
        """Checks if the acquired header is not already in the list

        Parameters
        ----------

        uid : str
            The uid that will compared to the list to see if it is new

        Returns
        -------
        True if data is new
        False if data is not new
        """
        if uid in self.key_list:
            return False
        return True

    def get_images_range(self, db_start, db_stop):
        """this funciton will get all of the images in a specified range

        Parameters
        ----------
        db_start : int
            the starting slice
        """

        for i in range(db_start, db_stop):
            uid, img = self.get_data(header_id=i, check_new_data=False)

            self.key_list.append(uid)
            self.data_dict[uid] = img
            print("db header " + str(i) + " with UID " + uid + " added to dict")

    def is_dark_tiff(self, header):
        """Checks if the current database header represents a dark tiff

        Parameters
        ----------
        header : databroker header
            The databroker header to be checked

        Returns
        -------
        True if header represents dark tiff
        False if otherwise
        """
        if 'sc_dk_field_uid' in header.start:
            return True
        else:
            return False

    def dark_subtraction(self, header):

