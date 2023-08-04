;;; Here's an example of using error in Racket:
#lang racket

(define (my-function arg)
    (if (not (string? arg))
        (error "my-function expects a string argument")
        ; rest of the function implementation
        ))

;;; Here's an example of using with-handlers in Racket:
#lang racket

(define (my-function arg)
    (with-handlers ([exn:fail?
                    (lambda (exn)
                        (error "my-function: an error occurred"))])
    ; rest of the function implementation
    ))