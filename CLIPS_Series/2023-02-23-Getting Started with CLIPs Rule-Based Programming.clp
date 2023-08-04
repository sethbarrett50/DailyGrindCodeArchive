; Here is a simple example of a CLIPs program that demonstrates the basics of rule-based programming. 
; This program defines a set of rules and a knowledge base to find the biggest number in a list of numbers.
(defrule find-biggest-number
(declare (salience 10))
(number ?x)
(not (number ?y&:(> ?y ?x)))
=>
(printout t "The biggest number is " ?x crlf))

(deftemplate number
"Template for storing numbers in the knowledge base."
(slot value))

(reset)
(assert (number (value 3)))
(assert (number (value 4)))
(assert (number (value 6)))
(assert (number (value 1)))
(run)