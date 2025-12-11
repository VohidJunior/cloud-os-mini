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

# class File:
#     ID = 1000
#     def __init__(self, name, value=''):
#         self.file_id = File.ID
#         self.name = name
#         self.value = value
        
#         File.ID += 1
        
#     def edit_file(self, new_value):
#         self.value = new_value
        
#     def get_info(self):
#         return {
#             'ID': self.file_id,
#             'name': self.name,
#             'value': self.value[:20]
#         }

def show_folders(path):
    if len(path) == 0:
        return list(file_tree.keys())
    else:
        tree = file_tree
        for i in path:
            tree = tree[i]
        return list(tree.keys())
    

def create_folder(path, name):
    if len(path) == 0:
        file_tree[name] = {}
        return f'Muvaffaqqiyat! {name} papkasi yaratildi!'
    else:
        tree = file_tree
        for i in path:
            tree = tree[i]
        tree[name] = {}
        return f'Muvaffaqqiyat! {name} papkasi yaratildi!'

def remove_folder(path, name):
    if len(path) == 0:
        del file_tree[name]
        return f'Muvaffaqqiyat! {name} papkasi o\'chirildi!'
    else:
        tree = file_tree
        for i in path:
            tree = tree[i]
        del tree[name]
        return f'Muvaffaqqiyat! {name} papkasi o\'chirildi!'
    
def make_file(path, name):
    if len(path) == 0:
        file_tree
    else:
        tree = file_tree
        for i in path:
            tree = tree[i]
        tree[name] = {}
    return f'Muvaffaqqiyat! {name} fayli yaratildi!'

main_path = '>> Disk | '
def program(path=[]):
    global main_path
    prompt = input(f'{main_path}').split()
    buyruq = prompt[0]
    
    if buyruq == 'to':
        if prompt[1] not in show_folders(path):
            print("Bunday papka mavjud emas!")
            return program(path=path)
        
        path.append(prompt[1])
        for i in path:
            main_path += f"{i} | "
        
    elif buyruq == 'back':
        if len(path) == 0:
            return program(path=path)
        path.remove(path[-1])
        for i in path:
            main_path += f"{i} | "
        
    elif buyruq == 'make_folder':
        print(create_folder(path, prompt[1]))
        
    elif buyruq == 'remove_folder':
        print(remove_folder(path, prompt[1]))
    
    elif buyruq == 'all':
        print(*show_folders(path), sep='\n')
        
    # elif buyruq == 'file':
    #     print(
    #         )
    
    elif buyruq == 'help':
        print(help_os)
        
    elif buyruq == 'cls':
        print('Xayr!')
        return None
    
    return program(path=path)

print()
program()
