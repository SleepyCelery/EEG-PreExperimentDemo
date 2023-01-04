FROM python:3.8

WORKDIR /usr/src/PreExperimentDemo

COPY requirements.txt ./
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple &&\
 pip install --no-cache-dir -r requirements.txt &&\
/bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /usr/src/PreExperimentDemo
COPY . .
ENV PYTHONPATH /usr/src/PreExperimentDemo
ENV BASE_DIR /userdata
ENV RAW_FILE_PATH ./MNE-sample-data/MEG/sample/sample_audvis_filt-0-40_raw.fif
ENV ICA_METHOD fastica
ENV ICA_COMPONENTS_COUNT 30
ENV CROP_TMIN 0
ENV CROP_TMAX 60
ENV USING_CHANNEL eeg
ENV FILTER_FMIN 1
ENV FILTER_FMAX 30
CMD [ "python", "ICA.py" ]