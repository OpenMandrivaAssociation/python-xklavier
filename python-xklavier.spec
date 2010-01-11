Name: python-xklavier
Version: 0.2
Release: %mkrel 4
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
BuildRequires: libpython-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Python binding for libxklavier.

%prep
%setup -q -n python-xklavier-0.2
%patch -p1


%build
%configure2_5x --disable-static am_cv_python_pyexecdir=%{python_sitelib}
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{python_sitelib}/*

