;;; Lists are perhaps the most commonly used data structure in Racket, and they can be created using the list function
(define my-list (list 1 2 3))

;;; Lists can be manipulated using a variety of functions, such as cons, which adds an element to the beginning of a list, and append, which concatenates two or more lists. 
;;; Here's an example that demonstrates these functions:
(define my-list (list 1 2 3))
(define my-other-list (list 4 5 6))
(define my-new-list (append my-list (cons 0 my-other-list)))

;;; Functions are a fundamental concept in Racket, and they are defined using the define keyword. 
;;; Here's an example of a simple function that takes two arguments and returns their sum:
(define (add a b)
    (+ a b))

;;; This function can be called like this:
(add 1 2) ; returns 3

;;; Functions can also have optional arguments and default values. 
;;; Here's an example:
(define (multiply a b #:c [c 1])
    (* a b c))

;;; Racket provides several control structures for controlling the flow of execution in a program. 
;;; The most commonly used control structures are if, cond, and case. 
;;; Here's an example of an if statement:
(define (is-positive x)
    (if (> x 0)
        #t
        #f))

;;; Here's an example of a cond statement:
(define (check-grade grade)
    (cond
      [(>= grade 90) "A"]
      [(>= grade 80) "B"]
      [(>= grade 70) "C"]
      [(>= grade 60) "D"]
      [else "F"]))