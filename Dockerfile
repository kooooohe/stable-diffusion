FROM pytorch/pytorch:latest
#FROM rocm/pytorch:latest

RUN pip3 install --upgrade diffusers transformers scipy
# ftfy python-slugify
#RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/rocm5.1.1
#RUN pip3 install transformers==4.19.2 scann kornia==0.6.4 torchmetrics==0.6.0

