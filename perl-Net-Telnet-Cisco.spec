%define upstream_name    Net-Telnet-Cisco
%define upstream_version 1.12
Name:		perl-%{upstream_name}
Version:	1.12
Release:	2

Summary:	Net-Telnet-Cisco Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-Telnet-Cisco
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VINSWORLD/Net-Telnet-Cisco-1.12.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Telnet::Cisco adds additional functionality to 
Net::Telnet that helps you automate Cisco router management
and statistic gathering.

%prep
%setup -q -n Net-Telnet-Cisco-1.12

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%{perl_vendorlib}/Net/Telnet/*
%{perl_vendorlib}/auto/Net/Telnet/*
%{_mandir}/*/*

