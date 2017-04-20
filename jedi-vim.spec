#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jedi-vim
Version  : 60056621256419913974543
Release  : 2
URL      : https://github.com/davidhalter/jedi-vim/archive/eef60e056a621e256cf4c1c9e91a397b454e3ede.tar.gz
Source0  : https://github.com/davidhalter/jedi-vim/archive/eef60e056a621e256cf4c1c9e91a397b454e3ede.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: jedi-vim-data
Requires: jedi
BuildRequires : jedi
BuildRequires : vim
Patch1: build.patch

%description
#################################################
jedi-vim - awesome Python autocompletion with VIM
#################################################

%package data
Summary: data components for the jedi-vim package.
Group: Data

%description data
data components for the jedi-vim package.


%prep
%setup -q -n jedi-vim-eef60e056a621e256cf4c1c9e91a397b454e3ede
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492655218
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1492655218
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/vim/vim80/after/ftplugin/python/jedi.vim
/usr/share/vim/vim80/after/syntax/python.vim
/usr/share/vim/vim80/autoload/health/jedi.vim
/usr/share/vim/vim80/autoload/jedi.vim
/usr/share/vim/vim80/ftplugin/python/jedi.vim
/usr/share/vim/vim80/initialize.py
/usr/share/vim/vim80/initialize.pyc
/usr/share/vim/vim80/initialize.pyo
/usr/share/vim/vim80/jedi_vim.py
/usr/share/vim/vim80/jedi_vim.pyc
/usr/share/vim/vim80/jedi_vim.pyo
/usr/share/vim/vim80/plugin/jedi.vim
