
def solution(files):
    answer = []
    files_split_list=[]
    for i in files:
        HEAD = ''
        NUMBER = ''
        TAIL = ''
        for j in i:
            if j.isdigit():
                break
            HEAD+=j
        for j in i[len(HEAD):]:
            if j.isdigit():
                NUMBER+=j
            else:
                break
        TAIL = i[len(HEAD)+len(NUMBER):]
        files_split_list.append([HEAD,NUMBER,TAIL])
        
    #print(files_split_list)
    files_HEAD_sort = sorted(files_split_list,key=lambda x : x[0].lower())
    files_NUMBER_sort = sorted(files_HEAD_sort, key=lambda x : int(x[1]))
    for i in files_NUMBER_sort:
        answer.append("".join(i))
    #print(answer)
    #print(files_NUMBER_sort)
    return answer
solution(["img12.png", "img10.png",
           "img02.png", "img1.png",
           "IMG01.GIF", "img2.JPG"])
'''

a=[['ac',2],['ad',5],['ac',6],['ad',4]]
sorted_a = sorted(a,key=lambda x: x[0])
print(sorted_a)
'''