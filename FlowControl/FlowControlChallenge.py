
ip_address = input("Enter an IP Address: ")
if ip_address[-1] != '.':
    ip_address += '.'

number_segment = 1
segment_length = 0
# char = ''

for char in ip_address:
    if char == '.':
        print("The length of segment {0} is {1}".format(number_segment, segment_length))
        segment_length = 0
        number_segment += 1
    else:
        segment_length += 1

# if char != '.':
#     print("The length of segment {0} is {1}".format(number_segment, segment_length))
