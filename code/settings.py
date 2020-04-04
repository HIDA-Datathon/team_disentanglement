import os
from pathlib import Path


def unify_path(path) -> Path:
    if type(path) == str:
        path = Path(path)

    if str(path).startswith('~'):
        # Unfortunately, the resolve() function cannot handle paths starting with ~. The workaround is to expand ~ to the home path in this case
        path = path.expanduser()

    if not path.is_absolute():
        # Path relative to the directory of this script file
        file_dir = Path(__file__).parent
        path = file_dir / path

    # Normalize the path (this makes it also absolute)
    return path.resolve()


# Path to the raw data
path_data = unify_path(os.environ.get('DATA_PATH', '../../data'))

# Path to a folder where we store intermediate results
path_results = unify_path(os.environ.get('RESULTS_PATH', '../../results'))
