Summary:	A highly configurable and extensible X11 window manager
Summary(es.UTF-8):	Un administrador de ventanas que se puede configurar y extender para X11
Summary(pl.UTF-8):	Zarządca okien dla X11 o dużych możliwościach konfiguracyjnych i skalowalności
Summary(pt_BR.UTF-8):	Um gerenciador de janelas configurável e extensível para o X11
Summary(ru.UTF-8):	Оконный менеджер для X Window
Summary(uk.UTF-8):	Віконний менеджер для X Window
Summary(zh_CN.UTF-8):	具有很强的扩展性和可配置性的图形窗口管理器
Name:		sawfish
Version:	1.3.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Window Managers
#Source0:	http://ftp.gnome.org/pub/gnome/sources/sawfish/2.0/%{name}-%{version}.tar.bz2
Source0:	http://dl.sourceforge.net/sawmill/%{name}-%{version}.tar.gz
# Source0-md5:	2ebed60d4fcae075f1f171972c40660a
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-applnk.patch
%define		repexecdir	%(rep-config --execdir || echo "Install_librep-devel_and_rebuild_this_package")
URL:		http://sawfish.wikia.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 1:0.2.27
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	librep-devel >= 0.16
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	rep-gtk >= 0.17
BuildRequires:	rep-gtk-gnome >= 0.17
BuildRequires:	rep-gtk-libglade >= 0.17
BuildRequires:	texinfo
BuildRequires:	xorg-proto-xextproto-devel
Requires:	%{repexecdir}
Requires:	rep-gtk >= 0.17
Requires:	rep-gtk-gnome >= 0.17
Provides:	gnome-wm
Obsoletes:	sawmill
Obsoletes:	sawmill-gnome
Obsoletes:	sawmill-themer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}
%define		_wmpropsdir	/usr/share/wm-properties

%description
This is an extensible window manager using a LISP-based scripting
language--all window decorations are configurable, the basic idea is
to have as much user-interface policy as possible controlled through
the Lisp language. All configuration may be performed through a GTK
interface; sawfish is mostly-GNOME compliant.

%description -l pl.UTF-8
Zarządca okien o dużych możliwościach rozszerzania, używający
bazowanego na LISP-ie języka skryptowego, dzięki czemu wszystkie
dodatki do okien są konfigurowalne. Ogólną ideą jest, aby dać jak
największą kontrolę w ręce użytkownika poprzez graficzny interfejs
dzięki właśnie LISP-owi. Sawfish jest najbardziej zgodny z GNOME-m.

%description -l pt_BR.UTF-8
O Sawfish é um gerenciador de janelas extensível que usa uma linguagem
de script baseada em Lisp. Todas as decorações de janelas são
configuráveis e a idéia básica e ter a maior parte possível das
políticas de interface de usuário controlada pela linguagem Lisp. A
configuração pode ser efetuada escrevendo-se código Lisp em um arquivo
.sawfishrc pessoal. O Sawfish provê suporte completo para o GNOME.

%description -l ru.UTF-8
Sawfish - это расширяемый оконный менеджер, использующий основанный на
Lisp язык сценариев. Все оконные декорации можно конфигурировать,
базовая идея состоит в том, чтобы контролировать через Lisp
максимально возможный объем поведения интерфейса пользователя.
Конфигурирование может быть исполнено написанием Lisp кода в
персональном файле .sawfishrc, или через GTK+ интерфейс. Sawfish в
основном совместим с GNOME; если хотите использовать его с GNOME,
необходимо также установить пакет sawfish-gnome.

%description -l uk.UTF-8
Sawfish - це розширюваний віконний менеджер, що використовує базовану
на Lisp мову сценаріїв. Всі віконні декорації можна конфігурувати,
базова ідея полягає в тому, щоб контролювати через Lisp максимально
можливий об'єм поведінки інтерфейса користувача. Конфігурування може
бути виконане написанням Lisp коду в персональному файлі .sawfishrc,
або через GTK+ інтерфейс. Sawfish здебільшого сумісний з GNOME; якщо
хочете використовувати його з GNOME, потрібно також встановити пакет
sawfish-gnome.

%package gnome
Summary:	GNOME support for sawmill
Summary(pl.UTF-8):	Support GNOME'a dla sawmilla
Group:		X11/Window Managers
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	rep-gtk-libglade >= 0.17

%description gnome
Optional GNOME support for sawmill. Includes a wm-entries spec, and a
control center applet.

%description gnome -l pl.UTF-8
Opcjonalne wsparcie GNOME'a dla sawmilla. Zawiera aplet dla
control-center oraz specyfikację wm-entries.

%description gnome -l ru.UTF-8
Пакет sawfish-gnome включает поддержку среды GNOME для оконного
менеджера sawfish (включая апплет для центра управления GNOME). Если
вы хотите использовать sawfish вместе с GNOME, вам необходимо
установить этот пакет.

%description gnome -l uk.UTF-8
Пакет sawfish-gnome включає підтримку середовища GNOME для віконного
менеджера sawfish (включаючи аплет для центру керування GNOME). Якщо
ви хочете використовувати sawfish з GNOME, вам потрібно встановити цей
пакет.

%prep
%setup -q
%patch0 -p1

mv -f po/{no,nb}.po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake} || :
%configure \
	--disable-static \
	--enable-themer \
	--enable-gnome-widgets \
	--with-readline \
	--with-esd \
	--with-audiofile \
	--with-gnu-ld
%{__make} \
	host_type=%{_host}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	G_MENU_DIR=%{_applnkdir}/Settings/GNOME \
	host_type=%{_host}

install Sawfish.desktop $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

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
%{_datadir}/xsessions/%{name}.desktop
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
%{_wmpropsdir}/Sawfish.desktop
