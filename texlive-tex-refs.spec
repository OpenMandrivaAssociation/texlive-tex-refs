# revision 15878
# category Package
# catalog-ctan /info/tex-references
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version 0.3.8
Name:		texlive-tex-refs
Version:	0.3.8
Release:	2
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
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs-source.tar.gz
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs.css
%doc %{_texmfdistdir}/doc/generic/tex-refs/tex-refs.html

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3.8-2
+ Revision: 756747
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3.8-1
+ Revision: 719712
- texlive-tex-refs
- texlive-tex-refs
- texlive-tex-refs

