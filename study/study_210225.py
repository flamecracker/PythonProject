from __future__ import print_function
import torch 

x = torch.empty(6,5) # 초기화되지 않은 행렬 생성
#x = torch.rand(6,5) # 무작위로 초개ㅣ화된 행렬 생성
#x = torch.zeros(6,5, dtype=torch.long) #dtype long인 0으로 초기화된 행렬 생성
#x = torch.tensor([[1.1,3],[2.5,8.1],[4.11,9.11]]) # 임의의 텐서 생성
#x = x.new_ones(6,5,dtype = torch.double) # new_*메소드는 크기를 받는다
#x = torch.randn_like(x, dtype = torch.float) # dtype을 오버라이드 한다. 결과는 동일한 크기
#print(x.size()) #행렬의 크기
#y = torch.rand(6,5)
#print(x + y) # 행렬 덧셈연산 = print(torch.add(x, y))
# result = torch.empty(6,5) 
# torch.add(x,y, out = result ) # 연산 결과를 result로 넘김
#y.add_(x) # y에 x 더해서 대입
#x = torch.randn(4,4)
#y = x.view(16)
#z = x.view(-1,8) # -1인자는 다른 차원에서 유추
#print(x.size(),y.size(),z.size())
if torch.cuda.is_available():
    device = torch.device("cuda")          # CUDA 장치 객체(device object)로
    y = torch.ones_like(x, device=device)  # GPU 상에 직접적으로 tensor를 생성하거나
    x = x.to(device)                       # ``.to("cuda")`` 를 사용하면 됩니다.
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` 는 dtype도 함께 변경합니다!