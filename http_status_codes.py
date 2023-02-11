class HttpStatusCodes:
    """
    Colletion of all http response status codes.

    1xx: informational responses.
    2xx: successful responses.
    3xx: redirection messages.
    4xx: client error responses.
    5xx: server error responses.
    """

    # 1xx
    HTTP_101_SWITCHING_PROTOCOLS: int = 101
    """
    Status code: 101
    ----------------

    This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.
    """

    HTTP_102_PROCESSIG: int = 102
    """
    Status code: 102 (WebDAV)
    -------------------------

    This code indicates that the server has received and is processing the request, but no response is available yet.
    """

    HTTP_103_EARLY_HINTS: int = 103
    """
    Status code: 103
    ----------------

    This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response.
    """

    # 2xx
    HTTP_200_OK: int = 200
    """
    Status code: 200
    ----------------

    The request succeeded. The result meaning of "success" depends on the HTTP method:
        GET : The resource has been fetched and transmitted in the message body.
        HEAD : The representation headers are included in the response without any message body.
        PUT or POST : The resource describing the result of the action is transmitted in the message body.
        TRACE : The message body contains the request message as received by the server.
    """

    HTTP_201_CREATED:int =201
    """
    Status code: 201
    ----------------

    The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.
    """

    HTTP_202_ACCEPTED:int = 202
    """
    Status code: 202
    ----------------

    The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous
    response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for
    batch processing.
    """

    HTTP_203_NON_AUTHORITATIVE_INFORMATION: int = 203
    """
    Status code: 203
    ----------------

    This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status.
    """

    HTTP_204_NO_CONTENT: int = 204
    """
    Status code: 204
    ----------------

    There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones.
    """

    HTTP_205_RESET_CONTENT: int = 205
    """
    Status code: 205
    ----------------

    Tells the user agent to reset the document which sent this request.
    """

    HTTP_206_PARTIAL_CONTENT: int = 206
    """
    Status code: 206
    ----------------

    This response code is used when the Range header is sent from the client to request only part of a resource.
    """

    HTTP_207_MULTI_STATUS: int = 207
    """
    Status code: 207 (WebDAV)
    -------------------------

    Conveys information about multiple resources, for situations where multiple status codes might be appropriate.
    """

    HTTP_208_ALREADY_REPORTED: int = 208
    """
    Status code: 208 (WebDAV)
    -------------------------

    Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.
    """

    HTTP_226_IM_USED: int = 226
    """
    Status code: 226 (HTTP Delta encoding)
    --------------------------------------

    The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instancemanipulations applied to the current instance.
    """

    # 3xx
    HTTP_300_MULTIPLE_CHOICES: int = 300

    HTTP_301_MOVED_PERMANENTLY: int = 301

    HTTP_302_FOUND: int = 302

    HTTP_303_SEE_OTHER: int = 303

    HTTP_304_NOT_MODIFIED: int = 304

    HTTP_307_TEMPORARY_REDIRECT: int = 307

    HTTP_308_PERMANENT_REDIRECT: int = 308

    # 4xx
    HTTP_400_BAD_REQUEST: int = 400

    HTTP_401_UNAUTHORIZED: int = 401

    HTTP_402_PAYMENT_REQUIRED: int = 402

    HTTP_403_FORBIDDEN: int = 403

    HTTP_404_NOT_FOUND: int = 404

    HTTP_405_METHOD_NOT_ALLOWED: int = 405

    HTTP_406_NOT_ACCEPTABLE: int = 406

    HTTP_407_PROXY_AUTHENTICATION_REQUIRED: int = 407

    HTTP_408_REQUEST_TIMEOUT: int = 408

    HTTP_409_CONFLICT: int = 409

    HTTP_410_GONE: int = 410

    HTTP_411_LENGTH_REQUIRED: int = 411

    HTTP_412_PRECONDITION_FAILED: int = 412

    HTTP_413_PAYLOAD_TOO_LARGE: int = 413

    HTTP_414_URI_TOO_LONG: int = 414

    HTTP_415_UNSUPPORTED_MEDIA_TYPE: int = 415

    HTTP_416_RANGE_NOT_SATISFIABLE: int = 416

    HTTP_418_IM_A_TEAPOT: int = 418

    HTTP_421_MISDIRECTED_REQUEST: int = 421

    HTTP_422_UNPROCESSABLE_ENTITY: int = 422

    HTTP_423_LOCKED: int = 423

    HTTP_424_FAILED_DEPENDENCY: int = 424

    HTTP_425_TOO_EARLY: int = 425

    HTTP_426_UPGRADE_REQUIRED: int = 426

    HTTP_428_PRECONDITION_REQUIRED: int = 428

    HTTP_429_TOO_MANY_REQUESTS: int = 429

    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE: int = 431

    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS: int = 451

    # 5xx
    HTTP_500_INTERNAL_SERVER_ERROR: int = 500

    HTTP_501_NOT_IMPLEMENTED: int = 501

    HTTP_502_BAD_GATEWAY: int = 502

    HTTP_503_SERVICE_UNAVAILABLE: int = 503

    HTTP_504_GATEWAY_TIMEOUT: int = 504

    HTTP_505_HTTP_VERSION_NOT_SUPPORTED: int = 505

    HTTP_506_VARIANT_ALSO_NEGOTIATES: int = 506

    HTTP_507_INSUFFICIENT_STORAGE: int = 507

    HTTP_508_LOOP_DETECTED: int = 508

    HTTP_510_NOT_EXTENDED: int = 510

    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED: int = 511


print(HttpStatusCodes.HTTP_101_SWITCHING_PROTOCOLS)