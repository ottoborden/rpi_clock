# TODO

## Known Issues
* Screen does go blank in 30 mins despite following instructions in README
  * 10 minutes if the RPi is not logged in as `pi`
  * Only when the app is running?
    * Seems to be that screen will stay awake at CLI
## Unsolved Problems
* How to architect this thing
  * Experiment with MVC
    * Model will be defined by me (current time, time-triggered events)
    * Views
      * Standard time view
      * Set time 
      * Set alarm
      * Set audio file
    * Controller
      * Touch screen
      * Events triggered by alarms
