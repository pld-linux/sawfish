Summary:	A highly configurable and extensible X11 window manager
Name:		sawfish
Version:	0.27.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Source:		ftp://sawmill.sourceforge.net/pub/sawmill/%{name}-%{version}.tar.gz
Patch0:		sawfish-info.patch
Patch1:		ftp://ftp.dcs.warwick.ac.uk/people/John.Harper/sawfish/patches/sawmill-gdk-pixbuf-diffs
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
Obsoletes:	sawmill
Obsoletes:	sawmill-gnome
Obsoletes:	sawmill-themer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_infodir	/usr/share/info

%description
This is an extensible window manager using a LISP-based scripting
language--all window decorations are configurable, the basic idea is to
have as much user-interface policy as possible controlled through the Lisp
language. All configuration may be performed through a GTK interface;
sawmill is mostly-GNOME compliant.

%package gnome
Summary:	GNOME support for sawmill
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}

%description gnome
Optional GNOME support for sawmill. Includes a wm-entries spec, and a
control center applet.

%package themer
Summary:	GUI for creating sawmill themes
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Requires:	%{name} = %{version}

%description themer
Optional theme builder for sawmill. Allows static window themes to be
created/edited in a graphical environment.

%prep
%setup -q
%patch0 -p1
# %patch1 

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

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/sawmill* \
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
%attr(755,root,root) %{_bindir}/sawmill
%attr(755,root,root) %{_bindir}/sawmill-client
%attr(755,root,root) %{_bindir}/sawmill-ui
%{_datadir}/sawmill
%dir %{_libexecdir}/sawmill
%dir %{_libexecdir}/sawmill/%{version}
%{_libexecdir}/sawmill/%{version}/%{_host}
%{_infodir}/sawmill*

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawmill-capplet
%{_datadir}/control-center/Sawmill
%{_datadir}/gnome/wm-properties/Sawmill.desktop

%files themer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sawmill-themer
%{_datadir}/sawmill/%{version}/themer.glade
