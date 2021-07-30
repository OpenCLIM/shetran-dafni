import subprocess
import shutil
from glob import glob
import os

data_path = os.getenv('DATA_PATH', '/data')

inputs = os.path.join(data_path, 'inputs')
outputs = os.path.join(data_path, 'outputs')

if os.path.exists(outputs):
    shutil.rmtree(outputs)

shutil.copytree(inputs, outputs)

try:
    library = glob(os.path.join(outputs, '*.xml'))[0]
except IndexError:
    raise Exception('Library file missing')


subprocess.call(['./shetran-prepare', library])
subprocess.call(['./shetran-linux', '-f', glob(os.path.join(outputs, 'rundata_*'))[0]])
