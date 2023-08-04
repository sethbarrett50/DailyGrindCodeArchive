;;; Here's an example of a higher-order function that takes a function f and an integer n as arguments and applies f to n n times:
(define (repeat f n)
    (if (= n 0)
        (lambda (x) x)
        (compose f (repeat f (- n 1)))))
  
(define (square x)
(* x x))

((repeat square 3) 2) ; returns 256

;;; Here's an example of a closure that takes an initial value x and returns a function that adds x to its argument:
(define (make-adder x)
    (lambda (y) (+ x y)))
  
(define add-5 (make-adder 5))
(add-5 10) ; returns 15