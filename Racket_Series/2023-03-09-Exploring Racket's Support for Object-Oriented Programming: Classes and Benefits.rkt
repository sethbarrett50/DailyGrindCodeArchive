;;; Here's an example of a simple class that defines a rectangle:
#lang racket

(define-class rectangle%
    (init width height)
    (define width width)
    (define height height)
    (define (area) (* width height)))

;;; We can create an object of the rectangle% class like this:
#lang racket

(require (class "rectangle.rkt"))

(define r (new rectangle% [width 5] [height 10]))

(send r area)