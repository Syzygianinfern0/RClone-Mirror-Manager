import rclone
import logging

cfg_path = "./rclone.conf"
from_drives = [
    "test",
    "___backups",
    "__code",
    "__meow",
    "__quack",
    "dumpyard",
    "pss",
    "public",
]
to_drives = [
    "1",
    "2",
    "3",
    "4",
    "5",
]

cfg = open(cfg_path).read()
rc = rclone.with_config(cfg)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

to_drive = to_drives[0]
for from_drive in from_drives:
    print(f"From: {from_drive}:")
    print(f"To: {to_drive}:sync/{from_drive}")
    result = rc.sync(
        f"{from_drive}:",
        f"{to_drive}:sync/{from_drive}",
        ["--drive-server-side-across-configs"],
    )
    if "error" in result["error"].decode("utf-8").lower():
        exit(1)

from_drive = to_drives[0]
for to_drive in to_drives[1:]:
    print(f"From: {from_drive}:sync/")
    print(f"To: {to_drive}:sync/")
    result = rc.sync(
        f"{from_drive}:sync/",
        f"{to_drive}:sync/",
        ["--drive-server-side-across-configs"],
    )
    if "error" in result["error"].decode("utf-8").lower():
        exit(1)
