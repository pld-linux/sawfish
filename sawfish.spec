Summary:	A highly configurable and extensible X11 window manager
Summary(pl):	Window Manad¿er dla X11 o du¿ych mo¿liwo¶ciach konfiguracyjnych i skalowalno¶ci
Name:		sawfish
Version:	1.0.1
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	http://prdownloads.sourceforge.net/sawmill/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_version.patch
Patch2:		%{name}-no_libnsl.spec
Patch3:		%{name}-make.patch
Patch4:         %{name}-windowmenu.patch
Patch5:		%{name}-nautilus.patch
URL:		http://sawmill.sourceforge.net/
Icon:		sawfish.xpm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	control-center-devel
BuildRequires:	gettext-devel
BuildRequires:	librep-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	librep-devel >= 0.14
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rep-gtk >= 0.14-3
BuildRequires:	rep-gtk-gnome >= 0.14-3
BuildRequires:	rep-gtk-libglade >= 0.14-3
BuildRequires:	texinfo
%define		repexecdir	%(rep-config --execdir)
Requires:	rep-gtk >= 0.14-3
Requires:	%{repexecdir}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	sawmill
Obsoletes:	sawmill-gnome
Obsoletes:	sawmill-themer

%define		_prefix		/usr/X11R6
%define		_libexecdir	%{_libdir}
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
This is an extensible window manager using a LISP-based scripting
language--all window decorations are configurable, the basic idea is
to have as much user-interface policy as possible controlled through
the Lisp language. All configuration may be performed through a GTK
interface; sawmill is mostly-GNOME compliant.

%description -l pl
Window manad¿er o du¿ych mo¿liwo¶ciach rozszerzania, u¿ywaj±cy
bazowanego na LISP'ie jêzyka skryptowego, dziêki czemu wszystkie
dodatki do okien s± configurowalne. Ogóln± ide± jest, aby daæ jak
najwiêksz± kontrolê w rêce u¿ytkownika poprzez graficzny interfejs
dziêki w³a¶nie LISP'owi.
Sawmill jest najbardziej zgodny z GNOME'em.

%package gnome
Summary:	GNOME support for sawmill
Summary(pl):	Support GNOME'a dla sawmill'a
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
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
Summary(pl):	GUI do tworzenia tematów dla sawmill'a
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}

%description themer
Optional theme builder for sawmill. Allows static window themes to be
created/edited in a graphical environment.

%description -l pl themer
Opcjonalna aplikacja do tworzenia tematów dla sawfish'a. Pozwala na 
tworzenie/modyfikacjê statycznych tematów w ¶rodowisku graficznym.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 
%patch5 -p1

%build
gettextize --copy --force
libtoolize --copy --force
aclocal
autoconf
automake -a -c || :
%configure \
	--disable-static \
	--enable-capplet \
	--enable-themer \
	--enable-gnome-widgets \
	--with-readline \
	--with-esd \
	--with-audiofile \
	--with-gnu-ld
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_wmpropsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	G_MENU_DIR=%{_applnkdir}/Settings/GNOME

install Sawfish.desktop $RPM_BUILD_ROOT%{_wmpropsdir}

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

%dir %{repexecdir}/sawfish
%attr(755,root,root) %{repexecdir}/sawfish/*.so
%attr(755,root,root) %{repexecdir}/sawfish/*.la

%{_infodir}/sawfish*

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawfish-capplet
%{_datadir}/control-center/Sawfish
%{_wmpropsdir}/Sawfish.desktop

%files themer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawfish-themer
%{_datadir}/sawfish/themer.glade
