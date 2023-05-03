import os
import shutil

# Создаем директорию 'drawing', если ее еще нет
if not os.path.exists('drawing'):
    os.makedirs('drawing')

# Копируем файл 'rainbow.py' в директорию 'drawing'
shutil.copy('rainbow.py', 'drawing')

# Копируем файл 'trees.py' в директорию 'drawing'
shutil.copy('trees.py', 'drawing')

# Копируем файл 'trees.py' в директорию 'drawing'
shutil.copy('smiley.py', 'drawing')

# Копируем файл 'trees.py' в директорию 'drawing'
shutil.copy('snowflake.py', 'drawing')

# Копируем файл 'trees.py' в директорию 'drawing'
shutil.copy('house.py', 'drawing')
