Name:		cvoicecontrol
Version:	0.9
Release:	%mkrel 0.alpha.7
License:	GPL
Group:		Sound
Source0:	http://www.kiecza.de/daniel/linux/%{name}-%{version}alpha.tar.bz2
Patch0:		%{name}-make.patch.bz2
Patch1:		%{name}-crash.patch.bz2
URL:		https://www.kiecza.de/daniel/linux/
BuildRequires:  texinfo
BuildRequires:  ncurses-devel >= 5.2
BuildRoot:	%_tmppath/%{name}-buildroot
Summary:	Speech recognition system enabling to use spoken commands

%description
CVoiceControl is a speech recognition system that enables a user to
connect spoken commands to unix commands.  It automagically detects
speech input from a microphone, performs recognition on this input and
in case of successful recognition - executes the associated unix
command. 

%prep 
%setup -q -n %{name}-%{version}alpha
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -m755 cvoicecontrol/cvoicecontrol  $RPM_BUILD_ROOT%{_bindir}
install -m755 cvoicecontrol/model_editor  $RPM_BUILD_ROOT%{_bindir}
install -m755 cvoicecontrol/microphone_config  $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS BUGS FAQ README cvoicecontrol/docs/en/index*.html
%{_bindir}/cvoicecontrol
%{_bindir}/model_editor
%{_bindir}/microphone_config


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-0.alpha.7mdv2011.0
+ Revision: 610182
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.9-0.alpha.6mdv2010.1
+ Revision: 508117
- use configure2_5x

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9-0.alpha.5mdv2008.1
+ Revision: 170237
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Stéphane Téletchéa <steletch@mandriva.org> 0.9-0.alpha.5mdv2008.0
+ Revision: 69841
- IGNORE
- Patch to avoid the crash (solves bug #27782)
- Import cvoicecontrol



* Thu Jan 05 2006 Lenny Cartier <lenny@mandriva.com> 0.9-0.alpha.4mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9-0.alpha.3mdk
- rebuild

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9-0.alpha.2mdk
- rebuild

* Tue Oct 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9-0.alpha.1mdk
- from Per �yvind Karlsen <peroyvind@delonic.no> :
	- Initial release, specfile adopted from PLD
