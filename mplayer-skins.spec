%define base_name	mplayer
%define name		%{base_name}-skins
%define summary		Skins for %{base_name}
%define version		1.3
%define release		%mkrel 15
%define skin_dir	%{_datadir}/%{base_name}/skins

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
Source0:	BlueHeart-1.5.tar.bz2
Source2:	Cyrus-1.2.tar.bz2
Source3:	standard-1.9.tar.bz2
Source4:	neutron-1.5.tar.bz2
Source5:	MidnightLove-1.6.tar.bz2
Source6:	plastic-1.2.tar.bz2
Source7:	Orange-1.3.tar.bz2
Source8:	Blue-small-1.4.tar.bz2
Source9:	xine-lcd-1.2.tar.bz2
Source10:	phony-1.1.tar.bz2
Source11:	mentalic-1.2.tar.bz2
Source12:	proton-1.2.tar.bz2
Source13:	slim-1.2.tar.bz2
Source14:	krystal-1.1.tar.bz2
Source15:	CubicPlayer-1.1.tar.bz2
Source16:	AlienMind-1.2.tar.bz2
Source17:	CornerMP-1.2.tar.bz2
Source18:	CornerMP-aqua-1.4.tar.bz2
URL:		http://www.mplayerhq.hu
License:	Freely redistributable without restriction
Group:		Video
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This package includes following skins:
- standard by FRD (Viktor Bekesi), the old default MPlayer skin 
- Midnight Love, by Gabucino, MPlayer conversion of the nice WinAMP/XMMS skin 
  of Rei Ayanami. 
- BlueHeart, by Gabucino, MPlayer conversion of a BlueHeart XMMS skin. 
- Neutron, by aleczapka (Oliwier Ptak), VERY nice skin! 
- Plastic, by FRD (Viktor Bekesi), remote control-like skin with plastic 
  feeling 
- Cyrus, by Roberto J., Cyrus skin from XMMS 
- Xine-LCD, by Gabucino, MPlayer conversion of Xine's LCD skin
- Phony
- Mentalic, by aleczapka (Oliwier Ptak) 
- Proton, by Pasquale Riccio, silver, shiny
- Slim, by FRD (Viktor Bekesi), small and cute
- Cubic Player, by Gabucino, for other oldtimers
- Alien Mind, by Gabucino, Alien Mind skin from XMMS
- CornerMP, by DC.Park, a WinAMP skin conversion, resides in desktop
  corner
- CornerMP-aqua, by DC.Park, a WinAMP skin conversion, resides in
  desktop corner
- Blue and Blue-small by Franciszek Wilamowski
- Orange by Ognian Vasilev
- krystal by Gary Whitmore, Jr.

%prep
%setup -q -c
%setup -q -c -T -D -a2
%setup -q -c -T -D -a3
%setup -q -c -T -D -a4
%setup -q -c -T -D -a5
%setup -q -c -T -D -a6
%setup -q -c -T -D -a7
%setup -q -c -T -D -a8
%setup -q -c -T -D -a9
%setup -q -c -T -D -a10
%setup -q -c -T -D -a11
%setup -q -c -T -D -a12
%setup -q -c -T -D -a13
%setup -q -c -T -D -a14
%setup -q -c -T -D -a15
%setup -q -c -T -D -a16
%setup -q -c -T -D -a17
%setup -q -c -T -D -a18
# correct perm problems
chmod -R go=u-w *

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 ${RPM_BUILD_ROOT}%{skin_dir}
cp -r * ${RPM_BUILD_ROOT}%{skin_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{skin_dir}/*

