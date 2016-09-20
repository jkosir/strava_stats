import asyncio
import os
import random

import aiohttp

import constants

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop, headers=constants.HEADERS)


async def get_profile(athlete_id):
    async with client.get(constants.PROFILE_URL.format(id=athlete_id)) as response:
        with open(os.path.join('profiles', '{}.html'.format(athlete_id)), 'wb') as out_file:
            out_file.write(await response.read())
    print('Loaded profile page for {}'.format(athlete_id))


for i in range(2000):
    athlete_id = random.randint(1, constants.MAX_ATHLETE_NUM)
    asyncio.ensure_future(get_profile(athlete_id))
loop.run_forever()
