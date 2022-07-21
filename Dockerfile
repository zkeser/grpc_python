FROM redhat/ubi8

WORKDIR /$HOME

ENV JAVA_HOME=/$HOME/jdk-11.0.2
ENV PATH=$JAVA_HOME/bin:$PATH

RUN yum install -y python38-devel \
    python3.8 \
    git \
    wget \
    gcc

RUN wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz && tar xvf openjdk-11.0.2_linux-x64_bin.tar.gz
RUN git clone https://github.com/primeqa/primeqa.git

WORKDIR /primeqa

RUN pip3 install torch~=1.11.0
RUN pip3 install -e .[all]