#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-NetPacket
Version  : 1.7.2
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/NetPacket-1.7.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/NetPacket-1.7.2.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnetpacket-perl/libnetpacket-perl_1.6.0-1.debian.tar.xz
Summary  : 'assemble/disassemble network packets at the protocol level'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-NetPacket-license = %{version}-%{release}
Requires: perl-NetPacket-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NetPacket version 0.41.1
This is a whole bunch of
Perl modules which I have named NetPacket::*.  These modules do basic
disassembly of network packets of various Internet protocols.  NetPacket
0.01 contained hooks for assembly of packets which have been implemented in
version 0.04 by Stephanie Wehner <atrak@itsx.com>.

%package dev
Summary: dev components for the perl-NetPacket package.
Group: Development
Provides: perl-NetPacket-devel = %{version}-%{release}
Requires: perl-NetPacket = %{version}-%{release}

%description dev
dev components for the perl-NetPacket package.


%package license
Summary: license components for the perl-NetPacket package.
Group: Default

%description license
license components for the perl-NetPacket package.


%package perl
Summary: perl components for the perl-NetPacket package.
Group: Default
Requires: perl-NetPacket = %{version}-%{release}

%description perl
perl components for the perl-NetPacket package.


%prep
%setup -q -n NetPacket-1.7.2
cd %{_builddir}
tar xf %{_sourcedir}/libnetpacket-perl_1.6.0-1.debian.tar.xz
cd %{_builddir}/NetPacket-1.7.2
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/NetPacket-1.7.2/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-NetPacket
cp %{_builddir}/NetPacket-1.7.2/LICENSE %{buildroot}/usr/share/package-licenses/perl-NetPacket/72832ad015dadb7d5df745c4b2b3638a06970d9f
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-NetPacket/738acd3bc6126f688fa1101e42d824b6dc2d7aa5
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/NetPacket.3
/usr/share/man/man3/NetPacket::ARP.3
/usr/share/man/man3/NetPacket::Ethernet.3
/usr/share/man/man3/NetPacket::ICMP.3
/usr/share/man/man3/NetPacket::ICMPv6.3
/usr/share/man/man3/NetPacket::IGMP.3
/usr/share/man/man3/NetPacket::IP.3
/usr/share/man/man3/NetPacket::IPX.3
/usr/share/man/man3/NetPacket::IPv6.3
/usr/share/man/man3/NetPacket::TCP.3
/usr/share/man/man3/NetPacket::UDP.3
/usr/share/man/man3/NetPacket::USBMon.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-NetPacket/72832ad015dadb7d5df745c4b2b3638a06970d9f
/usr/share/package-licenses/perl-NetPacket/738acd3bc6126f688fa1101e42d824b6dc2d7aa5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/ARP.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/Ethernet.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/ICMP.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/ICMPv6.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/IGMP.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/IP.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/IPX.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/IPv6.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/TCP.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/UDP.pm
/usr/lib/perl5/vendor_perl/5.32.1/NetPacket/USBMon.pm
