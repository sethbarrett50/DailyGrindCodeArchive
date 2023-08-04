; For example, here's how you would create a template for a "person" object:
(deftemplate person
(slot name (type STRING))
(slot age (type INTEGER)))

; For example, here's how you would create two instances of the "person" object:
(deftemplate person
(slot name (type STRING))
(slot age (type INTEGER)))

(assert (person (name "John") (age 30)))
(assert (person (name "Jane") (age 20)))

