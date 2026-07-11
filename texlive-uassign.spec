%global tl_name uassign
%global tl_revision 38459

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Environments and options for typesetting university assignments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uassign
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uassign.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uassign.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The purpose of this package is to provide simple question and solution
style environments for typesetting university assignments.

