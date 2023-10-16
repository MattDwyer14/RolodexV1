from Login import *
from home import *

verified = False
home = False
running = True

while running:
    if not verified:
        verified = login_page()
    
    if verified: 
        ended = blank_page()

