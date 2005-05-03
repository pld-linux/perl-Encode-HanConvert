#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Encode
%define		pnam	HanConvert
Summary:	Encode::HanConvert - Traditional and Simplified Chinese mappings
Summary(pl):	Encode::HanConvert - Mapowanie tradycyjne i uproszczone ideogramów jêzyka chiñskiego
Name:		perl-Encode-HanConvert
Version:	0.31
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	91d9a77355aa022958ce349ad11d95a7
BuildRequires:	perl-devel >= 1:5.7.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Encode >= 2.09-1
%{?with_tests:BuildRequires:  perl(Module::Signature)}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In the 1950's, the Chinese government simplified over 2000 Chinese
characters. Taiwan and Hong Kong still use the traditional characters.
The simplified characters are hard to read if you only know the
traditional ones, and vice-versa. This module attempts to convert
Chinese text between the two forms, using character-by-character
transliteration.

%description -l pl
W latach 1950-tych rz±d chiñski upro¶ci³ ponad 2000 chiñskich
ideogramów. Tajwan i Hong Kong nadal u¿ywaj± ideogramów tradycyjnych.
Ideogramy uproszczone s± nieczytelne dla znaj±cych tylko tradycyjne i
odwrotnie. Modu³ dokonuje wzajemnej konwersji tekstów chiñskich w tych
dwu postaciach stosuj±c z transliteracjê znak po znaku.

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
%doc Changes
%dir %{_bindir}
%dir %{perl_vendorarch}/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%{perl_vendorarch}/%{pdir}/%{pnam}/*.pm
%{perl_archlib}/*.pod
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.so
