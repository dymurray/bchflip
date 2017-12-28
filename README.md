# bchflip
A coin toss BCH game

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

### Response

| Status Code | Description |
| --- | --- |
| 200 OK | MUST be returned upon successful processing of this request. Expected response body is below. |

#### Body

| Response field | Type | Description |
| --- | --- | --- |
| balance | string | The currently active BCH address balance |
| exists | boolean | Whether this address currently exists. Should return `true` unless it is an invalid address. |

