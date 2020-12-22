import time
import asyncio
from google.cloud import storage

class DBbackup:
    def __init__(self, client):
        self.client = client
        self.db_backup_timer_obj = self.client.loop.create_task(self.db_backup_timer())

    async def db_backup_timer(self):
        backup_hours = 24
        db_paths = [
            'AttackonWikia/aow_db.db', 
            'ChooseYourAdventure/cya_db.db', 
            'Jaegermore/jaegermore_db.db', 
            'WarriorsvsSoldiers/wvs_db.db'
        ]
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            backup_count = 0
            while True:
                await asyncio.sleep(3600)
                backup_count += 1
                if backup_count >= backup_hours:
                    # Perform backup on all game dbs
                    for db_path in db_paths:
                        cur_date = str(time.gmtime().tm_year) + '_' + str(time.gmtime().tm_mon) + '_' + str(time.gmtime().tm_mday)
                        db_path_with_date = 'Archive/' + db_path[:-3] + '_' + cur_date + '.db'
                        try:
                            bucket_name = "discord-aot-bots"
                            source_file_name = db_path
                            destination_blob_name = db_path_with_date

                            storage_client = storage.Client.from_service_account_json(
                                'storage_credentials.json')
                            bucket = storage_client.bucket(bucket_name)
                            blob = bucket.blob(destination_blob_name)

                            blob.upload_from_filename(source_file_name)

                            print(
                                "File {} uploaded to {}.".format(
                                    source_file_name, destination_blob_name
                                )
                            )
                        except Exception as error:
                            print('Error while making backup:', error)
                    break
