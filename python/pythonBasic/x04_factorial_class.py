class Factorial(object):
    def __init__(self, tar_num): #target_number 여기선 0(맨뒤 무엇의 개수를 구할지)
        self.tar_num = tar_num
    def factorial(self, num): #num에 대한 factorial
        self.num = num
        if num <= 1:
            return 1
        else: #재귀함수로 factorial 구현
            return num * self.factorial(n-1)
    def tar_num_count(self, m):
        fac_nb = self.factorial(m)
        fac_nb = str(fac_nb) #fac_nb를 문자화 => for문 돌림
        count = 0
        for i in fac_nb[::-1]: #역으로 돌림
            if int(i) != self.tar_num: #int로 다시 변환해서 tar_num와 비교
                break #i와 tar_num가 다를 경우 break
            count += 1 #같다면 count = count+1 (1씩 증가)
        return count #count는 1씩 증가됨
    def print_all(self, k):
        k = k
        fac_nb = self.factorial(k)
        fac_tar_num = self.tar_num_count(k)
        print("{0} # {1}!은 {2} ".format(fac_tar_num, k, fac_nb))
        return None