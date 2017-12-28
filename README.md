# bchflip
A coin toss BCH game

## How to run
```
$ sudo pip install flask
$ EXPORT FLASK_APP=bchflip.py
$ flask run
```

## Generating a new address

### Request

#### Route
`GET /address`

`POST /address`

#### cURL
```
$ curl localhost:5000/address
{
    "address": "xxxxxxxxx", 
    "created": false
}

$ curl -X POST localhost:5000/address
{
    "address": "xxxxxxxxx", 
    "created": true
}
```

### Response

| Status Code | Description |
| --- | --- |
| 200 OK | MUST be returned upon successful processing of this request. Expected response body is below. |

#### Body

| Response field | Type | Description |
| --- | --- | --- |
| address | string | The currently active BCH address |
| created | boolean | Whether this address was just created. Should return `false` unless this was a POST request. |


## Get address balance

### Request

#### Route
`GET /address/<address>`

#### cURL
```
$ curl localhost:5000/address/<address>
{
    "balance": 20765760, 
    "exists": true
}

$ curl localhost:5000/address/<invalid_address>
{
    "balance": 0, 
    "exists": false
}
```

## Get addresses last transaction

### Request

#### Route
`GET /address/<address>/last_tx`

### Response

| Status Code | Description |
| --- | --- |
| 200 OK | Returned if a transaction is found with associated address. Expected body response is below. |
| 204 No Content | Returned if the address still has no associated transaction. |
| 500 Server Denied | Returned if something went wrong with verifying a transaction amount. This is NOT expected. |

#### Body

| Response field | Type | Description |
| --- | --- | --- |
| amount | float | The amount in BCH of the last transaction. |

#### cURL
```
$ curl localhost:5000/address/<address>/last_tx
{
    "amount": 0.2076576
}

$ curl localhost:5000/address/<address_with_no_tx>/last_tx
*   Trying ::1...
*   * TCP_NODELAY set
*   * connect to ::1 port 5000 failed: Connection refused
*   *   Trying 127.0.0.1...
*   * TCP_NODELAY set
*   * Connected to localhost (127.0.0.1) port 5000 (#0)
*   > GET /address/<address_with_no_tx>/last_tx HTTP/1.1
*   > Host: localhost:5000
*   > User-Agent: curl/7.51.0
*   > Accept: */*
*   > 
*   * HTTP 1.0, assume close after body
*   < HTTP/1.0 204 NO CONTENT
*   < Content-Type: application/json
*   < Content-Length: 0
*   < Server: Werkzeug/0.12.2 Python/2.7.13
*   < Date: Thu, 28 Dec 2017 16:30:36 GMT
*   < 
*   * Curl_http_done: called premature =>>>>>>
```
