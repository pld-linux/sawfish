Summary:	A highly configurable and extensible X11 window manager
Name:		sawfish
Version:	0.30.3
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://download.sourceforge.net/pub/sourceforge/sawmill/%{name}-%{version}.tar.gz
Patch0:		sawfish-info.patch
Patch1:		sawfish-xinerama.patch
Patch2:		sawfish-no_version.patch
URL:		http://sawmill.sourceforge.net
BuildRequires:	esound-devel
BuildRequires:	control-center-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librep-devel >= 0.12
BuildRequires:	librep-jl >= 0.12
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rep-gtk >= 0.13
Requires:	/usr/sbin/fix-info-dir
Obsoletes:	sawmill
Obsoletes:	sawmill-gnome
Obsoletes:	sawmill-themer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_infodir	/usr/share/info

%description
This is an extensible window manager using a LISP-based scripting
language--all window decorations are configurable, the basic idea is
to have as much user-interface policy as possible controlled through
the Lisp language. All configuration may be performed through a GTK
interface; sawmill is mostly-GNOME compliant.

%package gnome
Summary:	GNOME support for sawmill
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}

%description gnome
Optional GNOME support for sawmill. Includes a wm-entries spec, and a
control center applet.

%package themer
Summary:	GUI for creating sawmill themes
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}

%description themer
Optional theme builder for sawmill. Allows static window themes to be
created/edited in a graphical environment.

%prep
%setup -q
%patch0 -p1
%patch2 -p1

%build
gettextize --copy --force
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-static \
	--enable-capplet \
	--with-readline \
	--with-esd \
	--with-audiofile \
	--without-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	G_MENU_DIR=%{_applnkdir}/Settings

strip --strip-unneeded $RPM_BUILD_ROOT%{_libexecdir}/sawfish/*.so

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/sawfish* \
	README NEWS FAQ TODO

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
%dir %{_libexecdir}/sawfish
%{_libexecdir}/sawfish/DOC
%attr(755,root,root) %{_libexecdir}/sawfish/*.so
%attr(755,root,root) %{_libexecdir}/sawfish/*.la
%attr(755,root,root) %{_libexecdir}/sawfish/gtk-style
%attr(755,root,root) %{_libexecdir}/sawfish/sawfish-menu
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
