#!/bin/bash


get_token() {
   res=$(http POST http://localhost:8000/api/v1/auth/token username=raf password=raf | cut -d : -f 2)
   TOKEN=$(echo "$res" | sed 's/}//' | sed 's/"//' | sed 's/"//')
}

case $1 in
	 metals)
                 get_token
                 http GET http://localhost:8000/api/v1/resources/metals "Authorization: JWT $TOKEN"
		 ;;
	 gold)
	             get_token
                 http GET http://localhost:8000/api/v1/resources/metals?name=gold "Authorization: JWT $TOKEN"
		 ;;
     silver)
		         get_token
                 http GET http://localhost:8000/api/v1/resources/metals?name=silver "Authorization: JWT $TOKEN"
		 ;;
	 silver_sum)
		         get_token
                 http GET http://localhost:8000/api/v1/resources/metals?name=silver\&sum=true "Authorization: JWT $TOKEN"
		 ;;
	 gold_sum)
		         get_token
                 http GET http://localhost:8000/api/v1/resources/metals?name=gold\&sum=true "Authorization: JWT $TOKEN"
		 ;;
     create_gold)
		         get_token
                 http POST http://localhost:8000/api/v1/resources/metals name="gold" bought_price="20000" amount="4" unit="oz" date_of_bought="2019-11-26T11:00:30Z" description="test gold create" "Authorization: JWT $TOKEN"
		 ;;
	 create_gold_kg)
		         get_token
                 http POST http://localhost:8000/api/v1/resources/metals name="gold" bought_price="20000" amount="4" unit="kg" date_of_bought="2019-11-26T11:00:30Z" description="test gold create" "Authorization: JWT $TOKEN"
		 ;;
	 currency)
                 get_token
                 http GET http://localhost:8000/api/v1/resources/currency "Authorization: JWT $TOKEN"
		 ;;
	 usd)
                 get_token
                 http GET http://localhost:8000/api/v1/resources/currency?name=usd "Authorization: JWT $TOKEN"
		 ;;
	 create_usd)
		         get_token
                 http POST http://localhost:8000/api/v1/resources/currency bought_currency="500" bought_currency_currency="USD" bought_price="2000" bought_price_currency="PLN" date_of_bought="2019-12-26T12:01:36Z" "Authorization: JWT $TOKEN"
		 ;;
	 my_fortune)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet "Authorization: JWT $TOKEN"
		 ;;
	 metal_value)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/metal "Authorization: JWT $TOKEN"
		 ;;
	 silver_value)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/metal/silver "Authorization: JWT $TOKEN"
		 ;;
	 gold_value)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/metal/gold "Authorization: JWT $TOKEN"
		 ;;
	 cash)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/cash "Authorization: JWT $TOKEN"
		 ;;
	 currency_value)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/currency "Authorization: JWT $TOKEN"
		 ;;
	 usd_value)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/currency/usd "Authorization: JWT $TOKEN"
		 ;;
	 eur_value)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/currency/eur "Authorization: JWT $TOKEN"
		 ;;
	 chf_value)
		         get_token
                 http GET http://localhost:8000/api/v1/wallet/currency/chf "Authorization: JWT $TOKEN"
		 ;;
	 create_pln)
		         get_token
                 http POST http://localhost:8000/api/v1/resources/currency bought_currency="500" bought_currency_currency="PLN" bought_price="2000" bought_price_currency="PLN" date_of_bought="2019-12-26T12:01:36Z" "Authorization: JWT $TOKEN"
		 ;;
	create_pln_pay_usd)
		         get_token
                 http POST http://localhost:8000/api/v1/resources/currency bought_currency="500" bought_currency_currency="PLN" bought_price="2000" bought_price_currency="USD" date_of_bought="2019-12-26T12:01:36Z" "Authorization: JWT $TOKEN"
		 ;;
     *)
		 echo "Usage: test_client {metals|gold|silver|gold_sum|silver_sum|currency|usd|create_usd|my_fortune|metal_value|silver_value|gold_value|cash|currency_value|usd_value|eur_value|chf_value}"
		 ;;
 esac

 exit 0
