%define major 3
%define libname %mklibname PulseAudioQt %{major}
%define devname %mklibname PulseAudioQt -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		pulseaudio-qt
Version:	1.3
Release:	2
Source0: http://download.kde.org/%{stable}/pulseaudio-qt/%{name}-%{version}.tar.xz
Summary: Qt bindings to the PulseAudio sound system
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Test)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: doxygen
BuildRequires: qt5-assistant

%description
Qt bindings to the PulseAudio sound system.

%package -n %{libname}
Summary: Qt bindings to the PulseAudio sound system
Group: System/Libraries

%description -n %{libname}
Qt bindings to the PulseAudio sound system.

%package -n %{devname}
Summary: Development files for PulseAudio Qt bindings
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for PulseAudio Qt bindings.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}.0

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%doc %{_docdir}/qt5/*
