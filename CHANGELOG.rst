#########
Changelog
#########
All notable changes to the status NApp will be documented in this file.

[UNRELEASED] - Under development
********************************
Added
=====
- Added support for automated tests and CI with Travis.

Changed
=======
- Changed README.rst to include some info badges.

Deprecated
==========

Removed
=======
- Removed watchdog dependency from scrutinizer.

Fixed
=====
- Fixed Scrutinizer coverage error.

Security
========

[1.1.1] - 2019-03-15
********************
Added
=====

- Continuous integration enabled at scrutinizer.

Fixed
=====
- Fixing linter issues and improve code organization.

[1.1.0] - 2018-04-20
********************
Added
=====
- Add Status Compontent to be displayed in the Kytos UI .

[1.0.0] - 2018-01-31
********************
Added
=====
- Added enpoint `v1/` to return the controller status.
- Added enpoint `v1/napps` to return all loaded napps.
- Added basic openapi spec.
