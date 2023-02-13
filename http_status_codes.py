class HttpStatusCodes(object):
    """
    Colletion of all http response status codes.

    * 1xx: informational responses.
    * 2xx: successful responses.
    * 3xx: redirection messages.
    * 4xx: client error responses.
    * 5xx: server error responses.
    """

    # 1xx
    CODE_100_CONTINUE: int = 100
    """
    100 Continue
    
        The server has received the request headers and the client should proceed to send the request body (in the case of a request for which a body needs to be sent; for example, a POST request). Sending a large request body to a server after a request has been rejected for inappropriate headers would be inefficient. To have a server check the request's headers, a client must send Expect: 100-continue as a header in its initial request and receive a 100 Continue status code in response before sending the body. If the client receives an error code such as 403 (Forbidden) or 405 (Method Not Allowed) then it should not send the request's body. The response 417 Expectation Failed indicates that the request should be repeated without the Expect header as it indicates that the server does not support expectations (this is the case, for example, of HTTP/1.0 servers).
    """

    CODE_101_SWITCHING_PROTOCOLS: int = 101
    """
    101 Switching Protocols
    
        This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.
    """

    CODE_102_PROCESSING: int = 102
    """
    102 Processing (WebDAV)
    
        This code indicates that the server has received and is processing the request, but no response is available yet.
    """

    CODE_103_EARLY_HINTS: int = 103
    """
    103 Early Hints
    
        This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response.
    """

    # 2xx
    CODE_200_OK: int = 200
    """
    200 OK
    
        The request succeeded. The result meaning of "success" depends on the HTTP method:
        \n* GET : The resource has been fetched and transmitted in the message body.
        \n* HEAD : The representation headers are included in the response without any message body.
        \n* PUT or POST : The resource describing the result of the action is transmitted in the message body.
        \n* TRACE : The message body contains the request message as received by the server.
    """

    CODE_201_CREATED:int =201
    """
    201 Created
    
        The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.
    """

    CODE_202_ACCEPTED:int = 202
    """
    202 Accepted
    
        The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous
        response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for
        batch processing.
    """

    CODE_203_NON_AUTHORITATIVE_INFORMATION: int = 203
    """
    203 Non-Authoritative Information
    
        This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status.
    """

    CODE_204_NO_CONTENT: int = 204
    """
    204 No Content
    
        There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones.
    """

    CODE_205_RESET_CONTENT: int = 205
    """
    205 Reset Content
    
        Tells the user agent to reset the document which sent this request.
    """

    CODE_206_PARTIAL_CONTENT: int = 206
    """
    206 Partial Content
    
        This response code is used when the Range header is sent from the client to request only part of a resource.
    """

    CODE_207_MULTI_STATUS: int = 207
    """
    207 Multi-Status (WebDAV)
    
        Conveys information about multiple resources, for situations where multiple status codes might be appropriate.
    """

    CODE_208_ALREADY_REPORTED: int = 208
    """
    208 Already Reported (WebDAV)
    
        Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.
    """

    CODE_226_IM_USED: int = 226
    """
    226 IM Used (HTTP Delta encoding)
    
        The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instancemanipulations applied to the current instance.
    """

    # 3xx
    CODE_300_MULTIPLE_CHOICES: int = 300
    """
    300 Multiple Choices
    
        Indicates multiple options for the resource from which the client may choose (via agent-driven content negotiation). For example, this code could be used to present multiple video format options, to list files with different filename extensions, or to suggest word-sense disambiguation.
    """

    CODE_301_MOVED_PERMANENTLY: int = 301
    """
    301 Moved Permanently
    
        This and all future requests should be directed to the given URI.
    """

    CODE_302_FOUND: int = 302
    """
    302 Found
    
        Tells the client to look at (browse to) another URL. The HTTP/1.0 specification (RFC 1945) required the client to perform a temporary redirect with the same method (the original describing phrase was "Moved Temporarily"),[11] but popular browsers implemented 302 redirects by changing the method to GET. Therefore, HTTP/1.1 added status codes 303 and 307 to distinguish between the two behaviours.
    """

    CODE_303_SEE_OTHER: int = 303
    """
    303 See Other
    
        The response to the request can be found under another URI using the GET method. When received in response to a POST (or PUT/DELETE), the client should presume that the server has received the data and should issue a new GET request to the given URI.
    """

    CODE_304_NOT_MODIFIED: int = 304
    """
    304 Not Modified
    
        Indicates that the resource has not been modified since the version specified by the request headers If-Modified-Since or If-None-Match. In such case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.
    """

    CODE_307_TEMPORARY_REDIRECT: int = 307
    """
    307 Temporary Redirect
    
        In this case, the request should be repeated with another URI; however, future requests should still use the original URI. In contrast to how 302 was historically implemented, the request method is not allowed to be changed when reissuing the original request. For example, a POST request should be repeated using another POST request.
    """

    CODE_308_PERMANENT_REDIRECT: int = 308
    """
    308 Permanent Redirect
    
        This and all future requests should be directed to the given URI. 308 parallel the behaviour of 301, but does not allow the HTTP method to change. So, for example, submitting a form to a permanently redirected resource may continue smoothly.
    """

    # 4xx
    CODE_400_BAD_REQUEST: int = 400
    """
    400 Bad Request
    
        The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, size too large, invalid request message framing, or deceptive request routing).
    """

    CODE_401_UNAUTHORIZED: int = 401
    """
    401 Unauthorized
    
        Similar to 403 Forbidden, but specifically for use when authentication is required and has failed or has not yet been provided. The response must include a WWW-Authenticate header field containing a challenge applicable to the requested resource. See Basic access authentication and Digest access authentication. 401 semantically means "unauthorised", the user does not have valid authentication credentials for the target resource. Some sites incorrectly issue HTTP 401 when an IP address is banned from the website (usually the website domain) and that specific address is refused permission to access a website.
    """

    CODE_402_PAYMENT_REQUIRED: int = 402
    """
    402 Payment Required
    
        Reserved for future use. The original intention was that this code might be used as part of some form of digital cash or micropayment scheme, as proposed, for example, by GNU Taler,[13] but that has not yet happened, and this code is not widely used. Google Developers API uses this status if a particular developer has exceeded the daily limit on requests.[14] Sipgate uses this code if an account does not have sufficient funds to start a call.[15] Shopify uses this code when the store has not paid their fees and is temporarily disabled.[16] Stripe uses this code for failed payments where parameters were correct, for example blocked fraudulent payments.
    """

    CODE_403_FORBIDDEN: int = 403
    """
    403 Forbidden
    
        The request contained valid data and was understood by the server, but the server is refusing action. This may be due to the user not having the necessary permissions for a resource or needing an account of some sort, or attempting a prohibited action (e.g. creating a duplicate record where only one is allowed). This code is also typically used if the request provided authentication by answering the WWW-Authenticate header field challenge, but the server did not accept that authentication. The request should not be repeated.
    """

    CODE_404_NOT_FOUND: int = 404
    """
    404 Not Found
    
        The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.
    """

    CODE_405_METHOD_NOT_ALLOWED: int = 405
    """
    405 Method Not Allowed
    
        A request method is not supported for the requested resource; for example, a GET request on a form that requires data to be presented via POST, or a PUT request on a read-only resource.
    """

    CODE_406_NOT_ACCEPTABLE: int = 406
    """
    406 Not Acceptable
    
        The requested resource is capable of generating only content not acceptable according to the Accept headers sent in the request. See Content negotiation.
    """

    CODE_407_PROXY_AUTHENTICATION_REQUIRED: int = 407
    """
    407 Proxy Authentication Required
    
        The client must first authenticate itself with the proxy.
    """

    CODE_408_REQUEST_TIMEOUT: int = 408
    """
    408 Request Timeout
    
        The server timed out waiting for the request. According to HTTP specifications: "The client did not produce a request within the time that the server was prepared to wait. The client MAY repeat the request without modifications at any later time."
    """

    CODE_409_CONFLICT: int = 409
    """
    409 Conflict
    
        Indicates that the request could not be processed because of conflict in the current state of the resource, such as an edit conflict between multiple simultaneous updates.
    """

    CODE_410_GONE: int = 410
    """
    410 Gone
    
        Indicates that the resource requested was previously in use but is no longer available and will not be available again. This should be used when a resource has been intentionally removed and the resource should be purged. Upon receiving a 410 status code, the client should not request the resource in the future. Clients such as search engines should remove the resource from their indices. Most use cases do not require clients and search engines to purge the resource, and a "404 Not Found" may be used instead.
    """

    CODE_411_LENGTH_REQUIRED: int = 411
    """
    411 Length Required
    
        The request did not specify the length of its content, which is required by the requested resource.
    """

    CODE_412_PRECONDITION_FAILED: int = 412
    """
    412 Precondition Failed
    
        The server does not meet one of the preconditions that the requester put on the request header fields.
    """

    CODE_413_PAYLOAD_TOO_LARGE: int = 413
    """
    413 Payload Too Large
    
        The request is larger than the server is willing or able to process. Previously called "Request Entity Too Large" in RFC 2616.
    """

    CODE_414_URI_TOO_LONG: int = 414
    """
    414 URI Too Long
    
        The URI provided was too long for the server to process. Often the result of too much data being encoded as a query-string of a GET request, in which case it should be converted to a POST request. Called "Request-URI Too Long" previously in RFC 2616.
    """

    CODE_415_UNSUPPORTED_MEDIA_TYPE: int = 415
    """
    415 Unsupported Media Type
    
        The request entity has a media type which the server or resource does not support. For example, the client uploads an image as image/svg+xml, but the server requires that images use a different format.
    """

    CODE_416_RANGE_NOT_SATISFIABLE: int = 416
    """
    416 Range Not Satisfiable
    
        The client has asked for a portion of the file (byte serving), but the server cannot supply that portion. For example, if the client asked for a part of the file that lies beyond the end of the file. Called "Requested Range Not Satisfiable" previously RFC 2616.
    """

    CODE_417_EXPECTATION_FAILED: int = 417
    """
    417 Expectation Failed
    
        The server cannot meet the requirements of the Expect request-header field.
    """

    CODE_418_IM_A_TEAPOT: int = 418
    """
    418 I'm a teapot
    
        This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324, Hyper Text Coffee Pot Control Protocol, and is not expected to be implemented by actual HTTP servers. The RFC specifies this code should be returned by teapots requested to brew coffee. This HTTP status is used as an Easter egg in some websites, such as Google.com's "I'm a teapot" easter egg. Sometimes, this status code is also used as a response to a blocked request, instead of the more appropriate 403 Forbidden.
    """

    CODE_421_MISDIRECTED_REQUEST: int = 421
    """
    421 Misdirected Request
    
        The request was directed at a server that is not able to produce a response (for example because of connection reuse).
    """

    CODE_422_UNPROCESSABLE_ENTITY: int = 422
    """
    422 Unprocessable Entity
    
        The request was well-formed but was unable to be followed due to semantic errors.
    """

    CODE_423_LOCKED: int = 423
    """
    423 Locked (WebDAV)
    
        The resource that is being accessed is locked.
    """

    CODE_424_FAILED_DEPENDENCY: int = 424
    """
    424 Failed Dependency (WebDAV)
    
        The request failed because it depended on another request and that request failed (e.g., a PROPPATCH).
    """

    CODE_425_TOO_EARLY: int = 425
    """
    425 Too Early
    
        Indicates that the server is unwilling to risk processing a request that might be replayed.
    """

    CODE_426_UPGRADE_REQUIRED: int = 426
    """
    426 Upgrade Required
    
        The client should switch to a different protocol such as TLS/1.3, given in the Upgrade header field.
    """

    CODE_428_PRECONDITION_REQUIRED: int = 428
    """
    428 Precondition Required
    
        The origin server requires the request to be conditional. Intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it, and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict.
    """

    CODE_429_TOO_MANY_REQUESTS: int = 429
    """
    429 Too Many Requests
    
        The user has sent too many requests in a given amount of time. Intended for use with rate-limiting schemes.
    """

    CODE_431_REQUEST_HEADER_FIELDS_TOO_LARGE: int = 431
    """
    431 Request Header Fields Too Large
    
        The server is unwilling to process the request because either an individual header field, or all the header fields collectively, are too large.
    """

    CODE_451_UNAVAILABLE_FOR_LEGAL_REASONS: int = 451
    """
    451 Unavailable For Legal Reasons
    
        A server operator has received a legal demand to deny access to a resource or to a set of resources that includes the requested resource.The code 451 was chosen as a reference to the novel Fahrenheit 451 (see the Acknowledgements in the RFC).
    """

    # Microsoft Internet Information Service
    CODE_440_LOGIN_TIME_OUT: int = 440
    """
    440 Login Time-out (Microsoft IIS)
    
        The client's session has expired and must log in again.
    """

    CODE_449_RETRY_WITH: int = 449
    """
    449 Retry With (Microsoft IIS)
    
        The server cannot honour the request because the user has not provided the required information.
    """

    CODE_451_REDIRECT: int = 451
    """
    451 Redirect (Microsoft IIS)
    
        Used in Exchange ActiveSync when either a more efficient server is available or the server cannot access the users' mailbox.[44] The client is expected to re-run the HTTP AutoDiscover operation to find a more appropriate server.
    """

    # nginx
    CODE_444_NO_RESPONSE: int = 444
    """
    444 No Response (nginx)
    
        Used internally to instruct the server to return no information to the client and close the connection immediately.
    """

    CODE_494_REQUEST_HEADER_TOO_LARGE: int = 494
    """
    494 Request header too large (nginx)
    
        Client sent too large request or too long header line.
    """

    CODE_495_SSL_CERTIFICATE_ERROR: int = 495
    """
    495 SSL Certificate Error (nginx)
    
        An expansion of the 400 Bad Request response code, used when the client has provided an invalid client certificate.
    """

    CODE_496_SSL_CERTIFICATE_REQUIRED: int = 496
    """
    496 SSL Certificate Required (nginx)
    
        An expansion of the 400 Bad Request response code, used when a client certificate is required but not provided.
    """

    CODE_497_HTTP_REQUEST_SENT_TO_HTTPS_PORT: int = 497
    """
    497 HTTP Request Sent to HTTPS Port (nginx)
    
        An expansion of the 400 Bad Request response code, used when the client has made a HTTP request to a port listening for HTTPS requests.
    """

    CODE_499_CLIENT_CLOSED_REQUEST: int = 499
    """
    499 Client Closed Request (nginx)
    
        Used when the client has closed the request before the server could send a response.
    """

    # AWS Elastic Load Balancer
    CODE_460: int = 460
    """
    460 (AWS Elastic Load Balancer)
    
        Client closed the connection with the load balancer before the idle timeout period elapsed. Typically when client timeout is sooner than the Elastic Load Balancer's timeout.
    """

    CODE_463: int = 463
    """
    463 (AWS Elastic Load Balancer)
    
        The load balancer received an X-Forwarded-For request header with more than 30 IP addresses.
    """

    CODE_561_UNAUTHORIZED: int = 561
    """
    561 Unauthorized (AWS Elastic Load Balancer)
    
        An error around authentication returned by a server registered with a load balancer. You configured a listener rule to authenticate users, but the identity provider (IdP) returned an error code when authenticating the user.
    """

    # 5xx
    CODE_500_INTERNAL_SERVER_ERROR: int = 500
    """
    500 Internal Server Error
    
        A generic error message, given when an unexpected condition was encountered and no more specific message is suitable.
    """

    CODE_501_NOT_IMPLEMENTED: int = 501
    """
    501 Not Implemented
    
        The server either does not recognize the request method, or it lacks the ability to fulfil the request. Usually this implies future availability (e.g., a new feature of a web-service API).
    """

    CODE_502_BAD_GATEWAY: int = 502
    """
    502 Bad Gateway
    
        The server was acting as a gateway or proxy and received an invalid response from the upstream server.
    """

    CODE_503_SERVICE_UNAVAILABLE: int = 503
    """
    503 Service Unavailable
    
        The server cannot handle the request (because it is overloaded or down for maintenance). Generally, this is a temporary state.
    """

    CODE_504_GATEWAY_TIMEOUT: int = 504
    """
    504 Gateway Timeout
    
        The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.
    """

    CODE_505_HTTP_VERSION_NOT_SUPPORTED: int = 505
    """
    505 HTTP Version Not Supported
    
        The server does not support the HTTP version used in the request.
    """

    CODE_506_VARIANT_ALSO_NEGOTIATES: int = 506
    """
    506 Variant Also Negotiates
    
        Transparent content negotiation for the request results in a circular reference.
    """

    CODE_507_INSUFFICIENT_STORAGE: int = 507
    """
    507 Insufficient Storage (WebDAV)
    
        The server is unable to store the representation needed to complete the request.
    """

    CODE_508_LOOP_DETECTED: int = 508
    """
    508 Loop Detected (WebDAV)
    
        The server detected an infinite loop while processing the request (sent instead of 208 Already Reported).
    """

    CODE_510_NOT_EXTENDED: int = 510
    """
    510 Not Extended
    
        Further extensions to the request are required for the server to fulfill it.
    """

    CODE_511_NETWORK_AUTHENTICATION_REQUIRED: int = 511
    """
    511 Network Authentication Required
    
        The client needs to authenticate to gain network access. Intended for use by intercepting proxies used to control access to the network (e.g., "captive portals" used to require agreement to Terms of Service before granting full Internet access via a Wi-Fi hotspot).
    """

    # unofficial
    CODE_419_PAGE_EXPIRED: int = 419
    """
    419 Page Expired (Laravel Framework) (unofficial)
    
        Used by the Laravel Framework when a CSRF Token is missing or expired.
    """

    CODE_420_METHOD_FAILURE: int = 420
    """
    420 Method Failure (Spring Framework) (unofficial)
    
        A deprecated response used by the Spring Framework when a method has failed.
    """

    CODE_420_ENHANCE_YOUR_CALM: int = 420
    """
    420 Enhance Your Calm (Twitter) (unofficial)
    
        Returned by version 1 of the Twitter Search and Trends API when the client is being rate limited; versions 1.1 and later use the 429 Too Many Requests response code instead. The phrase "Enhance your calm" comes from the 1993 movie Demolition Man, and its association with this number is likely a reference to cannabis.
    """

    CODE_430_REQUEST_HEADER_FIELDS_TOO_LARGE: int = 430
    """
    430 Request Header Fields Too Large (Shopify) (unofficial)
    
        Used by Shopify, instead of the 429 Too Many Requests response code, when too many URLs are requested within a certain time frame.
    """

    CODE_450_BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS: int = 450
    """
    450 Blocked by Windows Parental Controls (Microsoft) (unofficial)
    
        The Microsoft extension code indicated when Windows Parental Controls are turned on and are blocking access to the requested webpage.
    """

    CODE_498_INVALID_TOKEN = 498
    """
    498 Invalid Token (Esri) (unofficial)
    
        Returned by ArcGIS for Server. Code 498 indicates an expired or otherwise invalid token.
    """

    CODE_499_TOKEN_REQUIRED: int = 499
    """
    499 Token Required (Esri) (unofficial)
    
        Returned by ArcGIS for Server. Code 499 indicates that a token is required but was not submitted.
    """

    CODE_509_BANDWITH_LIMIT_EXCEEDED: int = 509
    """
    509 Bandwidth Limit Exceeded (Apache Web Server/cPanel) (unofficial)
    
        The server has exceeded the bandwidth specified by the server administrator; this is often used by shared hosting providers to limit the bandwidth of customers.
    """

    CODE_529_SITE_IS_OVERLOADED: int = 529
    """
    529 Site is overloaded (unofficial)
    
        Used by Qualys in the SSLLabs server testing API to signal that the site can't process the request.
    """

    CODE_530_SITE_IS_FROZEN: int = 530
    """
    530 Site is frozen (unofficial)
    
        Used by the Pantheon Systems web platform to indicate a site that has been frozen due to inactivity.
    """

    CODE_598_NETWORK_READ_TIMEOUT_ERROR: int = 598
    """
    598 (Informal convention) Network read timeout error (unofficial)
    
        Used by some HTTP proxies to signal a network read timeout behind the proxy to a client in front of the proxy.
    """

    CODE_599_NETWORK_CONNECT_TIMEOUT_ERROR: int = 599
    """
    599 Network Connect Timeout Error (unofficial)
    
        An error used by some HTTP proxies to signal a network connect timeout behind the proxy to a client in front of the proxy.
    """

    # cloudflare
    CODE_520_WEB_SERVER_RETURNED_AN_UNKNOWN_ERROR: int = 520
    """
    520 Web Server Returned an Unknown Error (cloudflare)
    
        The origin server returned an empty, unknown, or unexpected response to Cloudflare.
    """

    CODE_521_WEB_SERVER_IS_DOWN: int = 521
    """
    521 Web Server Is Down (cloudflare)
    
        The origin server refused connections from Cloudflare. Security solutions at the origin may be blocking legitimate connections from certain Cloudflare IP addresses.
    """

    CODE_522_CONNECTION_TIMED_OUT: int = 522
    """
    522 Connection Timed Out (cloudflare)
    
        Cloudflare timed out contacting the origin server.
    """

    CODE_523_ORIGIN_IS_UNREACHABLE: int = 523
    """
    523 Origin Is Unreachable (cloudflare)
    
        Cloudflare could not reach the origin server; for example, if the DNS records for the origin server are incorrect or missing.
    """

    CODE_524_A_TIMEOUT_OCCURED: int = 524
    """
    524 A Timeout Occurred (cloudflare)
    
        Cloudflare was able to complete a TCP connection to the origin server, but did not receive a timely HTTP response.
    """

    CODE_525_SSL_HANDSHAKE_FAILED: int = 525
    """
    525 SSL Handshake Failed (cloudflare)
    
        Cloudflare could not negotiate a SSL/TLS handshake with the origin server.
    """

    CODE_526_INVALID_SSL_CERTIFICATE: int = 526
    """
    526 Invalid SSL Certificate (cloudflare)
    
        Cloudflare could not validate the SSL certificate on the origin web server. Also used by Cloud Foundry's gorouter.
    """

    CODE_527_RAILGUN_ERROR: int = 527
    """
    527 Railgun Error (cloudflare)
    
        Error 527 indicates an interrupted connection between Cloudflare and the origin server's Railgun server.
    """

    CODE_530: int = 530
    """
    530 (cloudflare)
    
        Error 530 is returned along with a 1xxx error.
    """

    def __setattr__(self, name, value):
        raise AttributeError(f"Cannot assign value {value} to {name}!!!")

    def __delattr__(self, name):
        raise AttributeError(f"Operation cannot be performed on attribute {name}!!!")


if __name__ == "__main__":
    HTTP_STATUS_CODES = HttpStatusCodes()
    print(HTTP_STATUS_CODES.CODE_100_CONTINUE)
