import subprocess
import os
from datetime import datetime, timedelta
import shutil

duration = timedelta(days=int(os.getenv('DURATION', '1')))
start = datetime(1980, 1, 1)
end = start + duration

path = 'aire-at-kildwick-bridge'

with open(f'{path}/Aire_at_Kildwick_BridgeLibraryFile_Template.xml') as f:
    text = f.read()

library = f'{path}/Aire_at_Kildwick_BridgeLibraryFile.xml'
with open(library, 'w') as f:
    f.write(text.format(month=end.month, day=end.day))

subprocess.call(['./shetran-prepare', library])
subprocess.call(['./shetran-linux', '-f', f'{path}/rundata_Aire_at_Kildwick_Bridge.txt'])

for f in os.listdir(path):
    if not any([f.endswith('Template.xml'), f.startswith('input'), f.startswith('rundata'), f == 'temporary.txt']):
        shutil.move(f'{path}/{f}', f'/data/outputs/{f}')
