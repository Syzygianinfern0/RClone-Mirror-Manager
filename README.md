<div align="center">

# 🪞 RClone Mirror Manager 🪞
⬇ Backup your Beloved RClone Drives to Multiple Mirrors

</div>

# Dependencies 🧰
- rclone
- python3
- brain

# Usage 👨‍💻
1. Create an `rclone.conf` file that complies with [RClone](https://rclone.org/).
2. Host it on some online paste bin. I personally use Secret Gists (yep, I’m obsessed with version control, how’d you guess?).
3. Fork/mirror this repo.
4. Create a GitHub Secret called `CONF_URL` and set it's value as the link to the rclone config (make sure you copy the link to the "RAW Text").
5. Edit the `from_drives` and `to_drives` in [`sync.py`](sync.py) as you wish.
6. The script is set to run every day at 6:30 AM UTC. Feel free to modify that under [`.github/workflows/sync.yaml`](.github/workflows/sync.yaml).
7. Profit 💯

Note: The [`sync.sh`](sync.sh) file is a bash equivalent of the [`sync.py`](sync.py). If you want to tinker with this project
but you don't like/know Python3, feel free to start there. 