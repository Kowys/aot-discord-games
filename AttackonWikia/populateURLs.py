import sqlite3
import asyncio
from AttackonWikia import fetchURL

class PopulateURLsObj:
    def __init__(self, client):
        self.client = client
        self.populate_urls_obj = self.client.loop.create_task(self.populate_urls())

    async def populate_urls(self):
        get_infos = [
            fetchURL.get_puzzle,
            fetchURL.get_hangman,
            fetchURL.get_image
        ]
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(0.1)
            valid_modes = [0,0,0]
            try:
                url = 'https://attackontitan.wikia.com/wiki/Special:Random'
                page_url, page_title, pagetext = fetchURL.getPage(url)
            except Exception as e:
                print(e)
                continue

            if page_title:
                for i, get_info in enumerate(get_infos):
                    try:
                        question_set = get_info(page_url, page_title, pagetext)
                        if question_set != None:
                            valid_modes[i] = 1
                    except Exception as e:
                        print(page_title, e)
                        continue

            try:
                conn = sqlite3.connect('AttackonWikia/aow_db.db')
                cursor = conn.cursor()

                url_query = 'SELECT puzzle, hangman, image FROM urls WHERE url = ?'
                cursor.execute(url_query, (page_url,))
                url_info = cursor.fetchone()

                if url_info:
                    if url_info == valid_modes:
                        continue
                    else:
                        update_url_query = 'UPDATE urls SET puzzle = ?, hangman = ?, image = ? WHERE url = ?'
                        url_data = valid_modes + [page_url]
                        cursor.execute(update_url_query, url_data)
                else:
                    insert_url_query = 'INSERT INTO urls VALUES (?,?,?,?)'
                    url_data = [page_url] + valid_modes
                    cursor.execute(insert_url_query, url_data)
                
                conn.commit()
                conn.close()

            except Exception as e:
                print(e)
                continue
