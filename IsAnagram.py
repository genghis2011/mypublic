
def IsAnagram(s, t):
	if sorted(s) == sorted(t):
		return True
	else:
		return False


#isAnagram = IsAnagram("anagram", "nagaram")
#print(isAnagram)
