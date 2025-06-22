#!/usr/bin/env python
# coding: utf-8

# # Đề thi Cuối kỳ HK2 năm 2025 - Xác suất cho KHDL
# ## Khoa CNTT - trường ĐH Công nghiệp TPHCM.
# > Thời gian làm bài: 90 phút, SV chỉ được dùng các tài liệu chuẩn bị sẵn.

# ### Bài 1. (3 điểm)
# 
# 1) Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ xác suất PDF sau đây
# $$f_X(x)=\left\{ \begin{align}
#   & kx ,\text{   } 0 \le x \le 5 \\ 
#  & 0,\text{    } \text{khác}. \\ 
# \end{align} \right..$$
# - **a.** Tìm giá trị của $k$. 
# - **b.** Tính kỳ vọng $E(3X+4).$
# - **c.** Tính phương sai $\textrm{Var}(2X)$.

# In[26]:


#a)
import sympy as sp

# Khai báo biến x và hằng số k
x, k = sp.symbols('x k', real=True, positive=True)

# Hàm mật độ xác suất f(x)
f = k * x * (5 - x)

integral = sp.integrate(f, (x, 0, 5))
k_value = sp.solve(sp.Eq(integral, 1), k)[0]
print(f"1) Giá trị k = {k_value}")


# In[47]:


#b)
#Ky vong E(3X + 4)
E_X = sp.integrate((x*3 + 4), (x, 0, 5))
print(f"1) E(X) = {E_X.evalf(4)}")


# In[25]:


#c)

E_X = sp.integrate(x * f, (x, 0, 5))
print(f"1) E(X) = {E_X.evalf(4)}")


E_X2 = sp.integrate(x**2 * f, (x, 0, 5))
# Tính Var(X) = E(X^2) - (E(X))^2
Var_X = E_X2 - E_X**2
print(f"2) Var(X) = {Var_X.evalf(4)}")
Var_2X = Var_X*2
print(f"3) Var(2X) = {Var_2X.evalf(4)}")


# 2) Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ xác suất PDF sau đây
# $$f_X(x)=\left\{ \begin{align}
#   & 4x^3 ,\text{   } 0 \le x \le 1 \\ 
#  & 0,\text{    } \text{khác}. \\ 
# \end{align} \right..$$
# - **a.** Tìm hàm phân phối tích lũy CDF. 
# - **b.** Tính xác suất $P(\frac{1}{3} \le X \le \frac{1}{2})$.
# - **c.** Tính trung vị $median(X).$

# In[61]:


#b)
P_X_ge_1_3_given_X_le_1_2 = sp.integrate(f_x_sub, (x, 1/3, 1/2)) / sp.integrate(f_x_sub, (x, 0, 1))

print(f"b)  P(X ≥ 1/3 | X ≤ 1/2) =", P_X_ge_2_given_X_le_3.evalf())


# ### Bài 2. (3.0 điểm)
# 
# 1. Cho hai biến ngẫu nhiên $(X,Y)$ có bảng phân bố xác suất đồng thời như bên dưới ($\Omega_X = \{1,3\}, \Omega_Y = \{2,4\}$):
# 
# |X & Y     | 2    | 4     |
# |----------|------|-------|
# | **1**    | $0.1$ | $0.2$  |
# | **3**    | $a$  | $b$ |
# 
# - **a)** Tính hiệp phương sai $\textrm{Cov}(X,Y)$ theo các giá trị $a,b$. Từ đó tìm $a,b$ để $\textrm{Cov}(X,Y) = 0.1$.
# - **b)** Tại sao khi muốn đo mức độ liên hệ giữa hai biến ngẫu nhiên, có khi ta cần phải xét hệ số tương quan $\textrm{Cor}(X,Y)$ thay vì $\textrm{Cov}(X,Y)$?

# In[ ]:





# 2. Gọi $c$ là số ngày nghỉ học thực hành của anh/chị ở môn này (*SV tự ước lượng và điền giá trị này vào*). 
# 
# Cho vector ngẫu nhiên $(X,Y)$ có hàm mật độ sau 
# $$f_{X,Y}(x,y)=\left\{ \begin{aligned}
#   & x+ky^2 \, \, \text{  khi  } 0 \le x \le \frac{1}{c+1}, \, 0 \le y \le 2 \\ 
#  & 0 \, \, \text{, khác} \\ 
# \end{aligned} \right..$$
# - **a)** Xác định $k$.
# - **b)** Tìm hàm phân phối lề $f_X(x), f_Y(y).$ Từ đó kiểm tra tính độc lập của $X,Y.$
# - **c)** Tính xác suất có điều kiện $P(X \le \frac{Y}{3} | X \le \frac{Y}{2}).$

# In[ ]:


#a)
#a)
import sympy as sp

# Khai báo biến x và hằng số k
x, k = sp.symbols('x k', real=True, positive=True)

# Hàm mật độ xác suất f(x)
f = x + k * x * (5 - x)

integral = sp.integrate(f, (x, 0, 5))
k_value = sp.solve(sp.Eq(integral, 1), k)[0]
print(f"1) Giá trị k = {k_value}")


# ### Bài 3. (1.5 điểm)
# Cân nặng của sinh viên trong lớp KHDL19A là đại lượng ngẫu nhiên có phân bố chuẩn với kỳ vọng bằng $60kg$ và độ lệch chuẩn bằng $15kg$. <br>
# - **a)** Hãy sinh ra một mảng dữ liệu của $X$ với kích thước $100$ và trực quan dữ liệu đó.
# - **b)** Tính xác suất để sinh viên được chọn trong lớp thì nhẹ hơn cân nặng của anh/chị (*SV tự điền giá trị này*)?
# - **c)** Tìm $x$ sao cho xác suất để cân nặng của sinh viên nặng hơn $x$ $(kg)$ thì bằng $0.3005.$

# In[2]:


#a)
import numpy as np
import scipy.stats as st
X = st.norm(loc = 60, scale = 15)
X.rvs(100)


# In[3]:


#b)
from scipy.stats import norm
sigma = 15 # độ lệch chuẩn
mu = 55   # kỳ vọng (can nang cua anh chi = 55).
# Tính xác suất
prob_55kg = norm.cdf(55, mu, sigma)     # P(X < 55)
print(f"Xác suất để sinh viên nhẹ hơn can nang cua anh/chi (55kg): {prob_55kg:.4f}")


# In[6]:


#c)
# Tìm giá trị a sao cho P(X > a) = 0.3005
a = 1 - norm.cdf(70, mu, sigma)
print(f"Giá trị a sao cho P(X > a) = 0.3005 la: {a:.2f}")


# ### Bài 4. (2 điểm)
# 
# Một người đánh cờ với xác suất thắng là $0.65$ đã đăng ký tham gia một giải cờ tướng online đánh tổng cộng $200$ ván cờ trong vòng 1 tuần. Nếu người này thắng **nhiều hơn** $150$ ván thì sẽ giành được giải thưởng từ ban tổ chức. Hãy tính xác suất người này giành được giải bằng 2 cách: 
# - Sử dụng luật số lớn để xấp xỉ (cần hiệu chỉnh liên tục).

# In[45]:


import math
import scipy.stats as st

n, p, k = 200, 0.65, 150
mu_a, sigma_a = n * p, math.sqrt(n * p * (1 - p))
prob_a = 1 - st.norm.cdf((k + 0.5 - mu_a) / sigma_a)
print(f"1 P(X > {k}) ≈ {prob_a:.4f}")


# - Sử dụng simulation với code mẫu gợi ý như bên dưới:

# In[ ]:


import random
from scipy import stats
def simulate_cotuong(N):
    m = 200
    for _ in range(N):
        
    return m/N

simulate_cotuong(...) #simulate với số lần đủ lớn thích hợp


# ### Bài 5. (0.5đ) Trong hai chọn một.
# *Ghi chú: nếu không xử lý được chi tiết, SV có thể trình bày ý tưởng các bước làm.*
# 
# - 1) Xét phương trình bậc hai $x^2+ax+b=0$ có tham số thực $a,b$ được chọn ngẫu nhiên trong đoạn $[0;1]$. Bằng phương pháp xác suất hình học đã biết, hãy tính xác suất để phương trình có hai nghiệm thực phân biệt. 

# - 2) Cho biến ngẫu nhiên liên tục $X$ dùng để mô hình hóa sự thay đổi về thủy văn của Mỹ vào năm 1985 có hàm tích lũy xác suất CDF được cho như sau đây
# $$F(x)=\left\{ \begin{align}
#   & 0 \, \, \text{ khi } x \le 0, \\
#   & \frac{x}{4}(1-\ln \frac{x}{4}) \, \, \text{ khi  } 0 < x \le 4 \\ 
#  & 1, \, \, \text{khi} \, x > 4. \\ 
# \end{align} \right..$$
# Hãy tính kỳ vọng $E(X^3).$

# In[ ]:


#CODE HERE

