#!/usr/bin/perl -wT
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# This Source Code Form is "Incompatible With Secondary Licenses", as
# defined by the Mozilla Public License, v. 2.0.

use strict;
use lib qw(. lib);

use Bugzilla;
use Bugzilla::Constants;
use Bugzilla::Error;
use Bugzilla::WebService::Constants;
BEGIN {
    if (!Bugzilla->feature('jsonrpc')) {
        ThrowCodeError('feature_disabled', { feature => 'jsonrpc' });
    }
}
use Bugzilla::WebService::Server::JSONRPC;

Bugzilla->usage_mode(USAGE_MODE_JSON);

local @INC = (bz_locations()->{extensionsdir}, @INC);
my $server = new Bugzilla::WebService::Server::JSONRPC;
$server->dispatch(WS_DISPATCH)->handle();
