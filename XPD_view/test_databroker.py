from databroker_handler import DBHandler
from databroker import DataBroker as db

DBH = DBHandler(dict(), list())

print(DBH.is_dark_tiff(db['970eae9d']))
print(db['970eae9d']['start'].sp_plan_name)

DBH.get_data(check_new_data=False)