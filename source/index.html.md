---
title: Syscoin API
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - javascript--nodejs: Node.JS
  - ruby: Ruby
  - python: Python
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<h1 id="Syscoin-API">Syscoin API v3.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Base URLs:

* <a href="http://localhost:8001/">http://localhost:8001/</a>

* <a href="https://localhost:8001/">https://localhost:8001/</a>

# Authentication

* API Key (token)
    - Parameter Name: **token**, in: header. 

<h1 id="Syscoin-API-Asset">Asset</h1>

Assets are similar to ERC20 tokens

## assetupdate

<a id="opIdassetupdate"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//assetupdate \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//assetupdate HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetupdate',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "interest_rate": 6.027456183070403,
  "asset": "asset",
  "category": "category",
  "supply": 0.8008281904610115
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetupdate',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//assetupdate',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//assetupdate', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetupdate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//assetupdate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /assetupdate`

Perform an update on an asset you control.

> Body parameter

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "interest_rate": 6.027456183070403,
  "asset": "asset",
  "category": "category",
  "supply": 0.8008281904610115
}
```

<h3 id="assetupdate-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetUpdateRequest](#schemaassetupdaterequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetupdate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="assetupdate-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assettransfer

<a id="opIdassettransfer"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//assettransfer \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//assettransfer HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assettransfer',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "alias": "alias",
  "asset": "asset"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assettransfer',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//assettransfer',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//assettransfer', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assettransfer");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//assettransfer", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /assettransfer`

Transfer asset from one user to another.

> Body parameter

```json
{
  "witness": "witness",
  "alias": "alias",
  "asset": "asset"
}
```

<h3 id="assettransfer-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetTransferRequest](#schemaassettransferrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assettransfer-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="assettransfer-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assetallocationsenderstatus

<a id="opIdassetallocationsenderstatus"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//assetallocationsenderstatus?asset=string&sender=string&txid=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//assetallocationsenderstatus?asset=string&sender=string&txid=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetallocationsenderstatus',
  method: 'get',
  data: '?asset=string&sender=string&txid=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetallocationsenderstatus?asset=string&sender=string&txid=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//assetallocationsenderstatus',
  params: {
  'asset' => 'string',
'sender' => 'string',
'txid' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//assetallocationsenderstatus', params={
  'asset': 'string',  'sender': 'string',  'txid': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetallocationsenderstatus?asset=string&sender=string&txid=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//assetallocationsenderstatus", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /assetallocationsenderstatus`

Show status as it pertains to any current Z-DAG conflicts or warnings related to a sender or sender/txid combination of an asset allocation transfer. Leave txid empty if you are not checking for a specific transfer. Return value is in the status field and can represent 4 levels(-1:Not Found, 0:OK, 1:Warning or 2:Critical)

<h3 id="assetallocationsenderstatus-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|asset|query|string|true|none|
|sender|query|string|true|none|
|txid|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "status": 0.8008281904610115
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetallocationsenderstatus-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[AssetAllocationSenderStatus](#schemaassetallocationsenderstatus)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assetallocationsend

<a id="opIdassetallocationsend"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//assetallocationsend \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//assetallocationsend HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetallocationsend',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "amounts": [
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    },
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    }
  ],
  "memo": "memo",
  "asset": "asset",
  "aliasfrom": "aliasfrom"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetallocationsend',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//assetallocationsend',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//assetallocationsend', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetallocationsend");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//assetallocationsend", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /assetallocationsend`

Send an asset you own to another alias as an asset allocation.

> Body parameter

```json
{
  "witness": "witness",
  "amounts": [
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    },
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    }
  ],
  "memo": "memo",
  "asset": "asset",
  "aliasfrom": "aliasfrom"
}
```

<h3 id="assetallocationsend-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetSendRequest](#schemaassetsendrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetallocationsend-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="assetallocationsend-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assetallocationcollectinterest

<a id="opIdassetallocationcollectinterest"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//assetallocationcollectinterest \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//assetallocationcollectinterest HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetallocationcollectinterest',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "alias": "alias",
  "asset": "asset"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetallocationcollectinterest',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//assetallocationcollectinterest',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//assetallocationcollectinterest', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetallocationcollectinterest");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//assetallocationcollectinterest", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /assetallocationcollectinterest`

Collect interest on this asset allocation if an interest rate is set on this asset.

> Body parameter

```json
{
  "witness": "witness",
  "alias": "alias",
  "asset": "asset"
}
```

<h3 id="assetallocationcollectinterest-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetAllocationCollectInterestRequest](#schemaassetallocationcollectinterestrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetallocationcollectinterest-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="assetallocationcollectinterest-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assetallocationinfo

<a id="opIdassetallocationinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//assetallocationinfo?asset=string&alias=string&getinputs=true \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//assetallocationinfo?asset=string&alias=string&getinputs=true HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetallocationinfo',
  method: 'get',
  data: '?asset=string&alias=string&getinputs=true',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetallocationinfo?asset=string&alias=string&getinputs=true',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//assetallocationinfo',
  params: {
  'asset' => 'string',
'alias' => 'string',
'getinputs' => 'boolean'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//assetallocationinfo', params={
  'asset': 'string',  'alias': 'string',  'getinputs': 'true'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetallocationinfo?asset=string&alias=string&getinputs=true");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//assetallocationinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /assetallocationinfo`

Show stored values of a single asset allocation. Set getinputs to true if you want to get the allocation inputs, if applicable.

<h3 id="assetallocationinfo-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|asset|query|string|true|none|
|alias|query|string|true|none|
|getinputs|query|boolean|true|none|

> Example responses

> 200 Response

```json
{
  "balance": 6.027456183070403,
  "inputs": [
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    },
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    }
  ],
  "txid": "txid",
  "alias": "alias",
  "interest_claim_height": 1.4658129805029452,
  "memo": "memo",
  "_id": "_id",
  "asset": "asset",
  "accumulated_interest": 5.962133916683182,
  "height": 0.8008281904610115
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetallocationinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[AssetAllocation](#schemaassetallocation)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assetnew

<a id="opIdassetnew"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//assetnew \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//assetnew HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetnew',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "symbol": "symbol",
  "witness": "witness",
  "publicvalue": "publicvalue",
  "can_adjust_interest_rate": true,
  "precision": 0.8008281904610115,
  "max_supply": 1.4658129805029452,
  "alias": "alias",
  "interest_rate": 5.962133916683182,
  "use_inputranges": true,
  "category": "category",
  "supply": 6.027456183070403
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetnew',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//assetnew',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//assetnew', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetnew");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//assetnew", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /assetnew`

Create a new Syscoin Asset.

> Body parameter

```json
{
  "symbol": "symbol",
  "witness": "witness",
  "publicvalue": "publicvalue",
  "can_adjust_interest_rate": true,
  "precision": 0.8008281904610115,
  "max_supply": 1.4658129805029452,
  "alias": "alias",
  "interest_rate": 5.962133916683182,
  "use_inputranges": true,
  "category": "category",
  "supply": 6.027456183070403
}
```

<h3 id="assetnew-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetNewRequest](#schemaassetnewrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetnew-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="assetnew-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assetsend

<a id="opIdassetsend"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//assetsend \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//assetsend HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetsend',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "amounts": [
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    },
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    }
  ],
  "memo": "memo",
  "asset": "asset",
  "aliasfrom": "aliasfrom"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetsend',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//assetsend',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//assetsend', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetsend");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//assetsend", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /assetsend`

Send an asset allocation you own to another alias.

> Body parameter

```json
{
  "witness": "witness",
  "amounts": [
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    },
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    }
  ],
  "memo": "memo",
  "asset": "asset",
  "aliasfrom": "aliasfrom"
}
```

<h3 id="assetsend-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetSendRequest](#schemaassetsendrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetsend-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="assetsend-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## assetinfo

<a id="opIdassetinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//assetinfo?asset=string&getinputs=true \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//assetinfo?asset=string&getinputs=true HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//assetinfo',
  method: 'get',
  data: '?asset=string&getinputs=true',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//assetinfo?asset=string&getinputs=true',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//assetinfo',
  params: {
  'asset' => 'string',
'getinputs' => 'boolean'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//assetinfo', params={
  'asset': 'string',  'getinputs': 'true'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//assetinfo?asset=string&getinputs=true");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//assetinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /assetinfo`

Show stored values of a single asset and its. Set getinputs to true if you want to get the allocation inputs, if applicable.

<h3 id="assetinfo-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|asset|query|string|true|none|
|getinputs|query|boolean|true|none|

> Example responses

> 200 Response

```json
{
  "symbol": "symbol",
  "can_adjust_interest_rate": true,
  "total_supply": 5.962133916683182,
  "inputs": [
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    },
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    }
  ],
  "precision": 7.061401241503109,
  "txid": "txid",
  "publicvalue": "publicvalue",
  "use_input_ranges": true,
  "balance": 1.4658129805029452,
  "max_supply": 5.637376656633329,
  "guid": "guid",
  "alias": "alias",
  "interest_rate": 2.3021358869347655,
  "time": 6.027456183070403,
  "category": "category",
  "height": 0.8008281904610115
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="assetinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Asset](#schemaasset)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

<h1 id="Syscoin-API-Blockmarket">Blockmarket</h1>

## login

<a id="opIdlogin"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//login?auth=string \
  -H 'Accept: application/json'

```

```http
GET http://localhost:8001//login?auth=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json'

};

$.ajax({
  url: 'http://localhost:8001//login',
  method: 'get',
  data: '?auth=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json'

};

fetch('http://localhost:8001//login?auth=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://localhost:8001//login',
  params: {
  'auth' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8001//login', params={
  'auth': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//login?auth=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//login", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /login`

Returns a session token for use with subsquent protected calls.

<h3 id="login-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|auth|query|string|true|SHA1 hash of the user's authentication information- usernamepassword.|

> Example responses

> 200 Response

```json
{
  "success": true,
  "message": "message",
  "token": "token"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="login-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[LoginResponse](#schemaloginresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="Syscoin-API-General">General</h1>

All general wallet operations.

## syscoinlistreceivedbyaddress

<a id="opIdsyscoinlistreceivedbyaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//syscoinlistreceivedbyaddress \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//syscoinlistreceivedbyaddress HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//syscoinlistreceivedbyaddress',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//syscoinlistreceivedbyaddress',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//syscoinlistreceivedbyaddress',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//syscoinlistreceivedbyaddress', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//syscoinlistreceivedbyaddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//syscoinlistreceivedbyaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /syscoinlistreceivedbyaddress`

Returns all addresses and balances associated with address

> Example responses

> 200 Response

```json
[
  {
    "address": "address",
    "balance": 0.8008281904610115,
    "alias": "alias",
    "label": "label"
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="syscoinlistreceivedbyaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="syscoinlistreceivedbyaddress-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[SyscoinAddressEntry](#schemasyscoinaddressentry)]|false|none|none|
|» address|string|false|none|none|
|» balance|number|false|none|none|
|» label|string|false|none|none|
|» alias|string|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getblock

<a id="opIdgetblock"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getblock?hash=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getblock?hash=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getblock',
  method: 'get',
  data: '?hash=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getblock?hash=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getblock',
  params: {
  'hash' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getblock', params={
  'hash': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getblock?hash=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getblock", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getblock`

If verbose is false, returns a string that is serialized, hex-encoded data for block 'hash'. If verbose is true, returns an Object with information about block <hash>.

<h3 id="getblock-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|hash|query|string|true|none|
|verbose|query|boolean|false|none|

> Example responses

> 200 Response

```json
{
  "tx": [
    "tx",
    "tx"
  ],
  "mediantime": 9.301444243932576,
  "data": "data",
  "previousblockhash": "previousblockhash",
  "bits": "bits",
  "weight": 5.962133916683182,
  "versionHex": "versionHex",
  "confirmations": 0.8008281904610115,
  "version": 2.3021358869347655,
  "nonce": 3.616076749251911,
  "nextblockhash": "nextblockhash",
  "difficulty": 2.027123023002322,
  "chainwork": "chainwork",
  "size": 6.027456183070403,
  "merkleroot": "merkleroot",
  "strippedsize": 1.4658129805029452,
  "time": 7.061401241503109,
  "hash": "hash",
  "height": 5.637376656633329
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getblock-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[GetBlockResponse](#schemagetblockresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getblockchaininfo

<a id="opIdgetblockchaininfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getblockchaininfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getblockchaininfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getblockchaininfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getblockchaininfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getblockchaininfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getblockchaininfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getblockchaininfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getblockchaininfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getblockchaininfo`

Returns an object containing various state info regarding block chain processing.

> Example responses

> 200 Response

```json
{
  "difficulty": 1.4658129805029452,
  "headers": 6.027456183070403,
  "bip9_softforks": "{}",
  "chain": "chain",
  "chainwork": "chainwork",
  "mediantime": 5.962133916683182,
  "verificationprogress": 5.637376656633329,
  "blocks": 0.8008281904610115,
  "pruned": true,
  "softforks": [
    "{}",
    "{}"
  ],
  "pruneheight": 2.3021358869347655,
  "bestblockhash": "bestblockhash"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getblockchaininfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[GetBlockchainInfoResponse](#schemagetblockchaininforesponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getblockcount

<a id="opIdgetblockcount"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getblockcount \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getblockcount HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getblockcount',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getblockcount',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getblockcount',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getblockcount', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getblockcount");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getblockcount", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getblockcount`

Returns the number of blocks in the longest block chain.

> Example responses

> 200 Response

```json
0
```

> default Response

```json
0
```

<h3 id="getblockcount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|number|
|default|Default|Error|number|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getinfo

<a id="opIdgetinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getinfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getinfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getinfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getinfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getinfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getinfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getinfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getinfo`

Returns an object containing various state info.

> Example responses

> 200 Response

```json
{
  "protocolversion": 6.027456183070403,
  "relayfee": 1.2315135367772556,
  "timeoffset": 2.3021358869347655,
  "blocks": 5.637376656633329,
  "version": 0.8008281904610115,
  "keypoolsize": 2.027123023002322,
  "unlocked_until": 4.145608029883936,
  "paytxfee": 7.386281948385884,
  "difficulty": 9.301444243932576,
  "proxy": "proxy",
  "walletversion": 1.4658129805029452,
  "balance": 5.962133916683182,
  "keypoololdest": 3.616076749251911,
  "testnet": true,
  "connections": 7.061401241503109,
  "errors": "errors"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Info](#schemainfo)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getmininginfo

<a id="opIdgetmininginfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getmininginfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getmininginfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getmininginfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getmininginfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getmininginfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getmininginfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getmininginfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getmininginfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getmininginfo`

Returns a json object containing mining-related information.

> Example responses

> 200 Response

```json
{
  "difficulty": 5.962133916683182,
  "chain": "chain",
  "currentblocktx": 1.4658129805029452,
  "blocks": 0.8008281904610115,
  "networkhashps": 2.3021358869347655,
  "currentblocksize": 6.027456183070403,
  "genproclimit": 5.637376656633329,
  "testnet": true,
  "pooledtx": 7.061401241503109,
  "generate": true,
  "errors": "errors"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getmininginfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[MiningInfo](#schemamininginfo)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getnetworkinfo

<a id="opIdgetnetworkinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getnetworkinfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getnetworkinfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getnetworkinfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getnetworkinfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getnetworkinfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getnetworkinfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getnetworkinfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getnetworkinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getnetworkinfo`

Returns a json object containing network-related information.

> Example responses

> 200 Response

```json
{
  "localaddresses": [
    "localaddresses",
    "localaddresses"
  ],
  "protocolversion": 6.027456183070403,
  "relayfee": 5.637376656633329,
  "subversion": "subversion",
  "timeoffset": 1.4658129805029452,
  "warnings": "warnings",
  "localrelay": true,
  "networks": [
    {
      "proxy": "proxy",
      "limited": true,
      "proxy_randomize_credentials": true,
      "name": "name",
      "reachable": true
    },
    {
      "proxy": "proxy",
      "limited": true,
      "proxy_randomize_credentials": true,
      "name": "name",
      "reachable": true
    }
  ],
  "version": 0.8008281904610115,
  "connections": 5.962133916683182,
  "localservices": "localservices"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getnetworkinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[NetworkInfo](#schemanetworkinfo)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getpeerinfo

<a id="opIdgetpeerinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getpeerinfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getpeerinfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getpeerinfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getpeerinfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getpeerinfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getpeerinfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getpeerinfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getpeerinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getpeerinfo`

Returns data about each connected network node as a json array of objects.

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "addr": "string",
    "addrlocal": "string",
    "services": "string",
    "relaytxes": true,
    "lastsend": 0,
    "lastrecv": 0,
    "bytessent": 0,
    "bytesrecv": 0,
    "conntime": 0,
    "timeoffset": 0,
    "pingtime": 0,
    "minping": 0,
    "version": 0,
    "subver": "string",
    "inbound": true,
    "startingheight": 0,
    "banscore": 0,
    "synced_headers": 0,
    "synced_blocks": 0,
    "inflight": [
      0
    ],
    "whitelisted": true,
    "bytessent_per_msg": {
      "addr": 0,
      "block": 0,
      "getaddr": 0,
      "getdata": 0,
      "getheaders": 0,
      "headers": 0,
      "inv": 0,
      "ping": 0,
      "pong": 0,
      "sendheaders": 0,
      "tx": 0,
      "verack": 0,
      "version": 0
    },
    "bytesrecv_per_msg": {
      "addr": 0,
      "block": 0,
      "getaddr": 0,
      "getdata": 0,
      "getheaders": 0,
      "headers": 0,
      "inv": 0,
      "ping": 0,
      "pong": 0,
      "sendheaders": 0,
      "tx": 0,
      "verack": 0,
      "version": 0
    }
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getpeerinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[PeerInfoResponse](#schemapeerinforesponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## validateaddress

<a id="opIdvalidateaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//validateaddress?syscoinaddress=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//validateaddress?syscoinaddress=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//validateaddress',
  method: 'get',
  data: '?syscoinaddress=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//validateaddress?syscoinaddress=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//validateaddress',
  params: {
  'syscoinaddress' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//validateaddress', params={
  'syscoinaddress': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//validateaddress?syscoinaddress=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//validateaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /validateaddress`

Return information about the given syscoin address.

<h3 id="validateaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|syscoinaddress|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "address": "address",
  "isscript": true,
  "iscompressed": true,
  "ismine": true,
  "isvalid": true,
  "iswatchonly": true,
  "account": "account",
  "pubkey": "pubkey"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="validateaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[ValidateAddressResponse](#schemavalidateaddressresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## verifymessage

<a id="opIdverifymessage"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//verifymessage?syscoinaddress=string&signature=string&message=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//verifymessage?syscoinaddress=string&signature=string&message=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//verifymessage',
  method: 'get',
  data: '?syscoinaddress=string&signature=string&message=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//verifymessage?syscoinaddress=string&signature=string&message=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//verifymessage',
  params: {
  'syscoinaddress' => 'string',
'signature' => 'string',
'message' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//verifymessage', params={
  'syscoinaddress': 'string',  'signature': 'string',  'message': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//verifymessage?syscoinaddress=string&signature=string&message=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//verifymessage", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /verifymessage`

Verify a signed message

<h3 id="verifymessage-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|syscoinaddress|query|string|true|The syscoin address to use for the signature.|
|signature|query|string|true|The signature provided by the signer in base 64 encoding (see signmessage).|
|message|query|string|true|The message that was signed.|

> Example responses

> 200 Response

```json
true
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="verifymessage-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|If the signature is verified or not.|boolean|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## addmultisigaddress

<a id="opIdaddmultisigaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//addmultisigaddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//addmultisigaddress HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//addmultisigaddress',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "nrequired": 0.8008281904610115,
  "keysobject": "keysobject",
  "account": "account"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//addmultisigaddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//addmultisigaddress',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//addmultisigaddress', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//addmultisigaddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//addmultisigaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /addmultisigaddress`

Add a nrequired-to-sign multisignature address to the wallet. Each key is a Syscoin address or hex-encoded public key. If 'account' is specified (DEPRECATED), assign address to that account.

> Body parameter

```json
{
  "nrequired": 0.8008281904610115,
  "keysobject": "keysobject",
  "account": "account"
}
```

<h3 id="addmultisigaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AddMultisigAddressRequest](#schemaaddmultisigaddressrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="addmultisigaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A syscoin address associated with the keys.|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## dumpprivkey

<a id="opIddumpprivkey"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//dumpprivkey?address=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//dumpprivkey?address=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//dumpprivkey',
  method: 'get',
  data: '?address=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//dumpprivkey?address=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//dumpprivkey',
  params: {
  'address' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//dumpprivkey', params={
  'address': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//dumpprivkey?address=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//dumpprivkey", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /dumpprivkey`

Reveals the private key corresponding to 'syscoinaddress'. Then the importprivkey can be used with this output.

<h3 id="dumpprivkey-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|address|query|string|true|The syscoin address for the private key|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="dumpprivkey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## dumpwallet

<a id="opIddumpwallet"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//dumpwallet?filename=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//dumpwallet?filename=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//dumpwallet',
  method: 'get',
  data: '?filename=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//dumpwallet?filename=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//dumpwallet',
  params: {
  'filename' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//dumpwallet', params={
  'filename': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//dumpwallet?filename=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//dumpwallet", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /dumpwallet`

Dumps all wallet keys in a human-readable format.

<h3 id="dumpwallet-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|filename|query|string|true|The filename|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="dumpwallet-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## encryptwallet

<a id="opIdencryptwallet"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//encryptwallet \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//encryptwallet HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//encryptwallet',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "passphrase": "passphrase"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//encryptwallet',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//encryptwallet',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//encryptwallet', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//encryptwallet");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//encryptwallet", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /encryptwallet`

Encrypts the wallet with 'passphrase'. This is for first time encryption. After this, any calls that interact with private keys such as sending or signing will require the passphrase to be set prior the making these calls. Use the walletpassphrase call for this, and then walletlock call. If the wallet is already encrypted, use the walletpassphrasechange call. Note that this will shutdown the server.

> Body parameter

```json
{
  "passphrase": "passphrase"
}
```

<h3 id="encryptwallet-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EncryptWalletRequest](#schemaencryptwalletrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="encryptwallet-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## generate

<a id="opIdgenerate"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//generate?numBlocks=0 \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//generate?numBlocks=0 HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//generate',
  method: 'get',
  data: '?numBlocks=0',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//generate?numBlocks=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//generate',
  params: {
  'numBlocks' => 'number'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//generate', params={
  'numBlocks': '0'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//generate?numBlocks=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//generate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /generate`

Mine up to numblocks blocks immediately (before the RPC call returns).

<h3 id="generate-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|numBlocks|query|number|true|How many blocks are generated immediately.|
|maxtries|query|number|false|How many iterations to try (default = 1000000).|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="generate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="generate-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## generatepublickey

<a id="opIdgeneratepublickey"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//generatepublickey \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//generatepublickey HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//generatepublickey',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//generatepublickey',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//generatepublickey',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//generatepublickey', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//generatepublickey");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//generatepublickey", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /generatepublickey`

Generates a public key for a wallet.

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="generatepublickey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="generatepublickey-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getaccount

<a id="opIdgetaccount"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getaccount?syscoinaddress=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getaccount?syscoinaddress=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getaccount',
  method: 'get',
  data: '?syscoinaddress=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getaccount?syscoinaddress=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getaccount',
  params: {
  'syscoinaddress' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getaccount', params={
  'syscoinaddress': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaccount?syscoinaddress=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getaccount", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getaccount`

DEPRECATED. Returns the account associated with the given address.

<h3 id="getaccount-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|syscoinaddress|query|string|true|The syscoin address for account lookup.|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaccount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getaccountaddress

<a id="opIdgetaccountaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getaccountaddress?account=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getaccountaddress?account=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getaccountaddress',
  method: 'get',
  data: '?account=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getaccountaddress?account=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getaccountaddress',
  params: {
  'account' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getaccountaddress', params={
  'account': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaccountaddress?account=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getaccountaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getaccountaddress`

DEPRECATED. Returns the current Syscoin address for receiving payments to this account.

<h3 id="getaccountaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|account|query|string|true|The account name for the address. It can also be set to the empty string "" to represent the default account. The account does not need to exist, it will be created and a new address created  if there is no account by the given name.|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaccountaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getaddressesbyaccount

<a id="opIdgetaddressesbyaccount"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getaddressesbyaccount?account=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getaddressesbyaccount?account=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getaddressesbyaccount',
  method: 'get',
  data: '?account=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getaddressesbyaccount?account=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getaddressesbyaccount',
  params: {
  'account' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getaddressesbyaccount', params={
  'account': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaddressesbyaccount?account=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getaddressesbyaccount", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getaddressesbyaccount`

DEPRECATED. Returns the list of addresses for the given account.

<h3 id="getaddressesbyaccount-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|account|query|string|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaddressesbyaccount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getaddressesbyaccount-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getbalance

<a id="opIdgetbalance"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getbalance \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getbalance HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getbalance',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getbalance',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getbalance',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getbalance', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getbalance");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getbalance", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getbalance`

If account is not specified, returns the server's total available balance. If account is specified (DEPRECATED), returns the balance in the account. Note that the account "" is not the same as leaving the parameter out. The server total may be different to the balance in the default "" account.

<h3 id="getbalance-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|account|query|string|false|It need "*" for entire wallet|
|minconf|query|number|false|Only include transactions confirmed at least this many times.|
|includeWatchonly|query|boolean|false|Also include balance in watchonly addresses (see 'importaddress')|

> Example responses

> 200 Response

```json
0
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getbalance-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|number|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getnewaddress

<a id="opIdgetnewaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//getnewaddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//getnewaddress HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getnewaddress',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "account": "account"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getnewaddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//getnewaddress',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//getnewaddress', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getnewaddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//getnewaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /getnewaddress`

Returns a new Syscoin address for receiving payments. If 'account' is specified (DEPRECATED), it is added to the address book so payments received with the address will be credited to 'account'.

> Body parameter

```json
{
  "account": "account"
}
```

<h3 id="getnewaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[GetNewAddressRequest](#schemagetnewaddressrequest)|false|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getnewaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getreceivedbyaccount

<a id="opIdgetreceivedbyaccount"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getreceivedbyaccount?account=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getreceivedbyaccount?account=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getreceivedbyaccount',
  method: 'get',
  data: '?account=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getreceivedbyaccount?account=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getreceivedbyaccount',
  params: {
  'account' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getreceivedbyaccount', params={
  'account': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getreceivedbyaccount?account=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getreceivedbyaccount", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getreceivedbyaccount`

Returns the total amount received by addresses with <account> in transactions with at least [minconf] confirmations.

<h3 id="getreceivedbyaccount-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|account|query|string|true|The selected account, may be the default account using "".|
|minconf|query|integer|false|Only include transactions confirmed at least this many times.|
|addlockconf|query|boolean|false|Whether to add 5 confirmations to transactions locked via InstantSend.|

> Example responses

> 200 Response

```json
0
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getreceivedbyaccount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|number|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getreceivedbyaddress

<a id="opIdgetreceivedbyaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getreceivedbyaddress?syscoinaddress=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getreceivedbyaddress?syscoinaddress=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getreceivedbyaddress',
  method: 'get',
  data: '?syscoinaddress=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getreceivedbyaddress?syscoinaddress=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getreceivedbyaddress',
  params: {
  'syscoinaddress' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getreceivedbyaddress', params={
  'syscoinaddress': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getreceivedbyaddress?syscoinaddress=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getreceivedbyaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getreceivedbyaddress`

Returns the total amount received by the given syscoinaddress in transactions with at least minconf confirmations.

<h3 id="getreceivedbyaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|syscoinaddress|query|string|true|The syscoin address for transactions.|
|minconf|query|integer|false|Only include transactions confirmed at least this many times.|
|addlockconf|query|boolean|false|Whether to add 5 confirmations to transactions locked via InstantSend.|

> Example responses

> 200 Response

```json
0
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getreceivedbyaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|number|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## gettransaction

<a id="opIdgettransaction"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//gettransaction?txid=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//gettransaction?txid=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//gettransaction',
  method: 'get',
  data: '?txid=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//gettransaction?txid=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//gettransaction',
  params: {
  'txid' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//gettransaction', params={
  'txid': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//gettransaction?txid=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//gettransaction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /gettransaction`

Get detailed information about in-wallet transaction <txid>

<h3 id="gettransaction-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|txid|query|string|true|The transaction id|
|includeWatchonly|query|boolean|false|Whether to include watchonly addresses in balance calculation and details[]|

> Example responses

> 200 Response

```json
{
  "amount": "amount",
  "blockhash": "blockhash",
  "timereceived": 5.637376656633329,
  "blocktime": 1.4658129805029452,
  "txid": "txid",
  "details": [
    {
      "amount": 2.3021358869347655,
      "address": "address",
      "label": "label",
      "category": "category",
      "account": "account",
      "vout": 7.061401241503109
    },
    {
      "amount": 2.3021358869347655,
      "address": "address",
      "label": "label",
      "category": "category",
      "account": "account",
      "vout": 7.061401241503109
    }
  ],
  "hex": "hex",
  "time": 5.962133916683182,
  "confirmations": 0.8008281904610115,
  "blockindex": 6.027456183070403
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="gettransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Transaction](#schematransaction)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getunconfirmedbalance

<a id="opIdgetunconfirmedbalance"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getunconfirmedbalance \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getunconfirmedbalance HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getunconfirmedbalance',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getunconfirmedbalance',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getunconfirmedbalance',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getunconfirmedbalance', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getunconfirmedbalance");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getunconfirmedbalance", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getunconfirmedbalance`

Returns the server's total unconfirmed balance

> Example responses

> 200 Response

```json
0
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getunconfirmedbalance-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|number|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getwalletinfo

<a id="opIdgetwalletinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getwalletinfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getwalletinfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getwalletinfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getwalletinfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getwalletinfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getwalletinfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getwalletinfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getwalletinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getwalletinfo`

Returns an object containing various wallet state info.

> Example responses

> 200 Response

```json
{
  "walletversion": 0.8008281904610115,
  "balance": 6.027456183070403,
  "txcount": 5.637376656633329,
  "keypoololdest": 2.3021358869347655,
  "unconfirmed_balance": 1.4658129805029452,
  "immature_balance": 5.962133916683182,
  "keypoolsize": 7.061401241503109,
  "unlocked_until": 9.301444243932576,
  "paytxfee": 3.616076749251911
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getwalletinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[WalletInfo](#schemawalletinfo)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## importaddress

<a id="opIdimportaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//importaddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//importaddress HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//importaddress',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "p2sh": true,
  "label": "label",
  "rescan": true,
  "script": "script"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//importaddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//importaddress',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//importaddress', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//importaddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//importaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /importaddress`

Adds a script (in hex) or address that can be watched as if it were in your wallet but cannot be used to spend.

> Body parameter

```json
{
  "p2sh": true,
  "label": "label",
  "rescan": true,
  "script": "script"
}
```

<h3 id="importaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ImportAddressRequest](#schemaimportaddressrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="importaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## importprivkey

<a id="opIdimportprivkey"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//importprivkey \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//importprivkey HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//importprivkey',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "syscoinprivkey": "syscoinprivkey",
  "label": "label",
  "rescan": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//importprivkey',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//importprivkey',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//importprivkey', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//importprivkey");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//importprivkey", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /importprivkey`

Adds a private key (as returned by dumpprivkey) to your wallet.

> Body parameter

```json
{
  "syscoinprivkey": "syscoinprivkey",
  "label": "label",
  "rescan": true
}
```

<h3 id="importprivkey-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ImportPrivKeyRequest](#schemaimportprivkeyrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="importprivkey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## importpubkey

<a id="opIdimportpubkey"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//importpubkey \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//importpubkey HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//importpubkey',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "label": "label",
  "rescan": true,
  "pubkey": "pubkey"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//importpubkey',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//importpubkey',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//importpubkey', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//importpubkey");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//importpubkey", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /importpubkey`

Adds a public key (in hex) that can be watched as if it were in your wallet but cannot be used to spend.

> Body parameter

```json
{
  "label": "label",
  "rescan": true,
  "pubkey": "pubkey"
}
```

<h3 id="importpubkey-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ImportPubKeyRequest](#schemaimportpubkeyrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="importpubkey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## importwallet

<a id="opIdimportwallet"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//importwallet \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//importwallet HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//importwallet',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "filename": "filename"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//importwallet',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//importwallet',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//importwallet', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//importwallet");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//importwallet", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /importwallet`

Imports keys from a wallet dump file (see dumpwallet).

> Body parameter

```json
{
  "filename": "filename"
}
```

<h3 id="importwallet-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ImportWalletRequest](#schemaimportwalletrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="importwallet-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## listaccounts

<a id="opIdlistaccounts"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//listaccounts \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//listaccounts HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//listaccounts',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//listaccounts',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//listaccounts',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//listaccounts', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//listaccounts");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//listaccounts", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /listaccounts`

Returns Object that has account names as keys, account balances as values.

<h3 id="listaccounts-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|minconf|query|integer|false|Only include transactions with at least this many confirmations|
|addlockconf|query|boolean|false|Whether to add 5 confirmations to transactions locked via InstantSend.|
|includeWatchonly|query|boolean|false|Include balances in watchonly addresses (see 'importaddress')|

> Example responses

> 200 Response

```json
{}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="listaccounts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="listaccounts-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## listaddressgroupings

<a id="opIdlistaddressgroupings"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//listaddressgroupings \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//listaddressgroupings HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//listaddressgroupings',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//listaddressgroupings',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//listaddressgroupings',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//listaddressgroupings', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//listaddressgroupings");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//listaddressgroupings", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /listaddressgroupings`

Lists groups of addresses which have had their common ownership made public by common use as inputs or as the resulting change in past transactions

> Example responses

> 200 Response

```json
[
  {
    "amount": 0.8008281904610115,
    "syscoinaddress": "syscoinaddress"
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="listaddressgroupings-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="listaddressgroupings-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[AddressGrouping](#schemaaddressgrouping)]|false|none|none|
|» syscoinaddress|string|false|none|The syscoin address|
|» amount|number|false|none|The amount in SYS|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## listreceivedbyaccount

<a id="opIdlistreceivedbyaccount"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//listreceivedbyaccount \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//listreceivedbyaccount HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//listreceivedbyaccount',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//listreceivedbyaccount',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//listreceivedbyaccount',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//listreceivedbyaccount', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//listreceivedbyaccount");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//listreceivedbyaccount", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /listreceivedbyaccount`

List balances by account.

<h3 id="listreceivedbyaccount-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|minconf|query|number|false|Only include transactions confirmed at least this many times.|
|addlockconf|query|boolean|false|Whether to add 5 confirmations to transactions locked via InstantSend.|
|includeempty|query|boolean|false|Whether to include accounts that haven't received any payments.|
|includeWatchonly|query|boolean|false|Whether to include watchonly addresses (see 'importaddress').|

> Example responses

> 200 Response

```json
[
  {
    "amount": 0.8008281904610115,
    "involvesWatchonly": true,
    "label": "label",
    "confirmations": 6.027456183070403,
    "account": "account"
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="listreceivedbyaccount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="listreceivedbyaccount-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Account](#schemaaccount)]|false|none|none|
|» involvesWatchonly|boolean|false|none|Only returned if imported addresses were involved in transaction|
|» account|string|false|none|The account name of the receiving account|
|» amount|number|false|none|The total amount received by addresses with this account|
|» confirmations|number|false|none|The number of confirmations of the most recent transaction included|
|» label|string|false|none|A comment for the address/transaction, if any|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## listreceivedbyaddress

<a id="opIdlistreceivedbyaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//listreceivedbyaddress \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//listreceivedbyaddress HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//listreceivedbyaddress',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//listreceivedbyaddress',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//listreceivedbyaddress',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//listreceivedbyaddress', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//listreceivedbyaddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//listreceivedbyaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /listreceivedbyaddress`

List balances by receiving address.

<h3 id="listreceivedbyaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|minconf|query|integer|false|Only include transactions confirmed at least this many times.|
|addlockconf|query|boolean|false|Whether to add 5 confirmations to transactions locked via InstantSend.|
|includeempty|query|boolean|false|Whether to include accounts that haven't received any payments.|
|includeWatchonly|query|boolean|false|Whether to include watchonly addresses (see 'importaddress').|

> Example responses

> 200 Response

```json
[
  {
    "amount": 0.8008281904610115,
    "address": "address",
    "v2address": "v2address",
    "ismine": true,
    "label": "label",
    "confirmations": 6.027456183070403,
    "account": "account",
    "txids": [
      "txids",
      "txids"
    ]
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="listreceivedbyaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="listreceivedbyaddress-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ListReceivedByAddress](#schemalistreceivedbyaddress)]|false|none|none|
|» address|string|false|none|none|
|» v2address|string|false|none|none|
|» account|string|false|none|none|
|» amount|number|false|none|none|
|» confirmations|number|false|none|none|
|» label|string|false|none|none|
|» txids|[string]|false|none|none|
|» ismine|boolean|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## listsinceblock

<a id="opIdlistsinceblock"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//listsinceblock \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//listsinceblock HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//listsinceblock',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//listsinceblock',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//listsinceblock',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//listsinceblock', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//listsinceblock");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//listsinceblock", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /listsinceblock`

Get all transactions in blocks since block [blockhash], or all transactions if omitted

<h3 id="listsinceblock-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|blockhash|query|string|false|The block hash to list transactions since|
|includeWatchonly|query|boolean|false|Whether to include watchonly addresses (see 'importaddress').|
|target-confirmations|query|number|false|none|

> Example responses

> 200 Response

```json
[
  {
    "lastblock": "lastblock",
    "transactions": [
      {
        "amount": 0.8008281904610115,
        "address": "address",
        "fee": 1.4658129805029452,
        "txid": "txid",
        "label": "label",
        "confirmations": 5.962133916683182,
        "vout": 6.027456183070403,
        "blockhash": "blockhash",
        "timereceived": 9.301444243932576,
        "blocktime": 2.3021358869347655,
        "comment": "comment",
        "time": 7.061401241503109,
        "to": "to",
        "category": "category",
        "blockindex": 5.637376656633329,
        "account": "account"
      },
      {
        "amount": 0.8008281904610115,
        "address": "address",
        "fee": 1.4658129805029452,
        "txid": "txid",
        "label": "label",
        "confirmations": 5.962133916683182,
        "vout": 6.027456183070403,
        "blockhash": "blockhash",
        "timereceived": 9.301444243932576,
        "blocktime": 2.3021358869347655,
        "comment": "comment",
        "time": 7.061401241503109,
        "to": "to",
        "category": "category",
        "blockindex": 5.637376656633329,
        "account": "account"
      }
    ]
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="listsinceblock-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="listsinceblock-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[ListSinceBlockResponse](#schemalistsinceblockresponse)]|false|none|none|
|» transactions|[[SinceBlockTransactionEntry](#schemasinceblocktransactionentry)]|false|none|none|
|»» account|string|false|none|DEPRECATED. The account name associated with the transaction. Will be "" for the default account.|
|»» address|string|false|none|The syscoin address of the transaction. Not present for move transactions (category = move).|
|»» category|string|false|none|The transaction category. 'send' has negative amounts, 'receive' has positive amounts.|
|»» amount|number|false|none|The amount in SYS. This is negative for the 'send' category, and for the 'move' category for moves outbound. It is positive for the 'receive' category, and for the 'move' category for inbound funds.|
|»» vout|number|false|none|the vout value|
|»» fee|number|false|none|The amount of the fee in SYS. This is negative and only available for the 'send' category of transactions.|
|»» confirmations|number|false|none|The number of confirmations for the transaction. Available for 'send' and 'receive' category of transactions.|
|»» blockhash|string|false|none|The block hash containing the transaction. Available for 'send' and 'receive' category of transactions.|
|»» blockindex|number|false|none|The block index containing the transaction. Available for 'send' and 'receive' category of transactions.|
|»» blocktime|number|false|none|The block time in seconds since epoch (1 Jan 1970 GMT).|
|»» txid|string|false|none|The transaction id. Available for 'send' and 'receive' category of transactions.|
|»» time|number|false|none|The transaction time in seconds since epoch (Jan 1 1970 GMT).|
|»» timereceived|number|false|none|The time received in seconds since epoch (Jan 1 1970 GMT). Available for 'send' and 'receive' category of transactions.|
|»» comment|string|false|none|If a comment is associated with the transaction.|
|»» label|string|false|none|A comment for the address/transaction, if any|
|»» to|string|false|none|If a comment to is associated with the transaction.|
|» lastblock|string|false|none|The hash of the last block|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## listunspent

<a id="opIdlistunspent"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//listunspent \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//listunspent HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//listunspent',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//listunspent',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//listunspent',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//listunspent', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//listunspent");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//listunspent", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /listunspent`

Returns array of unspent transaction outputs with between minconf and maxconf (inclusive) confirmations. Optionally filter to only include txouts paid to specified addresses. Results are an array of Objects, each of which has: {txid, vout, scriptPubKey, amount, confirmations}

<h3 id="listunspent-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|minconf|query|integer|false|The minimum confirmations to filter.|
|maxconf|query|number|false|The maximum confirmations to filter|
|adresses|query|number|false|A json array of syscoin addresses to filter|

> Example responses

> 200 Response

```json
[
  {
    "scriptPubKey": "scriptPubKey",
    "amount": 6.027456183070403,
    "ps_rounds": 5.962133916683182,
    "spendable": true,
    "solvable": true,
    "address": "address",
    "txid": "txid",
    "confirmations": 1.4658129805029452,
    "account": "account",
    "vout": 0.8008281904610115
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="listunspent-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="listunspent-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[UnspentListEntry](#schemaunspentlistentry)]|false|none|none|
|» txid|string|false|none|The transaction id|
|» vout|number|false|none|The vout value|
|» address|string|false|none|The syscoin address|
|» account|string|false|none|DEPRECATED. The associated account, or "" for the default account|
|» scriptPubKey|string|false|none|The script key|
|» amount|number|false|none|The transaction amount in SYS|
|» confirmations|number|false|none|The number of confirmations|
|» ps_rounds|number|false|none|The number of PS round|
|» spendable|boolean|false|none|Whether we have the private keys to spend this output|
|» solvable|boolean|false|none|Whether we know how to spend this output, ignoring the lack of keys|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## listtransactions

<a id="opIdlisttransactions"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//listtransactions \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//listtransactions HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//listtransactions',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//listtransactions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//listtransactions',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//listtransactions', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//listtransactions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//listtransactions", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /listtransactions`

Returns up to 'count' most recent transactions skipping the first 'from' transactions for account 'account'.

<h3 id="listtransactions-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|account|query|string|false|The account name. Should be "*".|
|count|query|number|false|The number of transactions to return|
|from|query|number|false|The number of transactions to skip|
|includeWatchonly|query|boolean|false|Include transactions to watchonly addresses (see 'importaddress')|

> Example responses

> 200 Response

```json
[
  {
    "amount": 0.8008281904610115,
    "address": "address",
    "instantlock": true,
    "bip125-replaceable": "bip125-replaceable",
    "fee": 1.4658129805029452,
    "txid": "txid",
    "label": "label",
    "otheraccount": "otheraccount",
    "confirmations": 5.962133916683182,
    "vout": 6.027456183070403,
    "blockhash": "blockhash",
    "timereceived": 9.301444243932576,
    "trusted": true,
    "blocktime": 2.3021358869347655,
    "comment": "comment",
    "time": 7.061401241503109,
    "category": "category",
    "blockindex": 5.637376656633329,
    "account": "account"
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="listtransactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="listtransactions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[TransactionListEntry](#schematransactionlistentry)]|false|none|none|
|» account|string|false|none|DEPRECATED. The account name associated with the transaction. It will be "" for the default account.|
|» address|string|false|none|The syscoin address of the transaction. Not present for move transactions (category = move).|
|» category|string|false|none|The transaction category. 'move' is a local (off blockchain) transaction between accounts, and not associated with an address, transaction id or block. 'send' and 'receive' transactions are associated with an address, transaction id and block details. Example values&#58; 'send|receive|move'|
|» amount|number|false|none|The amount in SYS. This is negative for the 'send' category, and for the 'move' category for moves outbound. It is positive for the 'receive' category, and for the 'move' category for inbound funds.|
|» vout|number|false|none|the vout value|
|» fee|number|false|none|The amount of the fee in SYS. This is negative and only available for the 'send' category of transactions.|
|» instantlock|boolean|false|none|Current transaction lock state. Available for 'send' and 'receive' category of transactions.|
|» confirmations|number|false|none|The number of blockchain confirmations for the transaction. Available for 'send' and 'receive' category of transactions. Negative confirmations indicate the transation conflicts with the block chain|
|» trusted|boolean|false|none|Whether we consider the outputs of this unconfirmed transaction safe to spend.|
|» blockhash|string|false|none|The block hash containing the transaction. Available for 'send' and 'receive' category of transactions.|
|» blockindex|number|false|none|The index of the transaction in the block that includes it. Available for 'send' and 'receive' category of transactions.|
|» blocktime|number|false|none|The block time in seconds since epoch (1 Jan 1970 GMT).|
|» txid|string|false|none|The transaction id. Available for 'send' and 'receive' category of transactions.|
|» time|number|false|none|The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).|
|» timereceived|number|false|none|The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available for 'send' and 'receive' category of transactions.|
|» comment|string|false|none|If a comment is associated with the transaction.|
|» label|string|false|none|A comment for the address/transaction, if any|
|» otheraccount|string|false|none|For the 'move' category of transactions, the account the funds came from (for receiving funds, positive amounts), or went to (for sending funds, negative amounts).|
|» bip125-replaceable|string|false|none|Whether this transaction could be replaced due to BIP125 (replace-by-fee); may be unknown for unconfirmed transactions not in the mempool. Example&#58; "yes|no|unknown"|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## move

<a id="opIdmove"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//move \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//move HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//move',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "fromaccount": "fromaccount",
  "amount": 0.8008281904610115,
  "minconf": "minconf",
  "toaccount": "toaccount",
  "comment": "comment"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//move',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//move',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//move', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//move");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//move", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /move`

DEPRECATED. Move a specified amount from one account in your wallet to another.

> Body parameter

```json
{
  "fromaccount": "fromaccount",
  "amount": 0.8008281904610115,
  "minconf": "minconf",
  "toaccount": "toaccount",
  "comment": "comment"
}
```

<h3 id="move-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MoveRequest](#schemamoverequest)|true|none|

> Example responses

> 200 Response

```json
true
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="move-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|boolean|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## sendfrom

<a id="opIdsendfrom"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//sendfrom \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//sendfrom HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//sendfrom',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "fromaccount": "fromaccount",
  "amount": 0.8008281904610115,
  "minconf": 6,
  "addlockconf": false,
  "commentto": "commentto",
  "comment": "comment",
  "tosyscoinaddress": "tosyscoinaddress"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//sendfrom',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//sendfrom',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//sendfrom', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//sendfrom");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//sendfrom", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /sendfrom`

DEPRECATED (use sendtoaddress). Sent an amount from an account to a syscoin address. The amount is a real and is rounded to the nearest 0.00000001. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "fromaccount": "fromaccount",
  "amount": 0.8008281904610115,
  "minconf": 6,
  "addlockconf": false,
  "commentto": "commentto",
  "comment": "comment",
  "tosyscoinaddress": "tosyscoinaddress"
}
```

<h3 id="sendfrom-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SendFromRequest](#schemasendfromrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="sendfrom-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## sendmany

<a id="opIdsendmany"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//sendmany \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//sendmany HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//sendmany',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "fromaccount": "fromaccount",
  "use_ps": false,
  "amounts": "amounts",
  "minconf": 0,
  "addlockconf": false,
  "use_is": false,
  "comment": "comment",
  "subtractfeefromamount": "subtractfeefromamount"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//sendmany',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//sendmany',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//sendmany', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//sendmany");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//sendmany", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /sendmany`

Send multiple times. Amounts are double-precision floating point numbers. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "fromaccount": "fromaccount",
  "use_ps": false,
  "amounts": "amounts",
  "minconf": 0,
  "addlockconf": false,
  "use_is": false,
  "comment": "comment",
  "subtractfeefromamount": "subtractfeefromamount"
}
```

<h3 id="sendmany-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SendManyRequest](#schemasendmanyrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="sendmany-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## sendtoaddress

<a id="opIdsendtoaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//sendtoaddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//sendtoaddress HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//sendtoaddress',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "use_ps": false,
  "amount": 0.8008281904610115,
  "syscoinaddress": "syscoinaddress",
  "use_is": false,
  "commentto": "commentto",
  "comment": "comment",
  "subtractfeefromamount": false
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//sendtoaddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//sendtoaddress',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//sendtoaddress', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//sendtoaddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//sendtoaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /sendtoaddress`

Send an amount to a given address. The amount is a real and is rounded to the nearest 0.00000001. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "use_ps": false,
  "amount": 0.8008281904610115,
  "syscoinaddress": "syscoinaddress",
  "use_is": false,
  "commentto": "commentto",
  "comment": "comment",
  "subtractfeefromamount": false
}
```

<h3 id="sendtoaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SendToAddressRequest](#schemasendtoaddressrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="sendtoaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## signmessage

<a id="opIdsignmessage"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//signmessage \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//signmessage HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//signmessage',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "syscoinaddress": "syscoinaddress",
  "message": "message"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//signmessage',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//signmessage',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//signmessage', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//signmessage");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//signmessage", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /signmessage`

Sign a message with the private key of an address. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "syscoinaddress": "syscoinaddress",
  "message": "message"
}
```

<h3 id="signmessage-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SignMessageRequest](#schemasignmessagerequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="signmessage-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## walletlock

<a id="opIdwalletlock"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//walletlock \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//walletlock HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//walletlock',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//walletlock',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//walletlock',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//walletlock', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//walletlock");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//walletlock", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /walletlock`

Removes the wallet encryption key from memory, locking the wallet. After calling this method, you will need to call walletpassphrase again before being able to call any methods which require the wallet to be unlocked.

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="walletlock-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## walletpassphrase

<a id="opIdwalletpassphrase"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//walletpassphrase \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//walletpassphrase HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//walletpassphrase',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "passphrase": "passphrase",
  "timeout": 0.8008281904610115
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//walletpassphrase',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//walletpassphrase',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//walletpassphrase', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//walletpassphrase");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//walletpassphrase", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /walletpassphrase`

Stores the wallet decryption key in memory for 'timeout' seconds. This is needed prior to performing transactions related to private keys such as sending syscoins

> Body parameter

```json
{
  "passphrase": "passphrase",
  "timeout": 0.8008281904610115
}
```

<h3 id="walletpassphrase-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WalletPassphraseRequest](#schemawalletpassphraserequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="walletpassphrase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## walletpassphrasechange

<a id="opIdwalletpassphrasechange"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//walletpassphrasechange \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//walletpassphrasechange HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//walletpassphrasechange',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "oldpassphrase": "oldpassphrase",
  "newpassphrase": "newpassphrase"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//walletpassphrasechange',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//walletpassphrasechange',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//walletpassphrasechange', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//walletpassphrasechange");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//walletpassphrasechange", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /walletpassphrasechange`

Changes the wallet passphrase from 'oldpassphrase' to 'newpassphrase'.

> Body parameter

```json
{
  "oldpassphrase": "oldpassphrase",
  "newpassphrase": "newpassphrase"
}
```

<h3 id="walletpassphrasechange-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WalletPassphraseChangeRequest](#schemawalletpassphrasechangerequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="walletpassphrasechange-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## syscoindecoderawtransaction

<a id="opIdsyscoindecoderawtransaction"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//syscoindecoderawtransaction?hexstring=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//syscoindecoderawtransaction?hexstring=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//syscoindecoderawtransaction',
  method: 'get',
  data: '?hexstring=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//syscoindecoderawtransaction?hexstring=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//syscoindecoderawtransaction',
  params: {
  'hexstring' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//syscoindecoderawtransaction', params={
  'hexstring': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//syscoindecoderawtransaction?hexstring=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//syscoindecoderawtransaction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /syscoindecoderawtransaction`

Decode raw syscoin transaction (serialized, hex-encoded) and display information pertaining to the service that is included in the transactiion data output(OP_RETURN)

<h3 id="syscoindecoderawtransaction-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|hexstring|query|string|true|The transaction hex string.|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="syscoindecoderawtransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getaddressbalance

<a id="opIdgetaddressbalance"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getaddressbalance?addresses=string \
  -H 'Accept: application/json'

```

```http
GET http://localhost:8001//getaddressbalance?addresses=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json'

};

$.ajax({
  url: 'http://localhost:8001//getaddressbalance',
  method: 'get',
  data: '?addresses=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json'

};

fetch('http://localhost:8001//getaddressbalance?addresses=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://localhost:8001//getaddressbalance',
  params: {
  'addresses' => 'array[string]'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8001//getaddressbalance', params={
  'addresses': [
  "string"
]
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaddressbalance?addresses=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getaddressbalance", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getaddressbalance`

get address balance 

<h3 id="getaddressbalance-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|addresses|query|array[string]|true|none|

> Example responses

> 200 Response

```json
{
  "balance": "balance",
  "received": "received"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaddressbalance-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[getAddressBalanceResponse](#schemagetaddressbalanceresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="success">
This operation does not require authentication
</aside>

## getaddressdeltas

<a id="opIdgetaddressdeltas"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getaddressdeltas?addresses=string&start=0&end=0 \
  -H 'Accept: application/json'

```

```http
GET http://localhost:8001//getaddressdeltas?addresses=string&start=0&end=0 HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json'

};

$.ajax({
  url: 'http://localhost:8001//getaddressdeltas',
  method: 'get',
  data: '?addresses=string&start=0&end=0',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json'

};

fetch('http://localhost:8001//getaddressdeltas?addresses=string&start=0&end=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://localhost:8001//getaddressdeltas',
  params: {
  'addresses' => 'array[string]',
'start' => 'number',
'end' => 'number'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8001//getaddressdeltas', params={
  'addresses': [
  "string"
],  'start': '0',  'end': '0'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaddressdeltas?addresses=string&start=0&end=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getaddressdeltas", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getaddressdeltas`

getaddressdeltas

<h3 id="getaddressdeltas-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|addresses|query|array[string]|true|none|
|start|query|number|true|none|
|end|query|number|true|none|

> Example responses

> 200 Response

```json
[
  {
    "address": "address",
    "txid": "txid",
    "index": 0.8008281904610115,
    "satoshis": "satoshis",
    "height": 6.027456183070403
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaddressdeltas-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getaddressdeltas-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[getAddressDeltasResponseObject](#schemagetaddressdeltasresponseobject)]|false|none|none|
|» satoshis|string|false|none|The difference of satoshis|
|» txid|string|false|none|The related txid|
|» index|number|false|none|The related input or output index|
|» height|number|false|none|The block height|
|» address|string|false|none|The base58check encoded address|

<aside class="success">
This operation does not require authentication
</aside>

## getaddressmempool

<a id="opIdgetaddressmempool"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getaddressmempool?addresses=string \
  -H 'Accept: application/json'

```

```http
GET http://localhost:8001//getaddressmempool?addresses=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json'

};

$.ajax({
  url: 'http://localhost:8001//getaddressmempool',
  method: 'get',
  data: '?addresses=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json'

};

fetch('http://localhost:8001//getaddressmempool?addresses=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://localhost:8001//getaddressmempool',
  params: {
  'addresses' => 'array[string]'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8001//getaddressmempool', params={
  'addresses': [
  "string"
]
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaddressmempool?addresses=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getaddressmempool", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getaddressmempool`

getaddressdeltas

<h3 id="getaddressmempool-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|addresses|query|array[string]|true|none|

> Example responses

> 200 Response

```json
[
  {
    "address": "address",
    "prevout": "prevout",
    "txid": "txid",
    "index": 0.8008281904610115,
    "prevtxid": "prevtxid",
    "satoshis": "satoshis",
    "height": 6.027456183070403,
    "timestamp": 1.4658129805029452
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaddressmempool-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getaddressmempool-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[getAddressMemPoolResponseObject](#schemagetaddressmempoolresponseobject)]|false|none|none|
|» satoshis|string|false|none|The difference of satoshis|
|» txid|string|false|none|The related txid|
|» index|number|false|none|The related input or output index|
|» height|number|false|none|The block height|
|» address|string|false|none|The base58check encoded address|
|» timestamp|number|false|none|The time the transaction entered the mempool (seconds)|
|» prevtxid|string|false|none|The previous txid (if spending)|
|» prevout|string|false|none|The previous transaction output index (if spending)|

<aside class="success">
This operation does not require authentication
</aside>

## syscoinsendrawtransaction

<a id="opIdsyscoinsendrawtransaction"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//syscoinsendrawtransaction \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//syscoinsendrawtransaction HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//syscoinsendrawtransaction',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "instantsend": true,
  "allowhighfees": true,
  "hexstring": "hexstring"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//syscoinsendrawtransaction',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//syscoinsendrawtransaction',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//syscoinsendrawtransaction', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//syscoinsendrawtransaction");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//syscoinsendrawtransaction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /syscoinsendrawtransaction`

Signed raw transaction (serialized, hex-encoded) sent out to the network.

> Body parameter

```json
{
  "instantsend": true,
  "allowhighfees": true,
  "hexstring": "hexstring"
}
```

<h3 id="syscoinsendrawtransaction-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SendRawTransactionRequest](#schemasendrawtransactionrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "txid": "txid"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="syscoinsendrawtransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[SendRawTransactionResponse](#schemasendrawtransactionresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## fundrawtransaction

<a id="opIdfundrawtransaction"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//fundrawtransaction \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//fundrawtransaction HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//fundrawtransaction',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "hexstring": "hexstring",
  "watching": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//fundrawtransaction',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//fundrawtransaction',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//fundrawtransaction', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//fundrawtransaction");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//fundrawtransaction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /fundrawtransaction`

Add inputs to a transaction until it has enough in value to meet its out value.

> Body parameter

```json
{
  "hexstring": "hexstring",
  "watching": true
}
```

<h3 id="fundrawtransaction-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[FundRawTransactionRequest](#schemafundrawtransactionrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="fundrawtransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## lockunspent

<a id="opIdlockunspent"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//lockunspent \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//lockunspent HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//lockunspent',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "unlock": true,
  "transactions": [
    {
      "txid": "txid",
      "vout": 0.8008281904610115
    },
    {
      "txid": "txid",
      "vout": 0.8008281904610115
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//lockunspent',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//lockunspent',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//lockunspent', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//lockunspent");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//lockunspent", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /lockunspent`

Updates list of temporarily unspendable outputs.

> Body parameter

```json
{
  "unlock": true,
  "transactions": [
    {
      "txid": "txid",
      "vout": 0.8008281904610115
    },
    {
      "txid": "txid",
      "vout": 0.8008281904610115
    }
  ]
}
```

<h3 id="lockunspent-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[LockUnspentRequest](#schemalockunspentrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="lockunspent-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## signrawtransaction

<a id="opIdsignrawtransaction"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//signrawtransaction \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//signrawtransaction HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//signrawtransaction',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "hexstring": "hexstring"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//signrawtransaction',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//signrawtransaction',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//signrawtransaction', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//signrawtransaction");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//signrawtransaction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /signrawtransaction`

Sign inputs for raw transaction (serialized, hex-encoded).

> Body parameter

```json
{
  "hexstring": "hexstring"
}
```

<h3 id="signrawtransaction-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SignRawTransactionRequest](#schemasignrawtransactionrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "hex": "hex",
  "complete": true,
  "errors": [
    {
      "sequence": 6.027456183070403,
      "scriptSig": "scriptSig",
      "txid": "txid",
      "error": "error",
      "vout": 0.8008281904610115
    },
    {
      "sequence": 6.027456183070403,
      "scriptSig": "scriptSig",
      "txid": "txid",
      "error": "error",
      "vout": 0.8008281904610115
    }
  ]
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="signrawtransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[SignRawTransactionResponse](#schemasignrawtransactionresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getblocktemplate

<a id="opIdgetblocktemplate"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getblocktemplate \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getblocktemplate HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getblocktemplate',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getblocktemplate',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getblocktemplate',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getblocktemplate', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getblocktemplate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getblocktemplate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getblocktemplate`

Add inputs to a transaction until it has enough in value to meet its out value.

> Example responses

> 200 Response

```json
{}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getblocktemplate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getblocktemplate-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getgenerate

<a id="opIdgetgenerate"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getgenerate \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getgenerate HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getgenerate',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getgenerate',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getgenerate',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getgenerate', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getgenerate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getgenerate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getgenerate`

Returns true if generation is ON, otherwise false

> Example responses

> 200 Response

```json
true
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getgenerate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|boolean|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## setgenerate

<a id="opIdsetgenerate"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//setgenerate?generate=true \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//setgenerate?generate=true HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//setgenerate',
  method: 'get',
  data: '?generate=true',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//setgenerate?generate=true',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//setgenerate',
  params: {
  'generate' => 'boolean'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//setgenerate', params={
  'generate': 'true'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//setgenerate?generate=true");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//setgenerate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /setgenerate`

Set 'generate' true or false to turn generation on or off.
Generation is limited to 'genproclimit' processors, -1 is unlimited.
See the getgenerate call for the current setting

<h3 id="setgenerate-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|generate|query|boolean|true|none|
|genproclimit|query|number|false|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="setgenerate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## setnetworkactive

<a id="opIdsetnetworkactive"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//setnetworkactive?state=true \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//setnetworkactive?state=true HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//setnetworkactive',
  method: 'get',
  data: '?state=true',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//setnetworkactive?state=true',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//setnetworkactive',
  params: {
  'state' => 'boolean'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//setnetworkactive', params={
  'state': 'true'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//setnetworkactive?state=true");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//setnetworkactive", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /setnetworkactive`

Set 'networkactive' true or false

<h3 id="setnetworkactive-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|state|query|boolean|true|none|

> Example responses

> 200 Response

```json
true
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="setnetworkactive-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|boolean|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## mnsync

<a id="opIdmnsync"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//mnsync?command=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//mnsync?command=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//mnsync',
  method: 'get',
  data: '?command=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//mnsync?command=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//mnsync',
  params: {
  'command' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//mnsync', params={
  'command': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//mnsync?command=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//mnsync", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /mnsync`

Returns the sync status, updates to the next step or resets it entirely.

<h3 id="mnsync-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|command|query|string|true|'status' - Sync status|

#### Detailed descriptions

**command**: 'status' - Sync status
'next' - Update to next step
'reset' - Reset it entirely

> Example responses

> default Response

```json
{
  "message": "string"
}
```

<h3 id="mnsync-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## dumphdinfo

<a id="opIddumphdinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//dumphdinfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//dumphdinfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//dumphdinfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//dumphdinfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//dumphdinfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//dumphdinfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//dumphdinfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//dumphdinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /dumphdinfo`

Returns an object containing sensitive private info about this HD wallet.

> Example responses

> 200 Response

```json
{
  "hdseed": "hdseed",
  "mnemonicpassphrase": "mnemonicpassphrase",
  "mnemonic": "mnemonic"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="dumphdinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DumpHdInfoResponse](#schemadumphdinforesponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## debug

<a id="opIddebug"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//debug?command=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//debug?command=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//debug',
  method: 'get',
  data: '?command=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//debug?command=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//debug',
  params: {
  'command' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//debug', params={
  'command': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//debug?command=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//debug", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /debug`

Change debug category on the fly. Specify single category or use comma to specify many.

<h3 id="debug-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|command|query|string|true|0|1|addrman|alert|bench|coindb|db|lock|rand|

#### Detailed descriptions

**command**: 0|1|addrman|alert|bench|coindb|db|lock|rand
|rpc|selectcoins|mempool|mempoolrej|net|proxy
|prune|http|libevent|tor|zmq|syscoin|privatesend|instantsend
|masternode|spork|keepass|mnpayments|gobject

> Example responses

> default Response

```json
{
  "message": "string"
}
```

<h3 id="debug-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## instantsendtoaddress

<a id="opIdinstantsendtoaddress"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//instantsendtoaddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//instantsendtoaddress HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//instantsendtoaddress',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "syscoinaddress": "string",
  "amount": 0,
  "comment": "string",
  "comment-to": "string",
  "subtractfeefromamount": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//instantsendtoaddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//instantsendtoaddress',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//instantsendtoaddress', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//instantsendtoaddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//instantsendtoaddress", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /instantsendtoaddress`

Send multiple times. Amounts are double-precision floating point numbers. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "syscoinaddress": "string",
  "amount": 0,
  "comment": "string",
  "comment-to": "string",
  "subtractfeefromamount": true
}
```

<h3 id="instantsendtoaddress-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[instantSendToAddressRequest](#schemainstantsendtoaddressrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="instantsendtoaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getaddresstxids

<a id="opIdgetaddresstxids"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getaddresstxids?addresses=string&start=0&end=0 \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getaddresstxids?addresses=string&start=0&end=0 HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getaddresstxids',
  method: 'get',
  data: '?addresses=string&start=0&end=0',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getaddresstxids?addresses=string&start=0&end=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getaddresstxids',
  params: {
  'addresses' => 'array[string]',
'start' => 'number',
'end' => 'number'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getaddresstxids', params={
  'addresses': [
  "string"
],  'start': '0',  'end': '0'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaddresstxids?addresses=string&start=0&end=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getaddresstxids", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getaddresstxids`

Get address transaction ids

<h3 id="getaddresstxids-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|addresses|query|array[string]|true|none|
|start|query|number|true|none|
|end|query|number|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaddresstxids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getaddresstxids-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getaddressutxos

<a id="opIdgetaddressutxos"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//getaddressutxos \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//getaddressutxos HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getaddressutxos',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "addresses": [
    "addresses",
    "addresses"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getaddressutxos',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//getaddressutxos',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//getaddressutxos', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getaddressutxos");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//getaddressutxos", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /getaddressutxos`

Returns all unspent outputs for addresses or aliases

> Body parameter

```json
{
  "addresses": [
    "addresses",
    "addresses"
  ]
}
```

<h3 id="getaddressutxos-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[GetAddressUTXOsRequest](#schemagetaddressutxosrequest)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "outputIndex": 0.8008281904610115,
    "address": "address",
    "txid": "txid",
    "script": "script",
    "satoshis": 6.027456183070403,
    "height": 1.4658129805029452
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getaddressutxos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getaddressutxos-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[GetAddressUTXOsEntry](#schemagetaddressutxosentry)]|false|none|none|
|» address|string|false|none|none|
|» txid|string|false|none|none|
|» outputIndex|number|false|none|none|
|» script|string|false|none|none|
|» satoshis|number|false|none|none|
|» height|number|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getblockhashes

<a id="opIdgetblockhashes"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getblockhashes?high=0&low=0 \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getblockhashes?high=0&low=0 HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getblockhashes',
  method: 'get',
  data: '?high=0&low=0',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getblockhashes?high=0&low=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getblockhashes',
  params: {
  'high' => 'number',
'low' => 'number'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getblockhashes', params={
  'high': '0',  'low': '0'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getblockhashes?high=0&low=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getblockhashes", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getblockhashes`

Returns array of hashes of blocks within the timestamp range provided.

<h3 id="getblockhashes-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|high|query|number|true|none|
|low|query|number|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getblockhashes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getblockhashes-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getblockheaders

<a id="opIdgetblockheaders"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getblockheaders?hash=string&count=0 \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getblockheaders?hash=string&count=0 HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getblockheaders',
  method: 'get',
  data: '?hash=string&count=0',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getblockheaders?hash=string&count=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getblockheaders',
  params: {
  'hash' => 'string',
'count' => 'number'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getblockheaders', params={
  'hash': 'string',  'count': '0'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getblockheaders?hash=string&count=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getblockheaders", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getblockheaders`

Returns an array of items with information about <count> blockheaders starting from <hash>.
If verbose is false, each item is a string that is serialized, hex-encoded data for a single blockheader.
If verbose is true, each item is an Object with information about a single blockheader.

<h3 id="getblockheaders-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|hash|query|string|true|none|
|count|query|number|true|none|
|verbose|query|boolean|false|none|

> Example responses

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getblockheaders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getchaintips

<a id="opIdgetchaintips"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getchaintips \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getchaintips HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getchaintips',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getchaintips',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getchaintips',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getchaintips', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getchaintips");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getchaintips", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getchaintips`

Returns chain tips

> Example responses

> 200 Response

```json
[
  {
    "difficulty": 6.027456183070403,
    "chainwork": "chainwork",
    "branchlen": 1.4658129805029452,
    "hash": "hash",
    "height": 0.8008281904610115,
    "status": "status"
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getchaintips-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="getchaintips-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[GetChainTipsResponse](#schemagetchaintipsresponse)]|false|none|none|
|» height|number|false|none|none|
|» hash|string|false|none|none|
|» difficulty|number|false|none|none|
|» chainwork|string|false|none|none|
|» branchlen|number|false|none|none|
|» status|string|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getspentinfo

<a id="opIdgetspentinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getspentinfo?txid=string&index=0 \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getspentinfo?txid=string&index=0 HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getspentinfo',
  method: 'get',
  data: '?txid=string&index=0',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getspentinfo?txid=string&index=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getspentinfo',
  params: {
  'txid' => 'string',
'index' => 'number'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getspentinfo', params={
  'txid': 'string',  'index': '0'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getspentinfo?txid=string&index=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getspentinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getspentinfo`

Returns the txid and index where an output is spent

<h3 id="getspentinfo-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|txid|query|string|true|none|
|index|query|number|true|none|

> Example responses

> 200 Response

```json
{
  "txid": "txid",
  "index": 0.8008281904610115
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getspentinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[GetSpentInfoResponse](#schemagetspentinforesponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getgovernanceinfo

<a id="opIdgetgovernanceinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getgovernanceinfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getgovernanceinfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getgovernanceinfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getgovernanceinfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getgovernanceinfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getgovernanceinfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getgovernanceinfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getgovernanceinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getgovernanceinfo`

Returns an object containing governance parameters

> Example responses

> 200 Response

```json
{
  "nextsuperblock": 2.3021358869347655,
  "proposalfee": 1.4658129805029452,
  "lastsuperblock": 5.637376656633329,
  "masternodewatchdogmaxseconds": 6.027456183070403,
  "governanceminquorum": 0.8008281904610115,
  "superblockcycle": 5.962133916683182
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getgovernanceinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[GovernanceInfoResponse](#schemagovernanceinforesponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getpoolinfo

<a id="opIdgetpoolinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getpoolinfo \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getpoolinfo HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getpoolinfo',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getpoolinfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getpoolinfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getpoolinfo', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getpoolinfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getpoolinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getpoolinfo`

Returns an object containing mixing pool related information

> Example responses

> 200 Response

```json
{
  "mixing_mode": "mixing_mode",
  "entries": 6.027456183070403,
  "warnings": "warnings",
  "state": "state",
  "addr": "addr",
  "queue": 0.8008281904610115,
  "outpoint": "outpoint",
  "status": "status",
  "keys_left": "keys_left"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getpoolinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[PoolInfoResponse](#schemapoolinforesponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## getsuperblockbudget

<a id="opIdgetsuperblockbudget"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//getsuperblockbudget?index=0 \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//getsuperblockbudget?index=0 HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//getsuperblockbudget',
  method: 'get',
  data: '?index=0',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//getsuperblockbudget?index=0',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//getsuperblockbudget',
  params: {
  'index' => 'number'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//getsuperblockbudget', params={
  'index': '0'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//getsuperblockbudget?index=0");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//getsuperblockbudget", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getsuperblockbudget`

Returns the absolute maximum sum of superblock payments allowed.

<h3 id="getsuperblockbudget-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|index|query|number|true|The block index|

> Example responses

> 200 Response

```json
0
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="getsuperblockbudget-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|number|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## gobject

<a id="opIdgobject"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//gobject?command=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//gobject?command=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//gobject',
  method: 'get',
  data: '?command=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//gobject?command=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//gobject',
  params: {
  'command' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//gobject', params={
  'command': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//gobject?command=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//gobject", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /gobject`

Manage governance objects.

<h3 id="gobject-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|command|query|string|true|'check' - Validate governance object data (proposal only)|

#### Detailed descriptions

**command**: 'check' - Validate governance object data (proposal only)
'prepare' - Prepare governance object by signing and creating tx
'submit' - Submit governance object to network
'deserialize' - Deserialize governance object from hex string to JSON
'count' - Count governance objects and votes
'get' - Get governance object by hash
'getvotes' - Get all votes for a governance object hash (including old votes)
'getcurrentvotes' - Get only current (tallying) votes for a governance object hash (does not include old votes)
'list' - List governance objects (can be filtered by signal and/or object type)
'diff' - List differences since last diff
'vote-alias' - Vote on a governance object by masternode alias (using masternode.conf setup)
'vote-conf' - Vote on a governance object by masternode configured in syscoin.conf
'vote-many'- Vote on a governance object by all masternodes (using masternode.conf setup)

> Example responses

> default Response

```json
{
  "message": "string"
}
```

<h3 id="gobject-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## masternode

<a id="opIdmasternode"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//masternode?command=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//masternode?command=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//masternode',
  method: 'get',
  data: '?command=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//masternode?command=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//masternode',
  params: {
  'command' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//masternode', params={
  'command': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//masternode?command=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//masternode", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /masternode`

Set of commands to execute masternode related actions.

<h3 id="masternode-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|command|query|string|true|'count' - Print number of all known masternodes (optional 'ps', 'enabled', 'all', 'qualify')|

#### Detailed descriptions

**command**: 'count' - Print number of all known masternodes (optional 'ps', 'enabled', 'all', 'qualify')
'current' - Print info on current masternode winner to be paid the next block (calculated locally)
'debug' - Print masternode status
'genkey' - Generate new masternodeprivkey
'outputs' - Print masternode compatible outputs
'start' - Start local Hot masternode configured in syscoin.conf
'start-alias' - Start single remote masternode by assigned alias configured in masternode.conf
'start-[mode]' - Start remote masternodes configured in masternode.conf ([mode] can be one of 'all', 'missing', or 'disabled')
'status' - Print masternode status information
'list' - Print list of all known masternodes (see masternodelist for more info)
'list-conf' - Print masternode.conf in JSON format
'winner' - Print info on next masternode winner to vote for
'winners'- Print list of masternode winners

> Example responses

> default Response

```json
{
  "message": "string"
}
```

<h3 id="masternode-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## masternodebroadcast

<a id="opIdmasternodebroadcast"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//masternodebroadcast?command=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//masternodebroadcast?command=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//masternodebroadcast',
  method: 'get',
  data: '?command=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//masternodebroadcast?command=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//masternodebroadcast',
  params: {
  'command' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//masternodebroadcast', params={
  'command': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//masternodebroadcast?command=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//masternodebroadcast", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /masternodebroadcast`

Set of commands to create and relay masternode broadcast messages.

<h3 id="masternodebroadcast-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|command|query|string|true|'create-alias' - Create single remote masternode broadcast message by assigned alias configured in masternode.conf|

#### Detailed descriptions

**command**: 'create-alias' - Create single remote masternode broadcast message by assigned alias configured in masternode.conf
'create-all' - Create remote masternode broadcast messages for all masternodes configured in masternode.conf
'decode' - Decode masternode broadcast message
'relay' - Relay masternode broadcast message to the network

> Example responses

> default Response

```json
{
  "message": "string"
}
```

<h3 id="masternodebroadcast-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## masternodelist

<a id="opIdmasternodelist"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//masternodelist \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//masternodelist HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//masternodelist',
  method: 'get',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//masternodelist',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//masternodelist',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//masternodelist', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//masternodelist");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//masternodelist", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /masternodelist`

Get a list of masternodes in different modes.

<h3 id="masternodelist-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|mode|query|string|false|(optional/required to use filter, defaults = status) The mode to run list in|

#### Detailed descriptions

**mode**: (optional/required to use filter, defaults = status) The mode to run list in
'activeseconds' - Print number of seconds masternode recognized by the network as enabled (since latest issued \"masternode start/start-many/start-alias\")
'addr' - Print ip address associated with a masternode (can be additionally filtered, partial match)
'full' - Print info in format 'status protocol payee lastseen activeseconds lastpaidtime lastpaidblock IP' (can be additionally filtered, partial match)
'info' - Print info in format 'status protocol payee lastseen activeseconds sentinelversion sentinelstate IP' (can be additionally filtered, partial match)
'lastpaidblock' - Print the last block height a node was paid on the network
'lastpaidtime' - Print the last time a node was paid on the network
'lastseen' - Print timestamp of when a masternode was last seen on the network
'payee' - Print Syscoin address associated with a masternode (can be additionally filtered,partial match)
'protocol' - Print protocol of a masternode (can be additionally filtered, exact match)
'pubkey' - Print the masternode (not collateral) public key
'rank' - Print rank of a masternode based on current block
'status' - Print masternode status PRE_ENABLED / ENABLED / EXPIRED / WATCHDOG_EXPIRED / NEW_START_REQUIRED / UPDATE_REQUIRED / POSE_BAN / OUTPOINT_SPENT (can be additionally filtered, partial match)

> Example responses

> default Response

```json
{
  "message": "string"
}
```

<h3 id="masternodelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

<h1 id="Syscoin-API-Aliases">Aliases</h1>

Operations related to aliases.

## aliasbalance

<a id="opIdaliasbalance"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//aliasbalance?alias=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//aliasbalance?alias=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliasbalance',
  method: 'get',
  data: '?alias=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliasbalance?alias=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//aliasbalance',
  params: {
  'alias' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//aliasbalance', params={
  'alias': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliasbalance?alias=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//aliasbalance", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /aliasbalance`

Returns the total amount received by the given alias in transactions with at least minconf confirmations.

<h3 id="aliasbalance-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|alias|query|string|true|The syscoin alias for transactions|

> Example responses

> 200 Response

```json
0
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliasbalance-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|number|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliaswhitelist

<a id="opIdaliaswhitelist"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//aliaswhitelist?aliasname=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//aliaswhitelist?aliasname=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliaswhitelist',
  method: 'get',
  data: '?aliasname=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliaswhitelist?aliasname=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//aliaswhitelist',
  params: {
  'aliasname' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//aliaswhitelist', params={
  'aliasname': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliaswhitelist?aliasname=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//aliaswhitelist", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /aliaswhitelist`

List all affiliates for this alias.

<h3 id="aliaswhitelist-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|aliasname|query|string|true|none|

> Example responses

> 200 Response

```json
[
  {
    "alias": "alias",
    "discount_percentage": 0.8008281904610115
  }
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliaswhitelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="aliaswhitelist-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WhitelistEntry](#schemawhitelistentry)]|false|none|none|
|» alias|string|false|none|none|
|» discount_percentage|number|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## syscointxfund

<a id="opIdsyscointxfund"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//syscointxfund \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//syscointxfund HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//syscointxfund',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "addresses": [
    "{}",
    "{}"
  ],
  "hexstring": "hexstring"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//syscointxfund',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//syscointxfund',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//syscointxfund', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//syscointxfund");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//syscointxfund", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /syscointxfund`

fund an alias creation (possibly other operations in the future)

> Body parameter

```json
{
  "addresses": [
    "{}",
    "{}"
  ],
  "hexstring": "hexstring"
}
```

<h3 id="syscointxfund-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SyscoinTransactionFundRequest](#schemasyscointransactionfundrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> 500 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="syscointxfund-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Could not send raw transaction: Cannot decode transaction from hex string or No funds found in addresses provided|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliasaddscript

<a id="opIdaliasaddscript"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//aliasaddscript \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//aliasaddscript HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliasaddscript',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "script": "script"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliasaddscript',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//aliasaddscript',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//aliasaddscript', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliasaddscript");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//aliasaddscript", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /aliasaddscript`

add a redeem script to alias

> Body parameter

```json
{
  "script": "script"
}
```

<h3 id="aliasaddscript-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AliasAddScriptRequest](#schemaaliasaddscriptrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> 500 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliasaddscript-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|unable to call aliasaddscript|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliasclearwhitelist

<a id="opIdaliasclearwhitelist"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//aliasclearwhitelist \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//aliasclearwhitelist HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliasclearwhitelist',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "owneralias": "owneralias"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliasclearwhitelist',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//aliasclearwhitelist',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//aliasclearwhitelist', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliasclearwhitelist");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//aliasclearwhitelist", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /aliasclearwhitelist`

Clear your whitelist(controls who can resell).

> Body parameter

```json
{
  "witness": "witness",
  "owneralias": "owneralias"
}
```

<h3 id="aliasclearwhitelist-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AliasClearWhiteListRequest](#schemaaliasclearwhitelistrequest)|true|none|

> Example responses

> 200 Response

```json
{}
```

> 500 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliasclearwhitelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|aliasclearwhitelist [owner alias] [witness].  Clear your whitelist(controls who can resell).|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="aliasclearwhitelist-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliasupdatewhitelist

<a id="opIdaliasupdatewhitelist"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//aliasupdatewhitelist \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//aliasupdatewhitelist HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliasupdatewhitelist',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "entries": [
    {
      "alias": "alias",
      "discount_percentage": 0.8008281904610115
    },
    {
      "alias": "alias",
      "discount_percentage": 0.8008281904610115
    }
  ],
  "owneralias": "owneralias"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliasupdatewhitelist',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//aliasupdatewhitelist',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//aliasupdatewhitelist', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliasupdatewhitelist");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//aliasupdatewhitelist", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /aliasupdatewhitelist`

Update to the whitelist(controls who can resell). Array of whitelist entries in parameter 1.

> Body parameter

```json
{
  "witness": "witness",
  "entries": [
    {
      "alias": "alias",
      "discount_percentage": 0.8008281904610115
    },
    {
      "alias": "alias",
      "discount_percentage": 0.8008281904610115
    }
  ],
  "owneralias": "owneralias"
}
```

<h3 id="aliasupdatewhitelist-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AliasUpdateWhitelistRequest](#schemaaliasupdatewhitelistrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliasupdatewhitelist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="aliasupdatewhitelist-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliasinfo

<a id="opIdaliasinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//aliasinfo?aliasname=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//aliasinfo?aliasname=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliasinfo',
  method: 'get',
  data: '?aliasname=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliasinfo?aliasname=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//aliasinfo',
  params: {
  'aliasname' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//aliasinfo', params={
  'aliasname': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliasinfo?aliasname=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//aliasinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /aliasinfo`

Show values of an alias.

<h3 id="aliasinfo-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|aliasname|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "publicvalue": "publicvalue",
  "address": "address",
  "expired": true,
  "encryption_privatekey": "encryption_privatekey",
  "expires_on": 1.4658129805029452,
  "txid": "txid",
  "_id": "_id",
  "time": 0.8008281904610115,
  "encryption_publickey": "encryption_publickey",
  "accepttransferflags": 6.027456183070403
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliasinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Alias](#schemaalias)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliasnew

<a id="opIdaliasnew"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//aliasnew \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//aliasnew HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliasnew',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "aliasname": "aliasname",
  "publicvalue": "publicvalue",
  "address": "address",
  "encryption_privatekey": "encryption_privatekey",
  "expire_timestamp": 6.027456183070403,
  "encryption_publickey": "encryption_publickey",
  "accept_transfers_flags": 0.8008281904610115
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliasnew',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//aliasnew',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//aliasnew', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliasnew");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//aliasnew", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /aliasnew`

Creates a new Syscoin Alias. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "witness": "witness",
  "aliasname": "aliasname",
  "publicvalue": "publicvalue",
  "address": "address",
  "encryption_privatekey": "encryption_privatekey",
  "expire_timestamp": 6.027456183070403,
  "encryption_publickey": "encryption_publickey",
  "accept_transfers_flags": 0.8008281904610115
}
```

<h3 id="aliasnew-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AliasNewRequest](#schemaaliasnewrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliasnew-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="aliasnew-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliaspay

<a id="opIdaliaspay"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//aliaspay \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//aliaspay HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliaspay',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "amounts": "{\"alias1\":0.02,\"alias2\":0.4,\"alias3\":0.004}",
  "instantsend": false,
  "aliasfrom": "aliasfrom",
  "subtractfeefromamount": [
    "alias1",
    "alias2"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliaspay',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//aliaspay',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//aliaspay', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliaspay");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//aliaspay", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /aliaspay`

Send multiple times from an alias. Amounts are double-precision floating point numbers.

> Body parameter

```json
{
  "amounts": "{\"alias1\":0.02,\"alias2\":0.4,\"alias3\":0.004}",
  "instantsend": false,
  "aliasfrom": "aliasfrom",
  "subtractfeefromamount": [
    "alias1",
    "alias2"
  ]
}
```

<h3 id="aliaspay-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AliasPayRequest](#schemaaliaspayrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliaspay-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="aliaspay-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## aliasupdate

<a id="opIdaliasupdate"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//aliasupdate \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//aliasupdate HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//aliasupdate',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "aliasname": "aliasname",
  "publicvalue": "publicvalue",
  "address": "address",
  "encryption_privatekey": "encryption_privatekey",
  "expire_timestamp": 6,
  "encryption_publickey": "encryption_publickey",
  "accept_transfers_flags": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//aliasupdate',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//aliasupdate',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//aliasupdate', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//aliasupdate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//aliasupdate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /aliasupdate`

Update and possibly transfer an alias. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "witness": "witness",
  "aliasname": "aliasname",
  "publicvalue": "publicvalue",
  "address": "address",
  "encryption_privatekey": "encryption_privatekey",
  "expire_timestamp": 6,
  "encryption_publickey": "encryption_publickey",
  "accept_transfers_flags": 0
}
```

<h3 id="aliasupdate-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AliasUpdateRequest](#schemaaliasupdaterequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="aliasupdate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="aliasupdate-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

<h1 id="Syscoin-API-Certificates">Certificates</h1>

Operations related to digital certificates.

## certinfo

<a id="opIdcertinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//certinfo?guid=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//certinfo?guid=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//certinfo',
  method: 'get',
  data: '?guid=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//certinfo?guid=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//certinfo',
  params: {
  'guid' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//certinfo', params={
  'guid': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//certinfo?guid=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//certinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /certinfo`

Show stored values of a single certificate.

<h3 id="certinfo-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|guid|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "publicvalue": "publicvalue",
  "expired": true,
  "expires_on": 5.962133916683182,
  "txid": "txid",
  "alias": "alias",
  "_id": "_id",
  "time": 6.027456183070403,
  "access_flags": 1.4658129805029452,
  "title": "title",
  "category": "category",
  "height": 0.8008281904610115
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="certinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Cert](#schemacert)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## certnew

<a id="opIdcertnew"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//certnew \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//certnew HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//certnew',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "alias": "alias",
  "title": "title",
  "category": "category"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//certnew',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//certnew',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//certnew', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//certnew");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//certnew", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /certnew`

Create a new Syscoin Certificate. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "alias": "alias",
  "title": "title",
  "category": "category"
}
```

<h3 id="certnew-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CertNewRequest](#schemacertnewrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="certnew-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="certnew-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## certtransfer

<a id="opIdcerttransfer"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//certtransfer \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//certtransfer HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//certtransfer',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "accessflags": 0.8008281904610115,
  "guid": "guid",
  "alias": "alias"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//certtransfer',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//certtransfer',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//certtransfer', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//certtransfer");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//certtransfer", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /certtransfer`

Transfer certificate from one user to another. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "accessflags": 0.8008281904610115,
  "guid": "guid",
  "alias": "alias"
}
```

<h3 id="certtransfer-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CertTransferRequest](#schemacerttransferrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="certtransfer-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="certtransfer-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## certupdate

<a id="opIdcertupdate"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//certupdate \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//certupdate HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//certupdate',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "guid": "guid",
  "title": "title",
  "category": "category"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//certupdate',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//certupdate',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//certupdate', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//certupdate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//certupdate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /certupdate`

Perform an update on an certificate you control. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "guid": "guid",
  "title": "title",
  "category": "category"
}
```

<h3 id="certupdate-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CertUpdateRequest](#schemacertupdaterequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="certupdate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="certupdate-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

<h1 id="Syscoin-API-Escrow">Escrow</h1>

Operations related to escrow.

## escrowacknowledge

<a id="opIdescrowacknowledge"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowacknowledge \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowacknowledge HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowacknowledge',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "escrowguid": "escrowguid"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowacknowledge',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowacknowledge',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowacknowledge', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowacknowledge");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowacknowledge", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowacknowledge`

Acknowledge escrow payment as seller of offer. Deducts qty of offer and increases number of sold inventory.

> Body parameter

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid"
}
```

<h3 id="escrowacknowledge-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowacknowledgeRequest](#schemaescrowacknowledgerequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowacknowledge-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="escrowacknowledge-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowcompleterefund

<a id="opIdescrowcompleterefund"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowcompleterefund \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowcompleterefund HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowcompleterefund',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowcompleterefund',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowcompleterefund',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowcompleterefund', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowcompleterefund");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowcompleterefund", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowcompleterefund`

Completes an escrow refund by creating the escrow complete refund transaction on syscoin blockchain.

> Body parameter

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx"
}
```

<h3 id="escrowcompleterefund-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowCompleteRefundRequest](#schemaescrowcompleterefundrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowcompleterefund-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="escrowcompleterefund-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowcompleterelease

<a id="opIdescrowcompleterelease"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowcompleterelease \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowcompleterelease HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowcompleterelease',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowcompleterelease',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowcompleterelease',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowcompleterelease', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowcompleterelease");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowcompleterelease", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowcompleterelease`

Completes an escrow release by creating the escrow complete release transaction on syscoin blockchain.

> Body parameter

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx"
}
```

<h3 id="escrowcompleterelease-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowCompleteReleaseRequest](#schemaescrowcompletereleaserequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowcompleterelease-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="escrowcompleterelease-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowfeedback

<a id="opIdescrowfeedback"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowfeedback \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowfeedback HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowfeedback',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "feedback": "feedback",
  "witness": "witness",
  "userfrom": "userfrom",
  "escrowguid": "escrowguid",
  "rating": 0,
  "userto": "userto"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowfeedback',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowfeedback',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowfeedback', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowfeedback");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowfeedback", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowfeedback`

Send feedback for primary and secondary users in escrow, depending on who you are.

> Body parameter

```json
{
  "feedback": "feedback",
  "witness": "witness",
  "userfrom": "userfrom",
  "escrowguid": "escrowguid",
  "rating": 0,
  "userto": "userto"
}
```

<h3 id="escrowfeedback-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowFeedbackRequest](#schemaescrowfeedbackrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "offer": "offer",
  "feedback": "feedback",
  "feedbackuserfrom": 5.962133916683182,
  "rating": 1.4658129805029452,
  "escrow": "escrow",
  "txid": 0.8008281904610115,
  "feedbackuserto": 5.637376656633329,
  "_id": "_id",
  "time": 6.027456183070403
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowfeedback-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[EscrowFeedbackResponse](#schemaescrowfeedbackresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowinfo

<a id="opIdescrowinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//escrowinfo?escrowguid=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//escrowinfo?escrowguid=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowinfo',
  method: 'get',
  data: '?escrowguid=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowinfo?escrowguid=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//escrowinfo',
  params: {
  'escrowguid' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//escrowinfo', params={
  'escrowguid': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowinfo?escrowguid=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//escrowinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /escrowinfo`

Show stored values of a single escrow

<h3 id="escrowinfo-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|escrowguid|query|string|true|GUID of escrow|

> Example responses

> 200 Response

```json
{
  "seller": "seller",
  "total_without_fee": 2.3021358869347655,
  "role": 6.84685269835264,
  "acknowledged": true,
  "redeem_txid": "redeem_txid",
  "offer_title": 1.4658129805029452,
  "offer": "offer",
  "expired": true,
  "shipping": 1.2315135367772556,
  "arbiterfee": 2.027123023002322,
  "commission": 3.616076749251911,
  "currency": "currency",
  "escrowaddress": "escrowaddress",
  "height": 1.4894159098541704,
  "total_with_fee": 5.637376656633329,
  "quantity": 5.962133916683182,
  "witnessfee": 7.386281948385884,
  "total_or_bid_in_payment_option_per_unit": 9.301444243932576,
  "paymentoption": "paymentoption",
  "networkfee": 4.145608029883936,
  "reseller": "reseller",
  "txid": "txid",
  "buyer": "buyer",
  "offer_price": 6.027456183070403,
  "witness": "witness",
  "arbiter": "arbiter",
  "buynow": true,
  "exttxid": "exttxid",
  "deposit": 1.0246457001441578,
  "redeem_script": "redeem_script",
  "_id": "_id",
  "time": 0.8008281904610115,
  "bid_in_offer_currency_per_unit": 7.061401241503109,
  "status": 7.457744773683766
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Escrow](#schemaescrow)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrownew

<a id="opIdescrownew"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrownew \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrownew HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrownew',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "bid_in_offer_currency": 9.301444243932576,
  "extTx": "extTx",
  "quantity": 0,
  "total_in_payment_option": 6.027456183070403,
  "paymentoption": "paymentoption",
  "witness_fee": 2.3021358869347655,
  "arbiter_alias": "arbiter_alias",
  "bid_in_payment_option": 7.061401241503109,
  "network_fee": 5.962133916683182,
  "offer": "offer",
  "shipping_amount": 1.4658129805029452,
  "witness": "witness",
  "buynow": true,
  "alias": "alias",
  "arbiter_fee": 5.637376656633329,
  "getamountandaddress": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrownew',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrownew',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrownew', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrownew");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrownew", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrownew`

Create new arbitrated Syscoin escrow.

> Body parameter

```json
{
  "bid_in_offer_currency": 9.301444243932576,
  "extTx": "extTx",
  "quantity": 0,
  "total_in_payment_option": 6.027456183070403,
  "paymentoption": "paymentoption",
  "witness_fee": 2.3021358869347655,
  "arbiter_alias": "arbiter_alias",
  "bid_in_payment_option": 7.061401241503109,
  "network_fee": 5.962133916683182,
  "offer": "offer",
  "shipping_amount": 1.4658129805029452,
  "witness": "witness",
  "buynow": true,
  "alias": "alias",
  "arbiter_fee": 5.637376656633329,
  "getamountandaddress": true
}
```

<h3 id="escrownew-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowNewRequest](#schemaescrownewrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrownew-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="escrownew-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowrefund

<a id="opIdescrowrefund"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowrefund \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowrefund HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowrefund',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx",
  "userrole": "userrole"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowrefund',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowrefund',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowrefund', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowrefund");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowrefund", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowrefund`

Refunds escrow funds back to buyer, buyer needs to sign the output transaction and send to the network. User role represents either 'seller' or 'arbiter'. Enter in rawTx if this is an external payment refund.

> Body parameter

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx",
  "userrole": "userrole"
}
```

<h3 id="escrowrefund-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowRefundRequest](#schemaescrowrefundrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowrefund-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="escrowrefund-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowrelease

<a id="opIdescrowrelease"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowrelease \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowrelease HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowrelease',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx",
  "userrole": "userrole"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowrelease',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowrelease',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowrelease', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowrelease");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowrelease", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowrelease`

Releases escrow funds to seller, seller needs to sign the output transaction and send to the network. User role represents either 'buyer' or 'arbiter'. Enter in rawTx if this is an external payment release.

> Body parameter

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx",
  "userrole": "userrole"
}
```

<h3 id="escrowrelease-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowReleaseRequest](#schemaescrowreleaserequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowrelease-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="escrowrelease-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## generateescrowmultisig

<a id="opIdgenerateescrowmultisig"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//generateescrowmultisig \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//generateescrowmultisig HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//generateescrowmultisig',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "arbiter": "arbiter",
  "quantity": 0.8008281904610115,
  "offerguid": "offerguid",
  "paymentoption": "paymentoption",
  "buyer": "buyer"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//generateescrowmultisig',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//generateescrowmultisig',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//generateescrowmultisig', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//generateescrowmultisig");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//generateescrowmultisig", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /generateescrowmultisig`

Generates a multisignature escrow transaction

> Body parameter

```json
{
  "arbiter": "arbiter",
  "quantity": 0.8008281904610115,
  "offerguid": "offerguid",
  "paymentoption": "paymentoption",
  "buyer": "buyer"
}
```

<h3 id="generateescrowmultisig-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[GenerateEscrowMultisigRequest](#schemagenerateescrowmultisigrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="generateescrowmultisig-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="generateescrowmultisig-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowbid

<a id="opIdescrowbid"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowbid \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowbid HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowbid',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "bid_in_offer_currency": 6.027456183070403,
  "witness": "witness",
  "bid_in_payment_option": 0.8008281904610115,
  "alias": "alias",
  "escrow": "escrow"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowbid',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowbid',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowbid', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowbid");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowbid", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowbid`

Bid on an auction.

> Body parameter

```json
{
  "bid_in_offer_currency": 6.027456183070403,
  "witness": "witness",
  "bid_in_payment_option": 0.8008281904610115,
  "alias": "alias",
  "escrow": "escrow"
}
```

<h3 id="escrowbid-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowBidRequest](#schemaescrowbidrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "offer": "offer",
  "bid_in_payment_option_per_unit": 1.4658129805029452,
  "witness": "witness",
  "bidder": "bidder",
  "escrow": "escrow",
  "_id": "_id",
  "bid_in_offer_currency_per_unit": 6.027456183070403,
  "height": 0.8008281904610115,
  "status": "status"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowbid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[EscrowBidResponse](#schemaescrowbidresponse)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## escrowcreaterawtransaction

<a id="opIdescrowcreaterawtransaction"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//escrowcreaterawtransaction \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//escrowcreaterawtransaction HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//escrowcreaterawtransaction',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "role": "role",
  "inputs": [
    {
      "txid": "txid",
      "vout": 0.8008281904610115,
      "satoshis": 6.027456183070403
    },
    {
      "txid": "txid",
      "vout": 0.8008281904610115,
      "satoshis": 6.027456183070403
    }
  ],
  "escrowguid": "escrowguid",
  "type": "type"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//escrowcreaterawtransaction',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//escrowcreaterawtransaction',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//escrowcreaterawtransaction', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//escrowcreaterawtransaction");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//escrowcreaterawtransaction", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /escrowcreaterawtransaction`

Creates raw transaction for escrow refund or release, sign the output raw transaction and pass it via the rawtx parameter to escrowrelease. Type is 'refund' or 'release'. Third parameter is array of input (txid, vout, amount) pairs to be used to fund escrow payment. User role represents either 'seller', 'buyer' or 'arbiter', represents who signed for the payment of the escrow. 'seller' or 'arbiter' is valid for type 'refund', while 'buyer' or 'arbiter' is valid for type 'release'. You only need to provide this parameter when calling escrowrelease or escrowrefund.

> Body parameter

```json
{
  "role": "role",
  "inputs": [
    {
      "txid": "txid",
      "vout": 0.8008281904610115,
      "satoshis": 6.027456183070403
    },
    {
      "txid": "txid",
      "vout": 0.8008281904610115,
      "satoshis": 6.027456183070403
    }
  ],
  "escrowguid": "escrowguid",
  "type": "type"
}
```

<h3 id="escrowcreaterawtransaction-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EscrowCreateRawTransactionRequest](#schemaescrowcreaterawtransactionrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="escrowcreaterawtransaction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="escrowcreaterawtransaction-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

<h1 id="Syscoin-API-Offers">Offers</h1>

Operations related to offers and the decentralized marketplace functionality.

## offerinfo

<a id="opIdofferinfo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//offerinfo?guid=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//offerinfo?guid=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//offerinfo',
  method: 'get',
  data: '?guid=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//offerinfo?guid=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//offerinfo',
  params: {
  'guid' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//offerinfo', params={
  'guid': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//offerinfo?guid=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//offerinfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /offerinfo`

Show values of an offer.

<h3 id="offerinfo-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|guid|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "auction_expires_on": 7.061401241503109,
  "offer_units": 5.637376656633329,
  "expires_on": 0.8008281904610115,
  "description": "description",
  "cert": "cert",
  "title": "title",
  "auction_deposit": 3.616076749251911,
  "expired": true,
  "price": 1.4658129805029452,
  "alias": "alias",
  "currency": "currency",
  "commission": 5.962133916683182,
  "auction_require_witness": true,
  "height": 6.027456183070403,
  "offertype": "offertype",
  "quantity": 2.3021358869347655,
  "address": "address",
  "txid": "txid",
  "privatevalue": true,
  "offerlink_guid": "offerlink_guid",
  "paymentoptions": "paymentoptions",
  "offerlink_seller": "offerlink_seller",
  "auction_reserve_price": 9.301444243932576,
  "_id": "_id",
  "category": "category"
}
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="offerinfo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[Offer](#schemaoffer)|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## offerlink

<a id="opIdofferlink"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//offerlink \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//offerlink HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//offerlink',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "witness": "witness",
  "alias": "alias",
  "guid": "guid",
  "description": "description",
  "commission": 0.8008281904610115
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//offerlink',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//offerlink',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//offerlink', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//offerlink");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//offerlink", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /offerlink`

Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "witness": "witness",
  "alias": "alias",
  "guid": "guid",
  "description": "description",
  "commission": 0.8008281904610115
}
```

<h3 id="offerlink-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[OfferLinkRequest](#schemaofferlinkrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="offerlink-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="offerlink-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## offernew

<a id="opIdoffernew"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//offernew \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//offernew HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//offernew',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "offertype": "offertype",
  "quantity": 0.8008281904610115,
  "auction_expires": 5.962133916683182,
  "description": "description",
  "privatevalue": true,
  "units": 1.4658129805029452,
  "auction_reserve": 5.637376656633329,
  "title": "title",
  "auction_deposit": 2.3021358869347655,
  "witness": "witness",
  "cert_guid": "cert_guid",
  "price": 6.027456183070403,
  "alias": "alias",
  "currency": "currency",
  "category": "category",
  "auction_require_witness": true,
  "payment_options": "payment_options"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//offernew',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//offernew',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//offernew', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//offernew");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//offernew", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /offernew`

Create a new offer on the Syscoin decentralized marketplace. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "offertype": "offertype",
  "quantity": 0.8008281904610115,
  "auction_expires": 5.962133916683182,
  "description": "description",
  "privatevalue": true,
  "units": 1.4658129805029452,
  "auction_reserve": 5.637376656633329,
  "title": "title",
  "auction_deposit": 2.3021358869347655,
  "witness": "witness",
  "cert_guid": "cert_guid",
  "price": 6.027456183070403,
  "alias": "alias",
  "currency": "currency",
  "category": "category",
  "auction_require_witness": true,
  "payment_options": "payment_options"
}
```

<h3 id="offernew-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[OfferNewRequest](#schemaoffernewrequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="offernew-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success; Returns an array of 2 elements- tx id and offer GUID.|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="offernew-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## offerupdate

<a id="opIdofferupdate"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//offerupdate \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//offerupdate HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//offerupdate',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "quantity": 0.8008281904610115,
  "auction_expires": 5.962133916683182,
  "description": "description",
  "privatevalue": true,
  "auction_reserve": 5.637376656633329,
  "title": "title",
  "auction_deposit": 2.3021358869347655,
  "witness": "witness",
  "cert_guid": "cert_guid",
  "price": 6.027456183070403,
  "alias": "alias",
  "guid": "guid",
  "currency": "currency",
  "commission": 1.4658129805029452,
  "category": "category",
  "offer_type": "offer_type",
  "auction_require_witness": true,
  "payment_options": "payment_options"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//offerupdate',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//offerupdate',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//offerupdate', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//offerupdate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//offerupdate", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /offerupdate`

Perform an update on an offer you control. Requires wallet passphrase to be set with walletpassphrase call.

> Body parameter

```json
{
  "quantity": 0.8008281904610115,
  "auction_expires": 5.962133916683182,
  "description": "description",
  "privatevalue": true,
  "auction_reserve": 5.637376656633329,
  "title": "title",
  "auction_deposit": 2.3021358869347655,
  "witness": "witness",
  "cert_guid": "cert_guid",
  "price": 6.027456183070403,
  "alias": "alias",
  "guid": "guid",
  "currency": "currency",
  "commission": 1.4658129805029452,
  "category": "category",
  "offer_type": "offer_type",
  "auction_require_witness": true,
  "payment_options": "payment_options"
}
```

<h3 id="offerupdate-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[OfferUpdateRequest](#schemaofferupdaterequest)|true|none|

> Example responses

> 200 Response

```json
[
  "string"
]
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="offerupdate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success; Returns an array with 1 element- tx id.|Inline|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<h3 id="offerupdate-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

<h1 id="Syscoin-API-Masternodes">Masternodes</h1>

## sentinelping

<a id="opIdsentinelping"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//sentinelping?version=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//sentinelping?version=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//sentinelping',
  method: 'get',
  data: '?version=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//sentinelping?version=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//sentinelping',
  params: {
  'version' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//sentinelping', params={
  'version': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//sentinelping?version=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//sentinelping", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /sentinelping`

Keep-alive message for masternode via TCP ping requests.

<h3 id="sentinelping-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|version|query|string|true|Sentinel version in the form 'x.x.x'|

> Example responses

> 200 Response

```json
true
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="sentinelping-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|boolean|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## voteraw

<a id="opIdvoteraw"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8001//voteraw \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
POST http://localhost:8001//voteraw HTTP/1.1
Host: localhost:8001
Content-Type: application/json
Accept: application/json

```

```javascript
var headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//voteraw',
  method: 'post',

  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');
const inputBody = '{
  "masternode-tx-index": 0.8008281904610115,
  "vote-signal": 6.027456183070403,
  "masternode-tx-hash": "masternode-tx-hash",
  "governance-hash": "governance-hash",
  "time": 1.4658129805029452,
  "vote-sig": "vote-sig",
  "vote-outcome": "vote-outcome"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//voteraw',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.post 'http://localhost:8001//voteraw',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.post('http://localhost:8001//voteraw', params={

}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//voteraw");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:8001//voteraw", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /voteraw`

Compile and relay a governance vote with provided external signature instead of signing vote internally.

> Body parameter

```json
{
  "masternode-tx-index": 0.8008281904610115,
  "vote-signal": 6.027456183070403,
  "masternode-tx-hash": "masternode-tx-hash",
  "governance-hash": "governance-hash",
  "time": 1.4658129805029452,
  "vote-sig": "vote-sig",
  "vote-outcome": "vote-outcome"
}
```

<h3 id="voteraw-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[VoteRawRequest](#schemavoterawrequest)|true|none|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="voteraw-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## privatesend

<a id="opIdprivatesend"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//privatesend?command=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//privatesend?command=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//privatesend',
  method: 'get',
  data: '?command=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//privatesend?command=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//privatesend',
  params: {
  'command' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//privatesend', params={
  'command': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//privatesend?command=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//privatesend", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /privatesend`

Anonymous mixing and sending coins.

<h3 id="privatesend-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|command|query|string|true|'start' - Start Mixing|

#### Detailed descriptions

**command**: 'start' - Start Mixing
'stop' - Stop mixing
'reset' - Reset mixing

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="privatesend-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

## importelectrumwallet

<a id="opIdimportelectrumwallet"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8001//importelectrumwallet?filename=string \
  -H 'Accept: application/json' \
  -H 'token: API_KEY'

```

```http
GET http://localhost:8001//importelectrumwallet?filename=string HTTP/1.1
Host: localhost:8001

Accept: application/json

```

```javascript
var headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

$.ajax({
  url: 'http://localhost:8001//importelectrumwallet',
  method: 'get',
  data: '?filename=string',
  headers: headers,
  success: function(data) {
    console.log(JSON.stringify(data));
  }
})

```

```javascript--nodejs
const request = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'token':'API_KEY'

};

fetch('http://localhost:8001//importelectrumwallet?filename=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'token' => 'API_KEY'
}

result = RestClient.get 'http://localhost:8001//importelectrumwallet',
  params: {
  'filename' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'token': 'API_KEY'
}

r = requests.get('http://localhost:8001//importelectrumwallet', params={
  'filename': 'string'
}, headers = headers)

print r.json()

```

```java
URL obj = new URL("http://localhost:8001//importelectrumwallet?filename=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "token": []string{"API_KEY"},
        
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:8001//importelectrumwallet", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /importelectrumwallet`

Imports keys from an Electrum wallet export file (.csv or .json).

<h3 id="importelectrumwallet-parameters">Parameters</h3>

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|filename|query|string|true|(string, required) The Electrum wallet export file, should be in csv or json format|
|index|query|number|false|(numeric, optional, default=0) Rescan the wallet for transactions starting from this block index|

> Example responses

> 200 Response

```json
"string"
```

> default Response

```json
{
  "message": "string"
}
```

<h3 id="importelectrumwallet-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|string|
|default|Default|Error|[ErrorResponse](#schemaerrorresponse)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
token
</aside>

# Schemas

<h2 id="tocSinstantsendtoaddressrequest">instantSendToAddressRequest</h2>

<a id="schemainstantsendtoaddressrequest"></a>

```json
{
  "syscoinaddress": "string",
  "amount": 0,
  "comment": "string",
  "comment-to": "string",
  "subtractfeefromamount": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|syscoinaddress|string|true|none|(string, required) The syscoin address to send to.|
|amount|number|true|none|(numeric, required) The amount in sys to send. eg 0.1|
|comment|string|false|none|(string, optional) A comment used to store what the transaction is for.|
|comment-to|string|false|none|(string, optional) A comment to store the name of the person or organization to which you're sending the transaction. This is not part of the transaction, just kept in your wallet.|
|subtractfeefromamount|boolean|false|none|The fee will be deducted from the amount being sent.|

<h2 id="tocSsendrawtransactionrequest">SendRawTransactionRequest</h2>

<a id="schemasendrawtransactionrequest"></a>

```json
{
  "instantsend": true,
  "allowhighfees": true,
  "hexstring": "hexstring"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hexstring|string|true|none|none|
|allowhighfees|boolean|false|none|none|
|instantsend|boolean|false|none|none|

<h2 id="tocSgetaddressutxosentry">GetAddressUTXOsEntry</h2>

<a id="schemagetaddressutxosentry"></a>

```json
{
  "outputIndex": 0.8008281904610115,
  "address": "address",
  "txid": "txid",
  "script": "script",
  "satoshis": 6.027456183070403,
  "height": 1.4658129805029452
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|false|none|none|
|txid|string|false|none|none|
|outputIndex|number|false|none|none|
|script|string|false|none|none|
|satoshis|number|false|none|none|
|height|number|false|none|none|

<h2 id="tocSescrowcreaterawtransactionrequest">EscrowCreateRawTransactionRequest</h2>

<a id="schemaescrowcreaterawtransactionrequest"></a>

```json
{
  "role": "role",
  "inputs": [
    {
      "txid": "txid",
      "vout": 0.8008281904610115,
      "satoshis": 6.027456183070403
    },
    {
      "txid": "txid",
      "vout": 0.8008281904610115,
      "satoshis": 6.027456183070403
    }
  ],
  "escrowguid": "escrowguid",
  "type": "type"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|true|none|none|
|escrowguid|string|true|none|none|
|inputs|[[EscrowCreateRawTransactionDataRequest](#schemaescrowcreaterawtransactiondatarequest)]|true|none|none|
|role|string|false|none|none|

<h2 id="tocSescrowacknowledgerequest">EscrowacknowledgeRequest</h2>

<a id="schemaescrowacknowledgerequest"></a>

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|escrowguid|string|true|none|Escrow guid|
|witness|string|true|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSescrowbidrequest">EscrowBidRequest</h2>

<a id="schemaescrowbidrequest"></a>

```json
{
  "bid_in_offer_currency": 6.027456183070403,
  "witness": "witness",
  "bid_in_payment_option": 0.8008281904610115,
  "alias": "alias",
  "escrow": "escrow"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|true|none|An alias you own.|
|escrow|string|true|none|Escrow GUID to place bid on.|
|bid_in_payment_option|number|true|none|Amount to bid on offer through escrow. Bid is in payment option currency. Example, If offer is paid in SYS and you have deposited 10 SYS in escrow and would like to increase your total bid to 14 SYS enter 14 here. It is per unit of purchase.|
|bid_in_offer_currency|number|true|none|Converted value of bid_in_payment_option from paymentOption currency to offer currency. For example, offer is priced in USD and purchased in BTC, this field will be the BTC/USD value. It is per unit of purchase.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSvoterawrequest">VoteRawRequest</h2>

<a id="schemavoterawrequest"></a>

```json
{
  "masternode-tx-index": 0.8008281904610115,
  "vote-signal": 6.027456183070403,
  "masternode-tx-hash": "masternode-tx-hash",
  "governance-hash": "governance-hash",
  "time": 1.4658129805029452,
  "vote-sig": "vote-sig",
  "vote-outcome": "vote-outcome"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|masternode-tx-hash|string|true|none|none|
|masternode-tx-index|number|true|none|none|
|governance-hash|string|true|none|none|
|vote-signal|number|true|none|none|
|vote-outcome|string|true|none|none|
|time|number|true|none|none|
|vote-sig|string|true|none|none|

<h2 id="tocSgetaddressmempoolresponseobject">getAddressMemPoolResponseObject</h2>

<a id="schemagetaddressmempoolresponseobject"></a>

```json
{
  "address": "address",
  "prevout": "prevout",
  "txid": "txid",
  "index": 0.8008281904610115,
  "prevtxid": "prevtxid",
  "satoshis": "satoshis",
  "height": 6.027456183070403,
  "timestamp": 1.4658129805029452
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|satoshis|string|false|none|The difference of satoshis|
|txid|string|false|none|The related txid|
|index|number|false|none|The related input or output index|
|height|number|false|none|The block height|
|address|string|false|none|The base58check encoded address|
|timestamp|number|false|none|The time the transaction entered the mempool (seconds)|
|prevtxid|string|false|none|The previous txid (if spending)|
|prevout|string|false|none|The previous transaction output index (if spending)|

<h2 id="tocSgetaddressdeltasresponseobject">getAddressDeltasResponseObject</h2>

<a id="schemagetaddressdeltasresponseobject"></a>

```json
{
  "address": "address",
  "txid": "txid",
  "index": 0.8008281904610115,
  "satoshis": "satoshis",
  "height": 6.027456183070403
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|satoshis|string|false|none|The difference of satoshis|
|txid|string|false|none|The related txid|
|index|number|false|none|The related input or output index|
|height|number|false|none|The block height|
|address|string|false|none|The base58check encoded address|

<h2 id="tocSgetaddressbalanceresponse">getAddressBalanceResponse</h2>

<a id="schemagetaddressbalanceresponse"></a>

```json
{
  "balance": "balance",
  "received": "received"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|balance|string|false|none|balance againts address|
|received|string|false|none|received againts address|

<h2 id="tocSinfo">Info</h2>

<a id="schemainfo"></a>

```json
{
  "protocolversion": 6.027456183070403,
  "relayfee": 1.2315135367772556,
  "timeoffset": 2.3021358869347655,
  "blocks": 5.637376656633329,
  "version": 0.8008281904610115,
  "keypoolsize": 2.027123023002322,
  "unlocked_until": 4.145608029883936,
  "paytxfee": 7.386281948385884,
  "difficulty": 9.301444243932576,
  "proxy": "proxy",
  "walletversion": 1.4658129805029452,
  "balance": 5.962133916683182,
  "keypoololdest": 3.616076749251911,
  "testnet": true,
  "connections": 7.061401241503109,
  "errors": "errors"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version|number|true|none|the server version|
|protocolversion|number|true|none|the protocol version|
|walletversion|number|true|none|the wallet version|
|balance|number|true|none|the total syscoin balance of the wallet|
|blocks|number|true|none|the current number of blocks processed in the server|
|timeoffset|number|true|none|the time offset|
|connections|number|true|none|the number of connections|
|proxy|string|true|none|the proxy used by the server|
|difficulty|number|true|none|the current difficulty|
|testnet|boolean|true|none|if the server is using testnet or not|
|keypoololdest|number|true|none|the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool|
|keypoolsize|number|true|none|how many new keys are pre-generated|
|unlocked_until|number|true|none|the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, or 0 if the wallet is locked|
|paytxfee|number|true|none|the transaction fee set in SYS/kB|
|relayfee|number|true|none|minimum relay fee for non-free transactions in SYS/kB|
|errors|string|true|none|any error messages|

<h2 id="tocSmininginfo">MiningInfo</h2>

<a id="schemamininginfo"></a>

```json
{
  "difficulty": 5.962133916683182,
  "chain": "chain",
  "currentblocktx": 1.4658129805029452,
  "blocks": 0.8008281904610115,
  "networkhashps": 2.3021358869347655,
  "currentblocksize": 6.027456183070403,
  "genproclimit": 5.637376656633329,
  "testnet": true,
  "pooledtx": 7.061401241503109,
  "generate": true,
  "errors": "errors"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|blocks|number|true|none|The current block|
|currentblocksize|number|true|none|The last block size|
|currentblocktx|number|true|none|The last block transaction|
|difficulty|number|true|none|The current difficulty|
|errors|string|true|none|Current errors|
|genproclimit|number|true|none|The processor limit for generation. -1 if no generation.|
|networkhashps|number|false|none|Current network hashrate in kbs|
|pooledtx|number|true|none|The size of the mem pool|
|testnet|boolean|true|none|If using testnet or not|
|chain|string|true|none|current network name as defined in BIP70 (main, test, regtest)|
|generate|boolean|true|none|If the generation is on or off (see getgenerate or setgenerate calls)|

<h2 id="tocSpeerinforesponse">PeerInfoResponse</h2>

<a id="schemapeerinforesponse"></a>

```json
[
  {
    "id": 0,
    "addr": "string",
    "addrlocal": "string",
    "services": "string",
    "relaytxes": true,
    "lastsend": 0,
    "lastrecv": 0,
    "bytessent": 0,
    "bytesrecv": 0,
    "conntime": 0,
    "timeoffset": 0,
    "pingtime": 0,
    "minping": 0,
    "version": 0,
    "subver": "string",
    "inbound": true,
    "startingheight": 0,
    "banscore": 0,
    "synced_headers": 0,
    "synced_blocks": 0,
    "inflight": [
      0
    ],
    "whitelisted": true,
    "bytessent_per_msg": {
      "addr": 0,
      "block": 0,
      "getaddr": 0,
      "getdata": 0,
      "getheaders": 0,
      "headers": 0,
      "inv": 0,
      "ping": 0,
      "pong": 0,
      "sendheaders": 0,
      "tx": 0,
      "verack": 0,
      "version": 0
    },
    "bytesrecv_per_msg": {
      "addr": 0,
      "block": 0,
      "getaddr": 0,
      "getdata": 0,
      "getheaders": 0,
      "headers": 0,
      "inv": 0,
      "ping": 0,
      "pong": 0,
      "sendheaders": 0,
      "tx": 0,
      "verack": 0,
      "version": 0
    }
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[PeerInfo](#schemapeerinfo)]|false|none|none|

<h2 id="tocSpeerinfo">PeerInfo</h2>

<a id="schemapeerinfo"></a>

```json
{
  "id": 0,
  "addr": "string",
  "addrlocal": "string",
  "services": "string",
  "relaytxes": true,
  "lastsend": 0,
  "lastrecv": 0,
  "bytessent": 0,
  "bytesrecv": 0,
  "conntime": 0,
  "timeoffset": 0,
  "pingtime": 0,
  "minping": 0,
  "version": 0,
  "subver": "string",
  "inbound": true,
  "startingheight": 0,
  "banscore": 0,
  "synced_headers": 0,
  "synced_blocks": 0,
  "inflight": [
    0
  ],
  "whitelisted": true,
  "bytessent_per_msg": {
    "addr": 0,
    "block": 0,
    "getaddr": 0,
    "getdata": 0,
    "getheaders": 0,
    "headers": 0,
    "inv": 0,
    "ping": 0,
    "pong": 0,
    "sendheaders": 0,
    "tx": 0,
    "verack": 0,
    "version": 0
  },
  "bytesrecv_per_msg": {
    "addr": 0,
    "block": 0,
    "getaddr": 0,
    "getdata": 0,
    "getheaders": 0,
    "headers": 0,
    "inv": 0,
    "ping": 0,
    "pong": 0,
    "sendheaders": 0,
    "tx": 0,
    "verack": 0,
    "version": 0
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|number|true|none|Peer index|
|addr|string|true|none|The ip address and port of the peer|
|addrlocal|string|true|none|local address|
|services|string|true|none|The services offered|
|relaytxes|boolean|true|none|Whether peer has asked us to relay transactions to it|
|lastsend|number|true|none|The time in seconds since epoch (Jan 1 1970 GMT) of the last send|
|lastrecv|number|true|none|The time in seconds since epoch (Jan 1 1970 GMT) of the last receive|
|bytessent|number|true|none|The total bytes sent|
|bytesrecv|number|true|none|The total bytes received|
|conntime|number|true|none|The connection time in seconds since epoch (Jan 1 1970 GMT)|
|timeoffset|number|true|none|The time offset in seconds|
|pingtime|number|true|none|ping time|
|minping|number|true|none|minimum observed ping time|
|version|number|true|none|The peer version, such as 7001|
|subver|string|true|none|The string version|
|inbound|boolean|true|none|Inbound (true) or Outbound (false)|
|startingheight|number|true|none|The starting height (block) of the peer|
|banscore|number|true|none|The ban score|
|synced_headers|number|true|none|The last header we have in common with this peer|
|synced_blocks|number|true|none|The last block we have in common with this peer|
|inflight|[number]|true|none|The heights of blocks we're currently asking from this peer|
|whitelisted|boolean|true|none|If this peer is whitelisted|
|bytessent_per_msg|[ByteMessageInfo](#schemabytemessageinfo)|true|none|none|
|bytesrecv_per_msg|[ByteMessageInfo](#schemabytemessageinfo)|true|none|none|

<h2 id="tocSbytemessageinfo">ByteMessageInfo</h2>

<a id="schemabytemessageinfo"></a>

```json
{
  "addr": 0,
  "block": 0,
  "getaddr": 0,
  "getdata": 0,
  "getheaders": 0,
  "headers": 0,
  "inv": 0,
  "ping": 0,
  "pong": 0,
  "sendheaders": 0,
  "tx": 0,
  "verack": 0,
  "version": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|addr|number|true|none|none|
|block|number|false|none|none|
|getaddr|number|false|none|none|
|getdata|number|false|none|none|
|getheaders|number|true|none|none|
|headers|number|true|none|none|
|inv|number|true|none|none|
|ping|number|true|none|none|
|pong|number|true|none|none|
|sendheaders|number|true|none|none|
|tx|number|false|none|none|
|verack|number|true|none|none|
|version|number|true|none|none|

<h2 id="tocSvalidateaddressresponse">ValidateAddressResponse</h2>

<a id="schemavalidateaddressresponse"></a>

```json
{
  "address": "address",
  "isscript": true,
  "iscompressed": true,
  "ismine": true,
  "isvalid": true,
  "iswatchonly": true,
  "account": "account",
  "pubkey": "pubkey"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|isvalid|boolean|false|none|If the address is valid or not. If not, this is the only property returned.|
|address|string|false|none|The syscoin address validated|
|ismine|boolean|false|none|If the address is yours or not|
|iswatchonly|boolean|false|none|If the address is watchonly|
|isscript|boolean|false|none|If the key is a script|
|pubkey|string|false|none|The hex value of the raw public key|
|iscompressed|boolean|false|none|If the address is compressed|
|account|string|false|none|DEPRECATED. The account associated with the address, "" is the default account|

<h2 id="tocSerrorresponse">ErrorResponse</h2>

<a id="schemaerrorresponse"></a>

```json
{
  "message": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|true|none|none|

<h2 id="tocSalias">Alias</h2>

<a id="schemaalias"></a>

```json
{
  "publicvalue": "publicvalue",
  "address": "address",
  "expired": true,
  "encryption_privatekey": "encryption_privatekey",
  "expires_on": 1.4658129805029452,
  "txid": "txid",
  "_id": "_id",
  "time": 0.8008281904610115,
  "encryption_publickey": "encryption_publickey",
  "accepttransferflags": 6.027456183070403
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_id|string|true|none|none|
|encryption_privatekey|string|false|none|none|
|encryption_publickey|string|false|none|none|
|publicvalue|string|false|none|none|
|txid|string|false|none|none|
|time|number|false|none|none|
|address|string|false|none|none|
|accepttransferflags|number|false|none|none|
|expires_on|number|false|none|none|
|expired|boolean|false|none|none|

<h2 id="tocScert">Cert</h2>

<a id="schemacert"></a>

```json
{
  "publicvalue": "publicvalue",
  "expired": true,
  "expires_on": 5.962133916683182,
  "txid": "txid",
  "alias": "alias",
  "_id": "_id",
  "time": 6.027456183070403,
  "access_flags": 1.4658129805029452,
  "title": "title",
  "category": "category",
  "height": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_id|string|false|none|none|
|txid|string|false|none|none|
|height|number|false|none|none|
|time|number|false|none|none|
|title|string|false|none|none|
|publicvalue|string|false|none|none|
|category|string|false|none|none|
|alias|string|false|none|none|
|access_flags|number|false|none|none|
|expires_on|number|false|none|none|
|expired|boolean|false|none|none|

<h2 id="tocSescrow">Escrow</h2>

<a id="schemaescrow"></a>

```json
{
  "seller": "seller",
  "total_without_fee": 2.3021358869347655,
  "role": 6.84685269835264,
  "acknowledged": true,
  "redeem_txid": "redeem_txid",
  "offer_title": 1.4658129805029452,
  "offer": "offer",
  "expired": true,
  "shipping": 1.2315135367772556,
  "arbiterfee": 2.027123023002322,
  "commission": 3.616076749251911,
  "currency": "currency",
  "escrowaddress": "escrowaddress",
  "height": 1.4894159098541704,
  "total_with_fee": 5.637376656633329,
  "quantity": 5.962133916683182,
  "witnessfee": 7.386281948385884,
  "total_or_bid_in_payment_option_per_unit": 9.301444243932576,
  "paymentoption": "paymentoption",
  "networkfee": 4.145608029883936,
  "reseller": "reseller",
  "txid": "txid",
  "buyer": "buyer",
  "offer_price": 6.027456183070403,
  "witness": "witness",
  "arbiter": "arbiter",
  "buynow": true,
  "exttxid": "exttxid",
  "deposit": 1.0246457001441578,
  "redeem_script": "redeem_script",
  "_id": "_id",
  "time": 0.8008281904610115,
  "bid_in_offer_currency_per_unit": 7.061401241503109,
  "status": 7.457744773683766
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_id|string|false|none|none|
|time|number|false|none|none|
|seller|string|false|none|none|
|arbiter|string|false|none|none|
|buyer|string|false|none|none|
|witness|string|false|none|none|
|offer|string|false|none|none|
|offer_price|number|false|none|none|
|offer_title|number|false|none|none|
|reseller|string|false|none|none|
|quantity|number|false|none|none|
|total_with_fee|number|false|none|none|
|total_without_fee|number|false|none|none|
|bid_in_offer_currency_per_unit|number|false|none|none|
|total_or_bid_in_payment_option_per_unit|number|false|none|none|
|buynow|boolean|false|none|none|
|commission|number|false|none|none|
|arbiterfee|number|false|none|none|
|networkfee|number|false|none|none|
|witnessfee|number|false|none|none|
|shipping|number|false|none|none|
|deposit|number|false|none|none|
|currency|string|false|none|none|
|exttxid|string|false|none|none|
|escrowaddress|string|false|none|none|
|paymentoption|string|false|none|none|
|redeem_txid|string|false|none|none|
|redeem_script|string|false|none|none|
|txid|string|false|none|none|
|height|number|false|none|none|
|role|number|false|none|none|
|expired|boolean|false|none|none|
|acknowledged|boolean|false|none|none|
|status|number|false|none|none|

<h2 id="tocSescrowrefundrequest">EscrowRefundRequest</h2>

<a id="schemaescrowrefundrequest"></a>

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx",
  "userrole": "userrole"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|escrowguid|string|true|none|Escrow ID|
|userrole|string|true|none|User role represents either 'seller' or 'arbiter'|
|rawtx|string|true|none|signed response from escrowreleasecreaterawtransaction.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSescrowreleaserequest">EscrowReleaseRequest</h2>

<a id="schemaescrowreleaserequest"></a>

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx",
  "userrole": "userrole"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|escrowguid|string|true|none|Escrow ID|
|userrole|string|true|none|User role represents either 'buyer' or 'arbiter'.|
|rawtx|string|true|none|Signed response from escrowcreaterawtransaction.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocStransaction">Transaction</h2>

<a id="schematransaction"></a>

```json
{
  "amount": "amount",
  "blockhash": "blockhash",
  "timereceived": 5.637376656633329,
  "blocktime": 1.4658129805029452,
  "txid": "txid",
  "details": [
    {
      "amount": 2.3021358869347655,
      "address": "address",
      "label": "label",
      "category": "category",
      "account": "account",
      "vout": 7.061401241503109
    },
    {
      "amount": 2.3021358869347655,
      "address": "address",
      "label": "label",
      "category": "category",
      "account": "account",
      "vout": 7.061401241503109
    }
  ],
  "hex": "hex",
  "time": 5.962133916683182,
  "confirmations": 0.8008281904610115,
  "blockindex": 6.027456183070403
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|amount|string|false|none|The transaction amount in SYS|
|confirmations|number|false|none|The number of confirmations|
|blockhash|string|false|none|The block hash|
|blockindex|number|false|none|The block index|
|blocktime|number|false|none|The time in seconds since epoch (1 Jan 1970 GMT)|
|txid|string|false|none|The transaction id.|
|time|number|false|none|The transaction time in seconds since epoch (1 Jan 1970 GMT)|
|timereceived|number|false|none|The time received in seconds since epoch (1 Jan 1970 GMT)|
|details|[[TransactionDetailEntry](#schematransactiondetailentry)]|false|none|none|
|hex|string|false|none|Raw data for transaction|

<h2 id="tocStransactiondetailentry">TransactionDetailEntry</h2>

<a id="schematransactiondetailentry"></a>

```json
{
  "amount": 2.3021358869347655,
  "address": "address",
  "label": "label",
  "category": "category",
  "account": "account",
  "vout": 7.061401241503109
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|account|string|false|none|DEPRECATED. The account name involved in the transaction, can be "" for the default account.|
|address|string|false|none|The syscoin address involved in the transaction|
|category|string|false|none|The category, either 'send' or 'receive'|
|amount|number|false|none|The amount in SYS|
|label|string|false|none|A comment for the address/transaction, if any|
|vout|number|false|none|the vout value|

<h2 id="tocSwalletinfo">WalletInfo</h2>

<a id="schemawalletinfo"></a>

```json
{
  "walletversion": 0.8008281904610115,
  "balance": 6.027456183070403,
  "txcount": 5.637376656633329,
  "keypoololdest": 2.3021358869347655,
  "unconfirmed_balance": 1.4658129805029452,
  "immature_balance": 5.962133916683182,
  "keypoolsize": 7.061401241503109,
  "unlocked_until": 9.301444243932576,
  "paytxfee": 3.616076749251911
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|walletversion|number|false|none|the wallet version|
|balance|number|false|none|the total confirmed balance of the wallet in SYS|
|unconfirmed_balance|number|false|none|the total unconfirmed balance of the wallet in SYS|
|immature_balance|number|false|none|the total immature balance of the wallet in SYS|
|txcount|number|false|none|the total number of transactions in the wallet|
|keypoololdest|number|false|none|the timestamp (seconds since GMT epoch) of the oldest pre-generated key in the key pool|
|keypoolsize|number|false|none|how many new keys are pre-generated|
|unlocked_until|number|false|none|the timestamp in seconds since epoch (midnight Jan 1 1970 GMT) that the wallet is unlocked for transfers, or 0 if the wallet is locked|
|paytxfee|number|false|none|the transaction fee configuration, set in SYS/kB|

<h2 id="tocSaddressgrouping">AddressGrouping</h2>

<a id="schemaaddressgrouping"></a>

```json
{
  "amount": 0.8008281904610115,
  "syscoinaddress": "syscoinaddress"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|syscoinaddress|string|false|none|The syscoin address|
|amount|number|false|none|The amount in SYS|

<h2 id="tocSaccount">Account</h2>

<a id="schemaaccount"></a>

```json
{
  "amount": 0.8008281904610115,
  "involvesWatchonly": true,
  "label": "label",
  "confirmations": 6.027456183070403,
  "account": "account"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|involvesWatchonly|boolean|false|none|Only returned if imported addresses were involved in transaction|
|account|string|false|none|The account name of the receiving account|
|amount|number|false|none|The total amount received by addresses with this account|
|confirmations|number|false|none|The number of confirmations of the most recent transaction included|
|label|string|false|none|A comment for the address/transaction, if any|

<h2 id="tocSlistsinceblockresponse">ListSinceBlockResponse</h2>

<a id="schemalistsinceblockresponse"></a>

```json
{
  "lastblock": "lastblock",
  "transactions": [
    {
      "amount": 0.8008281904610115,
      "address": "address",
      "fee": 1.4658129805029452,
      "txid": "txid",
      "label": "label",
      "confirmations": 5.962133916683182,
      "vout": 6.027456183070403,
      "blockhash": "blockhash",
      "timereceived": 9.301444243932576,
      "blocktime": 2.3021358869347655,
      "comment": "comment",
      "time": 7.061401241503109,
      "to": "to",
      "category": "category",
      "blockindex": 5.637376656633329,
      "account": "account"
    },
    {
      "amount": 0.8008281904610115,
      "address": "address",
      "fee": 1.4658129805029452,
      "txid": "txid",
      "label": "label",
      "confirmations": 5.962133916683182,
      "vout": 6.027456183070403,
      "blockhash": "blockhash",
      "timereceived": 9.301444243932576,
      "blocktime": 2.3021358869347655,
      "comment": "comment",
      "time": 7.061401241503109,
      "to": "to",
      "category": "category",
      "blockindex": 5.637376656633329,
      "account": "account"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transactions|[[SinceBlockTransactionEntry](#schemasinceblocktransactionentry)]|false|none|none|
|lastblock|string|false|none|The hash of the last block|

<h2 id="tocSsinceblocktransactionentry">SinceBlockTransactionEntry</h2>

<a id="schemasinceblocktransactionentry"></a>

```json
{
  "amount": 0.8008281904610115,
  "address": "address",
  "fee": 1.4658129805029452,
  "txid": "txid",
  "label": "label",
  "confirmations": 5.962133916683182,
  "vout": 6.027456183070403,
  "blockhash": "blockhash",
  "timereceived": 9.301444243932576,
  "blocktime": 2.3021358869347655,
  "comment": "comment",
  "time": 7.061401241503109,
  "to": "to",
  "category": "category",
  "blockindex": 5.637376656633329,
  "account": "account"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|account|string|false|none|DEPRECATED. The account name associated with the transaction. Will be "" for the default account.|
|address|string|false|none|The syscoin address of the transaction. Not present for move transactions (category = move).|
|category|string|false|none|The transaction category. 'send' has negative amounts, 'receive' has positive amounts.|
|amount|number|false|none|The amount in SYS. This is negative for the 'send' category, and for the 'move' category for moves outbound. It is positive for the 'receive' category, and for the 'move' category for inbound funds.|
|vout|number|false|none|the vout value|
|fee|number|false|none|The amount of the fee in SYS. This is negative and only available for the 'send' category of transactions.|
|confirmations|number|false|none|The number of confirmations for the transaction. Available for 'send' and 'receive' category of transactions.|
|blockhash|string|false|none|The block hash containing the transaction. Available for 'send' and 'receive' category of transactions.|
|blockindex|number|false|none|The block index containing the transaction. Available for 'send' and 'receive' category of transactions.|
|blocktime|number|false|none|The block time in seconds since epoch (1 Jan 1970 GMT).|
|txid|string|false|none|The transaction id. Available for 'send' and 'receive' category of transactions.|
|time|number|false|none|The transaction time in seconds since epoch (Jan 1 1970 GMT).|
|timereceived|number|false|none|The time received in seconds since epoch (Jan 1 1970 GMT). Available for 'send' and 'receive' category of transactions.|
|comment|string|false|none|If a comment is associated with the transaction.|
|label|string|false|none|A comment for the address/transaction, if any|
|to|string|false|none|If a comment to is associated with the transaction.|

<h2 id="tocSunspentlistentry">UnspentListEntry</h2>

<a id="schemaunspentlistentry"></a>

```json
{
  "scriptPubKey": "scriptPubKey",
  "amount": 6.027456183070403,
  "ps_rounds": 5.962133916683182,
  "spendable": true,
  "solvable": true,
  "address": "address",
  "txid": "txid",
  "confirmations": 1.4658129805029452,
  "account": "account",
  "vout": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txid|string|false|none|The transaction id|
|vout|number|false|none|The vout value|
|address|string|false|none|The syscoin address|
|account|string|false|none|DEPRECATED. The associated account, or "" for the default account|
|scriptPubKey|string|false|none|The script key|
|amount|number|false|none|The transaction amount in SYS|
|confirmations|number|false|none|The number of confirmations|
|ps_rounds|number|false|none|The number of PS round|
|spendable|boolean|false|none|Whether we have the private keys to spend this output|
|solvable|boolean|false|none|Whether we know how to spend this output, ignoring the lack of keys|

<h2 id="tocStransactionlistentry">TransactionListEntry</h2>

<a id="schematransactionlistentry"></a>

```json
{
  "amount": 0.8008281904610115,
  "address": "address",
  "instantlock": true,
  "bip125-replaceable": "bip125-replaceable",
  "fee": 1.4658129805029452,
  "txid": "txid",
  "label": "label",
  "otheraccount": "otheraccount",
  "confirmations": 5.962133916683182,
  "vout": 6.027456183070403,
  "blockhash": "blockhash",
  "timereceived": 9.301444243932576,
  "trusted": true,
  "blocktime": 2.3021358869347655,
  "comment": "comment",
  "time": 7.061401241503109,
  "category": "category",
  "blockindex": 5.637376656633329,
  "account": "account"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|account|string|false|none|DEPRECATED. The account name associated with the transaction. It will be "" for the default account.|
|address|string|false|none|The syscoin address of the transaction. Not present for move transactions (category = move).|
|category|string|false|none|The transaction category. 'move' is a local (off blockchain) transaction between accounts, and not associated with an address, transaction id or block. 'send' and 'receive' transactions are associated with an address, transaction id and block details. Example values&#58; 'send|receive|move'|
|amount|number|false|none|The amount in SYS. This is negative for the 'send' category, and for the 'move' category for moves outbound. It is positive for the 'receive' category, and for the 'move' category for inbound funds.|
|vout|number|false|none|the vout value|
|fee|number|false|none|The amount of the fee in SYS. This is negative and only available for the 'send' category of transactions.|
|instantlock|boolean|false|none|Current transaction lock state. Available for 'send' and 'receive' category of transactions.|
|confirmations|number|false|none|The number of blockchain confirmations for the transaction. Available for 'send' and 'receive' category of transactions. Negative confirmations indicate the transation conflicts with the block chain|
|trusted|boolean|false|none|Whether we consider the outputs of this unconfirmed transaction safe to spend.|
|blockhash|string|false|none|The block hash containing the transaction. Available for 'send' and 'receive' category of transactions.|
|blockindex|number|false|none|The index of the transaction in the block that includes it. Available for 'send' and 'receive' category of transactions.|
|blocktime|number|false|none|The block time in seconds since epoch (1 Jan 1970 GMT).|
|txid|string|false|none|The transaction id. Available for 'send' and 'receive' category of transactions.|
|time|number|false|none|The transaction time in seconds since epoch (midnight Jan 1 1970 GMT).|
|timereceived|number|false|none|The time received in seconds since epoch (midnight Jan 1 1970 GMT). Available for 'send' and 'receive' category of transactions.|
|comment|string|false|none|If a comment is associated with the transaction.|
|label|string|false|none|A comment for the address/transaction, if any|
|otheraccount|string|false|none|For the 'move' category of transactions, the account the funds came from (for receiving funds, positive amounts), or went to (for sending funds, negative amounts).|
|bip125-replaceable|string|false|none|Whether this transaction could be replaced due to BIP125 (replace-by-fee); may be unknown for unconfirmed transactions not in the mempool. Example&#58; "yes|no|unknown"|

<h2 id="tocSmessage">Message</h2>

<a id="schemamessage"></a>

```json
{
  "GUID": "string",
  "txid": "string",
  "time": 0,
  "from": "string",
  "to": "string",
  "subject": "string",
  "message": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|GUID|string|false|none|none|
|txid|string|false|none|none|
|time|number|false|none|none|
|from|string|false|none|none|
|to|string|false|none|none|
|subject|string|false|none|none|
|message|string|false|none|none|

<h2 id="tocSofferaccept">OfferAccept</h2>

<a id="schemaofferaccept"></a>

```json
{
  "offer": "string",
  "id": "string",
  "txid": "string",
  "title": "string",
  "exttxid": "string",
  "paymentoption": 0,
  "paymentoption_display": "string",
  "height": 0,
  "time": "string",
  "quantity": 0,
  "currency": "string",
  "offer_discount_percentage": 0,
  "systotal": 0,
  "sysprice": 0,
  "price": 0,
  "total": 0,
  "buyer": "string",
  "seller": "string",
  "ismine": true,
  "status": "string",
  "buyer_fedback": [
    "string"
  ],
  "seller_fedback": [
    "string"
  ],
  "avg_rating": 0,
  "avg_rating_display": "string",
  "pay_message": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|offer|string|false|none|none|
|id|string|false|none|none|
|txid|string|false|none|none|
|title|string|false|none|none|
|exttxid|string|false|none|none|
|paymentoption|number|false|none|none|
|paymentoption_display|string|false|none|none|
|height|number|false|none|none|
|time|string|false|none|none|
|quantity|number|false|none|none|
|currency|string|false|none|none|
|offer_discount_percentage|number|false|none|none|
|systotal|number|false|none|none|
|sysprice|number|false|none|none|
|price|number|false|none|none|
|total|number|false|none|none|
|buyer|string|false|none|none|
|seller|string|false|none|none|
|ismine|boolean|false|none|none|
|status|string|false|none|none|
|buyer_fedback|[string]|false|none|none|
|seller_fedback|[string]|false|none|none|
|avg_rating|number|false|none|none|
|avg_rating_display|string|false|none|none|
|pay_message|string|false|none|none|

<h2 id="tocSofferwhitelistentry">OfferWhitelistEntry</h2>

<a id="schemaofferwhitelistentry"></a>

```json
{
  "alias": "string",
  "expiresin": 0,
  "offer_discount_percentage": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|false|none|none|
|expiresin|number|false|none|none|
|offer_discount_percentage|number|false|none|none|

<h2 id="tocSoffer">Offer</h2>

<a id="schemaoffer"></a>

```json
{
  "auction_expires_on": 7.061401241503109,
  "offer_units": 5.637376656633329,
  "expires_on": 0.8008281904610115,
  "description": "description",
  "cert": "cert",
  "title": "title",
  "auction_deposit": 3.616076749251911,
  "expired": true,
  "price": 1.4658129805029452,
  "alias": "alias",
  "currency": "currency",
  "commission": 5.962133916683182,
  "auction_require_witness": true,
  "height": 6.027456183070403,
  "offertype": "offertype",
  "quantity": 2.3021358869347655,
  "address": "address",
  "txid": "txid",
  "privatevalue": true,
  "offerlink_guid": "offerlink_guid",
  "paymentoptions": "paymentoptions",
  "offerlink_seller": "offerlink_seller",
  "auction_reserve_price": 9.301444243932576,
  "_id": "_id",
  "category": "category"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_id|string|true|none|none|
|cert|string|false|none|none|
|txid|string|false|none|none|
|expires_on|number|false|none|none|
|expired|boolean|false|none|none|
|height|number|false|none|none|
|category|string|false|none|none|
|title|string|false|none|none|
|currency|string|false|none|none|
|price|number|false|none|none|
|commission|number|false|none|none|
|offerlink_guid|string|false|none|none|
|offerlink_seller|string|false|none|none|
|paymentoptions|string|false|none|none|
|offer_units|number|false|none|none|
|quantity|number|false|none|none|
|privatevalue|boolean|false|none|none|
|description|string|false|none|none|
|alias|string|false|none|none|
|address|string|false|none|none|
|offertype|string|false|none|none|
|auction_expires_on|number|false|none|none|
|auction_reserve_price|number|false|none|none|
|auction_require_witness|boolean|false|none|none|
|auction_deposit|number|false|none|none|

<h2 id="tocSaddmultisigaddressrequest">AddMultisigAddressRequest</h2>

<a id="schemaaddmultisigaddressrequest"></a>

```json
{
  "nrequired": 0.8008281904610115,
  "keysobject": "keysobject",
  "account": "account"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nrequired|number|true|none|The number of required signatures out of the n keys or addresses.|
|keysobject|string|true|none|A json array of syscoin addresses or hex-encoded public keys. [ "address"  (string) syscoin address or hex-encoded public key ... ]|
|account|string|false|none|DEPRECATED. An account to assign the addresses to.|

<h2 id="tocSaliasclearwhitelistrequest">AliasClearWhiteListRequest</h2>

<a id="schemaaliasclearwhitelistrequest"></a>

```json
{
  "witness": "witness",
  "owneralias": "owneralias"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|owneralias|string|true|none|your alias|
|witness|string|true|none|a witness alias|

<h2 id="tocSaliasupdatewhitelistrequest">AliasUpdateWhitelistRequest</h2>

<a id="schemaaliasupdatewhitelistrequest"></a>

```json
{
  "witness": "witness",
  "entries": [
    {
      "alias": "alias",
      "discount_percentage": 0.8008281904610115
    },
    {
      "alias": "alias",
      "discount_percentage": 0.8008281904610115
    }
  ],
  "owneralias": "owneralias"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|owneralias|string|true|none|owner alias controlling this whitelist.|
|entries|[[WhitelistEntry](#schemawhitelistentry)]|true|none|"entries"       (string) A json array of whitelist entries to add/remove/update [ "alias"     (string) Alias that you want to add to the affiliate whitelist. Can be * to represent that the offers owned by owner alias can be resold by anybody "discount_percentage"     (number) A discount percentage associated with this alias. The reseller can sell your offer at this discount, not accounting for any commissions he/she may set in his own reselling offer. 0 to 99. ,... ]|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSaliasnewrequest">AliasNewRequest</h2>

<a id="schemaaliasnewrequest"></a>

```json
{
  "witness": "witness",
  "aliasname": "aliasname",
  "publicvalue": "publicvalue",
  "address": "address",
  "encryption_privatekey": "encryption_privatekey",
  "expire_timestamp": 6.027456183070403,
  "encryption_publickey": "encryption_publickey",
  "accept_transfers_flags": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|aliasname|string|true|none|Alias name|
|publicvalue|string|true|none|alias public profile data, 256 characters max.|
|accept_transfers_flags|number|true|none|0 for none, 1 for accepting certificate transfers, 2 for accepting asset transfers and 3 for all. Default is 3.|
|expire_timestamp|number|true|none|Epoch time when to expire alias. It is exponentially more expensive per year, calculation is FEERATE*(2.88^years). FEERATE is the dynamic satoshi per byte fee set in the rate peg alias used for this alias. Defaults to 1 hour.|
|address|string|true|none|Address for this alias.|
|encryption_privatekey|string|true|none|Encrypted private key used for encryption decryption of private data related to this alias. Should be encrypted to publickey.|
|encryption_publickey|string|true|none|Public key used for encryption decryption of private data related to this alias.|
|witness|string|true|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSaliasupdaterequest">AliasUpdateRequest</h2>

<a id="schemaaliasupdaterequest"></a>

```json
{
  "witness": "witness",
  "aliasname": "aliasname",
  "publicvalue": "publicvalue",
  "address": "address",
  "encryption_privatekey": "encryption_privatekey",
  "expire_timestamp": 6,
  "encryption_publickey": "encryption_publickey",
  "accept_transfers_flags": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|aliasname|string|true|none|Alias name|
|publicvalue|string|false|none|alias public profile data, 256 characters max.|
|accept_transfers_flags|integer|false|none|0 for none, 1 for accepting certificate transfers, 2 for accepting asset transfers and 3 for all. Default is 3.|
|expire_timestamp|integer|false|none|Epoch time when to expire alias. It is exponentially more expensive per year, calculation is FEERATE*(2.88^years). FEERATE is the dynamic satoshi per byte fee set in the rate peg alias used for this alias. Defaults to 1 hour.|
|address|string|true|none|Address for this alias.|
|encryption_privatekey|string|false|none|Encrypted private key used for encryption decryption of private data related to this alias. Should be encrypted to publickey.|
|encryption_publickey|string|false|none|Public key used for encryption decryption of private data related to this alias.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocScertnewrequest">CertNewRequest</h2>

<a id="schemacertnewrequest"></a>

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "alias": "alias",
  "title": "title",
  "category": "category"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|true|none|An alias you own.|
|title|string|true|none|title, 256 bytes max.|
|publicvalue|string|false|none|public data, 256 characters max.|
|category|string|true|none|category, 25 characters max. Defaults to certificates;|
|witness|string|true|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocScerttransferrequest">CertTransferRequest</h2>

<a id="schemacerttransferrequest"></a>

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "accessflags": 0.8008281904610115,
  "guid": "guid",
  "alias": "alias"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|guid|string|true|none|Certificate guidkey.|
|alias|string|true|none|Alias to transfer this certificate to.|
|publicvalue|string|false|none|public data, 256 characters max.|
|accessflags|number|false|none|Set new access flags for new owner for this certificate, 0 for read-only, 1 for edit, 2 for edit and transfer access. Default is 2.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocScertupdaterequest">CertUpdateRequest</h2>

<a id="schemacertupdaterequest"></a>

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "guid": "guid",
  "title": "title",
  "category": "category"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|guid|string|true|none|certificate guidkey.|
|title|string|true|none|certificate title, 255 bytes max.|
|publicvalue|string|false|none|Public certificate data, 1024 characters max.|
|category|string|false|none|category, 256 characters max. Defaults to "certificates"|
|witness|string|true|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSescrowclaimrefundrequest">EscrowClaimRefundRequest</h2>

<a id="schemaescrowclaimrefundrequest"></a>

```json
{
  "guid": "string",
  "rawtx": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|guid|string|true|none|none|
|rawtx|string|false|none|none|

<h2 id="tocSescrowclaimreleaserequest">EscrowClaimReleaseRequest</h2>

<a id="schemaescrowclaimreleaserequest"></a>

```json
{
  "guid": "string",
  "rawtx": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|guid|string|true|none|none|
|rawtx|string|false|none|none|

<h2 id="tocSescrowcompleterefundrequest">EscrowCompleteRefundRequest</h2>

<a id="schemaescrowcompleterefundrequest"></a>

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|escrowguid|string|true|none|Escrow ID|
|rawtx|string|true|none|Raw fully signed syscoin escrow transaction. It is the signed response from escrowcreaterawtransaction. You must sign this transaction externally prior to passing in.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSescrowcompletereleaserequest">EscrowCompleteReleaseRequest</h2>

<a id="schemaescrowcompletereleaserequest"></a>

```json
{
  "witness": "witness",
  "escrowguid": "escrowguid",
  "rawtx": "rawtx"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|escrowguid|string|true|none|Escrow ID|
|rawtx|string|true|none|Raw fully signed syscoin escrow transaction. It is the signed response from escrowcreaterawtransaction. You must sign this transaction externally prior to passing in.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSescrownewrequest">EscrowNewRequest</h2>

<a id="schemaescrownewrequest"></a>

```json
{
  "bid_in_offer_currency": 9.301444243932576,
  "extTx": "extTx",
  "quantity": 0,
  "total_in_payment_option": 6.027456183070403,
  "paymentoption": "paymentoption",
  "witness_fee": 2.3021358869347655,
  "arbiter_alias": "arbiter_alias",
  "bid_in_payment_option": 7.061401241503109,
  "network_fee": 5.962133916683182,
  "offer": "offer",
  "shipping_amount": 1.4658129805029452,
  "witness": "witness",
  "buynow": true,
  "alias": "alias",
  "arbiter_fee": 5.637376656633329,
  "getamountandaddress": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|getamountandaddress|boolean|true|none|True or false. Get deposit and total escrow amount aswell as escrow address for funding. If buynow is false pass bid amount in bid_in_payment_option to get total needed to complete escrow. If buynow is true amount is calculated based on offer price and quantity.|
|alias|string|true|none|An alias you own.|
|arbiter_alias|string|true|none|Alias of Arbiter.|
|offer|string|true|none|GUID of offer that this escrow is managing.|
|quantity|integer|true|none|Quantity of items to buy of offer.|
|buynow|boolean|true|none|Specify whether the escrow involves purchasing offer for the full offer price if set to true, or through a bidding auction if set to false. If buynow is false, an initial deposit may be used to secure a bid if required by the seller.|
|total_in_payment_option|number|true|none|Total amount of the offer price. Amount is in paymentOption currency. It is per unit of purchase.|
|shipping_amount|number|true|none|Amount to add to shipping for merchant. Amount is in paymentOption currency. Example; If merchant requests 0.1 BTC for shipping and escrow is paid in BTC, enter 0.1 here. Default is 0. Buyer can also add shipping using escrowaddshipping upon merchant request.|
|network_fee|number|true|none|Network fee in satoshi per byte for the transaction. Generally the escrow transaction is about 400 bytes. Default is 25 for SYS or ZEC and 250 for BTC payments|
|arbiter_fee|number|true|none|Arbiter fee in fractional amount of the amount_in_payment_option value. For example 0.75% is 0.0075 and represents 0.0075*amount_in_payment_option satoshis paid to arbiter in the event arbiter is used to resolve a dispute. Default and minimum is 0.005.|
|witness_fee|number|true|none|Witness fee in fractional amount of the amount_in_payment_option value. For example 0.3% is 0.003 and represents 0.003*amount_in_payment_option satoshis paid to witness in the event witness signs off on an escrow through any of the following calls escrownew/escrowbid/escrowrelease/escrowrefund. Default is 0|
|extTx|string|true|none|External transaction ID if paid with another blockchain.|
|paymentoption|string|true|none|If extTx is defined, specify a valid payment option used to make payment. Default is SYS.|
|bid_in_payment_option|number|true|none|Initial bid amount you are willing to pay escrow for this offer. Amount is in paymentOption currency. It is per unit of purchase. If buynow is set to true, this value is disregarded.|
|bid_in_offer_currency|number|true|none|Converted value of bid_in_payment_option from paymentOption currency to offer currency. For example; offer is priced in USD and purchased in BTC, this field will be the BTC/USD value. If buynow is set to true, this value is disregarded.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSaliaspayrequest">AliasPayRequest</h2>

<a id="schemaaliaspayrequest"></a>

```json
{
  "amounts": "{\"alias1\":0.02,\"alias2\":0.4,\"alias3\":0.004}",
  "instantsend": false,
  "aliasfrom": "aliasfrom",
  "subtractfeefromamount": [
    "alias1",
    "alias2"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|aliasfrom|string|true|none|Alias to pay from|
|amounts|[AliasPayRequest_amounts](#schemaaliaspayrequest_amounts)|true|none|none|
|instantsend|boolean|false|none|Set to true to use InstantSend to send this transaction or false otherwise.|
|subtractfeefromamount|[string]|false|none|An addresses array to subtract fee from them.|

<h2 id="tocSgetnewaddressrequest">GetNewAddressRequest</h2>

<a id="schemagetnewaddressrequest"></a>

```json
{
  "account": "account"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|account|string|false|none|DEPRECATED. The account name for the address to be linked to. If not provided, the default account "" is used. It can also be set to the empty string "" to represent the default account. The account does not need to exist, it will be created if there is no account by the given name.|

<h2 id="tocSimportaddressrequest">ImportAddressRequest</h2>

<a id="schemaimportaddressrequest"></a>

```json
{
  "p2sh": true,
  "label": "label",
  "rescan": true,
  "script": "script"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|script|string|true|none|The hex-encoded script (or address)|
|label|string|false|none|An optional label|
|rescan|boolean|false|none|Rescan the wallet for transactions|
|p2sh|boolean|false|none|Add the P2SH version of the script as well|

<h2 id="tocSimportprivkeyrequest">ImportPrivKeyRequest</h2>

<a id="schemaimportprivkeyrequest"></a>

```json
{
  "syscoinprivkey": "syscoinprivkey",
  "label": "label",
  "rescan": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|syscoinprivkey|string|true|none|The private key (see dumpprivkey)|
|label|string|false|none|An optional label|
|rescan|boolean|false|none|Rescan the wallet for transactions|

<h2 id="tocSimportpubkeyrequest">ImportPubKeyRequest</h2>

<a id="schemaimportpubkeyrequest"></a>

```json
{
  "label": "label",
  "rescan": true,
  "pubkey": "pubkey"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pubkey|string|true|none|The hex-encoded public key|
|label|string|false|none|An optional label|
|rescan|boolean|false|none|Rescan the wallet for transactions|

<h2 id="tocSimportwalletrequest">ImportWalletRequest</h2>

<a id="schemaimportwalletrequest"></a>

```json
{
  "filename": "filename"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|filename|string|true|none|The wallet file|

<h2 id="tocSmessagenewrequest">MessageNewRequest</h2>

<a id="schemamessagenewrequest"></a>

```json
{
  "subject": "string",
  "fromalias": "string",
  "toalias": "string",
  "frommessage": "string",
  "tomessage": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subject|string|true|none|Subject of message.|
|fromalias|string|true|none|Alias to send message from.|
|toalias|string|true|none|Alias to send message to.|
|frommessage|string|true|none|Message encrypted to from alias.|
|tomessage|string|true|none|Message encrypted to sending alias.|

<h2 id="tocSmoverequest">MoveRequest</h2>

<a id="schemamoverequest"></a>

```json
{
  "fromaccount": "fromaccount",
  "amount": 0.8008281904610115,
  "minconf": "minconf",
  "toaccount": "toaccount",
  "comment": "comment"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|fromaccount|string|true|none|The name of the account to move funds from. May be the default account using "".|
|toaccount|string|true|none|The name of the account to move funds to. May be the default account using "".|
|amount|number|true|none|Quantity of SYS to move between accounts.|
|minconf|string|false|none|Only use funds with at least this many confirmations.|
|comment|string|false|none|An optional comment, stored in the wallet only.|

<h2 id="tocSofferacceptrequest">OfferAcceptRequest</h2>

<a id="schemaofferacceptrequest"></a>

```json
{
  "alias": "string",
  "guid": "string",
  "quantity": 0,
  "message": "string",
  "exttxid": "string",
  "paymentoption": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|true|none|An alias of the buyer.|
|guid|string|true|none|guidkey from offer.|
|quantity|number|false|none|quantity to buy. Defaults to 1.|
|message|string|false|none|payment message to seller, 1KB max.|
|exttxid|string|false|none|If paid in another coin, enter the Transaction ID here. Default is empty.|
|paymentoption|string|false|none|If Ext TxId is defined, specify a valid payment option used to make payment. Default is SYS.|

<h2 id="tocSofferaddwhitelistrequest">OfferAddWhitelistRequest</h2>

<a id="schemaofferaddwhitelistrequest"></a>

```json
{
  "offerguid": "string",
  "aliasguid": "string",
  "discountPercentage": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|offerguid|string|true|none|offer guid that you are adding to|
|aliasguid|string|true|none|alias guid representing an alias that you want to add to the affiliate list|
|discountPercentage|number|false|none|Percentage of discount given to affiliate for this offer. 0 to 99.|

<h2 id="tocSofferclearwhitelistrequest">OfferClearWhitelistRequest</h2>

<a id="schemaofferclearwhitelistrequest"></a>

```json
{
  "offerguid": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|offerguid|string|true|none|none|

<h2 id="tocSofferlinkrequest">OfferLinkRequest</h2>

<a id="schemaofferlinkrequest"></a>

```json
{
  "witness": "witness",
  "alias": "alias",
  "guid": "guid",
  "description": "description",
  "commission": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|true|none|An alias you own.|
|guid|string|true|none|offer guid that you are linking to|
|commission|number|true|none|percentage of profit desired over original offer price, > 0, ie 5 for 5%|
|description|string|false|none|description, 1 KB max. Defaults to original description. Leave as '' to use default.|
|witness|string|false|none|witness if any.  Leave '' if not available.|

<h2 id="tocSofferremovewhitelistrequest">OfferRemoveWhitelistRequest</h2>

<a id="schemaofferremovewhitelistrequest"></a>

```json
{
  "offerguid": "string",
  "aliasguid": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|offerguid|string|true|none|none|
|aliasguid|string|true|none|none|

<h2 id="tocSsendfromrequest">SendFromRequest</h2>

<a id="schemasendfromrequest"></a>

```json
{
  "fromaccount": "fromaccount",
  "amount": 0.8008281904610115,
  "minconf": 6,
  "addlockconf": false,
  "commentto": "commentto",
  "comment": "comment",
  "tosyscoinaddress": "tosyscoinaddress"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|fromaccount|string|true|none|The name of the account to send funds from. May be the default account using "".|
|tosyscoinaddress|string|true|none|The syscoin address to send funds to.|
|amount|number|true|none|he amount in SYS (transaction fee is added on top).|
|minconf|integer|false|none|Only use funds with at least this many confirmations.|
|addlockconf|boolean|false|none|Whether to add 5 confirmations to transactions locked via InstantSend.|
|comment|string|false|none|A comment used to store what the transaction is for. This is not part of the transaction, just kept in your wallet.|
|commentto|string|false|none|An optional comment to store the name of the person or organization to which you're sending the transaction. This is not part of the transaction, it is just kept in your wallet.|

<h2 id="tocSsendmanyrequest">SendManyRequest</h2>

<a id="schemasendmanyrequest"></a>

```json
{
  "fromaccount": "fromaccount",
  "use_ps": false,
  "amounts": "amounts",
  "minconf": 0,
  "addlockconf": false,
  "use_is": false,
  "comment": "comment",
  "subtractfeefromamount": "subtractfeefromamount"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|fromaccount|string|true|none|The account to send the funds from. Should be "" for the default account|
|amounts|string|true|none|A json object with addresses and amounts { "address":amount   (numeric) The syscoin address is the key, the numeric amount in SYS is the value,...}|
|minconf|integer|false|none|Only use the balance confirmed at least this many times.|
|addlockconf|boolean|false|none|Only use the balance confirmed at least this many times.|
|comment|string|false|none|A comment used to store what the transaction is for. This is not part of the transaction, just kept in your wallet.|
|subtractfeefromamount|string|false|none|A json array with addresses. The fee will be equally deducted from the amount of each selected address. Those recipients will receive less syscoins than you enter in their corresponding amount field. If no addresses are specified here, the sender pays the fee. [ "address" Subtract fee from this address,... ]|
|use_is|boolean|false|none|Send this transaction as InstantSend (default: false)|
|use_ps|boolean|false|none|Use anonymized funds only (default: false)|

<h2 id="tocSsendtoaddressrequest">SendToAddressRequest</h2>

<a id="schemasendtoaddressrequest"></a>

```json
{
  "use_ps": false,
  "amount": 0.8008281904610115,
  "syscoinaddress": "syscoinaddress",
  "use_is": false,
  "commentto": "commentto",
  "comment": "comment",
  "subtractfeefromamount": false
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|syscoinaddress|string|true|none|The syscoin address to send to.|
|amount|number|true|none|The amount in SYS to send. eg 0.1|
|comment|string|false|none|A comment used to store what the transaction is for. This is not part of the transaction, just kept in your wallet.|
|commentto|string|false|none|An optional comment to store the name of the person or organization to which you're sending the transaction. This is not part of the transaction, it is just kept in your wallet.|
|subtractfeefromamount|boolean|false|none|The fee will be deducted from the amount being sent. The recipient will receive less syscoins than you enter in the amount field.|
|use_is|boolean|false|none|Send this transaction as InstantSend (default: false)|
|use_ps|boolean|false|none|Use anonymized funds only (default: false)|

<h2 id="tocSsignmessagerequest">SignMessageRequest</h2>

<a id="schemasignmessagerequest"></a>

```json
{
  "syscoinaddress": "syscoinaddress",
  "message": "message"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|syscoinaddress|string|true|none|The syscoin address to use for the private key.|
|message|string|true|none|The message to create a signature of.|

<h2 id="tocSwalletpassphraserequest">WalletPassphraseRequest</h2>

<a id="schemawalletpassphraserequest"></a>

```json
{
  "passphrase": "passphrase",
  "timeout": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|passphrase|string|true|none|The wallet passphrase|
|timeout|number|true|none|The time to keep the decryption key in seconds.|

<h2 id="tocSwalletpassphrasechangerequest">WalletPassphraseChangeRequest</h2>

<a id="schemawalletpassphrasechangerequest"></a>

```json
{
  "oldpassphrase": "oldpassphrase",
  "newpassphrase": "newpassphrase"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|oldpassphrase|string|true|none|The current passphrase|
|newpassphrase|string|true|none|The new passphrase|

<h2 id="tocSmultisignatureinfo">MultiSignatureInfo</h2>

<a id="schemamultisignatureinfo"></a>

```json
{
  "reqsigs": 0,
  "reqsigners": "string",
  "redeemscript": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reqsigs|number|true|none|none|
|reqsigners|string|true|none|none|
|redeemscript|string|true|none|none|

<h2 id="tocSescrowfeedbackrequest">EscrowFeedbackRequest</h2>

<a id="schemaescrowfeedbackrequest"></a>

```json
{
  "feedback": "feedback",
  "witness": "witness",
  "userfrom": "userfrom",
  "escrowguid": "escrowguid",
  "rating": 0,
  "userto": "userto"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|escrowguid|string|true|none|Escrow ID|
|userfrom|string|true|none|Your role ('buyer', 'seller', 'reseller', or 'arbiter')|
|feedback|string|true|none|Feedback description|
|rating|integer|true|none|Ratings are numbers from 1 to 5|
|userto|string|true|none|His role ('buyer', 'seller', 'reseller', or 'arbiter')|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSgenerateescrowmultisigrequest">GenerateEscrowMultisigRequest</h2>

<a id="schemagenerateescrowmultisigrequest"></a>

```json
{
  "arbiter": "arbiter",
  "quantity": 0.8008281904610115,
  "offerguid": "offerguid",
  "paymentoption": "paymentoption",
  "buyer": "buyer"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|buyer|string|true|none|none|
|offerguid|string|true|none|none|
|quantity|number|true|none|none|
|arbiter|string|true|none|none|
|paymentoption|string|false|none|none|

<h2 id="tocSloginresponse">LoginResponse</h2>

<a id="schemaloginresponse"></a>

```json
{
  "success": true,
  "message": "message",
  "token": "token"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|success|boolean|true|none|none|
|message|string|true|none|none|
|token|string|true|none|none|

<h2 id="tocSgetblockresponse">GetBlockResponse</h2>

<a id="schemagetblockresponse"></a>

```json
{
  "tx": [
    "tx",
    "tx"
  ],
  "mediantime": 9.301444243932576,
  "data": "data",
  "previousblockhash": "previousblockhash",
  "bits": "bits",
  "weight": 5.962133916683182,
  "versionHex": "versionHex",
  "confirmations": 0.8008281904610115,
  "version": 2.3021358869347655,
  "nonce": 3.616076749251911,
  "nextblockhash": "nextblockhash",
  "difficulty": 2.027123023002322,
  "chainwork": "chainwork",
  "size": 6.027456183070403,
  "merkleroot": "merkleroot",
  "strippedsize": 1.4658129805029452,
  "time": 7.061401241503109,
  "hash": "hash",
  "height": 5.637376656633329
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hash|string|false|none|The block hash (same as provided)|
|confirmations|number|false|none|The number of confirmations, or -1 if the block is not on the main chain|
|size|number|false|none|The block size|
|strippedsize|number|false|none|The block size excluding witness data|
|weight|number|false|none|The block weight (BIP 141)|
|height|number|false|none|The block height or index|
|version|number|false|none|The block version|
|versionHex|string|false|none|The block version formatted in hexadecimal|
|merkleroot|string|false|none|The merkle root|
|tx|[string]|false|none|The transaction ids|
|time|number|false|none|The block time in seconds since epoch (Jan 1 1970 GMT)|
|mediantime|number|false|none|The median block time in seconds since epoch (Jan 1 1970 GMT)|
|nonce|number|false|none|The nonce|
|bits|string|false|none|The bits|
|difficulty|number|false|none|The difficulty|
|chainwork|string|false|none|Expected number of hashes required to produce the chain up to this block (in hex)|
|previousblockhash|string|false|none|The hash of the previous block|
|nextblockhash|string|false|none|The hash of the next block|
|data|string|false|none|(for verbose=false) A string that is serialized, hex-encoded data for block 'hash'.|

<h2 id="tocSgetblockchaininforesponse">GetBlockchainInfoResponse</h2>

<a id="schemagetblockchaininforesponse"></a>

```json
{
  "difficulty": 1.4658129805029452,
  "headers": 6.027456183070403,
  "bip9_softforks": "{}",
  "chain": "chain",
  "chainwork": "chainwork",
  "mediantime": 5.962133916683182,
  "verificationprogress": 5.637376656633329,
  "blocks": 0.8008281904610115,
  "pruned": true,
  "softforks": [
    "{}",
    "{}"
  ],
  "pruneheight": 2.3021358869347655,
  "bestblockhash": "bestblockhash"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|chain|string|false|none|Current network name as defined in BIP70 (main, test, regtest)|
|blocks|number|false|none|the current number of blocks processed in the server|
|headers|number|false|none|the current number of headers we have validated|
|bestblockhash|string|false|none|the hash of the currently best block|
|difficulty|number|false|none|the current difficulty|
|mediantime|number|false|none|median time for the current best block|
|verificationprogress|number|false|none|estimate of verification progress [0..1]|
|chainwork|string|false|none|total amount of work in active chain, in hexadecimal|
|pruned|boolean|false|none|if the blocks are subject to pruning|
|pruneheight|number|false|none|lowest-height complete block stored|
|softforks|[object]|false|none|status of softforks in progress|
|bip9_softforks|object|false|none|status of BIP9 softforks in progress|

<h2 id="tocSencryptwalletrequest">EncryptWalletRequest</h2>

<a id="schemaencryptwalletrequest"></a>

```json
{
  "passphrase": "passphrase"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|passphrase|string|true|none|The pass phrase to encrypt the wallet with. It must be at least 1 character, but should be long.|

<h2 id="tocSnetworkinfo">NetworkInfo</h2>

<a id="schemanetworkinfo"></a>

```json
{
  "localaddresses": [
    "localaddresses",
    "localaddresses"
  ],
  "protocolversion": 6.027456183070403,
  "relayfee": 5.637376656633329,
  "subversion": "subversion",
  "timeoffset": 1.4658129805029452,
  "warnings": "warnings",
  "localrelay": true,
  "networks": [
    {
      "proxy": "proxy",
      "limited": true,
      "proxy_randomize_credentials": true,
      "name": "name",
      "reachable": true
    },
    {
      "proxy": "proxy",
      "limited": true,
      "proxy_randomize_credentials": true,
      "name": "name",
      "reachable": true
    }
  ],
  "version": 0.8008281904610115,
  "connections": 5.962133916683182,
  "localservices": "localservices"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version|number|false|none|none|
|subversion|string|false|none|none|
|protocolversion|number|false|none|none|
|localservices|string|false|none|none|
|localrelay|boolean|false|none|none|
|timeoffset|number|false|none|none|
|connections|number|false|none|none|
|networks|[[NetworkInfoDetails](#schemanetworkinfodetails)]|false|none|none|
|relayfee|number|false|none|none|
|localaddresses|[string]|false|none|none|
|warnings|string|false|none|none|

<h2 id="tocSnetworkinfodetails">NetworkInfoDetails</h2>

<a id="schemanetworkinfodetails"></a>

```json
{
  "proxy": "proxy",
  "limited": true,
  "proxy_randomize_credentials": true,
  "name": "name",
  "reachable": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|limited|boolean|false|none|none|
|reachable|boolean|false|none|none|
|proxy|string|false|none|none|
|proxy_randomize_credentials|boolean|false|none|none|

<h2 id="tocSwhitelistentry">WhitelistEntry</h2>

<a id="schemawhitelistentry"></a>

```json
{
  "alias": "alias",
  "discount_percentage": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|false|none|none|
|discount_percentage|number|false|none|none|

<h2 id="tocSlistreceivedbyaddress">ListReceivedByAddress</h2>

<a id="schemalistreceivedbyaddress"></a>

```json
{
  "amount": 0.8008281904610115,
  "address": "address",
  "v2address": "v2address",
  "ismine": true,
  "label": "label",
  "confirmations": 6.027456183070403,
  "account": "account",
  "txids": [
    "txids",
    "txids"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|false|none|none|
|v2address|string|false|none|none|
|account|string|false|none|none|
|amount|number|false|none|none|
|confirmations|number|false|none|none|
|label|string|false|none|none|
|txids|[string]|false|none|none|
|ismine|boolean|false|none|none|

<h2 id="tocSsyscoinaddressentry">SyscoinAddressEntry</h2>

<a id="schemasyscoinaddressentry"></a>

```json
{
  "address": "address",
  "balance": 0.8008281904610115,
  "alias": "alias",
  "label": "label"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|false|none|none|
|balance|number|false|none|none|
|label|string|false|none|none|
|alias|string|false|none|none|

<h2 id="tocSgetchaintipsresponse">GetChainTipsResponse</h2>

<a id="schemagetchaintipsresponse"></a>

```json
{
  "difficulty": 6.027456183070403,
  "chainwork": "chainwork",
  "branchlen": 1.4658129805029452,
  "hash": "hash",
  "height": 0.8008281904610115,
  "status": "status"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|height|number|false|none|none|
|hash|string|false|none|none|
|difficulty|number|false|none|none|
|chainwork|string|false|none|none|
|branchlen|number|false|none|none|
|status|string|false|none|none|

<h2 id="tocSgetspentinforesponse">GetSpentInfoResponse</h2>

<a id="schemagetspentinforesponse"></a>

```json
{
  "txid": "txid",
  "index": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txid|string|false|none|none|
|index|number|false|none|none|

<h2 id="tocSgovernanceinforesponse">GovernanceInfoResponse</h2>

<a id="schemagovernanceinforesponse"></a>

```json
{
  "nextsuperblock": 2.3021358869347655,
  "proposalfee": 1.4658129805029452,
  "lastsuperblock": 5.637376656633329,
  "masternodewatchdogmaxseconds": 6.027456183070403,
  "governanceminquorum": 0.8008281904610115,
  "superblockcycle": 5.962133916683182
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|governanceminquorum|number|false|none|none|
|masternodewatchdogmaxseconds|number|false|none|none|
|proposalfee|number|false|none|none|
|superblockcycle|number|false|none|none|
|lastsuperblock|number|false|none|none|
|nextsuperblock|number|false|none|none|

<h2 id="tocSpoolinforesponse">PoolInfoResponse</h2>

<a id="schemapoolinforesponse"></a>

```json
{
  "mixing_mode": "mixing_mode",
  "entries": 6.027456183070403,
  "warnings": "warnings",
  "state": "state",
  "addr": "addr",
  "queue": 0.8008281904610115,
  "outpoint": "outpoint",
  "status": "status",
  "keys_left": "keys_left"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|state|string|false|none|none|
|mixing_mode|string|false|none|none|
|queue|number|false|none|none|
|entries|number|false|none|none|
|status|string|false|none|none|
|outpoint|string|false|none|none|
|addr|string|false|none|none|
|keys_left|string|false|none|none|
|warnings|string|false|none|none|

<h2 id="tocSdumphdinforesponse">DumpHdInfoResponse</h2>

<a id="schemadumphdinforesponse"></a>

```json
{
  "hdseed": "hdseed",
  "mnemonicpassphrase": "mnemonicpassphrase",
  "mnemonic": "mnemonic"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hdseed|string|false|none|none|
|mnemonic|string|false|none|none|
|mnemonicpassphrase|string|false|none|none|

<h2 id="tocSasset">Asset</h2>

<a id="schemaasset"></a>

```json
{
  "symbol": "symbol",
  "can_adjust_interest_rate": true,
  "total_supply": 5.962133916683182,
  "inputs": [
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    },
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    }
  ],
  "precision": 7.061401241503109,
  "txid": "txid",
  "publicvalue": "publicvalue",
  "use_input_ranges": true,
  "balance": 1.4658129805029452,
  "max_supply": 5.637376656633329,
  "guid": "guid",
  "alias": "alias",
  "interest_rate": 2.3021358869347655,
  "time": 6.027456183070403,
  "category": "category",
  "height": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|guid|string|true|none|none|
|symbol|string|false|none|none|
|txid|string|false|none|none|
|height|number|false|none|none|
|time|number|false|none|none|
|publicvalue|string|false|none|none|
|category|string|false|none|none|
|alias|string|false|none|none|
|balance|number|false|none|none|
|total_supply|number|false|none|none|
|max_supply|number|false|none|none|
|interest_rate|number|false|none|none|
|can_adjust_interest_rate|boolean|false|none|none|
|use_input_ranges|boolean|false|none|none|
|inputs|[[AssetInput](#schemaassetinput)]|false|none|none|
|precision|number|false|none|none|

<h2 id="tocSassetinput">AssetInput</h2>

<a id="schemaassetinput"></a>

```json
{
  "start": 6.027456183070403,
  "end": 1.4658129805029452
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|start|number|false|none|none|
|end|number|false|none|none|

<h2 id="tocSassetsendrequest">AssetSendRequest</h2>

<a id="schemaassetsendrequest"></a>

```json
{
  "witness": "witness",
  "amounts": [
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    },
    {
      "amount": 0.8008281904610115,
      "ranges": [
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        },
        {
          "start": 6.027456183070403,
          "end": 1.4658129805029452
        }
      ],
      "aliasto": "aliasto"
    }
  ],
  "memo": "memo",
  "asset": "asset",
  "aliasfrom": "aliasfrom"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|true|none|Asset guid.|
|aliasfrom|string|true|none|Alias to transfer from.|
|amounts|[[AssetAmount](#schemaassetamount)]|true|none|A json object with aliases and amounts { "aliasto":amount   alias to amounts mapping, can be multiple mappings OR if using inputranges "aliasto":"aliasname" alias to range mappings, can be multiple ranges and multiple mappings "ranges": "start":index "end":index }|
|memo|string|false|none|Message to include in this asset allocation transfer.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSassetamount">AssetAmount</h2>

<a id="schemaassetamount"></a>

```json
{
  "amount": 0.8008281904610115,
  "ranges": [
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    },
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    }
  ],
  "aliasto": "aliasto"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|aliasto|string|true|none|alias to send to|
|amount|number|false|none|amount you want to send|
|ranges|[[AssetInput](#schemaassetinput)]|false|none|[{'start':index,'end':index},...]},...]|

<h2 id="tocSassetallocation">AssetAllocation</h2>

<a id="schemaassetallocation"></a>

```json
{
  "balance": 6.027456183070403,
  "inputs": [
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    },
    {
      "start": 6.027456183070403,
      "end": 1.4658129805029452
    }
  ],
  "txid": "txid",
  "alias": "alias",
  "interest_claim_height": 1.4658129805029452,
  "memo": "memo",
  "_id": "_id",
  "asset": "asset",
  "accumulated_interest": 5.962133916683182,
  "height": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_id|string|true|none|none|
|asset|string|false|none|none|
|txid|string|false|none|none|
|height|number|false|none|none|
|alias|string|false|none|none|
|balance|number|false|none|none|
|interest_claim_height|number|false|none|none|
|memo|string|false|none|none|
|inputs|[[AssetInput](#schemaassetinput)]|false|none|none|
|accumulated_interest|number|false|none|none|

<h2 id="tocSassetallocationsenderstatus">AssetAllocationSenderStatus</h2>

<a id="schemaassetallocationsenderstatus"></a>

```json
{
  "status": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|number|false|none|Level -1 means not found, not a ZDAG transaction, perhaps it is already confirmed. Level 0 means OK. Level 1 means warning (checked that in the mempool there are more spending balances than current POW sender balance). An active stance should be taken and perhaps a deeper analysis as to potential conflicts related to the sender. Level 2 means an active double spend was found and any depending asset allocation sends are also flagged as dangerous and should wait for POW confirmation before proceeding.|

<h2 id="tocSassettransferrequest">AssetTransferRequest</h2>

<a id="schemaassettransferrequest"></a>

```json
{
  "witness": "witness",
  "alias": "alias",
  "asset": "asset"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|true|none|Asset guid.|
|alias|string|true|none|Alias to transfer this asset to.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSassetallocationcollectinterestrequest">AssetAllocationCollectInterestRequest</h2>

<a id="schemaassetallocationcollectinterestrequest"></a>

```json
{
  "witness": "witness",
  "alias": "alias",
  "asset": "asset"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|true|none|Asset guid.|
|alias|string|true|none|Alias that holds this asset allocation.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSassetupdaterequest">AssetUpdateRequest</h2>

<a id="schemaassetupdaterequest"></a>

```json
{
  "witness": "witness",
  "publicvalue": "publicvalue",
  "interest_rate": 6.027456183070403,
  "asset": "asset",
  "category": "category",
  "supply": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|false|none|Asset guid.|
|publicvalue|string|false|none|Public data, 512 characters max.|
|category|string|false|none|Set to assets|
|supply|number|false|none|New supply of asset. Can mint more supply up to total_supply amount or if max_supply is -1 then minting is uncapped.|
|interest_rate|number|false|none|The annual interest rate if any. Money supply is still capped to total supply. Should be between 0 and 1 and represents a percentage divided by 100. Can only set if this asset allows adjustment of interest rate.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSassetnewrequest">AssetNewRequest</h2>

<a id="schemaassetnewrequest"></a>

```json
{
  "symbol": "symbol",
  "witness": "witness",
  "publicvalue": "publicvalue",
  "can_adjust_interest_rate": true,
  "precision": 0.8008281904610115,
  "max_supply": 1.4658129805029452,
  "alias": "alias",
  "interest_rate": 5.962133916683182,
  "use_inputranges": true,
  "category": "category",
  "supply": 6.027456183070403
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|false|none|name, 20 characters max.|
|alias|string|false|none|An alias you own.|
|publicvalue|string|false|none|Public data, 256 characters max.|
|category|string|false|none|Category, 256 characters max. Defaults to assets.|
|precision|number|false|none|Precision of balances. Must be between 0 and 8. The lower it is the higher possible max_supply is available since the supply is represented as a 64 bit integer. With a precision of 8 the max supply is 10 billion.|
|supply|number|false|none|Initial supply of asset. Can mint more supply up to total_supply amount or if total_supply is -1 then minting is uncapped.|
|max_supply|number|false|none|Maximum supply of this asset. Set to -1 for uncapped.|
|use_inputranges|boolean|false|none|If this asset uses an input for every token, useful if you need to keep track of a token regardless of ownership.|
|interest_rate|number|false|none|The annual interest rate if any. Money supply is still capped to total supply. Should be between 0 and 1 and represents a percentage divided by 100.|
|can_adjust_interest_rate|boolean|false|none|Ability to adjust interest rate through assetupdate in the future.|
|witness|string|false|none|Witness alias name that will sign for web-of-trust notarization of this transaction.|

<h2 id="tocSfundrawtransactionrequest">FundRawTransactionRequest</h2>

<a id="schemafundrawtransactionrequest"></a>

```json
{
  "hexstring": "hexstring",
  "watching": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hexstring|string|false|none|none|
|watching|boolean|false|none|none|

<h2 id="tocSsignrawtransactionrequest">SignRawTransactionRequest</h2>

<a id="schemasignrawtransactionrequest"></a>

```json
{
  "hexstring": "hexstring"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hexstring|string|false|none|none|

<h2 id="tocSlockunspentrequest">LockUnspentRequest</h2>

<a id="schemalockunspentrequest"></a>

```json
{
  "unlock": true,
  "transactions": [
    {
      "txid": "txid",
      "vout": 0.8008281904610115
    },
    {
      "txid": "txid",
      "vout": 0.8008281904610115
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|unlock|boolean|false|none|none|
|transactions|[[LockUnspentTransaction](#schemalockunspenttransaction)]|false|none|none|

<h2 id="tocSlockunspenttransaction">LockUnspentTransaction</h2>

<a id="schemalockunspenttransaction"></a>

```json
{
  "txid": "txid",
  "vout": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txid|string|false|none|none|
|vout|number|false|none|none|

<h2 id="tocSoffernewrequest">OfferNewRequest</h2>

<a id="schemaoffernewrequest"></a>

```json
{
  "offertype": "offertype",
  "quantity": 0.8008281904610115,
  "auction_expires": 5.962133916683182,
  "description": "description",
  "privatevalue": true,
  "units": 1.4658129805029452,
  "auction_reserve": 5.637376656633329,
  "title": "title",
  "auction_deposit": 2.3021358869347655,
  "witness": "witness",
  "cert_guid": "cert_guid",
  "price": 6.027456183070403,
  "alias": "alias",
  "currency": "currency",
  "category": "category",
  "auction_require_witness": true,
  "payment_options": "payment_options"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|false|none|none|
|category|string|false|none|none|
|title|string|false|none|none|
|quantity|number|false|none|none|
|price|number|false|none|none|
|description|string|false|none|none|
|currency|string|false|none|none|
|cert_guid|string|false|none|none|
|payment_options|string|false|none|none|
|privatevalue|boolean|false|none|none|
|units|number|false|none|none|
|offertype|string|false|none|none|
|auction_expires|number|false|none|none|
|auction_reserve|number|false|none|none|
|auction_require_witness|boolean|false|none|none|
|auction_deposit|number|false|none|none|
|witness|string|false|none|none|

<h2 id="tocSofferupdaterequest">OfferUpdateRequest</h2>

<a id="schemaofferupdaterequest"></a>

```json
{
  "quantity": 0.8008281904610115,
  "auction_expires": 5.962133916683182,
  "description": "description",
  "privatevalue": true,
  "auction_reserve": 5.637376656633329,
  "title": "title",
  "auction_deposit": 2.3021358869347655,
  "witness": "witness",
  "cert_guid": "cert_guid",
  "price": 6.027456183070403,
  "alias": "alias",
  "guid": "guid",
  "currency": "currency",
  "commission": 1.4658129805029452,
  "category": "category",
  "offer_type": "offer_type",
  "auction_require_witness": true,
  "payment_options": "payment_options"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|string|false|none|none|
|guid|string|false|none|none|
|category|string|false|none|none|
|title|string|false|none|none|
|quantity|number|false|none|none|
|price|number|false|none|none|
|description|string|false|none|none|
|currency|string|false|none|none|
|privatevalue|boolean|false|none|none|
|cert_guid|string|false|none|none|
|commission|number|false|none|none|
|payment_options|string|false|none|none|
|offer_type|string|false|none|none|
|auction_expires|number|false|none|none|
|auction_reserve|number|false|none|none|
|auction_require_witness|boolean|false|none|none|
|auction_deposit|number|false|none|none|
|witness|string|false|none|none|

<h2 id="tocSescrowcreaterawtransactiondatarequest">EscrowCreateRawTransactionDataRequest</h2>

<a id="schemaescrowcreaterawtransactiondatarequest"></a>

```json
{
  "txid": "txid",
  "vout": 0.8008281904610115,
  "satoshis": 6.027456183070403
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txid|string|false|none|none|
|vout|number|false|none|none|
|satoshis|number|false|none|none|

<h2 id="tocSescrowbidresponse">EscrowBidResponse</h2>

<a id="schemaescrowbidresponse"></a>

```json
{
  "offer": "offer",
  "bid_in_payment_option_per_unit": 1.4658129805029452,
  "witness": "witness",
  "bidder": "bidder",
  "escrow": "escrow",
  "_id": "_id",
  "bid_in_offer_currency_per_unit": 6.027456183070403,
  "height": 0.8008281904610115,
  "status": "status"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_id|string|false|none|none|
|offer|string|false|none|none|
|escrow|string|false|none|none|
|height|number|false|none|none|
|bidder|string|false|none|none|
|bid_in_offer_currency_per_unit|number|false|none|none|
|bid_in_payment_option_per_unit|number|false|none|none|
|witness|string|false|none|none|
|status|string|false|none|none|

<h2 id="tocSescrowfeedbackresponse">EscrowFeedbackResponse</h2>

<a id="schemaescrowfeedbackresponse"></a>

```json
{
  "offer": "offer",
  "feedback": "feedback",
  "feedbackuserfrom": 5.962133916683182,
  "rating": 1.4658129805029452,
  "escrow": "escrow",
  "txid": 0.8008281904610115,
  "feedbackuserto": 5.637376656633329,
  "_id": "_id",
  "time": 6.027456183070403
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|_id|string|false|none|none|
|offer|string|false|none|none|
|escrow|string|false|none|none|
|txid|number|false|none|none|
|time|number|false|none|none|
|rating|number|false|none|none|
|feedbackuserfrom|number|false|none|none|
|feedbackuserto|number|false|none|none|
|feedback|string|false|none|none|

<h2 id="tocSsyscointransactionfundrequest">SyscoinTransactionFundRequest</h2>

<a id="schemasyscointransactionfundrequest"></a>

```json
{
  "addresses": [
    "{}",
    "{}"
  ],
  "hexstring": "hexstring"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hexstring|string|false|none|none|
|addresses|[object]|false|none|none|

<h2 id="tocSgetaddressutxosrequest">GetAddressUTXOsRequest</h2>

<a id="schemagetaddressutxosrequest"></a>

```json
{
  "addresses": [
    "addresses",
    "addresses"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|addresses|[string]|false|none|none|

<h2 id="tocSsignrawtransactionresponse">SignRawTransactionResponse</h2>

<a id="schemasignrawtransactionresponse"></a>

```json
{
  "hex": "hex",
  "complete": true,
  "errors": [
    {
      "sequence": 6.027456183070403,
      "scriptSig": "scriptSig",
      "txid": "txid",
      "error": "error",
      "vout": 0.8008281904610115
    },
    {
      "sequence": 6.027456183070403,
      "scriptSig": "scriptSig",
      "txid": "txid",
      "error": "error",
      "vout": 0.8008281904610115
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hex|string|false|none|none|
|complete|boolean|false|none|none|
|errors|[[SignRawTransactionError](#schemasignrawtransactionerror)]|false|none|none|

<h2 id="tocSsignrawtransactionerror">SignRawTransactionError</h2>

<a id="schemasignrawtransactionerror"></a>

```json
{
  "sequence": 6.027456183070403,
  "scriptSig": "scriptSig",
  "txid": "txid",
  "error": "error",
  "vout": 0.8008281904610115
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txid|string|false|none|none|
|vout|number|false|none|none|
|scriptSig|string|false|none|none|
|sequence|number|false|none|none|
|error|string|false|none|none|

<h2 id="tocSsendrawtransactionresponse">SendRawTransactionResponse</h2>

<a id="schemasendrawtransactionresponse"></a>

```json
{
  "txid": "txid"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txid|string|false|none|none|

<h2 id="tocSaliasaddscriptrequest">AliasAddScriptRequest</h2>

<a id="schemaaliasaddscriptrequest"></a>

```json
{
  "script": "script"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|script|string|false|none|none|

<h2 id="tocSaliaspayrequest_amounts">AliasPayRequest_amounts</h2>

<a id="schemaaliaspayrequest_amounts"></a>

```json
"{\"alias1\":0.02,\"alias2\":0.4,\"alias3\":0.004}"

```

*An object with aliases (pay to) and amounts. { "address":amount, ... } (numeric or string) The syscoin alias is the key, the numeric amount (can be string) in SYS is the value.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alias|number|false|none|none|

