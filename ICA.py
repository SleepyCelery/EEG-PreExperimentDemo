from time import time
import mne
from mne.preprocessing import ICA
from mne.datasets import sample
import matplotlib.pyplot as plt
import input_params

raw_fname = input_params.raw_file_name

raw = mne.io.read_raw_fif(raw_fname).crop(0, 60).pick('eeg').load_data()

reject = dict(mag=5e-12, grad=4000e-13)
raw.filter(1, 30, fir_design='firwin')


def run_ica(method, fit_params=None):
    ica = ICA(n_components=30, method=method, fit_params=fit_params,
              max_iter='auto', random_state=0)
    t0 = time()
    ica.fit(raw, reject=reject)
    fit_time = time() - t0
    title = ('ICA decomposition using %s (took %.1fs)' % (method, fit_time))
    figs = ica.plot_components(title=title)
    for index, fig in enumerate(figs):
        fig.savefig(f'./result_{index}.png')


if __name__ == '__main__':
    run_ica('fastica')
