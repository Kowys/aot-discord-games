import asyncio
import time
import yaml
import secrets
from botclient import MyClient

def handle_exit(client):
    print("Handling")
    client.loop.run_until_complete(client.logout())
    for t in asyncio.Task.all_tasks(loop=client.loop):
        t.cancel()
        try:
            client.loop.run_until_complete(asyncio.wait_for(t, 5, loop=client.loop))
            t.exception()
        except asyncio.InvalidStateError:
            pass
        except asyncio.TimeoutError:
            pass
        except asyncio.CancelledError:
            pass
        except:
            pass

def load_token():
    secrets_file = open('secrets.yml', "r")
    secrets_info = yaml.safe_load(secrets_file)

    if secrets_info['BOT_TOKEN4']:
        return secrets_info['BOT_TOKEN4']
    else:
        raise Exception('Please add a bot token to secrets.yml!')

client = MyClient()
bot_token = load_token()

while True:
    # Handle errors, restart client if exception is found
    try:
        # Your bot token here
        client.loop.run_until_complete(client.start(bot_token))
    except SystemExit:
        print('System exit')
        handle_exit(client)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        handle_exit(client)
        print('Exiting...')
        client.loop.close()
        break
    except Exception as e:
        print(e)
        handle_exit(client)

    time.sleep(10)
    print("Bot restarting")
    client = MyClient()