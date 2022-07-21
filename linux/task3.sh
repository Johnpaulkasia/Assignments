#!/bin/bash
#reads from the config file 
echo  " Reading configuration file $config"
config_file=$config

#checks the commands 
while IFS= read -r line;
 do
if ! command -v psql /dev/null ; then 
echo "this script requires psql"
exit 1 
fi

#checks for the database then logs in 
if psql -lqt | cut -d\| -f 1 | grep -qw chinook; then
exit 0
else
exit 1
fi

Database Host =$DB_port
Database name =$DB_name
Database Username =$DB_name
Database password =$pwd


psql -U postgres -h localip -p localport -d chinook
#runs query and inserts it in csv file.
$counter =2009
while [$counter -le 2013]
do
touch invoices_$counter.csv
SELECT invoices.InvoiceId, customers.CustomerId, invoice_items.TrackId, artists.Name, albums.Title, tracks.Name, invoices.InvoiceDate : invoices.InvoiceId 
FROM invoices, tracks
WHERE invoices.InvolcesDate>= '$counter-01-01 00:00:00'
AND invoices.InvoiceDate<'$counter-01-01 00:00:00' >> invoices_$counter.csv
((counter++))
done

