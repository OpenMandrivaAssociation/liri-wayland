%define major 0
%define libvibecore %mklibname VibeCore %{major}
%define libvibesettings %mklibname VibeSettings %{major}
%define devname %mklibname -d VibeCore
%define snapshot 20170210

Summary:        A collection of core classes used throughout Liri
Name:           liri-wayland
Version:        0.9.0.1
Release:        0
License:	LGPLv3
Url:		https://github.com/lirios/
#Source0:	https://github.com/lirios/wayland/archive/v%{version}.tar.gz
Source0:	%{name}-%{version}-%{snapshot}.tar.xz

BuildRequires:	qt5-devel
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickTest)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(Qt5WaylandCompositor)
BuildRequires:	cmake
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	extra-cmake-modules
BuildRequires:	%{_lib}qt5platformcompositorsupport-static-devel
BuildRequires:	%{_lib}qt5eglsupport-static-devel

%description
A collection of core classes used throughout Liri

%package -n     %{libvibecore}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libvibecore}
Library for %{name}

%package -n     %{libvibesettings}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libvibecore}
Library for %{name}

%package -n     %{devname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libvibecore} = %{EVRD}
Requires:       %{libvibesettings} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{devname}
Components for Qt Quick applications with Material Design and Universal
development files

%prep
%setup -qn %{name}-%{version}-%{snapshot}

%build
%cmake_qt5 -DBUILD_HACK=ON
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/liri-notify
%{_libdir}/qml/Vibe

%files -n %{libvibecore}
%{_libdir}/libVibeCore.so.%{major}*

%files -n %{libvibesettings}
%{_libdir}/libVibeSettings.so.%{major}*

%files -n %{devname}
%{_libdir}/libVibeCore.so
%{_libdir}/libVibeSettings.so
%{_includedir}/Vibe/
%{_libdir}/cmake/Vibe/
