import geopandas as gpd
from sqlalchemy import engine
from sqlalchemy import Table

def feature2postgis(fp, database, user, password, table_name, host='localhost',
                    port=5432, if_exists='replace', schema='public',dtype = None):
    """
        利用geopandas将要素导入postgis数据库，支持shp、geojson和geopandas的geodataframe格式
        :param fp: filepath文件路径或者GeoDataFrame类
        :param database: 数据库名称
        :param user: 用户名
        :param password: 密码
        :param table_name:存储的数表名称
        :param host:主机ip，默认localhost
        :param port:端口号，默认5432
        :param if_exists:  {'fail', 'replace', 'append'}, default 'replace'
                How to behave if the table already exists:
                - fail: Raise a ValueError.
                - replace: Drop the table before inserting new values.
                - append: Insert new values to the existing table.
        :param schema: 数据库中的位置，默认public
        """
    eng = engine.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    gdf = fp
    if not isinstance(fp, gpd.GeoDataFrame):
        gdf = gpd.read_file(fp, encoding='utf8')
    gdf.to_postgis(table_name, eng, if_exists=if_exists, schema=schema, index=True, index_label='gid',dtype = dtype)
    # 将gid设置为主键
    with eng.connect() as conn:
        conn.execute(f"ALTER TABLE {schema}.{table_name} ADD PRIMARY KEY (gid)")
    eng.dispose()
