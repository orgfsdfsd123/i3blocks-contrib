%global commit           fc2c10551c32558be44226c6924d64bae611e32c
%global shortcommit      fc2c105
%global date             2023

Name:           i3blocks-contrib
Version:        2.0.0
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        Community contributed blocklets for i3blocks.

License:        GPLv3+
URL:            https://github.com/vivien/i3blocks-contrib
Source0:        %{url}/archive/%{shortcommit}.tar.gz 

BuildRequires:  gcc
# we do not list all the optional requires here
# if user want to use some `plugins`, he/she should 
# read the README in blocklet dir and install it manually
Requires:       i3blocks

# remove some depends we do not have
%global opt Data::Validate::URI
%global opt %{opt}|JSON::Parse

%global __requires_exclude ^perl[(](%{opt})[)]

%description
This repository contains a set of scripts (a.k.a. blocklets) for i3blocks, contributed by the community.

%prep
%autosetup -n %{name}-%{commit}

%build
sed -i 's|/bin/perl|/usr/bin/perl|' purpleair/purpleair
make

%install
make DESTDIR=%{buildroot} PREFIX=%{_usr} install
install -d %{buildroot}%{_docdir}/%{name}
cp --parents */README* -t %{buildroot}%{_docdir}/%{name}/
cp --parents */LICENSE* -t %{buildroot}%{_docdir}/%{name}/
cp --parents */i3blocks.conf -t %{buildroot}%{_docdir}/%{name}/
cp --parents */*{,/}*.png -t %{buildroot}%{_docdir}/%{name}/

%files
%{_libexecdir}/i3blocks
%license LICENSE.md
%doc README.adoc
%doc ISSUE_TEMPLATE.md
%doc config.example
%doc CONTRIBUTING.md
%doc %{_docdir}/%{name}

%changelog
* Thu Feb 16 2023 lichaoran <pkwarcraft@hotmail.com> 2.0.0-1
- Initial build
