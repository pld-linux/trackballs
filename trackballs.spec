#
# TODO:
#   -fix problems with GLU in the other way than "ln -s /usr/{X11R6,}/lib/GLU.so"
#
Summary:	Game similar to Marble Madness
Summary(pl):	Gra podobna do Marble Madness
Name:		trackballs
Version:	1.0.0
Release:	0.9
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0d3ce4903aa60fba18c0e8c02b3cd563
Source1:	http://dl.sourceforge.net/%{name}/tb_design.ogg
Source2:	http://dl.sourceforge.net/%{name}/tb_genesis.ogg
Source3:	%{name}.desktop
URL:		http://trackballs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	guile-devel >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	%{_prefix}/games
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
Requires:	%{name}

%description music
Background music for trackballs.

%description music -l pl
Muzyka w tle dla trackballs.

%prep
%setup -q
#%%patch0 -p1

%build
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
LDFLAGS="-I/usr/include/GL"
%configure \
	--with-highscores=/var/games/trackballs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/music
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/music

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games
install share/icons/trackballs-64x64.png $RPM_BUILD_ROOT%{_pixmapsdir}/trackballs.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
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

%{_applnkdir}/Games/*
%{_pixmapsdir}/*

%files music
%defattr(644,root,root,755)
%{_datadir}/%{name}/music/*
