from sqlalchemy import create_engine
import pandas as pd


username = 'root'
password = '123456789'
host = 'pavani'
port = '3306' 
database = 'sales_product_db'

def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )



