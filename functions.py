 #functions
def add(a,b):
    z=a+b
    return(z)
print(add(10,20))

def largest(a,b):
    if a>b:
        return(f" {a} is the largest ")
    else:
        return(f" {b} is the largest ")
print(largest(15,8))

def even_odd(num):
    if num%2==0:
        return(f"{num} is even")
    else:
        return(f"{num} is odd")
print(even_odd(9))

def revstr(name):
    reversedname=name[::-1]
    return(reversedname)
print(revstr('python'))

args and kwargs
def add_numbers(*num):
    total=0
    for i in num:
        total = total+i
    print(total)
add_numbers(1,2,3,9,7,6)

def largest_number(*nums):
    largest=nums[0]
    for num in nums:
        if num>largest:
            largest = num
    return largest
print(largest_number(5,12,3,20,8))

def student_info(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value} ")
student_info(name = "pavan",age = "21",city="chennai")

4. Count Keyword Arguments (**kwargs
def count_info(**kwargs):
    count=0
    for key, value in kwargs.items():
        count = count+1
    print(count)
print(count_info(name="Pavan", age=21, city="Chennai"))

def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("python"))

def reverse_string(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    return reverse

print(reverse_string("python"))

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))

def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("I love Python"))

def sum_digits(num):
    total = 0

    for digit in str(num):
        total += int(digit)

    return total

print(sum_digits(1234)) 






