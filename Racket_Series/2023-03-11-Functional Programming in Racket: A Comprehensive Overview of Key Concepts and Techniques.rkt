;;; Here's an example of a simple function in Racket:
#lang racket

(define (square x)
    (* x x))

(square 5) ; Returns 25

;;; Here's an example of a higher-order function in Racket:
#lang racket

(define (apply-twice f x)
    (f (f x)))

(apply-twice square 5) ; Returns 625

;;; Here's an example of a lambda expression in Racket:
#lang racket

((lambda (x) (* x x)) 5) ; Returns 25

;;; Here's an example of a closure in Racket:
#lang racket

(define (make-adder x)
    (lambda (y) (+ x y)))

(define add5 (make-adder 5))
(add5 10) ; Returns 15

;;; Here's an example of an immutable data structure in Racket:
#lang racket

(define my-list '(1 2))
(define my-new-list (cons 3 my-list))

my-list 
; Returns '(1 2)

my-new-list 
; Returns '(3 1 2)