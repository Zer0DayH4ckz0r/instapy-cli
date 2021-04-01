from instapy_cli import client

username = 'Zer0DayJLD'
password = 'MySuperStrongPassword'

with client(username, password) as cli:
    # do stuffs with cli
    ig = cli.api()
    print(ig.current_user())
