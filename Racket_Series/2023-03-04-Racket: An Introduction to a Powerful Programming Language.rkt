;;; The following code defines a function that computes the factorial of a number:
(define (factorial n)
    (if (= n 0)
        1
        (* n (factorial (- n 1)))))

;;; The next example defines a function that adds two numbers together:
(define (add a b)
    (+ a b))

;;; Here is an example of a macro that defines a new loop construct:
(define-syntax-rule (loop i from start to end do body)
    (for ([i (in-range start end)])
      body))

;;; With this macro, you can write loops like this:
(loop i from 1 to 10 do
    (displayln i))
