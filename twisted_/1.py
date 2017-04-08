db = {}
def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken,try another: '
            continue
        else:
            break
    pwd = input('password: ')
    db[name] = pwd

def olduser():
    name = input('Login: ')
    pwd = input('passwd: ')
    passwd = db.get(name)
    if passwd == None:
        print('invalid username.')
    elif passwd == pwd:
        print('welcome back!',name)
    else:
        print('password error.')

def showmenu():
        prompt = """
        (N)ew User Login
        (E)xisting User Login
        (Q)uit
        Enter choice: 
        """
        done = False
        while not done:
            chosen = False
            while not chosen:
                try:
                    choice = input(prompt).strip()[0].lower()
                except (EOFError, KeyboardInterrupt):
                    choice = 'q'
                print('\n You picked: [%s]' % choice)
                if choice not in 'neq':
                    print('invalid option,try again')
                else:
                    chosen = True
            if choice == 'q':
                done = True
            if choice == 'n':
                newuser()
            if choice == 'e':
                olduser()
showmenu()
