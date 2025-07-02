from scapy.all import sniff

def process_packet(packet):
    print("\nCaptured Packet:")
    
    if packet.haslayer('IP'):
       
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        
        
        protocol = packet.proto
        
       
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        
        
        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"Payload: {payload[:100]}")  
        else:
            print("No payload")
    
    else:
        print("Packet is not IP based")


sniff(prn=process_packet, store=0, count=10)