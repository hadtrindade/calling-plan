FROM debian:buster-slim

LABEL AUTHOR="HADD TRINDADE"
LABEL VERSION="1.0.0"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Recife

WORKDIR /usr/src/

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
    autoconf \
    binutils-dev \
    build-essential \
    ca-certificates \
    curl \
    file \
    libcurl4-openssl-dev \
    libedit-dev \
    libgsm1-dev \
    libjansson4 \
    libjansson-dev \
    libogg-dev \
    libpopt-dev \
    libresample1-dev \
    libspandsp-dev \
    libspeex-dev \
    libspeexdsp-dev \
    libsqlite3-dev \
    libsrtp2-dev \
    libssl-dev \
    libvorbis-dev \
    libxml2-dev \
    libxslt1-dev \
    procps \
    portaudio19-dev \
    unixodbc \
    unixodbc-dev \
    odbcinst \
    uuid \
    uuid-dev \
    xmlstarlet \
    && curl -vsL http://downloads.asterisk.org/pub/telephony/certified-asterisk/asterisk-certified-16.8-current.tar.gz | tar --strip-components 1 -xz || \
    curl -vsL http://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/asterisk-certified-16.8-current.tar.gz | tar --strip-components 1 -xz \
    && ./configure --without-inotify --with-resample --with-pjproject-bundled \
    && make menuselect/menuselect menuselect-tree menuselect.makeopts \
    && menuselect/menuselect --enable chan_sip menuselect.makeopts \
    && menuselect/menuselect --disable-category MENUSELECT_CORE_SOUNDS \
    && menuselect/menuselect --disable-category MENUSELECT_MOH \
    && menuselect/menuselect --disable-category MENUSELECT_EXTRA_SOUNDS \
    && make install \
    && make samples 


RUN apt-get --yes purge \
    $(dpkg -l|grep '\-dev'|awk '{print $2}'|xargs) \
    autoconf \
    build-essential \
    bzip2 \
    cpp \
    m4 \
    make \
    patch \
    perl \
    perl-modules \
    pkg-config \
    xz-utils \
    && rm -rf /usr/src/* \
    && mkdir -p /etc/asterisk/ \
         /var/spool/asterisk/fax \
    && useradd --system asterisk \
    && chown -R asterisk:asterisk \
                /etc/asterisk \
                /var/*/asterisk \
                /usr/*/asterisk \
    && chmod -R 750 /var/spool/asterisk

COPY docker-entrypoint.sh .

EXPOSE 5060/udp 5060/tcp

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["/usr/sbin/asterisk", "-vvvdddf", "-T", "-W", "-U", "asterisk", "-p"]
