# 0x03-queuing_system_in_js

How to run a Redis server on your machine
-> Install Redis on machine
$ sudo apt install redis-server
-> Start redis service
$ sudo systemctl start redis
-> Enable redis service to start at boot
$ sudo systemctl enable redis

# Verify installation
$ redis-cli ping / redis-cli

# Redis Configuration

defualt port: 6379

file configuration location:
/etc/redis/redis.conf

After editing the config file, restart the service to apply the changes:

sudo systemctl restart redis

==============================================
# How to run simple operations with the Redis client
-> Open the redis cli 
$ redis-cli

you see:
127.0.0.1:6379>
Means the server is running on localhost at port 6379

# Basic operations

## String Operation
1. Set a key-value pair:
    $ SET mykey "Hello, Redis!"

2. Get a value by key:
    $ GET mykey  
    -> "Hello, Redis!"

## Hash Operation
1. Add fields to a hash
    $ HSET user:1 name "Alice" age "30"

2. Get a field from a hash
    $ HEGT user:1 name
    -> "Alice"
3. Get all fields
    $ HGETALL user:1
    -> 1)"name"
       2)"Alice"
       3)"age"
       4)"30"

## List Operation
1. Add an element to a list
 > LPUSH mylist "item1"
 > LPUSH mylist "item2"

2. getting elements from list
 > LRANGE mylist 0 -1

## Set Operations
1. Add an element to a set
 > SADD myset "value1" "value2"

2. Get all members
 > SMEMBERS myset 
  
  -> 1)"value1"
     2)"value2"

## Key Operations
list all keys:
 > KEYS * 
Check if keys exits:
 > EXISTS <mykey>
  -> (integer) <number of keys>

## Delete a key:
> DEL <key>

## Exit Redis:
> EXIT  / QUIT


==============================================
# How to use a Redis client with Node JS for basic operations

## 1. initialize project
$ npm init -y
## install redis library:
$ npm install redis

## 2. Import and Connect to Redis
const redis = require('redis');

// Create a Redis client
const client = redis.createClient({
  url: 'redis://127.0.0.1:6379', // Default Redis URL
});

// Connect to the Redis server
client.connect()
  .then(() => console.log('Connected to Redis'))
  .catch(err => console.error('Redis connection error:', err));


==============================================
# How to store hash values in Redis
->


==============================================
# How to deal with async operations with Redis
->


==============================================
# How to use Kue as a queue system
->


==============================================
# How to build a basic Express app interacting with a Redis server
->


==============================================
# How to the build a basic Express app interacting with a Redis server and queue
->


==============================================
