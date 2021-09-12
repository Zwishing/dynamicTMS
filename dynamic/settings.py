import os

DB_CONFIG = {
    'host': os.environ.get('POSTGRES_SERVICE_HOST', 'localhost'),
    'user': os.environ.get('POSTGRES_SERVICE_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_SERVICE_PASSWORD', 'admin'),
    'port': os.environ.get('POSTGRES_SERVICE_PORT', 5432),
    'database': os.environ.get('POSTGRES_SERVICE_DB_NAME', 'postgres')
}

PG_TILE_SERV = {
    # 'host': 'localhost',
    'host': '39.107.240.77',
    'port': 7800,
}
