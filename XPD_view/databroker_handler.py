"""This module handles getting images from databroker

"""

from databroker import DataBroker as db, get_images


class DBHandler:
    def __init__(self, data_dict, key_list):
        self.key_list = key_list
        self.data_dict = data_dict

    def get_data(self, header_id=None, check_new_data=True):
        """This method gets image data from a databroker header

        Parameters
        ----------
        header_id : int or str (optional)
            The id of the header, can be a uid, scan ID, or a slice such as -1
            if header_id is none the method defaults to db[-1]


        """
        header = self.get_header(header_id)
        img_data = get_images(header, 'pe1_image').get_frame(0)
        uid = header['start']['uid']

        if self.is_new_data(uid) and check_new_data:
            self.data_dict[uid] = img_data
            self.key_list.append(uid)


    def get_header(self, header_id=None):
        """This method fetches a databroker header

        Parameters
        ----------

        header_id : int or str (optional)
            The id of the header, can be a uid, scan ID, or a slice such as -1
            if header_id is none the method defaults to db[-1]

        Returns
        -------
        Databroker Header


        """
        if header_id is None:
            header = db[-1]
        else:
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
        for i in range(0, len(self.key_list), -1):
            if uid == self.key_list(i):
                return False
        return True

    def get_images_range(self, db_start, db_stop):
        """this funciton will get all of the images
        """

        for i in range()
