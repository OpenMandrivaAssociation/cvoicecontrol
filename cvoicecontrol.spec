Name:		cvoicecontrol
Version:	0.9
Release:	%mkrel 0.alpha.5
License:	GPL
Group:		Sound
Source0:	http://www.kiecza.de/daniel/linux/%{name}-%{version}alpha.tar.bz2
Patch0:		%{name}-make.patch.bz2
Patch1:		%{name}-crash.patch.bz2
URL:		http://www.kiecza.de/daniel/linux/
BuildRequires:  texinfo
BuildRequires:  ncurses-devel >= 5.2
BuildRoot:	%_tmppath/%{name}-buildroot
Summary:	CVoiceControl is a speech recognition system enabling to use spoken commands

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
%configure
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
