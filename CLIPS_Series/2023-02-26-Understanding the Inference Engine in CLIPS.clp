; Here's an example of a simple rule that uses the inference engine:
(defrule example-rule
(person (name ?name) (age ?age))
(test (> ?age 18))
=>
(printout t "Person " ?name " is older than 18." crlf))

(assert (person (name "John") (age 30)))
(assert (person (name "Jane") (age 20)))
(run)

; Here's an example of a simple program that uses the "halt" command to stop the inference engine:
(defrule example-rule
(person (name ?name) (age ?age))
(test (> ?age 18))
=>
(printout t "Person " ?name " is older than 18." crlf)
(halt))

(assert (person (name "John") (age 30)))
(assert (person (name "Jane") (age 20)))
(run)