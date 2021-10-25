import subprocess
import shutil
from glob import glob
import os
import datetime

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

title = os.getenv('TITLE', 'SHETran output')
description = ' '
geojson = {}


metadata = f"""{{
  "@context": ["metadata-v1"],
  "@type": "dcat:Dataset",
  "dct:language": "en",
  "dct:title": "{title}",
  "dct:description": "{description}",
  "dcat:keyword": [
    "citycat"
  ],
  "dct:subject": "Environment",
  "dct:license": {{
    "@type": "LicenseDocument",
    "@id": "https://creativecommons.org/licences/by/4.0/",
    "rdfs:label": null
  }},
  "dct:creator": [{{"@type": "foaf:Organization"}}],
  "dcat:contactPoint": {{
    "@type": "vcard:Organization",
    "vcard:fn": "DAFNI",
    "vcard:hasEmail": "support@dafni.ac.uk"
  }},
  "dct:created": "{datetime.datetime.now().isoformat()}Z",
  "dct:PeriodOfTime": {{
    "type": "dct:PeriodOfTime",
    "time:hasBeginning": null,
    "time:hasEnd": null
  }},
  "dafni_version_note": "created",
  "dct:spatial": {{
    "@type": "dct:Location",
    "rdfs:label": null
  }},
  "geojson": {geojson}
}}
"""
with open(os.path.join(outputs, 'metadata.json'), 'w') as f:
    f.write(metadata)
