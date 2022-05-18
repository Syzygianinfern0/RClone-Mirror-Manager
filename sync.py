import glob
import logging
import os

import rclone

cfg_path = "./rclone.conf"
from_drives = [
    "gdrive",
   
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

to_drive = to_drives[0]
for from_drive in from_drives:
    print(f"A-From: {from_drive}:")
    print(f"A-To: {to_drive}:")
    result = rc.copy(
        f"{from_drive}:",
        f"{to_drive}:",
        flags,
    )
    if "error" in result["error"].decode("utf-8").lower():
        exit(1)

from_drive = to_drives[0]
for to_drive in to_drives[1:]:
    print(f"B-From: {from_drive}:")
    print(f"B-To: {to_drive}:")
    result = rc.copy(
        f"{from_drive}:",
        f"{to_drive}:",
        flags,
    )
    if "error" in result["error"].decode("utf-8").lower():
        exit(1)
