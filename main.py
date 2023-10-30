from Login import *
from home import *

verified = True
home = False
running = True

while running:
    if not verified:
        verified = login_page()
    
    if verified: 
        ended = home_page()

