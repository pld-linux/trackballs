Summary:	Game similar to Marble Madness
Summary(pl):	Gra podobna do Marble Madness
Name:		trackballs
Version:	1.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4d1c4be3274ac88038bc03e2d470546c
Source1:	http://dl.sourceforge.net/%{name}/tb_design.ogg
# Source1-md5:	5623321cd954471c9fe16c02b7f166ca
Source2:	http://dl.sourceforge.net/%{name}/tb_genesis.ogg
# Source2-md5:	3f00e13798d5bdce40ec2807f3ea1889
Source3:	http://dl.sourceforge.net/%{name}/tb_hrluebke.ogg
# Source3-md5:	ab033eac91054ed9700f6e0a8e2f1280
Source4:	http://dl.sourceforge.net/%{name}/tb_plinkeplanke.ogg
# Source4-md5:	5a968fb86cc43fa08bbe323b63d0a457
Source5:	%{name}.desktop
Patch0:		%{name}-install.patch
URL:		http://trackballs.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	guile-devel >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Trackballs is a simple game similar to the classical game Marble
Madness on the Amiga in the 80's. By steering a marble ball through a
labyrinth filled with vicious hammers, pools of acid and other
obstacles the player collects points. When the ball reaches the
destination it continues to the next, more difficult track - unless
the time runs out.

%description -l pl
Trackballs jest prost± gr± podobn± do klasycznej Marble Madness
napisanej na Amigê w latach 80-ych. Gracz zdobywa punkty steruj±c
marmurow± kulk± w labiryncie wype³nionym okrutnymi m³otami, ka³u¿ami
kwasu i innymi przeszkodami. Gdy kilka osi±gnie cel, przenosi siê do
nastêpnego, trudniejszego, toru. Chyba ¿e skoñczy siê czas.

%package music
Summary:	Background music for trackballs
Summary(pl):	Muzyka w tle dla trackballs
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description music
Background music for trackballs.

%description music -l pl
Muzyka w tle dla trackballs.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} -pi -e "s,dnl LIBS=\"-lGLU,LIBS=\"-lGLU,g" configure.ac
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--with-highscores=/var/games/trackballs \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/%{_lib}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/music
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/music
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/music
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/%{name}/music

install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install share/icons/trackballs-64x64.png $RPM_BUILD_ROOT%{_pixmapsdir}/trackballs.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README README.html TODO
%attr(2755,root,games) %{_bindir}/trackballs
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/music
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_datadir}/%{name}/levels
%{_datadir}/%{name}/sfx
%{_mandir}/man6/*
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) /var/games/trackballs

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files music
%defattr(644,root,root,755)
%{_datadir}/%{name}/music/*
