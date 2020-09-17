import os
import redis

redis_host=10.171.139.78
redis_port=6379
redis_password= "3d66a3e822d96f9025cb8a0b1e30e97bc6f39ff74b8358e3153280a9cf84a195123"


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