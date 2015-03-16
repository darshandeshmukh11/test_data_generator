#/usr/bin/perl -w
use LWP::UserAgent;
use Crypt::SSLeay;
use Time::HiRes qw(gettimeofday);
use strict;
print "Enter URL to Time GET request for...  ";
my $host=<STDIN>;
chomp $host;
my $before=gettimeofday;
my $ua = LWP::UserAgent->new(); 
my $request = HTTP::Request->new('GET', "$host");
my $response = $ua->request($request);
my $elapsed=gettimeofday-$before;
print "ERROR: Bad URL\n" if($response->is_error);
my @content=split/\n/,$response->content;
print "Request took $elapsed seconds.\n";
my @title=grep /(?:title|TITLE)/, @content;
print "TITLE LINE: @title \n" unless($response->is_error);