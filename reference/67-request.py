import urllib.request

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


req = urllib.request.Request('https://www.google.com')
with urllib.request.urlopen(req, context=ctx) as f:
    print(f.read())