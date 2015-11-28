# TODO
# - extern/six -> python-six?

#
# Conditional build:
%bcond_without	doc		# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module	d2to1
Summary:	Allows using distutils2-like setup.cfg files with setup.py
Name:		python-%{module}
Version:	0.2.11
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/d/d2to1/%{module}-%{version}.tar.gz
# Source0-md5:	81addef3dde584ab89b35ada8177c0d0
URL:		http://pypi.python.org/pypi/d2to1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
Requires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
d2to1 allows using distutils2-like setup.cfg files for a package's
metadata with a distribute/setuptools setup.py script. It works by
providing a distutils2-formatted setup.cfg file containing all of a
package's metadata, and a very minimal setup.py which will slurp its
arguments from the setup.cfg.

%package -n python3-d2to1
Summary:	Allows using distutils2-like setup.cfg files with setup.py
Group:		Libraries/Python
Requires:	python3-setuptools

%description -n python3-d2to1
d2to1 allows using distutils2-like setup.cfg files for a package's
metadata with a distribute/setuptools setup.py script. It works by
providing a distutils2-formatted setup.cfg file containing all of a
package's metadata, and a very minimal setup.py which will slurp its
arguments from the setup.cfg.

%prep
%setup -q -n %{module}-%{version}

rm -r %{module}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%dir %{py_sitescriptdir}/d2to1
%{py_sitescriptdir}/d2to1/*.py[co]
%dir %{py_sitescriptdir}/d2to1/extern
%{py_sitescriptdir}/d2to1/extern/__init__.py[co]
%{py_sitescriptdir}/d2to1/extern/six.py[co]
%{py_sitescriptdir}/d2to1-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-d2to1
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/*
%endif
