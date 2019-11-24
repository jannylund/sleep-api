# Sleep API

This is a simple rest api to be used as simulating a slow response.

It has two primary endpoints:

- `/sleep/<x>` will sleep for x seconds and then return.
- `/sleep/<x>/<y>` will sleep for random time between x and y seconds and then return.


# Running

The api exposes on port 5000. To run it simply execute as:

`docker run --rm -it -p5000:5000 jannylund/sleep-api:latest`


# Performance

This is a very naive implementation, but it can handle at least 100 concurrent calls without varying _too much_


# Example

Running a test with 100 concurrency in siege, for example: `siege -c100 -r1 http://localhost:5000/sleep/1` is expected to produce something similar to:

```
Transactions:                 100 hits
Availability:              100.00 %
Elapsed time:                1.20 secs
Data transferred:            0.00 MB
Response time:               1.12 secs
Transaction rate:           83.33 trans/sec
Throughput:                  0.00 MB/sec
Concurrency:                93.73
Successful transactions:      100
Failed transactions:            0
Longest transaction:         1.19
Shortest transaction:        1.02
```

And a test with random delay 1-10s: `siege -c100 -r1 http://localhost:5000/sleep/1/10` is expected to produce something similar to:

```
Transactions:                 100 hits
Availability:              100.00 %
Elapsed time:               10.14 secs
Data transferred:            0.00 MB
Response time:               5.88 secs
Transaction rate:            9.86 trans/sec
Throughput:                  0.00 MB/sec
Concurrency:                57.98
Successful transactions:      100
Failed transactions:            0
Longest transaction:        10.13
Shortest transaction:        1.04
```
