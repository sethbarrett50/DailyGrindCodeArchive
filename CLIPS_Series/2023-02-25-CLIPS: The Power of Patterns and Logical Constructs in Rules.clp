; Here's an example of a simple rule that uses a pattern:
(defrule example-rule
(person (name ?name) (age ?age))
(test (> ?age 18))
=>
(printout t "Person " ?name " is older than 18." crlf))

; Here's an example of a rule that uses the "and" construct:
(defrule example-rule
(person (name ?name) (age ?age) (gender ?gender))
(and (test (> ?age 18))
(test (or (eq ?gender "Male") (eq ?gender "Female"))))
=>
(printout t "Person " ?name " is older than 18 and is male or female." crlf))
