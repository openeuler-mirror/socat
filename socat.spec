%global _hardened_build 1

Summary:     Multipurpose relay
Name:        socat
Version:     1.7.3.2
Release:     8
License:     GPLv2
Url:         http://www.dest-unreach.org/socat/
Source:      http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.gz

BuildRequires: gcc openssl-devel readline-devel ncurses-devel
BuildRequires: autoconf kernel-headers > 2.6.18
BuildRequires: iproute net-tools coreutils procps-ng openssl iputils

%description
Socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor (readline), a program, or a combination of two of these.

%package_help

%prep
%autosetup
iconv -f iso8859-1 -t utf-8 CHANGES > CHANGES.utf8
mv CHANGES.utf8 CHANGES

%build
%configure  \
        --enable-help --enable-stdio \
        --enable-retry --enable-fips \
        --enable-unix --enable-ip4 --enable-ip6 \
        --enable-rawip --enable-tcp --enable-udp \
        --enable-fdnum --enable-file --enable-creat \
        --enable-listen --enable-proxy --enable-exec \
        --enable-gopen --enable-pipe --enable-termios \
        --enable-openssl --enable-sycls --enable-filan \
        --enable-system --enable-pty --enable-readline


%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_docdir}/socat
cp -a *.sh %{buildroot}/%{_docdir}/socat/

%check

%files
%license COPYING COPYING.OpenSSL
%{_bindir}/socat
%{_bindir}/filan
%{_bindir}/procan

%files help
%doc README SECURITY BUGREPORTS CHANGES DEVELOPMENT EXAMPLES FAQ PORTING
%doc %{_docdir}/socat/*.sh
%doc %{_mandir}/man1/socat.1*

%changelog
* Tue Nov 19 2019 mengxian <mengxian@huawei.com> - 1.7.3.2-8
- Package init