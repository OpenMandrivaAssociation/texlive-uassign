Name:		texlive-uassign
Version:	38459
Release:	2
Summary:	Environments and options for typesetting university assignments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uassign
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uassign.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uassign.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of this package is to provide simple question and
solution style environments for typesetting university
assignments.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/uassign
%doc %{_texmfdistdir}/doc/latex/uassign

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
