%define pybasever 3.1
%define real_name python-memcached
%define pyver 31 
%define __python /usr/bin/python%{pybasever}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}


Name:           python%{pyver}-memcached
Version:        1.44
Release:        3.ius%{?dist}
Summary:        A Python memcached client library

Group:          Development/Languages
License:        Python
URL:            http://www.tummy.com/Community/software/python-memcached/
Source0:        ftp://ftp.tummy.com/pub/python-memcached/python-memcached-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{pyver}-devel, python%{pyver}-distribute

%description
This software is a 100% Python interface to the memcached memory cache
daemon.  It is the client side software which allows storing values in one
or more, possibly remote, memcached servers.  Search google for memcached
for more information.

%prep
%setup -q -n %{real_name}-%{version}

# This is a hack, but so far doesn't look like python-memcached is 
# Python 3 compatible
find ./ -iname "*.py" | xargs 2to3-3.1 -w

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%attr(755,root,root) %{python_sitelib}/memcache.py
%{python_sitelib}/memcache.py[co]
%{python_sitelib}/python_memcached-%{version}-py*.egg-info/

%changelog
* Mon Apr 16 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.44-3.ius
- Rebuilding against latest python31

* Mon Jun 13 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.44-2.ius
- Rebuilding against latest python 3.1.4

* Tue Oct 20 2009 BJ Dierkes <wdierkes@rackspace.com> - 1.44-1.ius
- Rebuilding for python31
- BuildRequires: python31-distribute (rather than setuptools)
- Latest sources from upstream
- Execute 2to3 on all .py files (only way around it for Python 3)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.43-3
- Rebuild for Python 2.6

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.43-2
- add BR: python-setuptools

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.43-1
- fix license tag
- update to 1.43

* Tue Aug 14 2007 Sean Reifschneider <jafo@tummy.com> 1.39-1
- Update to 1.39 upstream release.

* Sat Aug 11 2007 Sean Reifschneider <jafo@tummy.com> 1.38-1
- Update to 1.38 upstream release.

* Sun Jun 10 2007 Sean Reifschneider <jafo@tummy.com> 1.36-3
- Changes based on feedback from Ruben Kerkhof:
- Fixing license.
- Removing PKG-INFO from doc.
- Fixing summary.
- Removing setuptools build dependency.
- Changing permissions of memcache module to 

* Sat Jun 09 2007 Sean Reifschneider <jafo@tummy.com> 1.36-2
- Adding python-devel build requirement.

* Sat Jun 09 2007 Sean Reifschneider <jafo@tummy.com> 1.36-1
- Initial RPM spec file.
