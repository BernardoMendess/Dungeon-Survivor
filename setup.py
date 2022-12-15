import cx_Freeze

executables = [cx_Freeze.Executable('menu.py')]

cx_Freeze.setup(
    name="dungeon survivor",
    options={'build_exe': {'packages': ['pygame'],
    'include_files':['imagem', 'som','game.py', 'ranking.py', 'pause.py', 'ranking.txt', 'PPlay']}},
    executables = executables
)