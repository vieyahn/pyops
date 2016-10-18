import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

#在正则表达式中*是贪婪模式 会曹兆最长的可能匹配

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))  #this is what i don't want

str_pat1 = re.compile(r'\"(.*?)\"')

print(str_pat1.findall(text2))
