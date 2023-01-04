import os
import time
import platform

if platform.system() != "Windows":
    base_dir = os.getenv('BASE_DIR')
    task_name = f'PreExperiment_ICA_{int(time.time())}'
    raw_file_path = os.path.join(base_dir, os.getenv('RAW_FILE_PATH'))
    task_output_dir = os.path.join(base_dir, task_name)
    ica_method = os.getenv("ICA_METHOD")
    ica_components_count = int(os.getenv("ICA_COMPONENTS_COUNT"))
    crop_tmin = int(os.getenv("CROP_TMIN"))
    crop_tmax = int(os.getenv("CROP_TMAX"))
    using_channel = os.getenv('USING_CHANNEL').lower()
    filter_fmin = int(os.getenv("FILTER_FMIN"))
    filter_fmax = int(os.getenv("FILTER_FMAX"))
else:
    base_dir = "."
    task_name = f'PreExperiment_ICA_{int(time.time())}'
    raw_file_path = "./MNE-sample-data/MEG/sample/sample_audvis_filt-0-40_raw.fif"
    task_output_dir = os.path.join(base_dir, task_name)
    ica_method = 'fastica'
    ica_components_count = 30
    crop_tmin = 0
    crop_tmax = 60
    using_channel = "eeg"
    filter_fmin = 1
    filter_fmax = 30
