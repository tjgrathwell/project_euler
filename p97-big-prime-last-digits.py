# Find the last 10 digits of 28433 * 2 ** 7830457 + 1
# I initially figured the answer involves finding a pattern where the last 10 digits start repeating after a certain time, and using that to extrapolate what they'll be at 7830457
# But the digits don't repeat until well in the 7 millionth power so it's not worth it... just do the computation directly on the last 7 digits all the time and hope for the best
# Takes like 6 seconds, but not as slow as the stupid int(str(d*2)[-10:]) method I used before I read the forum.
# There's a faster way to multiply out powers than the linear solution: http://www.osix.net/modules/article/?id=696

d = 1
for i in xrange(7830457):
    d = (d * 2) % 10000000000

d = (d * 28433 + 1) % 10000000000
print d