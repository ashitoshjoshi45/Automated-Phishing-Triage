# added on 14-08-2026

#function parse_phishing_email(eml_file_path)
#   initialize artifacts dictionary to store sender, subject, and urls
  # open the eml_file_path and parse the email content
  # extract the "From" and "Subject" fields
  
  # check if the email contains multiple parts
  # outer loop: iterate through each part of the email
  #    inner loop / condition: if the part is text/plain or text/html
  #       append the content to our main body string
  
  # use regular expressions to find all URLs in the extracted body
  # return the dictionary of extracted artifacts
# end function