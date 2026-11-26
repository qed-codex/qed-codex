---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/IsSemiChar.lean",
  "declarations": [
    "Formalism.L2.Th1.H.inter"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Fourfold theta kernels and lattice intertwiners

[Definition / hypothesis ARAK.D173](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.StdData/)

Let $\omega_1,\omega_2\in\mathbb C$ be linearly independent over $\mathbb R$, $L=\mathbb Z\omega_1+\mathbb Z\omega_2$ and $A=|\Im(\bar\omega_1\omega_2)|$. The one-variable functions used here are defined by the literal sums and products $$\zeta_L(z)=\sum_{l\in L}\left(\frac1{z-l}+\frac1l+\frac z{l^2}\right),\qquad \sigma_L(z)=z\prod_{l\in L}\left(1-\frac zl\right)\exp\left(\frac zl+\frac{z^2}{2l^2}\right).$$ The indices in both formulas include $l=0$; division by zero is defined to be zero. An infinite sum is zero if it is not summable, and an infinite product is one if it is not multipliable. Thus these are total definitions. Let $\eta_L:\mathbb C\to\mathbb C$ be real linear with $\eta_L(\omega_i)=2\zeta_L(\omega_i/2)$, and put $$s_L=\frac{\eta_L(\omega_1)\bar\omega_2-\eta_L(\omega_2)\bar\omega_1}{\omega_1\bar\omega_2-\omega_2\bar\omega_1},\qquad \sigma_L^*(z)=\sigma_L(z)e^{-s_Lz^2/2}.$$ For a complex vector space and a form $H$ linear in its first argument and conjugate linear in its second, define $$U_x^HF(z)=F(z+x)\exp\left(-\pi H(z,x)-\frac\pi2 H(x,x)\right),\qquad E_H(x,y)=\Im H(x,y).$$ For an additive subgroup $\Lambda$, put $\Lambda^\#=\{x:E_H(x,y)\in\mathbb Z\text{ for all }y\in\Lambda\}$. It is self-dual when $\Lambda^\#=\Lambda$. A semicharacter for $(H,\Lambda)$ is a function $\alpha$ whose values on $\Lambda$ lie in $\{1,-1\}$ and satisfy $$\alpha(x+y)=\alpha(x)\alpha(y)e^{\pi iE_H(x,y)}\quad(x,y\in\Lambda).$$ Write $\mathcal T(H,\alpha,\Lambda)$ for the entire functions satisfying $\alpha(x)U_x^HF=F$ for all $x\in\Lambda$. A lattice means a discrete additive subgroup spanning the vector space over $\mathbb R$.

In one variable take $H_L(z,w)=z\bar w/A$, and define $$\theta_{L,t}(z)=\frac{U_t^{H_L}\sigma_L^*(z)}{U_t^{H_L}\sigma_L^*(0)},\qquad \varepsilon_L(x)=\begin{cases}1,&x/2\in L,\\-1,&x/2\notin L,\end{cases}$$ $$\alpha_{L,\omega_0}(x)=\varepsilon_L(x)\exp\left(\pi i\Im(x\bar\omega_0/A)\right).$$ In $\mathbb C^n$ let $H_h(z,w)=\sum_{i,j}z_ih_{ij}\bar w_j$ for a complex matrix $h$, and let $H_L^{(n)}(z,w)=A^{-1}\sum_i z_i\bar w_i$. The standard lattice is $L^n$ and the standard semicharacter is $\prod_i\alpha_{L,\omega_0}(x_i)$. For a real $c$ also define $\alpha_c^H(x)=\exp(\pi i c\Re H(x,x))$.

For additive subgroups $\Lambda_1,\Lambda_2$, let $[\Lambda_2:\Lambda_1\cap\Lambda_2]$ be zero when the index is infinite, and choose one representative $r$ in each coset of $\Lambda_2/(\Lambda_1\cap\Lambda_2)$. The lattice intertwiner is $$\mathcal I_{H,\beta;\Lambda_1,\Lambda_2}F(z)=\frac1{\sqrt{[\Lambda_2:\Lambda_1\cap\Lambda_2]}}\sum_{r\in\Lambda_2/(\Lambda_1\cap\Lambda_2)}^{\rm fin}\beta(r)U_r^HF(z).$$ Here the finite-support sum is zero if its terms do not have finite support; the inverse of zero is zero. The representatives are fixed choices.

Hypothesis (fourfold theta data). Choose $\omega_0\in L$ with $\omega_0/2\notin L$, an additive subgroup $\Lambda\subset\mathbb C^n$, functions $\alpha:\mathbb C^n\to\mathbb C$ and $\beta:(\mathbb C^n)^4\to\mathbb C$, and a complex-linear automorphism $g$ of $(\mathbb C^n)^4$. Let $h^{\oplus4}$ be the block diagonal matrix with four copies of $h$, let $\Lambda^4$ be the fourfold product, and write $x^{(a)}$ for block $a$. Require all of the following: $H_L^{(4n)}(gx,gy)=H_{h^{\oplus4}}(x,y)$ for every $x,y$; $\alpha(0)=1$; $\beta$ agrees with the standard semicharacter on $L^{4n}$; $\beta$ is a semicharacter for $(H_L^{(4n)},g\Lambda^4)$; and $$\beta(gx)=\prod_{a=0}^3\alpha(x^{(a)})\quad\text{for every }x.$$ Require $g\Lambda^4$ to be self-dual for $H_L^{(4n)}$, and require both $$[g\Lambda^4:L^{4n}\cap g\Lambda^4]\ne0,\qquad [L^{4n}:L^{4n}\cap g\Lambda^4]\ne0.$$ The fourfold kernel associated to these choices is the defined function $$K_4(z)=\mathcal I_{H_L^{(4n)},\beta;L^{4n},g\Lambda^4}\left(\prod_{a,i}\theta_{L,\omega_0/2}(x_{a,i})\right)(gz).$$ The fourfold tensor of a function $\theta$ is $\theta^{\otimes4}(z)=\prod_{a=0}^3\theta(z^{(a)})$.
