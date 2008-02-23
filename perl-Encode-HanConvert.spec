#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Encode
%define		pnam	HanConvert
Summary:	Encode::HanConvert - Traditional and Simplified Chinese mappings
Summary(pl.UTF-8):	Encode::HanConvert - Mapowanie tradycyjne i uproszczone ideogramów języka chińskiego
Name:		perl-Encode-HanConvert
Version:	0.34
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9ca7311ec9ec8d79a6e69c724cb37e3
URL:		http://search.cpan.org/dist/Encode-HanConvert/
BuildRequires:	perl(Encode) >= 2.09
BuildRequires:	perl-devel >= 1:5.7.3
BuildRequires:	rpm-perlprov >= 4.1-13
%{?with_tests:BuildRequires:  perl-Module-Signature}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In the 1950's, the Chinese government simplified over 2000 Chinese
characters. Taiwan and Hong Kong still use the traditional characters.
The simplified characters are hard to read if you only know the
traditional ones, and vice-versa. This module attempts to convert
Chinese text between the two forms, using character-by-character
transliteration.

%description -l pl.UTF-8
W latach 1950-tych rząd chiński uprościł ponad 2000 chińskich
ideogramów. Tajwan i Hong Kong nadal używają ideogramów tradycyjnych.
Ideogramy uproszczone są trudne do odczytania dla znających tylko
tradycyjne i odwrotnie. Moduł próbuje konwertować teksty chińskie
pomiędzy tymi postaciami stosując transliterację znak po znaku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Encode/HanConvert.pm
%dir %{perl_vendorarch}/Encode/HanConvert
%{perl_vendorarch}/Encode/HanConvert/*.pm
%dir %{perl_vendorarch}/auto/Encode/HanConvert
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/HanConvert/HanConvert.so
%{_mandir}/man1/*
