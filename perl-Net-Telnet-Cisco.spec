%define module  Net-Telnet-Cisco
%define name    perl-%{module}
%define version 1.10
%define release %mkrel 2


Name:		 %name
Summary:	 Net-Telnet-Cisco Perl module
Version:	 %version
Release:	 %release
License:	 GPL or Artistic
Group:		 Development/Perl
Source:		 ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{name}-%{version}.tar.bz2
BuildRoot:	 %_tmppath/%name-%version-root
URL:		 http://search.cpan.org/dist/%{module}
Buildarch:	noarch

%description
    Net::Telnet::Cisco adds additional functionality to 
    Net::Telnet that helps you automate Cisco router management
    and statistic gathering.


%prep

%setup

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{perl_vendorlib}/Net/Telnet/*
%{perl_vendorlib}/auto/Net/Telnet/*
%{_mandir}/*/*


