# loop API

## Callable functions

- None


## Namespaces and derivable objects

- **schedule_loop** <br>
  virtual: **true** <br>
  Derivable objects: <br>
  - `schedule_loop(delay, condition)`<br>
    type: **namespace** <br>
    >Creates a folder with specific functions, that will execute specific function every `delay`.
    >If `condition` is not empty, the scheduled function will be executed using `execute <condition> run ...`.
    >You have to derive `func execute()` in this folder, which will be executed every loop.
    >Call `run` function in this folder to start the loop.

    Arguments:<br>
    `delay`: An acceptable delay when using schedule command.<br>
    `condition`: A set of execute command syntax that will be used to execute specific function and reschedule function.

    Example usage:<br>
    ```
    # run "function test:exe_per_5t/run" to start the loop
    # make every player say his/her name every 5 ticks, until no one is standing on a stone block
    namespace test()
    {
      folder exe_per_5t() from schedule_loop(5t, "as @a at @s if block ~ ~-1 ~ minecraft:stone")
      {
        say @s
      }
    }
    ```

- **while_loop** <br>
  virtual: **true** <br>
  Derivable objects: <br>
  - `while_loop(delay, condition)`<br>
    type: **namespace** <br>
    >Creates a folder with specific functions, that will instantly execute specific function many times until the condition is not met.
    >You have to derive `func execute()` in this folder, which will be executed every loop.
    >Call `run` function in this folder to start the loop.

    Arguments:<br>
    `condition`: A set of execute command syntax that will be used to execute specific function and decide whether to loop again.

    Example usage:<br>
    ```
    # make a player run "function test:while_drop/run" to start the loop
    # tp the player straight down until the block below is a stone block.
    namespace test()
    {
      folder while_drop() from while_loop("unless block ~ ~-1 ~ minecraft:stone positioned ~ ~-1 ~")
      {
        func execute()
        {
          execute if block ~ ~-1 ~ minecraft:stone run tp @s ~ ~ ~
        }
      }
    }
    ```

- **for_loop** <br>
  virtual: **false** <br>
  Derivable objects: <br>
  - `for_loop().for(times, condition)`<br>
    type: **folder** <br>
    >Creates a folder with specific functions, that will instantly execute specific function for specific times or until the condition is not met.
    >You have to derive `func execute()` in this folder, which will be executed every loop.
    >Call `run` function in this folder to start the loop.

    Arguments:<br>
    `times`: A constant integer or `<entity> <scoreboard objectives>` string.
    `condition`: A set of execute command syntax that will be used to execute specific function and decide whether to loop again.

    Example usage:<br>
    ```
    # make a player run "function test:for_forward/run" to start the loop
    # tp the player foward 5 times or until the forward block is a stone block.
    namespace test()
    {
      folder for_forward() from for_loop().for(5, "rotated ~ 0 positioned ^ ^ ^1 unless block ~ ~ ~ minecraft:stone")
      {
        func execute()
        {
          tp @s ~ ~ ~
        }
      }
    }
    ```
    

## Used tags

-	load
	-	`for_loop:initial`
