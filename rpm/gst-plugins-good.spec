# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       gst-plugins-good

# >> macros
# << macros

Summary:    GStreamer streaming media framework good plug-ins
Version:    0.10.27
Release:    1
Group:      Applications/Multimedia
License:    LGPL
URL:        http://gstreamer.freedesktop.org/
Source0:    http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
Patch0:     0001-v4l2-fix-build-with-recent-kernels-the-v4l2_buffer-i.patch
Patch1:     0002-pulsesink-Set-specific-media.role-for-pulsesink-prob.patch
Patch2:     0003-isomp4-Add-support-for-rotation-information-in-strea.patch
BuildRequires:  pkgconfig(orc-0.4) >= 0.4.5
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libjpeg-devel
BuildRequires:  python-devel
BuildRequires:  gettext-devel

%description
GStreamer Good Plug-ins is a collection of well-supported plug-ins of good 
quality and under the LGPL license.


%prep
%setup -q -n %{name}-%{version}/%{name}

# 0001-v4l2-fix-build-with-recent-kernels-the-v4l2_buffer-i.patch
%patch0 -p1
# 0002-pulsesink-Set-specific-media.role-for-pulsesink-prob.patch
%patch1 -p1
# 0003-isomp4-Add-support-for-rotation-information-in-strea.patch
%patch2 -p1
# >> setup
# << setup

%build
# >> build pre
export NOCONFIGURE="1"
%autogen
# << build pre

%configure --disable-static \
    --with-package-name='MeeGo GStreamer Plugins Good package' \
    --with-package-origin='http://www.meego.com' \
    --enable-experimental \
    --disable-examples \
    --enable-orc \
    --disable-schema-install \
    --with-gudev \
    --disable-nls \
    --disable-gtk-doc \
    --disable-gconf \
    --disable-gconftool

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
# >> files
# Equaliser presets
%{_datadir}/gstreamer-0.10/presets/
%{_libdir}/gstreamer-0.10/*.so
# << files
