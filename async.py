import aiohttp
import asyncio

async def register(session, course=None, units=None):
    authorization = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SWQiOiI5ODEwMTQ2OSIsImNyZWF0ZWRBdCI6MTY2NDY1OTY4ODc2OSwic3VwZXJVc2VyIjpmYWxzZSwiaWF0IjoxNjY0NjU5Njg4fQ.Ojg7ZKghF3NrE7tde2jSle-jIgmOBlI_tM4rwy478UY'
    
    headers = {'Authorization': authorization}
    body = {
        'action': 'add',
        'course': course,
        'units': units
    }

    async with session.post('https://my.edu.sharif.edu/api/reg', json=body, headers=headers) as resp:
        print(await resp.text())

async def main(courses):
    session = aiohttp.ClientSession()
    await asyncio.gather(*(register(session, *course) for course in courses))

if __name__ == '__main__':
    courses = [('22635-1', 4), ('25577-1', 3), ('25647-1', 3), ('37446-10', 2)]
    asyncio.run(main(courses)) 

