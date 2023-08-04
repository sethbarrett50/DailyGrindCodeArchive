;;; Here's an example of a simple test case in Racket:
#lang racket

(require rackunit)

(define (test-my-function)
    (check-equal? (my-function 2) 4)
    (check-equal? (my-function -3) 9))

;;; Here's an example of a simple integration test in Racket:
#lang racket

(require web-server/testing)

(define (test-my-web-app)
    (with-handlers ([exn:fail? (lambda (exn) (void))])
    (run-server-tests
        (list
        (test-post "/submit" "name=John&email=john@example.com"
                    (λ (response)
                    (check-equal? (response-status response) 200)
                    (check-true (string-contains? (response-body/response response)
                                                    "Thank you for submitting your information!"))))
        (test-get "/contact"
                    (λ (response)
                    (check-equal? (response-status response) 200)
                    (check-true (string-contains? (response-body/response response)
                                                    "Contact Us"))))))))

(test-my-web-app)
