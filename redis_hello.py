import os
import redis

redis_host=10.171.139.78
redis_port=6379
redis_password= "dfhdhdfh5ru5u34u33442462346234634jtjrtjrtjj5646u35u35u54"


def hello_redis(): 
	try:
		v = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
		v.set("Test:Meldung", "Testing 123 Funktioniert")
		
		meldung= v.get("Test:Meldung")
		print(meldung)
	
	except Exception as e:
		print(e)
		
if __name__ == '__main__':
    hello_redis()
