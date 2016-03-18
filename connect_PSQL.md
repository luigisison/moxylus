#Connect to PostgreSQL with pgAdmin III via New Server Registration

* Reference: http://www.mkfoster.com/2008/12/21/setting-up-postgresql-on-linux-and-connecting-using-pgadmin-iii/

#Configure PostgreSQL Connection Settings
*sudo nano /etc/postgresql/9.3/main/postgresql.conf
Change #listen_addresses='localhost' to listen_addresses ='*'
Save file
Restart PostgreSQL
sudo /etc/init.d/postgresql restart
Grant users remote access
sudo nano /etc/postgresql/9.3/main/pg_hba.conf
host all all 10.0.0.0/16 md5
local all postgres trust
Comment the ff two lines with a "#" character
#local all all ident sameuser
#host all all 127.0.0.1/32 md5
Save file
Restart PostgreSQL
sudo /etc/init.d/postgresql restart
Reset PostgreSQL password
sudo -u postgres psql postgres
\password postgres
give your password when prompted
\q
In pgAdmin, enter Name=Odoo, Host=localhost, Password=what you created in the previous step
