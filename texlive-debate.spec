Name:		texlive-debate
Version:	64846
Release:	2
Summary:	Debates between reviewers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/debate
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/debate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/debate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/debate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package helps to organize debates between multiple
reviewers of a paper within the text.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/debate
%{_texmfdistdir}/tex/latex/debate
%doc %{_texmfdistdir}/doc/latex/debate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
