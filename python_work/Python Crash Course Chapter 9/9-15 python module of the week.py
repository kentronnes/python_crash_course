
import difflib
from difflib_data import *

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print("\n".join(diff))

# diff = difflib.unified_diff(
# 	text1_lines,
# 	text2_lines,
# 	lineterm='',
# )
# print('\n'.join(diff))


# Why do we use '%04.3f' in Python? [closed]

# The format %04.3f specifies:

# %f => float value precision
# %.3f => float value with 3 decimal precision
# %04.3f => float value, with 3 decimal precision 
# and 4 digits to the left of decimal. The 04 implies 
# that the number will be 