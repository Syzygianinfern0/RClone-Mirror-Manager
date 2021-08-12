import logging
import subprocess
import tempfile


class RClone:
    def __init__(self, cfg):
        self.cfg = cfg.replace("\\n", "\n")
        self.log = logging.getLogger("RClone")

    def _execute(self, command_with_args):
        self.log.debug("Invoking : %s", " ".join(command_with_args))
        try:
            with subprocess.Popen(command_with_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
                (out, err) = proc.communicate()

                # out = proc.stdout.read()
                # err = proc.stderr.read()

                self.log.debug(out)
                if err:
                    self.log.warning(err.decode("utf-8").replace("\\n", "\n"))

                return {"code": proc.returncode, "out": out, "error": err}
        except FileNotFoundError as not_found_e:
            self.log.error("Executable not found. %s", not_found_e)
            return {"code": -20, "error": not_found_e}
        except Exception as generic_e:
            self.log.exception("Error running command. Reason: %s", generic_e)
            return {"code": -30, "error": generic_e}

    def run_cmd(self, command, extra_args=None):
        # save the configuration in a temporary file
        if extra_args is None:
            extra_args = []
        with tempfile.NamedTemporaryFile(mode="wt", delete=True) as cfg_file:
            # cfg_file is automatically cleaned up by python
            # self.log.debug("rclone config: ~%s~", self.cfg)
            cfg_file.write(self.cfg)
            cfg_file.flush()

            command_with_args = ["rclone", command, "--config", cfg_file.name]
            command_with_args += extra_args
            command_result = self._execute(command_with_args)
            cfg_file.close()
            return command_result

    def copy(self, source, dest, flags=None):
        if flags is None:
            flags = []
        return self.run_cmd(command="copy", extra_args=[source] + [dest] + flags)

    def sync(self, source, dest, flags=None):
        if flags is None:
            flags = []
        return self.run_cmd(command="sync", extra_args=[source] + [dest] + flags)

    def listremotes(self, flags=None):
        if flags is None:
            flags = []
        return self.run_cmd(command="listremotes", extra_args=flags)

    def ls(self, dest, flags=None):
        if flags is None:
            flags = []
        return self.run_cmd(command="ls", extra_args=[dest] + flags)

    def lsjson(self, dest, flags=None):
        if flags is None:
            flags = []
        return self.run_cmd(command="lsjson", extra_args=[dest] + flags)

    def delete(self, dest, flags=None):
        if flags is None:
            flags = []
        return self.run_cmd(command="delete", extra_args=[dest] + flags)


def with_config(cfg):
    inst = RClone(cfg=cfg)
    return inst
