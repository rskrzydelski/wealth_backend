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
     create_silver)
		         get_token
                 http POST http://localhost:8000/api/v1/resources/metals "Authorization: JWT $TOKEN"
		 ;;
     *)
		 echo "Usage: test_client {metals|gold|silver|gold_sum|silver_sum}"
		 ;;
 esac

 exit 0
