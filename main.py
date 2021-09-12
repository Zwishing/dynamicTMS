
from refer.edit.upload import feature2postgis
from sqlalchemy import VARCHAR,INTEGER


def main(fp):
    DB_CONFIG = {
        'database': 'postgres',
        'user': 'postgres',
        'password': 'admin',
        'host': 'localhost',
    }
    dtype = {
        'RVCD': VARCHAR(255),
        'gid': INTEGER,
    }
    table_name = 'riv'

    feature2postgis(fp=fp, table_name=table_name,dtype = dtype,**DB_CONFIG)

if __name__ == '__main__':
    fp = '/usr/src/river/river.geojson'
    main(fp)
