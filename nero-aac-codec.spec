# NOTE:
# - requires GLIBC_2.4
#
# TODO
# - http://security.gentoo.org/glsa/glsa-200803-08.xml
#
# Conditional build:
%bcond_with	license_agreement	# generates package

%define		rel 0.1
%define		base_name	nero-aac-codec
Summary:	Nero AAC Codec
%if %{with license_agreement}
Name:		%{base_name}
%else
Name:		%{base_name}-installer
%endif
Version:	1.3.3.0
Release:	%{rel}%{?with_license_agreement:wla}
License:	Free for non-commercial use
Group:		Libraries
%if %{with license_agreement}
Source0:	http://ftp6.nero.com/tools/NeroDigitalAudio.zip
%else
Source1:	license-installer.sh
%endif
%if %{without license_agreement}
Requires:	rpm-build-tools
%endif
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define     _enable_debug_packages  0

%description
The Nero AAC Encoder is a fully functional, high quality, commandline
LC and HE AAC encoder.

%if %{without license_agreement}
This package is empty. Build package yourself with "--with license_agreement"
and install the wla release.

%endif

%prep
%if %{with license_agreement}
%setup -q -c
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{without license_agreement}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}
install %{_specdir}/%{base_name}.spec $RPM_BUILD_ROOT%{_datadir}

sed -e '
	s/@BASE_NAME@/%{base_name}/g
	s/@TARGET_CPU@/%{_target_cpu}/g
	s-@VERSION@-%{version}-g
	s-@RELEASE@-%{release}-g
	s,@SPECFILE@,%{_datadir}/%{base_name}.spec,g
' %{SOURCE1} > $RPM_BUILD_ROOT%{_bindir}/%{base_name}.install

%else

install -d $RPM_BUILD_ROOT%{_bindir}
install linux/* $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_libdir}/codecs/*.xa
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{without license_agreement}
%post
%{_bindir}/%{base_name}.install
%endif

%files
%defattr(644,root,root,755)
%if %{without license_agreement}
%attr(755,root,root) %{_bindir}/%{base_name}.install
%{_datadir}/%{base_name}.spec
%else
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%endif
