adr=1
base=192.168.1

trap trapint 2
function trapint {
    exit 0
}

while [ $adr -le 255 ]
do
  
  time=$(ping $base.$adr -c 1 -t 1 | sed -nE 's/.*time=([0-9.]+).*/\1/p')

  if [ -z "$time" ]
  then
    echo IP: $base.$adr not found
  else
    echo IP: $base.$adr found!
    # host=$(nslookup $base.$adr | sed -nE 's/.*name = ([A-z.]+).*/\1/p)'
    # echo $host
    nslookup $base.$adr

  fi
  ((adr++))
done
