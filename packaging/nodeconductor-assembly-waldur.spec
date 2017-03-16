Name: nodeconductor-assembly-waldur
Summary: NodeConductor assembly for Waldur project
Group: Development/Libraries
Version: 2.4.0
Release: 1.el7
License: MIT
Url: http://nodeconductor.com
Source0: %{name}-%{version}.tar.gz

Requires: nodeconductor > 0.126.0
Requires: nodeconductor-auth-social >= 0.4.0
Requires: nodeconductor-auth-openid >= 0.4.1
Requires: nodeconductor-aws >= 0.4.0
Requires: nodeconductor-digitalocean >= 0.4.0
Requires: nodeconductor-openstack >= 0.20.0
Requires: python-jira >= 1.0.7

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
NodeConductor assembly for Waldur project.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}

install -d %{buildroot}%{_bindir}
install packaging/usr/bin/%{name}-check %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*
%{_bindir}/*

%defattr(-,root,root)

%changelog
* Wed Mar 15 2017 Jenkins <jenkins@opennodecloud.com> - 2.4.0-1.el7
- New upstream release

* Sat Feb 18 2017 Jenkins <jenkins@opennodecloud.com> - 2.3.0-1.el7
- New upstream release

* Tue Feb 14 2017 Jenkins <jenkins@opennodecloud.com> - 2.2.3-2.el7
- Add setup check script

* Wed Feb 8 2017 Jenkins <jenkins@opennodecloud.com> - 2.2.3-1.el7
- New upstream release

* Thu Jan 26 2017 Jenkins <jenkins@opennodecloud.com> - 2.2.2-1.el7
- New upstream release

* Thu Jan 19 2017 Jenkins <jenkins@opennodecloud.com> - 2.2.1-1.el7
- New upstream release

* Tue Jan 17 2017 Jenkins <jenkins@opennodecloud.com> - 2.2.0-1.el7
- New upstream release

* Sat Jan 14 2017 Jenkins <jenkins@opennodecloud.com> - 2.1.0-1.el7
- New upstream release

* Fri Dec 23 2016 Jenkins <jenkins@opennodecloud.com> - 2.0.0-1.el7
- New upstream release

* Mon Aug 22 2016 Juri Hudolejev <juri@opennodecloud.com> - 0.1.0-1.el7
- Initial version of the package

