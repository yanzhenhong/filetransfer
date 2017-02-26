ps -ef|grep -E "Server.pyw"|grep -v grep |awk  '{printf  "kill -9 "$2"\012"  }' >stopprocess.sh
sh stopprocess.sh
python Server.pyw
