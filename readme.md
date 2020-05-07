My sister was trying to sign up for the MCAT exam, but the MCAT only specified a time range of 6am-12pm.
(https://twitter.com/AAMC_MCAT/status/1257401110316408832)

This script gets the page and then hashes the HTML. If the landing page changed at all from the known "this page is
currently not taking requests", it will use Twilio's api and call my sisters phone to notify her.

Originally I had this running on a crontab (* 5-12 * * *), but changed to making a request every 10 seconds.