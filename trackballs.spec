#	TODO:
# - subpackage with music
# - desktop file, icon
# - proper score file
#
Summary:	Game similar to Marble Madness
Summary(pl):	Gra podobna do Marble Madness
Name:		trackballs
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
Source1:	http://dl.sf.net/%{name}/tb_design.ogg
Source2:	http://dl.sf.net/%{name}/tb_genesis.ogg
Patch0:		%{name}-chown.patch
BuildRequires:	guile-devel >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/music
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/music

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README README.html TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
