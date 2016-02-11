##MRI program

 - explode this tarball in a python (2.7) virtualenv

 - make sure that requirements are installed (pip install -r requirements.txt)

 - run it, for instance, like this:
    python ./find_tumor.py --inputfile=./mri_lib/tests/data_files/good_data_001.in

   or like this:
    python ./find_all_tumors.py --inputdir=mri_lib/tests/data_files --outputfile=out.csv

 -run (admittedly skimpy)  tests like this
    nosetests -v
