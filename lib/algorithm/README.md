# algorithm API

## Callable functions

-	`compare:initial`<br>
	>Initializes scoreboard objectives.


## Derivable objects

-	`compare().min(targets, objective, result_tag)`<br>
	type: **folder** <br>
	>Add `result_tag` to the `targets` with the minimum value of the scoreboard `objective`.
	
	**Arguments:** <br>
	`targets`: An entity selector that defines which entities will have their scores compared.<br>
	`objective`: A scoreboard objectives that is going to be compared.<br>
	`result_tag`: The tag that will be added to the target with the minimum score.
	
	**Example usage:** <br>
	```
	# run "test:minimum_death/search" to add a tag `winner` to the player with minimum score in `death` scoreboard
	namespace test()
	{
		folder minimum_death() from compare().min("@a[gamemode=!spectator]", "death", "winner");
	}
	```

-	`compare().max(targets, objective, result_tag)`<br>
	type: **folder** <br>
	>Add `result_tag` to the `targets` with the maximum value of the scoreboard `objective`.
	
	**Arguments:** <br>
	`targets`: An entity selector that defines which entities will have their scores compared.<br>
	`objective`: A scoreboard objectives that is going to be compared.<br>
	`result_tag`: The tag that will be added to the target with the maximum score.
	
	**Example usage:** <br>
	```
	# run "test:maximum_kill/search" to add a tag `winner` to the player with maximum score in `kill` scoreboard
	namespace test()
	{
		folder maximum_kill() from compare().max("@a[gamemode=!spectator]", "kill", "winner");
	}
	```


## Used tags

-	load
	-	`algorithm:initial`
