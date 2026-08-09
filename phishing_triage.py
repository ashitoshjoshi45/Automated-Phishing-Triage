#added-on 09-08-2026
# 
# function analyze_phishing_url(url)
#   set ip_pattern to match standard IPv4 addresses
  
#   if length of url is greater than 75 then
#     return "[HIGH RISK]: URL length exceeds safety threshold."
#   else if url matches ip_pattern then
#     return "[HIGH RISK]: URL uses raw IP address."
#   else if url contains "@" symbol then
#     return "[MEDIUM RISK]: URL contains '@' symbol."
#   else
#     return "[LOW RISK]: No obvious static indicators found."
#   end if
# end function