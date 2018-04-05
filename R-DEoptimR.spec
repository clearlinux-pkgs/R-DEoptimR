#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DEoptimR
Version  : 1.0.8
Release  : 3
URL      : https://cran.r-project.org/src/contrib/DEoptimR_1.0-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DEoptimR_1.0-8.tar.gz
Summary  : Differential Evolution Optimization in Pure R
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-DEoptim
BuildRequires : R-DEoptim
BuildRequires : clr-R-helpers

%description
optimization of problems with and without constraints.
  The aim is to curate a collection of its state-of-the-art variants that
  (1) do not sacrifice simplicity of design,
  (2) are essentially tuning-free, and
  (3) can be efficiently implemented directly in the R language.
  Currently, it only provides an implementation of the 'jDE' algorithm by

%prep
%setup -q -c -n DEoptimR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521189741

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521189741
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DEoptimR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DEoptimR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DEoptimR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library DEoptimR|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DEoptimR/DESCRIPTION
/usr/lib64/R/library/DEoptimR/INDEX
/usr/lib64/R/library/DEoptimR/Meta/Rd.rds
/usr/lib64/R/library/DEoptimR/Meta/features.rds
/usr/lib64/R/library/DEoptimR/Meta/hsearch.rds
/usr/lib64/R/library/DEoptimR/Meta/links.rds
/usr/lib64/R/library/DEoptimR/Meta/nsInfo.rds
/usr/lib64/R/library/DEoptimR/Meta/package.rds
/usr/lib64/R/library/DEoptimR/NAMESPACE
/usr/lib64/R/library/DEoptimR/NEWS.Rd
/usr/lib64/R/library/DEoptimR/R/DEoptimR
/usr/lib64/R/library/DEoptimR/R/DEoptimR.rdb
/usr/lib64/R/library/DEoptimR/R/DEoptimR.rdx
/usr/lib64/R/library/DEoptimR/help/AnIndex
/usr/lib64/R/library/DEoptimR/help/DEoptimR.rdb
/usr/lib64/R/library/DEoptimR/help/DEoptimR.rdx
/usr/lib64/R/library/DEoptimR/help/aliases.rds
/usr/lib64/R/library/DEoptimR/help/paths.rds
/usr/lib64/R/library/DEoptimR/html/00Index.html
/usr/lib64/R/library/DEoptimR/html/R.css
/usr/lib64/R/library/DEoptimR/xtraR/opt-test-funs.R
