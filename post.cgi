#!/usr/bin/perl

use CGI;
use SQLite::DB;
use POSIX qw(strftime);
my $q = CGI->new;
my $db = SQLite::DB->new('guestbook.db');
$db->connect;

my $now = time();
my $Date = strftime('%Y-%m-%d', localtime($now));

print $q->header;
my $Name = $q->param("name");
my $Email = $q->param("email");
my $Comment = $q->param("comment");
my $Country = $q->param("country");
my $Captcha = $q->param("captcha");
if ($Name eq "") {
    print "Enter a name\n";
    die;
}
if ($Comment eq "") {
    print "Enter a comment\n";
    die;

}
if(!$Email eq "") {
    unless($Email =~ /.*@.*.\..*/) {
        print "Please enter valid E-mail address\n";
        die;
    }
}

unless($Captcha eq "sun" || $Captcha eq "Sun")
{
    print "wrong answer";
    die;
    
}


    $db->exec("INSERT INTO guestbook (NAME, EMAIL, COMMENT, COUNTRY, DATE) VALUES (?, ?, ?, ?, ?)",$Name, $Email, $Comment, $Country, $Date) || print $db->get_error;


print "<p>Succesfully added</p>";
