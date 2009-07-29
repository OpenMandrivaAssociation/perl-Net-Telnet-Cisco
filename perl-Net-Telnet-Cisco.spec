%define upstream_name    Net-Telnet-Cisco
%define upstream_version 1.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Net-Telnet-Cisco Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Net::Telnet::Cisco adds additional functionality to 
Net::Telnet that helps you automate Cisco router management
and statistic gathering.

%prep
%setup -q -n %{name}-%{upstream_version}

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
