%define sname	cryptui

%define major	0
%define gimajor	0.0
%define libname %mklibname %{sname} %{major}
%define girname %mklibname %{sname}-gir %{gimajor}
%define devname %mklibname -d %{sname}

Summary:	Interface components for OpenPGP
Name:		libcryptui
Version:	3.12.2
Release:	5
License:	LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://seahorse.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libcryptui/%{name}-%{version}.tar.xz
Patch1:		libcryptui-3.12.2-gnugpg2.1.patch
Patch2:		0002-Accept-GnuPG-2.2.x-as-supported-version.patch
BuildRequires:	autoconf
BuildRequires:	gnupg
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	gnupg
BuildRequires:	gpgme-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(sm)
Requires:	gnupg
Conflicts:	seahorse < 3.1.4

%description
libcryptui is a library used for prompting for PGP keys.

%package -n %{libname}
Group:		System/Libraries
Summary:	Interface components for OpenPGP

%description -n %{libname}
libcryptui is a library used for prompting for PGP keys.
 
%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Header files required to develop with libcryptui
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The libcryptui-devel package contains the header files and developer
documentation for the libcryptui library.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fiv
%configure \
	--disable-dependency-tracking \
	--disable-update-mime-database \
	--disable-schemas-compile 

%make_build

%install
%make_install

%find_lang %{sname}

%files -f %{sname}.lang
%{_bindir}/seahorse-daemon
%{_datadir}/cryptui
%{_datadir}/dbus-1/services/*.service
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pixmaps/cryptui
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/CryptUI-%{gimajor}.typelib

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/%{name}



%changelog
* Mon Jul 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 809932
- imported package libcryptui

