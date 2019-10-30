class Difference:
    def __init__(self, a):
        self.__elements = a
 
	# Add your code here
    def computeDifference (self):
        diffs = []
        for i in range(0,len(a)):
            for j in range(0,len(a)):
                temp = j+1
                if temp == len(a):
                    break;
                else:
                    diff = abs(a[i]-a[j+1])
                    diffs.append(diff)
        self.maximumDifference = max(diffs)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)