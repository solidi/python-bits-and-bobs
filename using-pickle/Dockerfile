FROM python:3

ADD . /

RUN pip install dill
RUN pip install pathos

CMD [ "python", "using-pickle.py" ]
CMD [ "python", "using-multiprocessing.py" ]
