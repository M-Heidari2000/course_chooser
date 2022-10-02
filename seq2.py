import requests
import time

def register(course=None, units=None):
    authorization = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SWQiOiI5ODEwMTQ2OSIsImNyZWF0ZWRBdCI6MTY2NDcwMTQ3ODI3OSwic3VwZXJVc2VyIjpmYWxzZSwiaWF0IjoxNjY0NzAxNDc4fQ.gTKhVYfhxypSROjm70gGB-N8nGSALsk3HquJv7wFHH0'
    
    headers = {'Authorization': authorization}
    body = {
        'action': 'add',
        'course': course,
        'units': units
    }

    resp = requests.post('https://my.edu.sharif.edu/api/reg', json=body, headers=headers)
    print(resp.text)


courses = [('25647-1', 3)]
time.sleep(2)

for course in courses:
    register(*course)

