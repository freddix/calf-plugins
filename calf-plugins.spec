Summary:	Calf Studio Gear
Name:		calf-plugins
Version:	0.0.19
Release:	2
License:	GPL v2/LGPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/calf/calf-%{version}.tar.gz
# Source0-md5:	9570cb742522218a11b2dbefdb3aabc9
URL:		http://calf.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-single-devel
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lash-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calf Studio Gear is an audio plug-in pack for LV2 and JACK
environments under LINUX operating systems. The suite contains lots of
effects (delay, modulation, signal processing, dynamics, distortion
and mastering effects), instruments (SF2 player, organ simulator and
a monophonic synthesizer) and tools (analyzer, mono/stereo tools).

%prep
%setup -qn calf-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--enable-sse		\
	--with-lv2-dir="%{_libdir}/lv2"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/calf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/manuals
%attr(755,root,root) %{_bindir}/calfjackhost

%dir %{_libdir}/lv2/calf.lv2
%attr(755,root,root) %{_libdir}/lv2/calf.lv2/calf.so
%attr(755,root,root) %{_libdir}/lv2/calf.lv2/calflv2gui.so
%{_libdir}/lv2/calf.lv2/*.ttl

%dir %{_libdir}/calf
%attr(755,root,root) %{_libdir}/calf/calf.so
%{_datadir}/calf
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_mandir}/man1/calfjackhost.1*
%{_mandir}/man7/calf.7*

