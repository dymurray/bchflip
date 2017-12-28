# bchflip
A coin toss BCH game

### Request

#### Route
`GET /address`

#### cURL
```
$ curl http://localhost/address
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
