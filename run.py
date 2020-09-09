import subprocess
import os
from datetime import datetime, timedelta
import shutil

duration = timedelta(days=int(os.getenv('DURATION', '1')))
start = datetime(1977, 10, 1)
end = start + duration

with open('cobres-model/input_cob_frd_template.txt') as f:
    text = f.read()

with open('cobres-model/input_cob_frd.txt', 'w') as f:
    f.write(text.format(month=end.month, day=end.day))

subprocess.call(['./shetran-linux', '-f', 'cobres-model/rundata_cob.txt'])

for f in os.listdir('cobres-model'):
    if f.startswith('output'):
        shutil.move(f'cobres-model/{f}', '/data/outputs')
