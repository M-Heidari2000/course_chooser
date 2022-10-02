import requests


def register(course=None, units=None):
    authorization = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SWQiOiI5ODEwMTQ2OSIsImNyZWF0ZWRBdCI6MTY2NDY4ODAwMjI3Miwic3VwZXJVc2VyIjpmYWxzZSwiaWF0IjoxNjY0Njg4MDAyfQ.vK0mKnZaS0FF-Kw-T-APAWe346Eq_MEESFAXCgJBhNQ'
    
    headers = {'Authorization': authorization}
    body = {
        'action': 'add',
        'course': course,
        'units': units
    }

    resp = requests.post('https://my.edu.sharif.edu/api/reg', json=body, headers=headers)
    print(resp.text)

courses = [('25647-1', 3), ('22635-1', 4), ('25577-1', 3), ('37446-10', 2), ('22059-1', 3)]

for course in courses:
    register(*course)

