# random API

## Callable functions

-	`random:initial`<br>
	>Initializes scoreboard objectives and uses current gametime to set seed.
	>Called by `load` function

-	`random:set_seed`<br>
	>Uses current gametime to set seed.


## Derivable objects

-	`random().generate(min, max, result)`<br>
	type: **func** <br>
	>Creates a function that generate a random number between `min` and `max`, and then store the number in `result`.
	
	**Arguments:** <br>
	`min`: A constant integer or `<entity> <scoreboard objectives>` string.<br>
	`max`: A constant integer or `<entity> <scoreboard objectives>` string.<br>
	`result`: An `<entity> <scoreboard objectives>` string.
	
	**Example usage:** <br>
	```
	# make a player run "test:random_a_100" to generate a random number between the player's test score and 100
	# the generated number is stored in the player's test2 score
	namespace test()
	{
		func random_a_100() from random().generate("@s test", 100, "@s test2");
	}
	```


## Used tags

-	load
	-	`random:initial`
