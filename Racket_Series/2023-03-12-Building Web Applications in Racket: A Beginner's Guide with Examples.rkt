;;; Here is an example of how to set up a simple web server that responds to HTTP GET requests with the text "Hello, world!":
#lang racket

(require web-server/servlet)

(define (hello-world request)
    (response/xexpr `(html (body (p "Hello, world!")))))

(serve/servlet hello-world
                #:launch-browser? #t
                #:port 8080
                #:servlet-path "/")

;;; Here is an example of how to handle a POST request that submits a form with a name field:
#lang racket

(require web-server/servlet)

(define (handle-form request)
    (match (request-method request)
    ["POST"
        (match-define (cons 'name (list name)) (request-post-params request))
        (response/xexpr `(html (body (p ,(string-append "Hello, " name "!")))))]
    [_
        (response/xexpr `(html (body (form ((method "POST") (action "/")) "Name: " (input ((type "text") (name "name")))))))]))
        
(serve/servlet handle-form
                #:launch-browser? #t
                #:port 8080
                #:servlet-path "/")

;;; Here is an example of how to handle a GET request with a name parameter in the URL:
#lang racket

(require web-server/servlet)

(define (handle-name request)
    (match-define (list "" name) (regexp-match* #px"\\A/([^/]*)\\z" (request-uri request)))
    (response/xexpr `(html (body (p ,(string-append "Hello, " name "!"))))))

(serve/servlet handle-name
                #:launch-browser? #t
                #:port 8080
                #:servlet-path "/name/*")