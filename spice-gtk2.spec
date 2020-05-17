#
# Conditional build:
%bcond_without	smartcard		# Smartcard support
%bcond_without	usbredir		# USB redirection
%bcond_without	static_libs		# static libraries
%bcond_without	system_spiceglib	# disable packaging spice-glib

%if %{without system_spiceglib}
# usbredir option doesn't affect gtk library (just glib library and spicy program)
%undefine	with_usbredir
%endif

Summary:	SPICE Client GTK 2.0 library
Summary(pl.UTF-8):	Biblioteka kliencka SPICE GTK 2.0
Name:		spice-gtk2
Version:	0.31
Release:	3
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://www.spice-space.org/download/gtk/spice-gtk-%{version}.tar.bz2
# Source0-md5:	1ef438eabc19b0f339d746a93cab4f56
Patch0:		%{name}-builddir.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-no-tunnel.patch
Patch3:		%{name}-openssl.patch
Patch4:		%{name}-sysmacros.patch
URL:		https://spice-space.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	celt051-devel >= 0.5.1.1
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	gcc >= 5:3.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gobject-introspection-devel >= 0.9.4
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.40.0
%{?with_smartcard:BuildRequires:	libcacard-devel >= 0.1.2}
BuildRequires:	libepoxy-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libsoup-devel >= 2.50
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	lz4-devel
BuildRequires:	openssl-devel >= 1.0.0
BuildRequires:	opus-devel >= 0.9.14
BuildRequires:	perl-Text-CSV
BuildRequires:	perl-base >= 1:5.8.1
BuildRequires:	phodav-devel >= 2.0
BuildRequires:	pixman-devel >= 0.17.7
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python >= 2
BuildRequires:	python-devel >= 2.0
BuildRequires:	python-pygtk-devel >= 2:2.0.0
BuildRequires:	python-pyparsing
BuildRequires:	python-six
BuildRequires:	sed >= 4.0
BuildRequires:	spice-protocol >= 0.12.11
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	zlib-devel
%if %{with usbredir}
BuildRequires:	acl-devel
BuildRequires:	libusb-devel >= 1.0.16
BuildRequires:	polkit-devel >= 0.96
BuildRequires:	usbredir-devel >= 0.5.2
%endif
%{?with_smartcard:Requires:	libcacard >= 0.1.2}
Requires:	gtk+2 >= 2:2.18.0
Requires:	spice-glib >= %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPICE Client GTK 2.0 library.

%description -l pl.UTF-8
Biblioteka kliencka SPICE GTK 2.0.

%package devel
Summary:	Header files for SPICE GTK 2.0 Client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej SPICE GTK 2.0
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.18.0
Requires:	spice-glib-devel >= %{version}-%{release}

%description devel
Header files for SPICE GTK 2.0 client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej SPICE GTK 2.0.

%package static
Summary:	Static SPICE GTK 2.0 client library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka SPICE GTK 2.0
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SPICE GTK 2.0 client library.

%description static -l pl.UTF-8
Statyczna biblioteka kliencka SPICE GTK 2.0.

%package -n python-spice-gtk
Summary:	Python interface to SPICE client GTK library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki klienckiej SPICE GTK
Group:		Libraries/Python
Requires:	spice-gtk2 = %{version}-%{release}

%description -n python-spice-gtk
Python interface to SPICE client GTK library.

%description -n python-spice-gtk -l pl.UTF-8
Pythonowy interfejs do biblioteki klienckiej SPICE GTK.

%package -n spice-glib
Summary:	SPICE Client GLib library
Summary(pl.UTF-8):	Biblioteka kliencka SPICE GLib
Group:		Libraries
Requires:	celt051 >= 0.5.1.1
Requires:	glib2 >= 1:2.44
%{?with_smartcard:Requires:	libcacard >= 0.1.2}
Requires:	libsoup >= 2.50
Requires:	opus >= 0.9.14
Requires:	pixman >= 0.17.7
%if %{with usbredir}
Requires:	libusb >= 1.0.16
Requires:	usbredir >= 0.5.2
%endif

%description -n spice-glib
SPICE Client GLib library.

%description -n spice-glib -l pl.UTF-8
Biblioteka kliencka SPICE GLib.

%package -n spice-glib-devel
Summary:	Header files for SPICE Client GLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej SPICE GLib
Group:		Development/Libraries
Requires:	celt051-devel >= 0.5.1.1
Requires:	cyrus-sasl-devel >= 2.0
Requires:	glib2-devel >= 1:2.44
%{?with_smartcard:Requires:	libcacard-devel >= 0.1.2}
Requires:	libjpeg-devel
Requires:	openssl-devel >= 1.0.0
Requires:	pixman-devel >= 0.17.7
Requires:	pulseaudio-devel
Requires:	spice-glib = %{version}-%{release}
Requires:	spice-protocol >= 0.12.11
%if %{with usbredir}
Requires:	libusb-devel >= 1.0.16
Requires:	usbredir-devel >= 0.5.2
%endif

%description -n spice-glib-devel
Header files for SPICE Client GLib library.

%description -n spice-glib-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej SPICE GLib.

%package -n spice-glib-static
Summary:	SPICE Client GLib static library
Summary(pl.UTF-8):	Statyczna biblioteka kliencka SPICE GLib
Group:		Development/Libraries
Requires:	spice-glib-devel = %{version}-%{release}

%description -n spice-glib-static
SPICE Client GLib static library.

%description -n spice-glib-static -l pl.UTF-8
Statyczna biblioteka kliencka SPICE GLib.

%package -n spice-glib-usb
Summary:	USB redirection ACL helper for SPICE Client GLib library
Summary(pl.UTF-8):	Program pomocniczy ACL do przekierowań USB dla biblioteki klienckiej SPICE GLib
Group:		Applications/System
Requires:	polkit >= 0.96
Requires:	spice-glib = %{version}-%{release}

%description -n spice-glib-usb
USB redirection ACL helper for SPICE Client GLib library.

%description -n spice-glib-usb -l pl.UTF-8
Program pomocniczy ACL do przekierowań USB dla biblioteki klienckiej
SPICE GLib.

%prep
%setup -q -n spice-gtk-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# force regeneration
%{__rm} spice-common/common/generated_*marshallers.[ch]

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd spice-common
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..

%configure \
	--enable-lz4 \
	--disable-controller \
	--disable-silent-rules \
	%{!?with_smartcard:--disable-smartcard} \
	%{?with_static_libs:--enable-static} \
	%{!?with_usbredir:--disable-usbredir} \
	--with-gtk=2.0 \
	--with-html-dir=%{_gtkdocdir} \
	--with-pnp-ids-path=/lib/hwdata/pnp.ids \
	--with-usb-ids-path=/lib/hwdata/usb.ids
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/SpiceClientGtk.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/SpiceClientGtk.a
%endif
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%{__rm} $RPM_BUILD_ROOT%{_bindir}/* \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	$RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/spice-gtk.mo \
	$RPM_BUILD_ROOT%{_datadir}/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy \
	$RPM_BUILD_ROOT%{_datadir}/vala/vapi/spice-protocol.vapi
%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}/spice-gtk

%if %{with system_spiceglib}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libspice-client-glib-2.0.* \
	$RPM_BUILD_ROOT%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib \
	$RPM_BUILD_ROOT%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/spice-client-glib-2.0.pc
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/spice-client-glib-2.0
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n spice-glib -p /sbin/ldconfig
%postun	-n spice-glib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libspice-client-gtk-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-gtk-2.0.so.4
%{_libdir}/girepository-1.0/SpiceClientGtk-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-gtk-2.0.so
%{_includedir}/spice-client-gtk-2.0
%{_pkgconfigdir}/spice-client-gtk-2.0.pc
%{_datadir}/gir-1.0/SpiceClientGtk-2.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-gtk-2.0.a
%endif

%files -n python-spice-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/SpiceClientGtk.so

%if %{without system_spiceglib}
%files -n spice-glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspice-client-glib-2.0.so.8
%{_libdir}/girepository-1.0/SpiceClientGLib-2.0.typelib

%files -n spice-glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspice-client-glib-2.0.so
%{_includedir}/spice-client-glib-2.0
%{_pkgconfigdir}/spice-client-glib-2.0.pc
%{_datadir}/gir-1.0/SpiceClientGLib-2.0.gir

%if %{with static_libs}
%files -n spice-glib-static
%defattr(644,root,root,755)
%{_libdir}/libspice-client-glib-2.0.a
%endif
%endif
