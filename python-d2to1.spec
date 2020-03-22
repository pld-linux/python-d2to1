# TODO: extern/six -> python-six?
#
# Conditional build:
%bcond_with	tests	# test target (no tests in release tarball)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	d2to1
Summary:	Allow using distutils2-like setup.cfg files with setup.py (Python 2 version)
Summary(pl.UTF-8):	Możliwość używania setup.cfg w stylu distutils2 z setup.py (wersja dla Pythona 2)
Name:		python-%{module}
Version:	0.2.12.post1
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: URL: https://pypi.org/simple/d2to1/
Source0:	https://files.pythonhosted.org/packages/source/d/d2to1/%{module}-%{version}.tar.gz
# Source0-md5:	1ba7e64ead23cbf104993122f0871030
URL:		https://pypi.org/project/d2to1/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
d2to1 allows using distutils2-like setup.cfg files for a package's
metadata with a distribute/setuptools setup.py script. It works by
providing a distutils2-formatted setup.cfg file containing all of a
package's metadata, and a very minimal setup.py which will slurp its
arguments from the setup.cfg.

%description -l pl.UTF-8
d2to1 pozwala na używanie plików setup.cfg w stylu distutils2 jako
metadanych pakietu ze skryptem setup.py typowym dla
distribute/setuptools. Działa poprzez dostarczenie pliku setup.cfg w
formacie distutils2, zawierającego wszystkie metadane pakietu oraz
minimalnego pliku setup.py, który pobiera wszystkie argumenty z pliku
setup.cfg.

%package -n python3-d2to1
Summary:	Allow using distutils2-like setup.cfg files with setup.py (Python 3 version)
Summary(pl.UTF-8):	Możliwość używania setup.cfg w stylu distutils2 z setup.py (wersja dla Pythona 3)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-d2to1
d2to1 allows using distutils2-like setup.cfg files for a package's
metadata with a distribute/setuptools setup.py script. It works by
providing a distutils2-formatted setup.cfg file containing all of a
package's metadata, and a very minimal setup.py which will slurp its
arguments from the setup.cfg.

%description -n python3-d2to1 -l pl.UTF-8
d2to1 pozwala na używanie plików setup.cfg w stylu distutils2 jako
metadanych pakietu ze skryptem setup.py typowym dla
distribute/setuptools. Działa poprzez dostarczenie pliku setup.cfg w
formacie distutils2, zawierającego wszystkie metadane pakietu oraz
minimalnego pliku setup.py, który pobiera wszystkie argumenty z pliku
setup.cfg.

%prep
%setup -q -n %{module}-%{version}

%{__rm} -r %{module}.egg-info

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
%doc CHANGES.rst CONTRIBUTORS LICENSE README.rst
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
%doc CHANGES.rst CONTRIBUTORS LICENSE README.rst
%{py3_sitescriptdir}/d2to1
%{py3_sitescriptdir}/d2to1-%{version}-py*.egg-info
%endif
