import psycopg2
from psycopg2.extensions import connection, cursor
from .logger import logger

def try_connect_to_db(
    host: str, database_name: str, user: str, password: str, port: str
):
    try:
        connect = psycopg2.connect(
            dbname=database_name,  # 데이터베이스 이름
            user=user,  # 사용자 이름
            password=password,  # 비밀번호
            host=host,  # 데이터베이스 호스트 (예: localhost, IP 주소)
            port=port,  # PostgreSQL 포트
        )
        cursor = connect.cursor()
        logger.info(f"Connected to database {database_name} on {host}:{port}")
        return connect, cursor
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        return None, None
    
    
# Create Table if not exists