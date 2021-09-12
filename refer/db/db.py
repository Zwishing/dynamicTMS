import psycopg2
from PIL import Image
from io import BytesIO
import numpy as np
import time
import mercantile

conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='admin',
    host='localhost',
    port="5432"
)
start = time.time()
cur = conn.cursor()
table = 'raster_data.gf1_20210222'
sql = """
  SELECT ST_EXTENT(rast::geometry) FROM {0} WHERE rid=1
""".format(table)
cur.execute(sql)
rows = cur.fetchall()
print(rows[0][0])
tile = mercantile.bounding_tile(117.2091389688099952,31.5469355246168988,117.2880448628000067,31.6136325638866005)
print(tile)
bound = mercantile.bounds(tile)
print(bound)
print(time.time() - start)
# print(rows[0][0].tobytes())
# with open('t.png', 'wb+') as fp:
#     fp.write(rows[0][0].tobytes())

conn.close()
