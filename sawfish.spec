Summary:	A highly configurable and extensible X11 window manager
Summary(pl):	Window Manad�er dla X11 o du�ych mo�liwo�ciach konfiguracyjnych i skalowalno�ci
Name:		sawfish
Version:	0.38
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
Source0:	ftp://sawmill.sourceforge.net/pub/sawmill/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_version.patch
Patch2:		%{name}-no_libnsl.spec
Patch3:		%{name}-make.patch
URL:		http://sawmill.sourceforge.net/
Icon:		sawfish.xpm
Requires:	rep-gtk >= 0.14-3
BuildRequires:	autoconf
BuildRequires:	esound-devel
BuildRequires:	control-center-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	librep-devel >= 0.13.2-2
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gmp-devel
BuildRequires:	rep-gtk >= 0.14-3
BuildRequires:	rep-gtk-gnome >= 0.14-3
BuildRequires:	rep-gtk-libglade >= 0.14-3
Obsoletes:	sawmill
Obsoletes:	sawmill-gnome
Obsoletes:	sawmill-themer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is an extensible window manager using a LISP-based scripting
language--all window decorations are configurable, the basic idea is
to have as much user-interface policy as possible controlled through
the Lisp language. All configuration may be performed through a GTK
interface; sawmill is mostly-GNOME compliant.

%description -l pl
Window manad�er o du�ych mo�liwo�ciach rozszerzania, u�ywaj�cy
bazowanego na LISP'ie j�zyka skryptowego, dzi�ki czemu wszystkie
dodatki do okien s� configurowalne. Og�ln� ide� jest, aby da� jak
najwi�ksz� kontrol� w r�ce u�ytkownika poprzez graficzny interfejs
dzi�ki w�a�nie LISP'owi.
Sawmill jest najbardziej zgodny z GNOME'em.

%package gnome
Summary:	GNOME support for sawmill
Summary(pl):	Support GNOME'a dla sawmill'a
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
Requires:	%{name} = %{version}
Requires:	rep-gtk-gnome >= 0.14-3
Requires:	rep-gtk-libglade >= 0.14-3

%description gnome
Optional GNOME support for sawmill. Includes a wm-entries spec, and a
control center applet.

%description -l pl gnome
Opcjonalny support GNOME'a dla sawmill'a. Zawiera aplet dla control-center
oraz wm-entries spec.

%package themer
Summary:	GUI for creating sawmill themes
Summary(pl):	GUI do tworzenia temat�w dla sawmill'a
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
Requires:	%{name} = %{version}

%description themer
Optional theme builder for sawmill. Allows static window themes to be
created/edited in a graphical environment.

%description -l pl themer
Opcjonalna aplikacja do tworzenia temat�w dla sawfish'a. Pozwala na 
tworzenie/modyfikacj� statycznych temat�w w �rodowisku graficznym.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
gettextize --copy --force
autoconf
%configure \
	--disable-static \
	--enable-capplet \
	--enable-themer \
	--enable-gnome-widgets \
	--with-readline \
	--with-esd \
	--with-audiofile \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	G_MENU_DIR=%{_applnkdir}/Settings/GNOME

gzip -9nf README NEWS FAQ TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/sawfish
%attr(755,root,root) %{_bindir}/sawfish-client
%attr(755,root,root) %{_bindir}/sawfish-ui
%{_datadir}/sawfish

%{_pixmapsdir}/*

%dir %{_libexecdir}/sawfish
%dir %{_libexecdir}/sawfish/%{_host}
%attr(755,root,root) %{_libexecdir}/sawfish/%{_host}/*.so
%attr(755,root,root) %{_libexecdir}/sawfish/%{_host}/*.la
%attr(755,root,root) %{_libexecdir}/sawfish/%{_host}/gtk-style
%attr(755,root,root) %{_libexecdir}/sawfish/%{_host}/sawfish-menu
%attr(755,root,root) %{_libexecdir}/sawfish/%{_host}/sawfish-about
%dir %{_libexecdir}/sawfish/%{_host}/sawfish
%dir %{_libexecdir}/sawfish/%{_host}/sawfish/wm
%dir %{_libexecdir}/sawfish/%{_host}/sawfish/wm/util
%attr(755,root,root) %{_libexecdir}/sawfish/%{_host}/sawfish/wm/util/*.so
%attr(755,root,root) %{_libexecdir}/sawfish/%{_host}/sawfish/wm/util/*.la
%{_libexecdir}/sawfish/%{_host}/DOC

%dir /usr/libexec/rep/%{_host}/sawfish
%attr(755,root,root) /usr/libexec/rep/%{_host}/sawfish/*.so
%attr(755,root,root) /usr/libexec/rep/%{_host}/sawfish/*.la

%{_infodir}/sawfish*

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawfish-capplet
%{_datadir}/control-center/Sawfish
%{_datadir}/gnome/wm-properties/Sawfish.desktop

%files themer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawfish-themer
%{_datadir}/sawfish/themer.glade
