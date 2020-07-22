import asyncio
import time
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

client = MyClient()
while True:
    # Handle errors, restart client if exception is found
    try:
        # Your bot token here
        client.loop.run_until_complete(client.start(secrets.BOT_TOKEN))
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