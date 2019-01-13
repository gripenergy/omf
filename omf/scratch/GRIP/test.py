'''
Start GRIP container, test the API endpoints.

TODO
XXX Docker build.
XXX Test interface.
XXX File handling backend and test.
XXX What routes? https://docs.google.com/presentation/d/17KTL5q3Nd8E_iUehLKGhCDZar8nkyn7hm8JOu6RMZ4Y/edit#slide=id.g389c95e613_0_15
XXX Implement a route.
OOO Implement the rest of the routes.
'''

import os
import webbrowser
import requests


# Start the server.

# Make sure it's up.
# webbrowser.open_new('http://localhost:5000/eatfile')
# Test a simple route.
response1 = requests.post('http://localhost:5001/eatfile',
                          files={'test.txt': 'NOTHING_TO_SEE_HERE\nMY_DUDE'})
print '##### RESPONSE STATUS CODE', response1.status_code
print '##### RESPONSE CONTENT', response1.content
# print 'YOOOOOOOOOOO', dir(response1)
# print 'YOOOOOOOOOOO', response1.text
# print 'YOOOOOOOOOOO', dir(response1.raw)
# Test the image drawing route.
testGlmPath = './test_ieee123nodeBetter.glm'
#testGlmPath = './ieee123.glm'
response2 = requests.post('http://localhost:5001/oneLineGridlab',
                          files={'glm': open(testGlmPath).read()}, data={'useLatLons': True})
# print response2.content # it's a png yo. don't actually print it. duh.
with open('picture_out.png', 'wb') as f:
    f.write(response2.content)
# Block until the process terminates.
# p.join()
# I SUFFER. KILL ME.
