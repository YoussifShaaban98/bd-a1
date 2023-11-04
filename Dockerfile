# Use the Ubuntu base image
FROM ubuntu:latest
WORKDIR /bd-a1/



# Update The Package
RUN apt-get update -y 
RUN apt-get install -y

# Install Python 3 and pip
RUN apt-get install -y python3 python3-pip

# Install Python python libraries
RUN pip3 install pandas 
RUN pip3 install numpy
RUN pip3 install seaborn
RUN pip3 install matplotlib
RUN pip3 install scikit-learn
# Move Dataset
RUN mkdir /home/doc-bd-a1/
COPY CarPriceBigdata1.csv/ /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1/

# Move the .py files
COPY load.py /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/
COPY vis.py /home/doc-bd-a1/
COPY model.py /home/doc-bd-a1/


RUN python3 load.py CarPriceBigdata1.csv

# Run the container bash
CMD ["bash"]