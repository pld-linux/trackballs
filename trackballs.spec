#
Summary:	Game similar to Marble Madness
Summary(pl):	Gra podobna do Marble Madness
Name:		trackballs
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	36385b18f6062652b656d08d18e38b24
Source1:	http://dl.sf.net/%{name}/tb_design.ogg
Source2:	http://dl.sf.net/%{name}/tb_genesis.ogg
Source3:	%{name}.desktop
Patch0:		%{name}-chown.patch
URL:		http://trackballs.sourceforge.net/
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
Trackballs jest prost� gr� podobn� do klasycznej Marble Madness
napisanej na Amig� w latach 80-ych. Gracz zdobywa punkty steruj�c
marmurow� kulk� w labiryncie wype�nionym okrutnymi m�otami, ka�u�ami
kwasu i innymi przeszkodami. Gdy kilka osi�gnie cel, przenosi si� do
nast�pnego, trudniejszego, toru. Chyba �e sko�czy si� czas.

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
%patch0 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
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
