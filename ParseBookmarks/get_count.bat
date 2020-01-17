echo off
for /F %%h in ('dir /B *.html') do grep -c -i http %%h

