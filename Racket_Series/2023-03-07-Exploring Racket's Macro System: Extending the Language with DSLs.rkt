;;; Here's an example of a macro that implements a simple DSL for generating HTML:
#lang racket

(define-syntax-rule (html tag attrs content ...)
    (begin
        (printf "<~a" ',tag)
        (for-each (lambda (attr)
                    (printf " ~a=\"~a\"" (car attr) (cdr attr)))
                ',attrs)
        (printf ">")
        ,content
        (printf "</~a>" ',tag)))

;;; We can use the html macro like this:
(html h1 '((class . "title")) "Hello, world!")

;;; This generates the following HTML code:
; <h1 class="title">Hello, world!</h1>
