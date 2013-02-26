%define		_class		HTML
%define		_subclass	QuickForm
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	3.2.12
Release:	%mkrel 4
Summary:	Methods for creating, validating, processing HTML forms
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_QuickForm/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The PEAR::HTML_QuickForm package provides methods for creating,
validating, processing HTML forms. Features:
- Creates xHTML compliant form elements of various type.
- Allows you to choose an unlimited number of html attributes.
- Allows you to create your own custom elements using your own
  classes.
- Process form values (you should override the process method).
- Creates javascript validation code using regular expression.
- Server-side validation too.
- Allows you to create your own validation rules.
- Manages file uploads.
- Allows you to freeze some elements in your form.
- Allows you to customize the look of your form in many ways.
- Template-like form elements customization...

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.12-2mdv2011.0
+ Revision: 667504
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.12-1mdv2011.0
+ Revision: 587641
- update to new version 3.2.12

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.11-2mdv2010.1
+ Revision: 477871
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.11-1mdv2010.0
+ Revision: 383550
- update to new version 3.2.11

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.10-2mdv2009.1
+ Revision: 321846
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.10-1mdv2009.0
+ Revision: 272587
- 3.2.7

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.2.7-3mdv2009.0
+ Revision: 224740
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.7-2mdv2008.1
+ Revision: 178512
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2.7-1mdv2008.0
+ Revision: 15538
- 3.2.7


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-2mdv2007.0
+ Revision: 81101
- Import php-pear-HTML_QuickForm

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-1mdk
- 3.2.5
- fix deps

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.4pl1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.4pl1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.4pl1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.4pl1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.4pl1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.4pl1-1mdk
- initial Mandriva package (PLD import)

