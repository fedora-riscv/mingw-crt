%{?mingw_package_header}

%global snapshot_date 20120713

Name:           mingw-crt
Version:        2.0.999
Release:        0.9.trunk.%{snapshot_date}%{?dist}
Summary:        MinGW Windows cross-compiler runtime

License:        Public Domain and ZPLv2.1
Group:          Development/Libraries
URL:            http://mingw-w64.sourceforge.net/
%if 0%{?snapshot_date}
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-src_%{snapshot_date}.tar.bz2
%else
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.gz
%endif

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-gcc


%description
MinGW Windows cross-compiler runtime, base libraries.


%package -n mingw32-crt
Summary:        MinGW Windows cross-compiler runtime for the win32 target
Obsoletes:      mingw32-runtime < 3.18-7%{?dist}
Provides:       mingw32-runtime = 3.18-7%{?dist}
Requires:       mingw32-filesystem >= 95

%description -n mingw32-crt
MinGW Windows cross-compiler runtime, base libraries for the win32 target.

%package -n mingw64-crt
Summary:        MinGW Windows cross-compiler runtime for the win64 target
Obsoletes:      mingw64-runtime < 1.0-0.3.20100914%{?dist}
Provides:       mingw64-runtime = 1.0-0.3.20100914%{?dist}
Requires:       mingw64-filesystem >= 95

%description -n mingw64-crt
MinGW Windows cross-compiler runtime, base libraries for the win64 target.


%prep
%if 0%{?snapshot_date}
rm -rf mingw-w64-v%{version}
mkdir mingw-w64-v%{version}
cd mingw-w64-v%{version}
tar -xf %{S:0}
%setup -q -D -T -n mingw-w64-v%{version}/mingw
%else
%setup -q -n mingw-w64-v%{version}
%endif


%build
pushd mingw-w64-crt
    MINGW64_CONFIGURE_ARGS="--disable-lib32"
    %mingw_configure
    %mingw_make %{?_smp_mflags}
popd


%install
pushd mingw-w64-crt
    %mingw_make_install DESTDIR=$RPM_BUILD_ROOT
popd

# Dunno what to do with these files
rm -rf $RPM_BUILD_ROOT%{mingw32_prefix}/libsrc
rm -rf $RPM_BUILD_ROOT%{mingw64_prefix}/libsrc


%files -n mingw32-crt
%doc COPYING DISCLAIMER DISCLAIMER.PD
%{mingw32_libdir}/*

%files -n mingw64-crt
%doc COPYING DISCLAIMER DISCLAIMER.PD
%{mingw64_libdir}/*


%changelog
* Fri Jul 13 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.9.trunk.20120713
- Update to 20120703 snapshot
- Fixes testsuite failure in the qt_qmake_test_static_mingw32 testcase

* Mon Jul  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.8.trunk.20120709
- Update to 20120709 snapshot (contains full Cygwin support)
- Eliminated various manual kludges as upstream now installs their
  files to the correct folders by default

* Thu Jul  5 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.7.trunk.20120705
- Update to 20120705 snapshot (contains various Cygwin changes)

* Sat Jun  2 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.6.trunk.20120601
- Update to 20120601 snapshot

* Tue Mar  6 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.5.trunk.20120224
- Enable support for the win64 target

* Sat Feb 25 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.4.trunk.20120224
- Update to mingw-w64 trunk 20120224 snapshot
- Made the win64 pieces optional for now (pending approval of the mingw-gcc/mingw-binutils package reviews)
- Dropped the use of the mingw_pkg_name macro
- Eliminated some conditionals related to snapshot builds
- Use smaller SourceForge source URLs
- Improved summary of the various packages
- Simplified the configure, make and make install calls
- Dropped upstreamed patch
- Added DISCLAIMER and DISCLAIMER.PD files
- Added ZPLv2.1 to the license tag
- Bumped obsoletes/provides version for mingw32-runtime

* Tue Jan 24 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.3.trunk.20120124
- Update to mingw-w64 trunk 20120124 snapshot
- Apply upstream r4758 to fix vsnprintf and vscanf failures

* Fri Jan 20 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.2.trunk.20120120
- Update to mingw-w64 trunk 20120120 snapshot (fixes various errno related compile failures)

* Thu Jan 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.1.trunk.20120112
- Update to mingw-w64 trunk 20120112 snapshot

* Sat Nov 19 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.1-1
- Update to mingw-w64 v2.0.1

* Sat Oct 22 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0-1
- Update to mingw-w64 v2.0

* Sun Sep 25 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0-0.3.rc1
- Replaced the boilerplate code with the mingw_package_header macro
- Bumped the obsoletes mingw32-runtime
- Dropped unneeded RPM tags

* Sat Aug 13 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0-0.2.rc1
- Rebuild because of broken mingw-find-requires.sh in the mingw-filesystem package

* Mon Aug  8 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0-0.1.rc1
- Update to 2.0-rc1

* Tue Jul 12 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-0.7.20110711.trunk
- Update to 20110711 snapshot of the trunk branch

* Sat Jun 25 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-0.6.20110625.trunk
- Update to 20110625 snapshot of the trunk branch (fixes gstreamer d3d issue)
- Replaced the patch with one which doesn't require the autotools

* Thu Jun  9 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-0.5.20110609.trunk
- Update to 20110609 snapshot of the trunk branch

* Thu Apr 14 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-0.4.20110413.trunk
- Update to 20110413 snapshot of the trunk branch
- Made the package compliant with the new packaging guidelines

* Wed Jan 12 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-0.3.20101003
- Update to 20101003 snapshot
- Generate per-target RPMs
- Bundle the COPYING file

* Wed Sep 29 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-0.2.20100914
- Update to snapshot 20100915 (v1.0 branch)
- Renamed the package to mingw-crt
- Added support for both i686-w64-mingw32 and x86_64-w64-mingw32
- Obsoletes/provides the mingw32-runtime package

* Fri May 14 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0-0.1.20100513
- Updated to snapshot 20100513 (v1.0 branch)
- Updated Source0 tag
- Fixed %%defattr tag

* Wed Feb 11 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1-0.svn607.3
- Started mingw64 development.

* Tue Feb 10 2009 Richard W.M. Jones <rjones@redhat.com> - 3.15.2-1
- New upstream release 3.15.2.

* Tue Dec  9 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-10
- Force rebuild to get rid of the binary bootstrap package and replace
  with package built from source.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-9
- No runtime dependency on binutils or gcc.
- But it DOES BR w32api.

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-8
- Rebuild against latest filesystem package.
- MINGW_CFLAGS -> MINGW32_CFLAGS.
- Rewrite the summary for accuracy and brevity.

* Fri Nov 21 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-6
- Remove obsoletes for a long dead package.
- Reenable (and fix) _mingw32_configure (Levente Farkas).

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-5
- Don't use _mingw32_configure macro - doesn't work here.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-4
- Rebuild against mingw32-filesystem 37

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-3
- Remove the useconds patch, which is no longer needed (Levente Farkas).
- Use _mingw32_configure macro.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-2
- Rebuild against mingw32-filesystem 36

* Thu Oct 16 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-1
- New upstream version 3.15.1.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-6
- Rename mingw -> mingw32.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-4
- Use RPM macros from mingw-filesystem.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-2
- Initial RPM release, largely based on earlier work from several sources.
