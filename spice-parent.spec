Name:           spice-parent
Version:        15
Release:        6
Summary:        Sonatype Spice Components

Group:          Development/Java
License:        ASL 2.0
URL:            http://svn.sonatype.org/spice/tags/spice-parent-15
#svn export http://svn.sonatype.org/spice/tags/spice-parent-15 spice-parent-15
#tar zcf spice-parent-15.tar.gz spice-parent-15/
Source0:        %{name}-%{version}.tar.gz
Patch0:        pom.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires:  jpackage-utils >= 0:1.7.2

Requires:          jpackage-utils
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

%description
Spice components and libraries are common components 
used throughout the Sonatype Forge.

%prep
%setup -q -n %{name}-%{version}
#Remove plexus-javadoc
%patch0

%build
#nothing to do for the pom

%install
rm -rf %{buildroot}

%add_to_maven_depmap org.sonatype.spice spice-parent %{version} JPP spice-parent

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*



%changelog
* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 15-6
+ Revision: 734240
- rebuild
- imported package spice-parent

