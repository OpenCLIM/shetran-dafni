import subprocess
import shutil
from glob import glob
import os

data_path = os.getenv('DATA_PATH', '/data')

inputs = os.path.join(data_path, 'inputs')
outputs = os.path.join(data_path, 'outputs')

if os.path.exists(outputs):
    shutil.rmtree(outputs)
    os.mkdir(outputs)

run_path = os.path.join(outputs, 'shetran')

shutil.copytree(inputs, run_path)

try:
    library = glob(os.path.join(run_path, '*.xml'))[0]
except IndexError:
    raise Exception('Library file missing')


subprocess.call(['./shetran-prepare', library])
subprocess.call(['./shetran-linux', '-f', glob(os.path.join(run_path, 'rundata_*'))[0]])
