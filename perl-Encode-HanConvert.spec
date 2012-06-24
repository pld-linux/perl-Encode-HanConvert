#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Encode
%define		pnam	HanConvert
Summary:	Encode::HanConvert - Traditional and Simplified Chinese mappings
Summary(pl):	Encode::HanConvert - Mapowanie tradycyjne i uproszczone ideogram�w j�zyka chi�skiego
Name:		perl-Encode-HanConvert
Version:	0.31
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	91d9a77355aa022958ce349ad11d95a7
BuildRequires:	perl-Encode >= 2.09-1
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

%description -l pl
W latach 1950-tych rz�d chi�ski upro�ci� ponad 2000 chi�skich
ideogram�w. Tajwan i Hong Kong nadal u�ywaj� ideogram�w tradycyjnych.
Ideogramy uproszczone s� nieczytelne dla znaj�cych tylko tradycyjne i
odwrotnie. Modu� dokonuje wzajemnej konwersji tekst�w chi�skich w tych
dwu postaciach stosuj�c z transliteracj� znak po znaku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
