%define name enity
%define version 0.0.1
%define release %mkrel 9

Summary: Command line tool for creating Etk-based dialogs
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: Development/Other
URL: https://www.enlightenment.org/
Source: %{name}-%{version}.tar.bz2
BuildRequires: etk-devel >= 0.1.0.042, ecore-devel >= 0.9.9.050
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Enity allows users to create Etk dialogs using shell scripts or other
scripting languages that can call programs. The basic idea is to ease
the development of quick interfaces for input, configuration,
installation, etc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING* INSTALL README doc/*
%{_bindir}/%{name}
