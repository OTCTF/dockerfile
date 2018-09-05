
  FROM sagemath/sagemath


MAINTAINER ot-oldman <otctfmail@gmail.com>

# basic
RUN mkdir -p /home/tools
RUN dpkg --add-architecture i386
RUN apt-get update
## common binary
RUN apt-get install -y apt-file vim git unzip net-tools openssl netcat telnet curl wget man-db socat tmux nginx ascii p7zip-full
## language: c/c++ python node.js ruby java
RUN apt-get install -y autoconf autotools-dev build-essential gcc-multilib g++ software-properties-common gdb libc6-dbg:i386
RUN apt-get install -y python2.7 python2.7-dev python-pip
RUN apt-get install -y python3 python3-dev python3-pip
RUN apt-get install -y nodejs npm
RUN apt-get install -y ruby ruby-dev
RUN apt-get install -y default-jdk
## python common libary
### there is no python3-lzma
RUN apt-get install -y python-lzma
RUN pip install -U setuptools
RUN pip3 install -U setuptools

# web related
RUN apt-get install -y nmap
RUN pip install flask
## flask session cookie manager
RUN wget https://raw.githubusercontent.com/noraj/flask-session-cookie-manager/master/session_cookie_manager.py -O /home/tools/flask_session_cookie_manager.py


# crypto related
RUN apt-get install -y libgmp3-dev libecm-dev gmp-ecm
RUN apt-get install -y python-gmpy2 python-crypto
RUN apt-get install -y python3-gmpy2 python3-crypto
RUN pip install rsa sympy
RUN pip3 install rsa sympy
## yafu
RUN mkdir -p /tmp/yafu \
      && wget https://downloads.sourceforge.net/project/yafu/1.34/yafu-1.34.zip -O /tmp/yafu/yafu.zip \
      && cd /tmp/yafu \
      && unzip yafu.zip \
      && chmod a+x yafu \
      && mv yafu /usr/local/bin/yafu \
      && cd /home \
      && rm -rf /tmp/yafu
## RSHack
RUN git clone --depth=1 https://github.com/zweisamkeit/RSHack.git /home/tools/rshack \
      && rm -rf /home/tools/rshack/.git \
      && chmod a+x /home/tools/rshack/rshack.py \
      && ln -s /home/tools/rshack/rshack.py /usr/local/bin/rshack

# reverse and pwn related
RUN apt-get install -y libffi-dev qemu libstdc++6-armhf-cross
### uncompyle2 only support python2.7
RUN pip install capstone enum34 ipaddress cryptography pwntools uncompyle2
RUN pip3 install capstone enum34 ipaddress cryptography pwntools

  RUN gem install one_gadget


  RUN gem install seccomp-tools

## gdb-peda and Pwngdb
RUN git clone --depth=1 https://github.com/longld/peda.git /home/tools/peda \
      && rm -rf /home/tools/peda/.git \
      && git clone --depth=1 https://github.com/scwuaptx/Pwngdb.git /home/tools/Pwngdb \
      && rm -rf /home/tools/Pwngdb/.git \
      && cp /home/tools/Pwngdb/.gdbinit ~/ \
      && sed -i 's!~/!/home/tools/!' ~/.gdbinit

# misc related
RUN apt-get install -y outguess python-pil sleuthkit

  RUN gem install zsteg

## binwalk
RUN git clone --depth=1 https://github.com/ReFirmLabs/binwalk.git /tmp/binwalk \
      && cd /tmp/binwalk \
      && python setup.py install \
      && cd /home \
      && rm -rf /tmp/binwalk