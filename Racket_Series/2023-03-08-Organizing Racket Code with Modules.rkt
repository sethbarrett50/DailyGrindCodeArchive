;;; Here's an example of a simple module that defines a function:
#lang racket

(module mymodule racket
    (define (square x)
    (* x x)))

(provide square)

;;; We can use the square function like this:
#lang racket

(require 'mymodule)

(square 5)