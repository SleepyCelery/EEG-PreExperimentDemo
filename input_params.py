import os

debug = True
if not debug:
    raw_file_name = os.getenv('RAW_FILE_NAME')
else:
    raw_file_name = "./MNE-sample-data/MEG/sample/sample_audvis_filt-0-40_raw.fif"
