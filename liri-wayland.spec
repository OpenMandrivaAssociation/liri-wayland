%define major 0
%define libplatform %mklibname LiriPlatform %{major}
%define libwaylandclient %mklibname WaylandClient %{major}
%define libwaylandserver %mklibname WaylandServer %{major}
%define devname %mklibname -d liri-wayland
%define snapshot 20170219

Summary:        QtWayland additions and QPA plugin
Name:           liri-wayland
Version:        0.9.0.1
Release:        0
License:	LGPLv3
Url:		https://github.com/lirios/
#Source0:	https://github.com/lirios/wayland/archive/v%{version}.tar.gz
Source0:	%{name}-%{version}-%{snapshot}.tar.xz

BuildRequires:	qt5-devel
BuildRequires:	qt5-qtwayland-private-devel
BuildRequires:	qt5-qtcompositor-private-devel
BuildRequires:	qt5-qtqml-private-devel
BuildRequires:	qt5-qtquick-private-devel
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickTest)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(Qt5WaylandCompositor)
BuildRequires:	cmake
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	extra-cmake-modules
BuildRequires:	%{_lib}qt5platformcompositorsupport-static-devel
BuildRequires:	%{_lib}qt5eglsupport-static-devel
BuildRequires:	%{_lib}qt5fontdatabasesupport-static-devel
BuildRequires:	%{_lib}qt5themesupport-static-devel
BuildRequires:	%{_lib}qt5servicesupport-static-devel
BuildRequires:	%{_lib}qt5eventdispatchersupport-static-devel

%description
QtWayland additions and QPA plugin.

%package -n     %{libplatform}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libplatform}
Library for %{name}

%package -n     %{libwaylandclient}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libwaylandclient}
Library for %{name}

%package -n     %{libwaylandserver}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libwaylandserver}
Library for %{name}

%package -n     %{devname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libplatform} = %{EVRD}
Requires:       %{libwaylandclient} = %{EVRD}
Requires:       %{libwaylandserver} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{devname}
Components for Qt Quick applications with Material Design and Universal
development files

%prep
%setup -qn %{name}-%{version}-%{snapshot}

%build
%cmake_qt5 -DBUILD_HACK=ON -DBUILD_HACK:BOOL=ON
%make

%install
%makeinstall_std -C build

%files
%{_libdir}/qml/Liri
%{_libdir}/plugins/liri/egldeviceintegration/kms.so
%{_libdir}/plugins/wayland-decoration-client/libmaterial.so
%{_libdir}/plugins/platforms/lirieglfs.so
%{_libdir}/plugins/wayland-shell-integration/libfullscreen-shell.so

%files -n %{libplatform}
%{_libdir}/libLiriPlatform.so.%{major}*

%files -n %{libwaylandclient}
%{_libdir}/libLiriWaylandClient.so.%{major}*

%files -n %{libwaylandserver}
%{_libdir}/libLiriWaylandServer.so.%{major}*

%files -n %{devname}
%{_libdir}/libLiriWaylandClient.so
%{_libdir}/libLiriWaylandServer.so
%{_libdir}/libLiriPlatform.so
%{_includedir}/Liri
%{_libdir}/cmake/Liri*
%{_prefix}/mkspecs/modules/qt_Liri*.pri
