%global tl_name debate
%global tl_revision 64846

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.1
Release:	%{tl_revision}.1
Summary:	Debates between reviewers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/debate
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/debate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/debate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/debate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(listings)
Requires:	texlive(listingsutf8)
Requires:	texlive(pdfcol)
Requires:	texlive(tcolorbox)
Requires:	texlive(xcolor)
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package helps to organize debates between multiple reviewers of a
paper within the text.

