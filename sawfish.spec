Summary:	A highly configurable and extensible X11 window manager
Name:		sawfish
Version:	0.27.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://sawmill.sourceforge.net/pub/sawmill/%{name}-%{version}.tar.gz
Patch0:		sawfish-info.patch
Patch1:		ftp://ftp.dcs.warwick.ac.uk/people/John.Harper/sawfish/patches/sawmill-gdk-pixbuf-diffs
Patch2:		sawfish-xinerama.patch
URL:		http://sawmill.sourceforge.net
BuildRequires:	control-center-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librep-devel >= 0.11
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gettext-devel
BuildRequires:	audiofile-devel
BuildRequires:	esound-devel
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
# %patch1 
%patch2 

%build
gettextize --copy --force
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-capplet \
	--with-readline \
	--with-esd \
	--with-audiofile \
	--without-static
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{gnome/wm-properties,control-center}

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/sawfish* \
	README NEWS FAQ TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/sawfish
%attr(755,root,root) %{_bindir}/sawfish-client
%attr(755,root,root) %{_bindir}/sawfish-ui
%{_datadir}/sawfish
%dir %{_libexecdir}/sawfish
%dir %{_libexecdir}/sawfish/%{version}
%{_libexecdir}/sawfish/%{version}/%{_host}
%{_infodir}/sawfish*

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawfish-capplet
%{_datadir}/control-center/Sawfish
%{_datadir}/gnome/wm-properties/Sawfish.desktop

%files themer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawfish-themer
%{_datadir}/sawfish/%{version}/themer.glade
