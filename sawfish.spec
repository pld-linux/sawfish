Summary:	A highly configurable and extensible X11 window manager
Summary(pl.UTF-8):   Window Manadżer dla X11 o dużych możliwościach konfiguracyjnych i skalowalności
Name:		sawfish
Version:	2.0
Release:	2
Epoch:		2
License:	GPL
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/gnome/sources/sawfish/2.0/%{name}-%{version}.tar.bz2
Patch0:		%{name}-applnk.patch
URL:		http://sawmill.sourceforge.net/
Icon:		sawfish.xpm
BuildRequires:	autoconf		
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.27
BuildRequires:	gettext-devel
BuildRequires:	librep-devel >= 0.16
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rep-gtk >= 0.16
BuildRequires:	rep-gtk-gnome >= 0.16
BuildRequires:	rep-gtk-libglade >= 0.16
BuildRequires:	texinfo
%define		repexecdir	%(rep-config --execdir || echo "Install_librep-devel_and_rebuild_this_package")
Requires:	rep-gtk >= 0.16
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

%description -l pl.UTF-8
Window manadżer o dużych możliwościach rozszerzania, używający
bazowanego na LISP-ie języka skryptowego, dzięki czemu wszystkie
dodatki do okien są configurowalne. Ogólną ideą jest, aby dać jak
największą kontrolę w ręce użytkownika poprzez graficzny interfejs
dzięki właśnie LISP-owi. Sawmill jest najbardziej zgodny z GNOME-m.

%package gnome
Summary:	GNOME support for sawmill
Summary(pl.UTF-8):   Support GNOME'a dla sawmilla
Group:		X11/Window Managers
Requires:	%{name} = %{version}
Requires:	rep-gtk-gnome >= 0.14-3
Requires:	rep-gtk-libglade >= 0.14-3

%description gnome
Optional GNOME support for sawmill. Includes a wm-entries spec, and a
control center applet.

%description gnome -l pl.UTF-8
Opcjonalny support GNOME'a dla sawmilla. Zawiera aplet dla
control-center oraz wm-entries spec.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake} || :
%configure \
	--disable-static \
	--enable-capplet \
	--enable-themer \
	--enable-gnome-widgets \
	--with-readline \
	--with-esd \
	--with-audiofile \
	--with-gnu-ld
%{__make} host_type=%{_host}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_wmpropsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	G_MENU_DIR=%{_applnkdir}/Settings/GNOME \
	host_type=%{_host}

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sawfish
%{_pixmapsdir}/*

%dir %{_libexecdir}/sawfish
%dir %{_libexecdir}/sawfish/%{version}
%dir %{_libexecdir}/sawfish/%{version}/%{_host}
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/*.so
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/*.la
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/gtk-style
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish-menu
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish-about
%dir %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish
%dir %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm
%dir %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm/util
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm/util/*.so
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm/util/*.la
%{_libexecdir}/sawfish/%{version}/%{_host}/DOC

%dir %{repexecdir}/sawfish
%attr(755,root,root) %{repexecdir}/sawfish/*.so
%attr(755,root,root) %{repexecdir}/sawfish/*.la
%{_infodir}/sawfish*

%files gnome
%defattr(644,root,root,755)
%{_datadir}/control-center-2.0/capplets/*
%{_wmpropsdir}/Sawfish.desktop
