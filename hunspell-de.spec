Name: hunspell-de
Summary: German hunspell dictionaries
%define upstreamid 20090107
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Source: http://www.j3e.de/ispell/igerman98/dict/igerman98-%{upstreamid}.tar.bz2
Group: Applications/Text
URL: http://www.j3e.de/ispell/igerman98
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2 or GPLv3
BuildArch: noarch
BuildRequires: aspell, hunspell
Patch1: igerman98-20090107-useaspell.patch

Requires: hunspell

%description
German (Germany, Switzerland, etc.) hunspell dictionaries.

%prep
%setup -q -n igerman98-%{upstreamid}
%patch1 -p1 -b .useaspell.patch

%build
make hunspell/de_AT.dic hunspell/de_AT.aff \
     hunspell/de_CH.dic hunspell/de_CH.aff \
     hunspell/de_DE.dic hunspell/de_DE.aff
cd hunspell
for i in README_*.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cd hunspell
cp -p de_??.dic de_??.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
de_DE_aliases="de_BE de_LU"
for lang in $de_DE_aliases; do
	ln -s de_DE.aff $lang.aff
	ln -s de_DE.dic $lang.dic
done
de_CH_aliases="de_LI"
for lang in $de_CH_aliases; do
	ln -s de_CH.aff $lang.aff
	ln -s de_CH.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc hunspell/README_de_??.txt hunspell/COPYING_OASIS hunspell/COPYING_GPLv2 hunspell/COPYING_GPLv3 hunspell/Copyright
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090107-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090107-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090107-3
- tidy spec

* Thu Apr 23 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090107-2
- fix dictionaries

* Thu Feb 26 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090107-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 11 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071211-1
- latest version

* Thu Aug 30 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070829-1
- latest version
- build from canonical source

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.20051213-2
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20051213-1
- initial version
