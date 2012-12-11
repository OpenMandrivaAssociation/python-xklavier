Name: python-xklavier
Version: 0.2
Release: 5
Summary: Python binding for libxklavier
License: LGPLv2+
Group: Development/Python
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/external/python-xklavier/python-xklavier-%version.tar.gz
Patch: python-xklavier-0.2-xklavier-5.0.patch

Requires: python-gobject >= 2.6.2
Requires: python  

BuildRequires: gtk+2-devel >= 2.2.0
BuildRequires: libxklavier-devel >= 5.0
BuildRequires: python-gobject-devel >= 2.6.2
BuildRequires: python-devel  


%description
Python binding for libxklavier.

%prep
%setup -q -n python-xklavier-0.2
%patch -p1


%build
%configure2_5x --disable-static am_cv_python_pyexecdir=%{python_sitelib}
%make

%install
%makeinstall_std

%files 
%defattr(-,root,root,-)
%{python_sitelib}/*



%changelog
* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 0.2-4mdv2010.1
+ Revision: 489679
- patch for new libxklavier
- spec fixes
- update license

* Tue Oct 13 2009 Aleksey Lim <alsroot@mandriva.org> 0.2-3mdv2010.0
+ Revision: 456995
- Fix x86_64 build

* Mon Sep 14 2009 Aleksey Lim <alsroot@mandriva.org> 0.2-2mdv2010.0
+ Revision: 440153
- Initial build

