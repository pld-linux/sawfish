Summary:	A highly configurable and extensible X11 window manager
Summary(es):	Un administrador de ventanas que se puede configurar y extender para X11
Summary(pl):	Zarz╠dca okien dla X11 o du©ych mo©liwo╤ciach konfiguracyjnych i skalowalno╤ci
Summary(pt_BR):	Um gerenciador de janelas configurАvel e extensМvel para o X11
Summary(ru):	Оконный менеджер для X Window
Summary(uk):	В╕конний менеджер для X Window
Summary(zh_CN):	╬ъсп╨эг©╣дю╘у╧пт╨м©иеДжцпт╣дм╪пн╢╟©з╧эюМфВ
Name:		sawfish
Version:	1.2
Release:	1
Epoch:		3
License:	GPL
Group:		X11/Window Managers
#Source0:	http://ftp.gnome.org/pub/gnome/sources/sawfish/2.0/%{name}-%{version}.tar.bz2
Source0:	http://unc.dl.sourceforge.net/sourceforge/sawmill/%{name}-%{version}-gtk2.tar.gz
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
BuildRequires:	rep-gtk >= 0.17
BuildRequires:	rep-gtk-gnome >= 0.17
BuildRequires:	rep-gtk-libglade >= 0.17
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
interface; sawfish is mostly-GNOME compliant.

%description -l pl
Zarz╠dca okien o du©ych mo©liwo╤ciach rozszerzania, u©ywaj╠cy
bazowanego na LISP-ie jЙzyka skryptowego, dziЙki czemu wszystkie
dodatki do okien s╠ konfigurowalne. OgСln╠ ide╠ jest, aby daФ jak
najwiЙksz╠ kontrolЙ w rЙce u©ytkownika poprzez graficzny interfejs
dziЙki wЁa╤nie LISP-owi. Sawfish jest najbardziej zgodny z GNOME-m.

%description -l pt_BR
O Sawfish И um gerenciador de janelas extensМvel que usa uma linguagem
de script baseada em Lisp. Todas as decoraГУes de janelas sЦo
configurАveis e a idИia bАsica e ter a maior parte possМvel das
polМticas de interface de usuАrio controlada pela linguagem Lisp. A
configuraГЦo pode ser efetuada escrevendo-se cСdigo Lisp em um arquivo
.sawfishrc pessoal. O Sawfish provЙ suporte completo para o GNOME.

%description -l ru
Sawfish - это расширяемый оконный менеджер, использующий основанный на
Lisp язык сценариев. Все оконные декорации можно конфигурировать,
базовая идея состоит в том, чтобы контролировать через Lisp
максимально возможный объем поведения интерфейса пользователя.
Конфигурирование может быть исполнено написанием Lisp кода в
персональном файле .sawfishrc, или через GTK+ интерфейс. Sawfish в
основном совместим с GNOME; если хотите использовать его с GNOME,
необходимо также установить пакет sawfish-gnome.

%description -l uk
Sawfish - це розширюваний в╕конний менеджер, що використову╓ базовану
на Lisp мову сценар╕╖в. Вс╕ в╕конн╕ декорац╕╖ можна конф╕гурувати,
базова ╕дея поляга╓ в тому, щоб контролювати через Lisp максимально
можливий об'╓м повед╕нки ╕нтерфейса користувача. Конф╕гурування може
бути виконане написанням Lisp коду в персональному файл╕ .sawfishrc,
або через GTK+ ╕нтерфейс. Sawfish здеб╕льшого сум╕сний з GNOME; якщо
хочете використовувати його з GNOME, потр╕бно також встановити пакет
sawfish-gnome.

%package gnome
Summary:	GNOME support for sawmill
Summary(pl):	Support GNOME'a dla sawmilla
Group:		X11/Window Managers
Requires:	%{name} = %{version}
Requires:	rep-gtk-gnome >= 0.14-3
Requires:	rep-gtk-libglade >= 0.14-3

%description gnome
Optional GNOME support for sawmill. Includes a wm-entries spec, and a
control center applet.

%description gnome -l pl
Opcjonalne wsparcie GNOME'a dla sawmilla. Zawiera aplet dla
control-center oraz specyfikacjЙ wm-entries.

%description gnome -l ru
Пакет sawfish-gnome включает поддержку среды GNOME для оконного
менеджера sawfish (включая апплет для центра управления GNOME). Если
вы хотите использовать sawfish вместе с GNOME, вам необходимо
установить этот пакет.

%description gnome -l uk
Пакет sawfish-gnome включа╓ п╕дтримку середовища GNOME для в╕конного
менеджера sawfish (включаючи аплет для центру керування GNOME). Якщо
ви хочете використовувати sawfish з GNOME, вам потр╕бно встановити цей
пакет.

%prep
%setup -q -n %{name}-%{version}-gtk2
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS FAQ TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sawfish
%{_pixmapsdir}/*

%dir %{_libexecdir}/sawfish
%dir %{_libexecdir}/sawfish/%{version}
%dir %{_libexecdir}/sawfish/%{version}/%{_host}
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/*.so
%{_libexecdir}/sawfish/%{version}/%{_host}/*.la
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/gtk-style
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish-menu
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish-about
%dir %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish
%dir %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm
%dir %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm/util
%attr(755,root,root) %{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm/util/*.so
%{_libexecdir}/sawfish/%{version}/%{_host}/sawfish/wm/util/*.la
%{_libexecdir}/sawfish/%{version}/%{_host}/DOC

%dir %{repexecdir}/sawfish
%attr(755,root,root) %{repexecdir}/sawfish/*.so
%{repexecdir}/sawfish/*.la
%{_infodir}/sawfish*

%files gnome
%defattr(644,root,root,755)
%{_datadir}/control-center-2.0/capplets/*
%{_wmpropsdir}/Sawfish.desktop
