import re
from mri_lib.slice_reader import SliceReader
from collections import OrderedDict

class TumorFinder():
    def __init__(self, in_file=None):
        if in_file is None:
            raise RuntimeError

        reader = SliceReader(in_file)
        try:
            reader.read_file()
            self.image = reader.in_xlated.splitlines()
        except ValueError:
            self.image = []
        self.neighborhood = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        self.rows = len(self.image) if len(self.image) else None
        self.cols = len(self.image[0]) if len(self.image) else None

    def _get_cell(self, i, j):
        if (i < 0 or i >= self.rows) or (j < 0 or j >= self.cols):
            return None
        return self.image[i][j]

    def _set_cell(self, i, j, val):
        if (i < 0 or i >= self.rows) or (j < 0 or j >= self.cols):
            return
        l = list(self.image[i])
        l[j] = val
        self.image[i] = "".join(l)

    def _char_neighbors(self, i, j, ch):
        for coord in self.neighborhood:
            cell_coord = i + coord[0], j + coord[1]
            if self._get_cell(cell_coord[0], cell_coord[1]) == ch:
                yield cell_coord

    def _mark_blob(self, i, j, ch):
        blob_neighborhood = OrderedDict()
        for cell_coord in self._char_neighbors(i, j, ch):
            blob_neighborhood[cell_coord] = 1
        while True:
            if len(blob_neighborhood) == 0:
                break
            ##  get the next element out of the dict
            ci, cj = blob_neighborhood.keys()[0]
            ##  put matching neighbors into the set
            for new_coord in self._char_neighbors(ci, cj, ch):
                blob_neighborhood[new_coord] = 1
            ## mark the current cell's contents and remove that cell
            ## address from the dict
            self._set_cell(ci, cj, ch.upper())
            blob_neighborhood.popitem(0)

    def _mark_char(self, ch):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.image[i][j] == ch:
                    self._mark_blob(i, j, ch)
                    return

    def _check_tumor(self):
        ##  form a set of all the unique characters in the image
        character_set = set()
        for row in self.image:
            character_set.update(set(list(row)))
        ## for each character in the set, toggle the first blob of
        ## characters to upper case
        for c in list(character_set):
            self._mark_char(c)
        ##  now scan the image for lower case characters.  if any are
        ##  present then we have at least one tumor
        has_tumor = "False"
        for row in self.image:
            if re.search(r'[a-z]', row):
                has_tumor = "True"
        return(has_tumor)

    def dump_image(self):
        for row in self.image:
            print row

    def process_image(self):
        if len(self.image) == 0:
            retcode = 'Error,NA,NA'
        else:
            retcode = '%s,%s,%s' % (self._check_tumor(), len(self.image), len(self.image[0]))
        return(retcode)
