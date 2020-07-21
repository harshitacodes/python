seconds = 96768
seconds_to_report = (seconds/ 1) % (60)
minutes = (seconds/60) % 60 
hours = (seconds/(60*60)) % 24
days = seconds/(60*60*24)
print days, hours, minutes, seconds_to_report