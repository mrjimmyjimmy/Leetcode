# Network concept
## 1. Five layers
Layer Name     | Protcol    | Data unit    | Addressing  
-------- | :------:  | :-------: | :---------:
Application    |  HTTP,DNS | message| none 
Transport  | TCP/UDP | Segement/Datagram | port
Network | IP   | Packets | IP address
Data Link | Ethernet | Frames | MAC address
Physical | 802.11 | Bits | none

- **Application layer**: translate data for software
- **Transport layer**: process communicate using connection/broadcast
- **Network layer**: routing, where it from and where to go
- **Data Link layer**: cut 0/1 to serveral frames(include head and data)
- **Physical layer**: hardware connection, transport 0/1
