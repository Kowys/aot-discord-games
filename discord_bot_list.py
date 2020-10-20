import dbl
import discord
import yaml
import asyncio

class DBList:
    def __init__(self, client):
        self.client = client
        self.token = load_token()
        self.dblpy = dbl.DBLClient(self.client, self.token, autopost=True)
        self.db_list_timer_obj = self.client.loop.create_task(self.db_list_timer())

    async def db_list_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            while True:
                try:
                    await self.dblpy.post_guild_count()
                    # print('Posted server count ({})'.format(self.dblpy.guild_count()))
                except Exception as e:
                    print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))

                # if you are not using the tasks extension, put the line below
                await asyncio.sleep(1800)

def load_token():
    secrets_file = open('secrets.yml', "r")
    secrets_info = yaml.safe_load(secrets_file)

    if secrets_info['DBL_TOKEN']:
        return secrets_info['DBL_TOKEN']
    else:
        raise Exception('Please add a bot token to secrets.yml!')