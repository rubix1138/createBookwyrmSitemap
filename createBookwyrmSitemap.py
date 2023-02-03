import psycopg2
from typing import Iterator
from xml_sitemap_writer import XMLSitemap
from dotenv import load_dotenv
import os

rootUrl = 'https://dev-arm.bookwyrm.tech'
targetDir = '/opt/bookwyrm/sitemaps'

def connect_to_db():
    try:
        return psycopg2.connect(
            database=os.environ.get('POSTGRES_DB'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            host=os.environ.get('POSTGRES_HOST'),
            port=os.environ.get('PGPORT'),
        )
    except:
        return False

def get_products_for_sitemap() -> Iterator[str]:
    conn=connect_to_db()
    if conn:
        curr = conn.cursor()
        curr.execute("SELECT id FROM bookwyrm_book;")
        data = curr.fetchall()
        for idx in data:
            yield f"/book/{idx[0]}"
        conn.close()

with XMLSitemap(path=targetDir, root_url=rootUrl) as sitemap:
    sitemap.add_section('books')
    sitemap.add_urls(get_products_for_sitemap())
