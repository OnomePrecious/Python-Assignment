sample_string = "google.com"
sample = dict() # = {}

for char in sample_string:
     sample[char] = sample_string.count(char)

print(sample)


sample_list = 'google.com'
print({sample:sample_list.count(sample) for sample in sample_list})