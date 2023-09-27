
from Login import *
from home import *
verified = False
home = False
running = True
while running:
    if not verified:
        login_page()
        print(verified, "after")

    print(verified, "outisde")
    if home:
        home_page()


