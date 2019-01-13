'''
Start GRIP container, test the API endpoints.

TODO
XXX Docker build.
XXX Test interface.
XXX File handling backend and test.
XXX What routes? https://docs.google.com/presentation/d/17KTL5q3Nd8E_iUehLKGhCDZar8nkyn7hm8JOu6RMZ4Y/edit#slide=id.g389c95e613_0_15
XXX Implement a route.
XXX Implement the rest of the routes.
'''

import os, webbrowser, requests
from multiprocessing import Process

testGlmPath = 'test_ieee123nodeBetter.glm'
response2 = requests.post('http://localhost:5000/v1/oneLineGridlab', files={'glm':open(testGlmPath).read()}, data={'useLatLons':False})
print(response2)
with open('picture_out.png', 'wb') as f:
    f.write(response2.content)