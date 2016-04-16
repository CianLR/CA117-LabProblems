print(__import__('sys').argv[1][1:-1], end=('' if len(__import__('sys').argv[1]) < 3 else '\n'))
