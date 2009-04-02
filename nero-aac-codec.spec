# TODO
# - http://security.gentoo.org/glsa/glsa-200803-08.xml
#
# Conditional build:
%bcond_with	license_agreement	# generates package
%define		_rel .1
Summary:	Nero AAC Codec
Name:		nero-aac-codec
Version:	1.3.3.0
Release:	%{_rel}%{?with_license_agreement:wla}
License:	Free for non-commercial use
Group:		Libraries
%if %{with license_agreement}
Source0:	http://ftp6.nero.com/tools/NeroDigitalAudio.zip
%endif
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define     _enable_debug_packages  0

%description
The Nero AAC Encoder is a fully functional, high quality, commandline
LC and HE AAC encoder.
%if !%{with license_agreement}
This package is empty. Build package yourself with "--with license_agreement" and install
The Nero AAC Encoder is a fully functional, high quality, commandline
LC and HE AAC encoder. the wla release.
%endif

The Nero AAC Encoder is a fully functional, high quality, commandline
LC and HE AAC encoder. the wla release.
%prep
%if %{with license_agreement}
%setup -q -c
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with license_agreement}
install -d $RPM_BUILD_ROOT%{_bindir}
install linux/* $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_libdir}/codecs/*.xa
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{with license_agreement}
%attr(755,root,root) %{_bindir}/*
%doc *.txt
%endif
