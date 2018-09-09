import redis
import time
pool = redis.ConnectionPool(host='192.168.1.3', port=6379)
r = redis.Redis(connection_pool=pool)
#pipe = r.pipeline(transaction=False)
pipe = r.pipeline()

r.brpoplpush('names','names2',timeout=30)
pipe.set('name7', 'wupeiqi')
time.sleep(50)
pipe.set('age','23')
pipe.execute()