import pymysql
import pytest

@pytest.fixture(scope="module")
def a():
    """Fixture: Connect to target DB (MySQL in this example)"""
    c = pymysql.connect(
        host="localhost",      # change to your DB host
        user="root",
        password="1234",
        database="sql_inventory"      # use your target DB/schema
    )
    yield c
    c.close()

def test_ri_check(a):
 cursor = a.cursor()
 cursor.execute("""
                SELECT product_id
                FROM products
                where product_id = '1'
                """)
 ri = cursor.fetchall()
 cursor.close()

 assert len(ri) == 1, "RI check Pass : {ri}"
 print (ri)

