import asyncio

import aiohttp


async def test_post():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'http://127.0.0.1:8000/api/products/',
            data={'title': 'nigbob', 'price': 500},
        ) as response:
            assert response.status == 201
            resp_data = await response.json()
            assert isinstance(resp_data, dict)
            assert resp_data['title'] == resp_data['description']


async def test_put():
    async with aiohttp.ClientSession() as session:
        async with session.put(
            'http://127.0.0.1:8000/api/products/1/',
            data={'price': 500, 'title': 'bo'},
        ) as response:
            assert response.status == 200
            resp_data = await response.json()
            assert isinstance(resp_data, dict)
            assert resp_data['title'] == resp_data['description']


async def test_get_list():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'http://127.0.0.1:8000/api/products/',
        ) as response:
            assert response.status == 200
            resp_data = await response.json()
            assert isinstance(resp_data, list)
            assert len(resp_data) > 0
            assert isinstance(resp_data[0], dict)


async def main():
    tasks = [
        asyncio.create_task(test_get_list()),
        asyncio.create_task(test_post()),
        asyncio.create_task(test_put()),
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
