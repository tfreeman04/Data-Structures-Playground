import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print('project_root=', project_root)
print('cwd=', os.path.abspath(os.getcwd()))
print('sys.path before insert:', sys.path[:3])
sys.path.insert(0, project_root)
print('sys.path after insert:', sys.path[:3])
try:
    import structures.binary_tree as bt
    print('import OK')
except Exception as e:
    print('IMPORT ERROR:', e)
    raise
