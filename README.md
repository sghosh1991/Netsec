# Statistical Analysis of attacks on popular network services

This project aims at analysing the patterns in the brute force style attacks carried out against popular network services like SSH,POP3, FTP, Joomla and wordpress. For the purpose of the project honeypots were set up across three locations 

1) USA
2) Japan
3) Ireland

openssl SSH, dovecot POP3, pure FTPD , Woordpress and Joomla were customized to log information to elasticsearch database via Logstash. And then those records were analysee in Kibana. The complete ELK stack was used that helped easy analysis and data collection.

Files in the repo:

1) Config files for Logstash
2) Source Code for the modified network services
3) Complete report
