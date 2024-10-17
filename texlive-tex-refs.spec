Name:		texlive-tex-refs
Version:	57349
Release:	2
Summary:	References for TeX and Friends
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tex-references
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-refs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-refs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is an ongoing project with the aim of providing a help
file for LaTeX (and its friends like ConTeXt, Metapost,
Metafont, etc.) using a state-of-the-art source format, aka
DocBook/XML.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/tex-refs/README
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs-0.4.1.tar.bz2
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs.css
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs.epub
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs.html
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
