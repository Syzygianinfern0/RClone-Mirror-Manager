import glob
import logging
import os

import rclone

import itertools

cfg_path = "./rclone.conf"
from_drives = [
    "backup2",
    "backup3",
   
]
to_drives = [
    "backup2",
    "backup3",
]

cfg = open(cfg_path).read()
rc = rclone.with_config(cfg)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

flags = ["--drive-server-side-across-configs"]

flags.append("--fast-list")
flags.append("--drive-chunk-size")
flags.append("64M")
             
if os.path.isdir("accounts"):
    sa_files = glob.glob("accounts/*.json")
    assert len(sa_files)
    flags.append("--drive-service-account-file-path")
    flags.append("accounts")
    
for a_drive,b_drive in itertools.product(from_drives,to_drives):
    if a_drive == b_drive:
        continue
    print(f"From Drive: {a_drive}:")
    print(f"To Drive: {b_drive}:")
    result = rc.sync(
        f"{a_drive}:",
        f"{b_drive}:",
        flags,
    )
    if "error" in result["error"].decode("utf-8").lower():
        exit(1)
print("DONE")
