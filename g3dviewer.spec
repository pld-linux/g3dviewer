Summary:	-
Name:		g3dviewer
Version:	0.2.99.4
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://automagically.de/files/%{name}-%{version}.tar.gz
# Source0-md5:	b7da4a68dd18309805ea2ca081542cfd
URL:		-
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libg3d-devel >= 0.0.8
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS CHANGES ChangeLog NEWS README THANKS TODO
