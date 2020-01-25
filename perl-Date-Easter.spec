#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Date
%define		pnam	Easter
Summary:	Date::Easter - calculate Easter for any given year
Summary(pl.UTF-8):	Date::Easter - obliczanie daty Wielkanocy w danym roku
Name:		perl-Date-Easter
Version:	1.14
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a6e8aa50ffdc1958dc3d9585e22422f
URL:		http://search.cpan.org/dist/Date-Easter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Easter is a Perl module for calculating Easter for a given year.

%description -l pl.UTF-8
Date::Easter jest modułem Perla do obliczania daty Wielkanocy w danym
roku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorlib}/Date/Easter.pm
%{_mandir}/man3/*
