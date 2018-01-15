# py-udp-autobox
Python and Simulink files to send messages **through ethernet(UDP)** from `linux` to `MicroAutobox`

![20180115_134605](./assets/20180115_134605.gif)



## Dependencies

- Python 2.7 (Linux)
- MATLAB 2015b (Tested on Windows 10)




## Configurations
### sender.py
Set IP address at `./sender-py/sender.py`

```
# Bind the socket to the port
server_address = ('10.0.0.1', 5005)

...

# Address to send message
_address = ('10.0.0.2', 5005)
```

### udp_autobox.mdl
Set IP address at `./receiver-autobox/udp_autobox.mdl`.
You may need MicroAutobox License and MATLAB Simulink to modify this.


## Usage
1. Set size of array you want to send. In `sender.py`, an array with 3 `uint32` elements (`data_notpacked` variable) is set as default.
2. Set corresponding `message_size` at `udp_autobox.mdl`. If you want to receive the array with 3 `uint32` elements, set `message_size` to 12 byte (= 3 * 4 byte each).
3. Enjoy!
