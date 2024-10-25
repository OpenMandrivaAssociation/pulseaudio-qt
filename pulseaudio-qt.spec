%define major 5
%define oldlibname %mklibname PulseAudioQt 3
%define olddevname %mklibname PulseAudioQt -d
%define libname %mklibname KF5PulseAudioQt
%define devname %mklibname KF5PulseAudioQt -d
%define lib6name %mklibname KF6PulseAudioQt
%define dev6name %mklibname KF6PulseAudioQt -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20231101

Name:		pulseaudio-qt
Version:	1.6.1
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/pulseaudio-qt/-/archive/master/pulseaudio-qt-master.tar.bz2#/%{name}-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/pulseaudio-qt/%{name}-%{version}.tar.xz
%endif
Summary:	Qt bindings to the PulseAudio sound system
URL:		https://kde.org/
License:	GPL
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	doxygen
BuildRequires:	qt5-assistant

%description
Qt bindings to the PulseAudio sound system.

%package -n %{libname}
Summary: Qt 5 bindings to the PulseAudio sound system
Group: System/Libraries
%rename %{oldlibname}

%description -n %{libname}
Qt 5 bindings to the PulseAudio sound system.

%package -n %{devname}
Summary: Development files for PulseAudio Qt 5 bindings
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files for PulseAudio Qt 5 bindings.

%package -n %{lib6name}
Summary: Qt 6 bindings to the PulseAudio sound system
Group: System/Libraries

%description -n %{lib6name}
Qt bindings to the PulseAudio sound system.

%package -n %{dev6name}
Summary: Development files for PulseAudio Qt 6 bindings
Group: Development/KDE and Qt
Requires: %{lib6name} = %{EVRD}

%description -n %{dev6name}
Development files for PulseAudio Qt 6 bindings.

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
%cmake_kde5
cd ..

export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build
%ninja -C build-qt6

%install
%ninja_install -C build
%ninja_install -C build-qt6

%files -n %{libname}
%{_libdir}/libKF5PulseAudioQt.so.%{major}
%{_libdir}/libKF5PulseAudioQt.so.1*

%files -n %{devname}
%{_includedir}/KF5/*
%{_libdir}/libKF5PulseAudioQt.so
%{_libdir}/cmake/KF5*
%{_libdir}/pkgconfig/KF5PulseAudioQt.pc
%doc %{_docdir}/qt5/*

%files -n %{lib6name}
%{_libdir}/libKF6PulseAudioQt.so.%{major}
%{_libdir}/libKF6PulseAudioQt.so.1*

%files -n %{dev6name}
%{_includedir}/KF6/*
%{_libdir}/libKF6PulseAudioQt.so
%{_libdir}/pkgconfig/KF6PulseAudioQt.pc
%{_libdir}/cmake/KF6*
