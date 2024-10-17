%define name x11-driver-input-hidtouch
%define sname xf86-input-hidtouch
%define version 9.04.04
%define distname %{sname}-%{version}
%define release %mkrel 1

Summary: hidtouch input device driver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.zip
Patch0:  xf86-input-hidtouch-9.04.04-xiABI3.patch
License: GPLv3+
Group: System/X11
Url: https://sourceforge.net/projects/hidtouchsuite/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: x11-server-devel libx11-devel x11-util-macros

%description
hidtouch is an input device driver supporting USB touchscreens that
are not recognized by Linux as event devices but as regular HID
devices. A few companion programs will ease the setup and calibration
process.

%prep
%setup -q -n %{distname}
%patch0 -p1 -b .xiABI3

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/hidtouch_drv.la
%{_libdir}/xorg/modules/input/hidtouch_drv.so
