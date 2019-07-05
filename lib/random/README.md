# random API

## Callable functions

-	`random:initial`<br>
	Initializes scoreboard objectives and uses current gametime to set seed.

-	`random:set_seed`<br>
	Uses current gametime to set seed.


## Derivable objects

-	`random().generate(min, max, result)`<br>
	type: **func** <br>
	Creates a function that generate a random number between `min` and `max`, and then store the number in `result`.
	
	Arguments:<br>
	-	`min`: A constant integer or `<entity> <scoreboard objectives>` string.
	-	`max`: A constant integer or `<entity> <scoreboard objectives>` string.
	-	`result`: An `<entity> <scoreboard objectives>` string.
	
	Example usage:<br>
	-	`func random_10_20() from random().generate(10, 20, "@s test")`
  	-	`func random_a_100() from random().generate("@s test", 100, "@s test2")`


## Used tags

-	load
	-	`random:initial`
