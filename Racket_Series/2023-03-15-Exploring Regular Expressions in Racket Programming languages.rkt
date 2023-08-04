;;; Here's an example of using regex in Racket:
#lang racket

(require racket/regexp)

(define regex (regexp #rx"^hello, (.*)$"))

(define (my-function str)
(if (regexp-match? regex str)
    (let ((match (regexp-match regex str)))
        (match:get match 1))
    "no match"))