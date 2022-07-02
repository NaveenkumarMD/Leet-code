# =begin
#     Ruby is an open-source object-oriented scripting language 
# invented in the mid-90s by Yukihiro Matsumoto.

# Unlike languages such as C and C++, a scripting language doesn't talk directly to hardware. 
# It's written to a text file and then parsed by an interpreter and turned into code.

# =end


# # --------------------------Dynamic typing or loosely typed -------------------

# # name="naveen"
# # puts name
# name=12
# puts name


    


# # --------------------------Data types-------------------------

# # ***Numbers
# # ***Strings
# # ***Symobols
# # ***Hashes
# # ***Arrays
# # ***Booleans


# # object.class returns the data type
# # Everything is a object
# name="naveen"
# puts name.class 

# #*** Numbers

# #Fixmum number -they are normal numbers

# a=12
# puts a.class

# # Float - they are floating point numbers
# b=12.32134
# puts b.class

# #Bignum- they are very big numbers
# c=2332646234777777777747627543276252346536543654
# puts c.class

# # #-------------------------------number methods-------------------------

# # puts a.abs

# # puts a.round
# # puts a.ceil
# # puts a.floor
# # puts a.to_s # string
# # puts a.to_f # float
# # puts a.to_i #integer
# # puts a.odd? #checks for odd
# # puts a.even? #checks for even

# # puts a.next # returns next value
# # puts a.succ # returns next value
# # puts a.pred # returns previous value

# a=12
# b=14
# puts a+b
# puts a-b
# puts a*b
# puts a/b
# puts a%b
# puts a**b


#*** -------------------------------------strings----------------------

# first_name="naveen"
# last_name='kumar' # sigle or double quotes

# puts first_name+" "+last_name #string concatenation
# puts first_name[0] #string indexing
# puts first_name[0,3] #string indexing
# puts first_name[-1] #string indexing
# puts first_name[-3,3] #string indexing
# puts first_name[0..4] # string slicing

# puts first_name.length #string length
# puts first_name.upcase #string upcase
# puts first_name.downcase #string downcase
# puts first_name.capitalize #string capitalize
# puts first_name.include?("n") #string include
# puts first_name.include?("N") #string include

#mutiline string
# puts "this is a multiline string
# this is the second line
# fwewqyugf4
# gereqge"

# puts %/this is a multiline string
# this is the second line/

# puts <<STRING
# this is a multiline string
# this is the second line
# STRING

# string formatting
# first_name="naveen"
# j=34
# puts "this is my name #{first_name} #{j}"

# # comparing strings

# x="naveen"
# y="naveen"

# puts x==y
# puts x.eql?(y)
# puts x.casecmp(y) # will return 0 if equal 1 if x is higher and -1 if y is higher
# # casecmp will compare the strings ignoring the case

# --------------------------------------------Loops before getting into arrays----------------------------

#if loop

a=12
# if a==12
#     puts "a is 12"
# else
#     puts "a is not 12"
# end

# a=34
# if a==12
#     puts "a is 12"
# elsif a==21
#     puts "a is 21"
# else
#     puts "a is not 12 or 21"    
# end

# for loop

# for i in 1..10 do
#     puts i
# end

# arr=[1,2,3,4,5]
# for i in arr do
#     puts i
# end

# switch case
# d=34
# case d
# when 34
#     puts "34"
# when 35
#     puts "35"
# else
#     puts "default condition"
# end

# while loop

# i=0
# while i<4 do
#     puts i
#     i+=1    
# end

# #forever loop
# i=0
# loop do
#    i+=1
#    puts i
# #    if i==4
# #        break
# #    end 
# end
# # redo loop

# i = 0   
# while(i < 5)   # Prints "012345" instead of "01234"   
#   puts i   
#   i += 1   
#    redo if i == 5   #runs without seeing the conditions
# end 

# until

# i=3
# until i==0 do
#     puts i
#     i-=1    
# end

#--------------------------------------------arrays-----------------------------------
# arr=[1,2,3,"naveen",3542.5342]
# # puts arr 
# puts arr[0]
# puts arr[0,3]
# puts arr[-1]
# for i in arr do
#     puts i
# end
# using array class

# arr=Array.new(10)
# puts arr

# puts arr.length
# puts arr.size
# arr=Array.new(10,1)
# puts arr

# arr=Array(1..10)
# puts arr
# arr=Array(1..10).to_s # converting arr to string
# puts arr.class
# puts arr

# arr=[1,2,3,4]
# arr.at(-1) # returns the last element
# arr.fetch(2) # returns the element at index 2
# arr.first # returns the first element
# arr.last # returns the last element

# arr.pop # returns the last element and removes it
# arr.push(10) # adds the element to the end

# arr.shift # removes the first element
# arr.unshift(10) # adds the element to the beginning
# arr.insert(2,10) # inserts the element at index 2

# arr.delete_at(2) # deletes the element at index 2

# arr.delete(2) # deletes the element 2

# arr.reverse # reverses the array

# arr.sort # sorts the array
# arr.shuffle # shuffles the array

# arr=[1,2,3]
# l= arr.join # joins the array
# puts l.class

#--------------------------------------------hashes-----------------------------------

dit={
    "name"=>"naveen",
    "course"=>"ruby",
    "fees"=>"0000",
  
}
puts dit

puts dit["name"]

# #modifying
# dit["name"]="naveen kumar"

# puts dit

# #hash methods
# dit.each do |key,value|
#     puts "#{key} => #{value}"
# end

# dit.clear()
# puts dit


# -------------------------------------------Functions-----------------------------------

def print_name #method without params
    puts "naveen"    
end

def print_name(name)
    puts name
end # method with params
# with return keyword

# def add(a,b)
#     return a+b
# end
# puts add(0342,324)
# def print_name(name,course)
#     puts "#{name} is taking #{course}"
# end # method with multiple params

# #any data type

# def print_type(x)
#     puts x.class
# end

# print_type("naveen")
# print_type(10)

# # -----------------------------------classes---------------------------------

# class Animal
#     def initialize(name,weight,canfly)# constructors
#         @name=name  #instance variables @ represents this or self
#         @weight=weight
#         @canfly=canfly
#     end
#     def print
#         puts "name is #{@name} weight is #{@weight} can fly is #{@canfly}"
#     end        
# end

# x=Animal.new("Hippo",10000,true)
# x.print()

# #sub classes

# class Shape
#     def initialize(name,color) # constructors
#         @name=name
#         @color=color
#     end
# end
# class Square < Shape
#     def initialize(name,color,side)
#         super(name,color)
#         @side=side
#     end
#     def get_area
#         return @side*@side
#     end
#     def set_side(side)
#         @side=side

#     end
# end
# c=Square.new("square","red",10)
# puts c.get_area()

# importing a module



