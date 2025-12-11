help_os = """
    all --> ls, dir
    to --> cd file
    back --> cd ..
    help --> help
    make_folder --> mkdir
    delete_folder --> rmdir
    cls --> exit
    
    file yaratish --> file
"""
file_tree = {
    'user': {
        'Media': {}, 'Documents': {}
    },
    'Programs': {
        'bin': {
            
        }
    }
}

def show_folders(path):
    if len(path) == 0:
        return list(file_tree.keys())
    else:
        tree = file_tree
        for i in path:
            tree = tree[i]
        return list(tree.keys())
    

def create_folder(path, name):
    tree = file_tree
    for i in path:
        tree = tree[i]
    tree[name] = {}
    return f'Muvaffaqqiyat! {name} papkasi yaratildi!'

def remove_folder(path, name):
    tree = file_tree
    for i in path:
        tree = tree[i]
    del tree[name]
    return f'Muvaffaqqiyat! {name} papkasi o\'chirildi!'

def make_file(path, name):
    tree = file_tree
    for i in path:
        tree = tree[i]
    tree[name] = {}
    return f'Muvaffaqqiyat! {name} fayli yaratildi!'

# Asosiy terminal funksiyasi
def program():
    path = []
    main_path = '>> Disk | '
    
    while True:
        main_path = '>> Disk | ' + ' | '.join(path) + ' | ' if path else '>> Disk | '
        prompt = input(f'{main_path}').split()
        if not prompt:
            continue
        
        buyruq = prompt[0]

        if buyruq == 'to':
            if len(prompt) < 2 or prompt[1] not in show_folders(path):
                print("Bunday papka mavjud emas!")
                continue
            path.append(prompt[1])

        elif buyruq == 'back':
            if path:
                path.pop()

        elif buyruq == 'make_folder':
            if len(prompt) >= 2:
                print(create_folder(path, prompt[1]))
            else:
                print("Papka nomini yozing!")

        elif buyruq == 'remove_folder':
            if len(prompt) >= 2:
                print(remove_folder(path, prompt[1]))
            else:
                print("Papka nomini yozing!")

        elif buyruq == 'all':
            print(*show_folders(path), sep='\n')

        # Fayl yaratish hozircha oddiy
        elif buyruq == 'file':
            if len(prompt) >= 2:
                print(make_file(path, prompt[1]))
            else:
                print("Fayl nomini yozing!")

        elif buyruq == 'help':
            print(help_os)

        elif buyruq == 'cls':
            print('Xayr!')
            break

# print()
# program()
