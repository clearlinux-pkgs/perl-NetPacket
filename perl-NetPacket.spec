#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-NetPacket
Version  : 1.6.0
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/NetPacket-1.6.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/NetPacket-1.6.0.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnetpacket-perl/libnetpacket-perl_1.6.0-1.debian.tar.xz
Summary  : 'assemble/disassemble network packets at the protocol level'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-NetPacket-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
NetPacket - assemble/disassemble network packets at the protocol level
VERSION
version 1.6.0

%package dev
Summary: dev components for the perl-NetPacket package.
Group: Development
Provides: perl-NetPacket-devel = %{version}-%{release}

%description dev
dev components for the perl-NetPacket package.


%package license
Summary: license components for the perl-NetPacket package.
Group: Default

%description license
license components for the perl-NetPacket package.


%prep
%setup -q -n NetPacket-1.6.0
cd ..
%setup -q -T -D -n NetPacket-1.6.0 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/NetPacket-1.6.0/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-NetPacket
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-NetPacket/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-NetPacket/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1NetPacket.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/ARP.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/Ethernet.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/ICMP.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/IGMP.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/IP.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/IPX.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/TCP.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/UDP.pm
/usr/lib/perl5/vendor_perl/5.28.1NetPacket/USBMon.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/NetPacket.3
/usr/share/man/man3/NetPacket::ARP.3
/usr/share/man/man3/NetPacket::Ethernet.3
/usr/share/man/man3/NetPacket::ICMP.3
/usr/share/man/man3/NetPacket::IGMP.3
/usr/share/man/man3/NetPacket::IP.3
/usr/share/man/man3/NetPacket::IPX.3
/usr/share/man/man3/NetPacket::TCP.3
/usr/share/man/man3/NetPacket::UDP.3
/usr/share/man/man3/NetPacket::USBMon.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-NetPacket/LICENSE
/usr/share/package-licenses/perl-NetPacket/deblicense_copyright
