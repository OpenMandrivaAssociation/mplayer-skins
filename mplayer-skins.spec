%define base_name	mplayer
%define name		%{base_name}-skins
%define summary		Skins for %{base_name}
%define version		1.4
%define release		%mkrel 18
%define skin_dir	%{_datadir}/%{base_name}/skins

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
Source0:	http://mplayerhq.hu/MPlayer/skins/BlueHeart-1.5.tar.bz2
Source2:	http://mplayerhq.hu/MPlayer/skins/Cyrus-1.2.tar.bz2
Source3:	http://mplayerhq.hu/MPlayer/skins/standard-1.9.tar.bz2
Source4:	http://mplayerhq.hu/MPlayer/skins/neutron-1.5.tar.bz2
Source5:	http://mplayerhq.hu/MPlayer/skins/MidnightLove-1.6.tar.bz2
Source6:	http://mplayerhq.hu/MPlayer/skins/plastic-1.2.tar.bz2
Source7:	http://mplayerhq.hu/MPlayer/skins/Orange-1.3.tar.bz2
Source8:	http://mplayerhq.hu/MPlayer/skins/Blue-small-1.5.tar.bz2
Source9:	http://mplayerhq.hu/MPlayer/skins/xine-lcd-1.2.tar.bz2
Source10:	http://mplayerhq.hu/MPlayer/skins/phony-1.1.tar.bz2
Source11:	http://mplayerhq.hu/MPlayer/skins/mentalic-1.2.tar.bz2
Source12:	http://mplayerhq.hu/MPlayer/skins/proton-1.2.tar.bz2
Source13:	http://mplayerhq.hu/MPlayer/skins/slim-1.2.tar.bz2
Source14:	http://mplayerhq.hu/MPlayer/skins/krystal-1.1.tar.bz2
Source15:	http://mplayerhq.hu/MPlayer/skins/CubicPlayer-1.1.tar.bz2
Source16:	http://mplayerhq.hu/MPlayer/skins/AlienMind-1.2.tar.bz2
Source17:	http://mplayerhq.hu/MPlayer/skins/CornerMP-1.2.tar.bz2
Source18:	http://mplayerhq.hu/MPlayer/skins/CornerMP-aqua-1.4.tar.bz2
URL:		http://mplayerhq.hu/
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
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{skin_dir}
cp -r * %{buildroot}%{skin_dir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{skin_dir}/*



%changelog
* Tue May 08 2012 GÃ¶tz Waschk <waschk@mandriva.org> 1.4-18mdv2012.0
+ Revision: 797439
- update Bllue-small to version 1.5
- add source URLs

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3-18
+ Revision: 666493
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-17mdv2011.0
+ Revision: 606664
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-16mdv2010.1
+ Revision: 523386
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3-15mdv2010.0
+ Revision: 426195
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.3-14mdv2009.0
+ Revision: 223322
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.3-13mdv2008.1
+ Revision: 153263
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 30 2007 Adam Williamson <awilliamson@mandriva.org> 1.3-12mdv2008.0
+ Revision: 75097
- rebuild for 2008
- correct license (following Fedora policy)
- update Blue-small to 1.4


* Fri Sep 01 2006 Götz Waschk <waschk@mandriva.org> 1.3-11mdv2007.0
- move skins to the new dir

* Sun Feb 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.3-10mdk
- Rebuild
- use mkrel

* Fri Feb 04 2005 Götz Waschk <waschk@linux-mandrake.com> 1.3-9mdk
- update all skins to their current versions

* Fri Jan 23 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3-8mdk
- rename default as old-default
- remove Blue skin (moved to mplayer-gui)

