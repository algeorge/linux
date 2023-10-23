import re

# log string to parse, replace line breaks
log_str = '''libgomp1:amd64 (10.2.1-6, automatic), libwebpmux3:amd64 ... intel-media-va-driver:amd64 (21.1.1+dfsg1-1, automatic)'''
log_str = log_str.replace('\n', '') #remove line breaks from console copy-paste

# remove ':amd64 (..)' and split by comma
clean_list = re.sub(r':amd64 \([^)]+\)', '', log_str).split(',')

# clean up whitespace
clean_list = list(map(str.strip, clean_list))

# compose `apt remove` command
apt_command = 'sudo apt remove ' + ' '.join(clean_list)
print(apt_command)
