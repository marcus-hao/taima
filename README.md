# taima

Taima is a Pomodoro timer for the command line.
It is barebones to reduce distraction.

> *Note: taima uses the winsound library, so it only works on Windows.*

## Usage

By default, taima sets a timer for 25 minutes.
This can be changed in the program flags.

    python taima.py -t <duration>

Flags can also be set for the task description and custom notification sounds.
For more information:

    python taima.py -h