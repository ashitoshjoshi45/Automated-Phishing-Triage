# // title: network sensor packet inspection
# class solution:
#     def inspect_packets(packet_stream, watchlist_ips):
#         // Initialize an empty list for flagged packets
#         // OUTER LOOP: For each packet in packet_stream
#             // Extract source_ip and dest_ip from the packet
#             // INNER LOOP: For each malicious_ip in watchlist_ips
#                 // If source_ip equals malicious_ip or dest_ip equals malicious_ip
#                     // Add the packet to the flagged packets list
#                     // Break out of the inner loop to avoid duplicate flags
#         // Return the flagged packets list
# end function