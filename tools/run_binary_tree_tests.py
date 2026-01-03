import runpy
import inspect
import traceback
import os
import sys

# Ensure project root is on sys.path so `structures` can be imported
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Ensure project root is first on sys.path
sys.path.insert(0, project_root)
# also ensure current working directory is on sys.path for safety
cwd = os.path.abspath(os.getcwd())
if cwd not in sys.path:
    sys.path.insert(0, cwd)

# Execute the test file in isolation and collect functions
ns = runpy.run_path('tests/test_binary_tree.py')

# Find functions whose names start with 'test_'
test_funcs = [(name, obj) for name, obj in ns.items() if callable(obj) and name.startswith('test_')]

if not test_funcs:
    print('No test functions found in tests/test_binary_tree.py')
    raise SystemExit(1)

passed = 0
failed = 0

for name, func in test_funcs:
    try:
        func()
        print(f'PASSED {name}')
        passed += 1
    except AssertionError:
        print(f'FAILED {name}')
        traceback.print_exc()
        failed += 1
    except Exception:
        print(f'ERROR {name}')
        traceback.print_exc()
        failed += 1

print(f"\nSummary: {passed} passed, {failed} failed")

raise SystemExit(1 if failed else 0)
