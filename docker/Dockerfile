FROM alpine:3.8

WORKDIR /home/

ENV REPO_BRANCH master

RUN apk add --update \
    git \
 && git clone --branch ${REPO_BRANCH} https://github.com/ABSLord/DRFdnsenum \
 && cd DRFdnsenum/ \
 && apk add --update \
    perl \
    perl-utils \
    perl-module-install \
    build-base \
    perl-module-build \
    musl-dev \
    perl-dev \
    python3 \
    py3-pip \
 && pip3 install -r requirements.txt \
 && cpan --notest -f -i \
    Log::Log4perl \
    Digest::HMAC \
    Canary::Stability \
    Getopt::Long \
    IO::File \
    Thread::Queue \
    Net::IP \
    Net::DNS \
    Net::Netmask \
    HTML::Parser \
    WWW::Mechanize \
    XML::Writer \
    String::Random

WORKDIR /home/DRFdnsenum/

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
