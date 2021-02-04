FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime

# init
RUN apt-get update && apt-get upgrade -y && apt-get install -y git
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -U pip

# KILT
WORKDIR /tmp
RUN git clone https://github.com/facebookresearch/KILT.git
WORKDIR /tmp/KILT
RUN python setup.py install

# GENRE
WORKDIR /tmp
RUN git clone https://github.com/DenDen047/GENRE.git
WORKDIR /tmp/GENRE
RUN python setup.py install

# pip
WORKDIR /tmp
COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt

# torch
RUN pip install torchsummary
RUN pip install torch_optimizer

# clearn
RUN rm -rf /var/lib/apt/lists/*
