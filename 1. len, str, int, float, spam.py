# 1.Hello, world!
print('Hello, world!')
myName = input()
print('It is good to meet you, ' + myName + '!')

# 2.len('123')
print('The length of your name is:')    
print(len(myName))  # [Kítựđặcbiệt+Chữ+Số+Dấucách, ò chỉ tính 1 kí tự o]
print('Monster ảt ả t?! . 21 --> The length of this clause is:')
print(len('Monster ảt ả t?! . 21'))
#123
# code ghép
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# 3.str(0)
print('str')    
print(str(11.4))    # [giữ nguyên dạng số liệu nhập vào]
print(str(11.400))  # [ko điền '0' đằng trc số đc]

# 4.int('42') 
print('int') 
print(int(7))           # [lam tron xuong]
print(int(7.7) + 1)     # [ko điền '0' đằng trc số đc]
print(int(11.400))

# 5.float('3.14')
print('float') 
print(float('12'))      # [hiển thị số liệu dạng có " , " + e/E biểu thị lũy thừa 10]
print(float('135.15'))
print(float('0012.34500'))
print('x= ' + str(float('35e3')), '   y= ' + str(float('12E4')), '   z= ' + str(float('-87.7e100')))

# 6.[spam ra KQ dạng chuỗi - nhập số thì số cũng như chữ thôi, ko tính đc]
print('spam số - dạng chuỗi') 
spam = input()  
spam    #[spam các số đc lúc ko có code hiển thị đằng sau]

# [spam ra KQ dạng số - nhập số thì tính đc bthg]
print('spam số - dạng số') 
spam = input()
spam = int(spam)   
print(str(float(spam * 10 / 3))) 


# https://quizlet.com/gdnewell17/sets

# 1. Which of the following are operators, and which are values?
# https://toidicode.com/cac-toan-tu-co-ban-trong-python-349.html  
    # *
    # 'hello'
    # -88.8
    # -         # [toán tử là dấu trong phép tính, g.trị là dữ liệu nhập vào]
    # /
    # +
    # 5

# 2. Which of the following is a variable, and which is a string?
    # spam      --> Variable (biến)
    # 'spam'    --> String (chuỗi)

# 3. Name three data types.     --> 6 loại cơ bản: Numbers, List, Tuple, Strings, Set, Dictionary
# https://texmath.com/python-ban-co-phan-biet-dung-data-types-va-data-structures-trong-python/       # [các kiểu dữ liệu chung chung]
# https://viblo.asia/p/cac-kieu-du-lieu-co-ban-trong-python-Ljy5VmRolra                              # [1 số hàm cơ bản]

# 4. What is an expression made up of? What do all expressions do?
        # --> An expression is a combination of values, variables, operators, and calls to functions. To produce some other value.
        # --> Một biểu thức là sự kết hợp của Các giá trị, biến, toán tử và lệnh gọi hàm. Để tạo ra một số giá trị khác. 
    # [An expression is a combination of value & operators. All expressions evaluate (that is, reduce) to a single value.]
    # [Một biểu thức là sự kết hợp của giá trị & toán tử. Tất cả các biểu thức đánh giá (nghĩa là giảm) thành một giá trị duy nhất.]

# 5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
        # --> Expressions produce a value, and that value will be passed into the function. Statements don't produce a value, and so they can't be used as function arguments.
        # --> Các biểu thức tạo ra 1 giá trị, và giá trị đó sẽ được chuyển vào hàm. Các câu lệnh không tạo ra 1 giá trị, và vì vậy chúng không thể được sử dụng làm đối số của hàm.
    # [An expression evaluates to a single value. A statement does not.]

# 6. What does the variable bacon contain after the following code runs?
    # bacon = 20    --> bacon = 20. The bacon + 1 expression does not reassign the value in bacon (that would need an assignment statement: bacon = bacon + 1)
    # bacon + 1     [cần một câu lệnh gán: bacon = bacon + 1]

# 7. What should the following two expressions evaluate to?
    # 'spam' + 'spamspam'       --> [đều ra 'spamspamspam']
    # 'spam' * 3

# 8. Why is eggs a valid variable name while 100 is invalid?
    # --> [Tên biến ko thể b.đầu = số]
# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
    # --> int: số nguyên, float: số dấu phẩy động, str: chuỗi của 1 g.trị
# 10. Why does this expression cause an error? How can you fix it?
    # 'I have eaten ' + 99 + ' burritos.'
        # --> str(99)