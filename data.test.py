import os

print os.listdir('.')
del_paths = [name for name in os.listdir('.') if name.endswith('.pyc') or name.endswith('.py~')]
for del_path in del_paths:
    os.remove(del_path)
print os.listdir('.')
