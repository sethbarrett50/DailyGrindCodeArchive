;;; Here's an example of a simple program that uses threads:
#lang racket

(define (print-loop id)
    (for ([i 10])
    (printf "Thread ~a: ~a\n" id i)
    (sleep 1)))

(define t1 (thread (lambda () (print-loop "A"))))
(define t2 (thread (lambda () (print-loop "B"))))

(join-thread t1)
(join-thread t2)

;;; Here's an example of a simple program that uses futures:
#lang racket

(define (fib n)
    (if (< n 2)
        n
        (+ (future (fib (- n 1)))
            (future (fib (- n 2))))))

(fib 30)

