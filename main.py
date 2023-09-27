from Login import *
from home import *

verified = False
home = False
running = True

while running:
    if not verified:
        verified = login_page()
        print(verified, "after")

    if verified:
        home_page()


