# // title: network sensor packet inspection
# class solution:
class solution:
#     def inspect_packets(packet_stream, watchlist_ips):
    def inspect_packets(self, packet_stream , watchlist_ips):
#         // Initialize an empty list for flagged packets
# added on 02-08-2026
        flagged_packets = []

        #convert list to set for 0(1) time complexity

#       // OUTER LOOP: For each packet in packet_stream
        for packet in packet_stream:
#       // Extract source_ip and dest_ip from the packet
            source_ip = packet.get('source_ip')
            dest_ip = packet.get('dest_ip')           
#  // INNER LOOP: For each malicious_ip in watchlist_ips
#                 // If source_ip equals malicious_ip or dest_ip equals malicious    
#                // Add the packet to the flagged packets list
                    if source_ip == malicious_ip or dest_ip == malicious_ip:
                        flagged_packets.append(packet)
#  // Break out of the inner loop to avoid duplicate flags
                        break        
# // Return the flagged packets list
# end function
                return flagged_packets