'''
paragraphs = re.split(r'[ \t\r\f\v]*\n[ \t\r\f\v]*\n[ \t\r\f\v]*',
                      story)  # splits story into list of paragraphs
print(len(paragraphs))
first = paragraphs[0].split()
index = first.index('slow.')
first[index] = '_'*int(len(first[index])-1) + '.'
print(first)
'''
