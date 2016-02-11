import subprocess
import os


class SliceReader():
    def __init__(self, f=None):
        self.file_path = f

    def read_file(self, f=None):
        if f is not None:
            self.file_path = f
        if not os.access(self.file_path, os.R_OK):
            raise ValueError  ##  file is not readable

        pipeline = r"""tr A-Z a-z < %s | tr -cd 'a-z\n'""" % self.file_path
        self.in_xlated = subprocess.Popen(pipeline, shell=True,
                                          stdout=subprocess.PIPE).stdout.read()
        ary = self.in_xlated.splitlines()
        lengths = set([len(row) for row in ary])
        if len(lengths) > 1:
            raise ValueError  ## not all lines are the same length
