%define upstream_name    Net-Telnet-Cisco
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Net-Telnet-Cisco Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Telnet::Cisco adds additional functionality to 
Net::Telnet that helps you automate Cisco router management
and statistic gathering.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%{perl_vendorlib}/Net/Telnet/*
%{perl_vendorlib}/auto/Net/Telnet/*
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 404248
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.10-5mdv2009.0
+ Revision: 241804
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.10-3mdv2008.0
+ Revision: 25196
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.10-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- URL
- use mkrel

* Tue Feb 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.10-1mdk
- 1.10

