;  For example, here's how you would create a module called "my-module": (defmodule my-module)
; After you have created a module, you can start adding rules and data to it. 
; For example, here's how you would add a rule to the "my-module" module:
(defmodule my-module)
(defrule my-rule
(person (name ?name) (age ?age))
(test (> ?age 18))
=>
(printout t "Person " ?name " is older than 18." crlf))

(assert (person (name "John") (age 30)))
(assert (person (name "Jane") (age 20)))
(run)

; Here's an example of how you would include the "my-module" module in a main program:
(defmodule main)
(load "my-module.clp")
(run)