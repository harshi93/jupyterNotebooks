"""
The slow cooker problem, there is a hotcooker full of delicious soup but there are two consumers and each must get fair
share of soup in programming context these two consumers can be seen as two hungry thread that are competing for shared
resource hot soup and slow cooker lid will act as mutex to protect it. Only the thread that holds the lid can
- open the lid
- check how much soup is left
- determine if it's their turn
- modify the amount of soup that is left

mutex - it restricts multiple threads from taking soup or acquiring shared resource at the same time, but it doesn't
give signals to processes to synchronize their action

busy waiting - is the process of repeatedly acquiring and releasing lock to see if certain condition is met in order to
continue, not very efficient

condition variable
- acts as a queue of threads waiting for certain conditions to occur, think of it as a place for threads to wait and be
notified
- it is associated with mutex and work together to implement a higher level construct called a monitor

monitor
- protect section of code with mutual exclusion
- provide ability for threads to wait or be blocked until certain condition has occured
- provide mechanism to notify threads waiting when the condition has met


think of a room that has some resource that you wanna access now there is a guard sitting at the door (mutex), a certain
condition is met and guard allows the process to come in while the process inside performs its desired action (executing
critical section of code) it asks the guard to lock the door aka lock on mutex. Once the process inside is done doing
what it is supposed to it signals the condition or next condition to execute and releases the lock on door

condition variable has three operations
- wait
    - a process acquires mutex, checks for condition, sees that it's not their turn execute the
    wait condition after which
    - lock on mutex is released automatically
    - process goes to sleep or pause state by entering into waiting queue
    - reacquiring lock when woken up
- signal
    - once the process is done executing it's operation it uses signal operation to notify process
    in the waiting queue
    - depending on the programming language being used this can also be referred to as notify or wake
- broadcast
    - same as signal operation except that it wakes up all threads in the condition variable queue
    - depeneding on the programming language being used this can also be referred to as notify all or wake all

"""