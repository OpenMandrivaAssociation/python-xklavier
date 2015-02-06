%define _disable_ld_no_undefined 1

Name:		python-xklavier
Version:	0.2
Release:	7
Summary:	Python binding for libxklavier
License:	LGPLv2+
Group:		Development/Python
Url:		http://sugarlabs.org/

Source0:	http://download.sugarlabs.org/sources/external/python-xklavier/python-xklavier-%version.tar.gz
Patch:		python-xklavier-0.2-xklavier-5.0.patch

Requires:	python-gobject >= 2.6.2
Requires:	python  

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	python-gobject-devel >= 2.6.2
BuildRequires:	python-devel  


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
%{python_sitelib}/*
