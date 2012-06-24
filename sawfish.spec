Summary:	A highly configurable and extensible X11 window manager
Summary(es):	Un administrador de ventanas que se puede configurar y extender para X11
Summary(pl):	Zarz�dca okien dla X11 o du�ych mo�liwo�ciach konfiguracyjnych i skalowalno�ci
Summary(pt_BR):	Um gerenciador de janelas configur�vel e extens�vel para o X11
Summary(ru):	������� �������� ��� X Window
Summary(uk):	�������� �������� ��� X Window
Summary(zh_CN):	���к�ǿ����չ�ԺͿ������Ե�ͼ�δ��ڹ�����
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
Zarz�dca okien o du�ych mo�liwo�ciach rozszerzania, u�ywaj�cy
bazowanego na LISP-ie j�zyka skryptowego, dzi�ki czemu wszystkie
dodatki do okien s� konfigurowalne. Og�ln� ide� jest, aby da� jak
najwi�ksz� kontrol� w r�ce u�ytkownika poprzez graficzny interfejs
dzi�ki w�a�nie LISP-owi. Sawfish jest najbardziej zgodny z GNOME-m.

%description -l pt_BR
O Sawfish � um gerenciador de janelas extens�vel que usa uma linguagem
de script baseada em Lisp. Todas as decora��es de janelas s�o
configur�veis e a id�ia b�sica e ter a maior parte poss�vel das
pol�ticas de interface de usu�rio controlada pela linguagem Lisp. A
configura��o pode ser efetuada escrevendo-se c�digo Lisp em um arquivo
.sawfishrc pessoal. O Sawfish prov� suporte completo para o GNOME.

%description -l ru
Sawfish - ��� ����������� ������� ��������, ������������ ���������� ��
Lisp ���� ���������. ��� ������� ��������� ����� ���������������,
������� ���� ������� � ���, ����� �������������� ����� Lisp
����������� ��������� ����� ��������� ���������� ������������.
���������������� ����� ���� ��������� ���������� Lisp ���� �
������������ ����� .sawfishrc, ��� ����� GTK+ ���������. Sawfish �
�������� ��������� � GNOME; ���� ������ ������������ ��� � GNOME,
���������� ����� ���������� ����� sawfish-gnome.

%description -l uk
Sawfish - �� ������������ צ������ ��������, �� ����������դ ��������
�� Lisp ���� �����Ҧ��. �Ӧ צ���Φ ������æ� ����� ���Ʀ��������,
������ ���� ������� � ����, ��� ������������ ����� Lisp �����������
�������� ��'�� ����Ħ��� ���������� �����������. ���Ʀ��������� ����
���� �������� ���������� Lisp ���� � ������������� ���̦ .sawfishrc,
��� ����� GTK+ ���������. Sawfish ���¦������ ��ͦ���� � GNOME; ����
������ ��������������� ���� � GNOME, ���Ҧ��� ����� ���������� �����
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
control-center oraz specyfikacj� wm-entries.

%description gnome -l ru
����� sawfish-gnome �������� ��������� ����� GNOME ��� ��������
��������� sawfish (������� ������ ��� ������ ���������� GNOME). ����
�� ������ ������������ sawfish ������ � GNOME, ��� ����������
���������� ���� �����.

%description gnome -l uk
����� sawfish-gnome ������� Ц������� ���������� GNOME ��� צ�������
��������� sawfish (��������� ����� ��� ������ ��������� GNOME). ����
�� ������ ��������������� sawfish � GNOME, ��� ���Ҧ��� ���������� ���
�����.

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
