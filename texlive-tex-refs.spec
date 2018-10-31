# revision 31946
# category Package
# catalog-ctan /info/tex-references
# catalog-date 2013-10-18 11:31:56 +0200
# catalog-license other-free
# catalog-version 0.4.8
Name:		texlive-tex-refs
Version:	0.4.8
Release:	10
Summary:	References for TeX and Friends
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/tex-references
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-refs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-refs.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
