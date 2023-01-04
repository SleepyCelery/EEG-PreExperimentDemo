import os

from input_params import *
from time import time
from mne.preprocessing import ICA
import mne
import sys

if __name__ == '__main__':
    os.makedirs(name=f'./{task_output_dir}/', exist_ok=True)
    logfile = open(f'./{task_output_dir}/logs.txt', mode='w')
    sys.stdout = logfile
    sys.stderr = logfile

    raw_fname = raw_file_path
    raw = mne.io.read_raw_fif(raw_fname).crop(crop_tmin, crop_tmax).pick(
        using_channel).load_data()

    raw.filter(filter_fmin, filter_fmax, fir_design='firwin')

    ica = ICA(n_components=ica_components_count, method=ica_method, max_iter='auto',
              random_state=0)
    t0 = time()
    ica.fit(raw)
    fit_time = time() - t0
    title = ('ICA decomposition using %s (took %.1fs)' % (ica_method, fit_time))
    figs = ica.plot_components(title=title)

    for index, fig in enumerate(figs):
        fig.savefig(f'./{task_output_dir}/result_{index}.png')
    logfile.close()
