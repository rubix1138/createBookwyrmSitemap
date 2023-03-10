# createBookwyrmSitemap
Create a sitemap for a Bookwyrm site

This is a python script to build a sitemap from all the books in your bookwrym database.  

# Installation
This uses xml_sitemap_writer which isn't installed by default on a bookwyrm server.  This was written for a dockerless setup.  You will need to adjust the instructions below for a dockerized bookwyrm server.
```
sudo su - bookwyrm
cd /opt/bookwyrm
./venv/bin/pip3 install xml-sitemap-writer
```
At this point you can download the script to the bookwyrm home directory.  By default, this script creates the sitemap files in /opt/bookwyrm/sitemaps, which doesn't exist in a default setup.
```
curl -o createBookwyrmSitemap.py https://raw.githubusercontent.com/rubix1138/createBookwyrmSitemap/main/createBookwyrmSitemap.py
mkdir /opt/bookwyrm/sitemaps
```
The last configuration setup is to modify your nginx config.
```
exit
sudo vi /etc/nginx/sites-available/bookwyrm.conf
```
Add the following lines in your main server block.  I put mine right below the certbot location block
```
    location ^~ /sitemap {
        autoindex on;
        root /opt/bookwyrm/sitemaps;
    }
```
Then reload nginx:
```
sudo systemctl reload nginx
```
# Usage
To run manually:
```
sudo su - bookwyrm
./venv/bin/python3 createBookwyrmSitemap.py
```
To add to cron:
```
sudo su - bookwyrm
crontab -e
0 0 * * * /opt/bookwyrm/venv/bin/python3 /opt/bookwyrm/createBookwyrmSitemap.py
````
