---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/DefsInst.lean",
  "declarations": [
    "Formalism.MainNotions.G.KapIDef",
    "Formalism.MainNotions.G.kapISet"
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

## Local loss from polynomial lattices

[Definition / hypothesis PHT.D146](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.KapIDef/)

Hypothesis (polynomial lattice loss). Use the scale and weight hypotheses of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)). Let $g_\Lambda,g_{D,I},g_{\kappa,1},g_{\kappa,2}$ be real constants and put $N_1,r_o,M_0,G'$ equal to the orbit-test quantities defined in ([Local lattice, orbit-count and gain conditions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.LinkG_at/)). Put $\delta_1=x^{-\varepsilon/8}$ and $\Lambda_G=g_\Lambda N_1^2\log(xb)$. For every natural $p,n'$, subset $T'\subset\{0,\ldots,n'-1\}$ and integer functions $a',b'$ on that cyclic set, define $\kappa^I(p,n',T',a',b')$ to be the infimum of the nonnegative real $\kappa$ satisfying the universal local lattice rank condition below. This equality is required for every input, including those for which no local setting exists; real logarithms and division use the total conventions $\log0=0$ and $a/0=0$.

The local lattice rank condition defining the infimum is the following. Its inputs are natural numbers $p,n'$, a subset $T'\subset\{0,\ldots,n'-1\}$ and integer functions $a',b'$ on that cyclic set. Write $c_G=4S$, $N^+=40n'\delta_1$, and put $$D_I=\left\lceil g_{D,I}N^+x^{26}(N_1^5+k^3)\log_p(xb)\right\rceil_+,$$ $$c_6=8(D_I+1)+g_{\kappa,2}N^+k\log_p(xb)+4N^+c_G+2n'c_G,$$ $$Q_p=p^{G'},\qquad G'=(M_0+5)(6r_o+1)\lceil1/\delta_1\rceil_+,$$ where $M_0$ is the integer in the orbit test of ([Local lattice, orbit-count and gain conditions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.LinkG_at/)). If $d_-(y)$ is the least $1\le d\le n'$ for which $y-d\in T'$ has even representative, and is zero when there is no such $d$, define $$\begin{aligned}t_I={}&\sum_{\substack{y\in T'\\y\ {\rm odd},\ d_-(y)>0}}\min\{b'(y),a'(y-d_-(y))/p^{d_-(y)}\}\\ &+g_{\kappa,1}|T'|N_1\{xb/p^2+\Lambda_Gxb/(pk)\}\\ &+g_{\kappa,2}|T'|\{Q_pc_6+kQ_p+k\log_p(xb)+c_G\}+2n'c_G. \end{aligned}$$ A nonnegative real $\kappa$ is in the set whose infimum defines $\kappa^I$ when the following holds for every local setting and every weight array. A local setting consists of complete DVRs $W,O$ with fraction fields $F,K$, an embedding $\iota:F\to K$, an automorphism $\sigma$ of $F$, a finite map $W\to O$ compatible with $\iota$, and a uniformizer $w\in O$, with $p\ge5$, even $n'\ge2$, $p$ a uniformizer of $W$, residue cardinalities $p^{n'}$ and $p^{2n'}$, $w^2=p$, $\sigma^{n'}=1$, $\sigma(z)\equiv z^p\pmod{pW}$ on $W$, and every integer a square in $O$. A weight array consists of weakly decreasing integer rows $\lambda_i=(\lambda_{i,0},\ldots,\lambda_{i,k-1})$. For $i\in T'$, its endpoints are $a'(i),-b'(i)$ and its interior entries have absolute value at most $\lfloor c_G\rfloor_+$; outside $T'$ every entry has that bound. At odd $i$ replace the row by its negative in reverse order, and at even $i$ keep it; denote the resulting row by $\lambda_i^*$.

Use polynomial dual Weyl modules with the normalization in ([A prime-power inclusion between polynomial Weyl lattices](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.INST.Top.sandwichZp/)). For a rank-$k$ lattice $L\subset F^k$, and its $i$th Frobenius image in $K^k$, take the polynomial lattice of highest weight $\lambda_i^*$: if $g$ is any basis matrix, this is the inverse image of the integral dual Weyl module of weight $\lambda_i^*-\lambda_{i,k-1}^*$ under row substitution by $g$, multiplied by $\det(g)^{-\lambda_{i,k-1}^*}$. Intersect these lattices over all basis matrices of that lattice. Tensor them over all $i$ inside the polynomial tensor representation $V$, obtaining $H(L)$. Here row substitution sends $X_{ai}$ to $\sum_b g_{ab}X_{bi}$; the tensor lattice is the span of products in disjoint variable sets. An edge $e=(L_0,L_1)$ has $L_0\subset L_1$, $pL_1\subset L_0$ and $|L_1/L_0|=p^{n'}$. For each $i$ replace the Frobenius image of $L$ by the span of the image of $L_0$ and $w^{-1}$ times the image of $pL_1$; the same polynomial construction gives $H_e$. Put $$A_\lambda=\sum_i\lambda_{i,0}^*,\quad R_e=w^{-A_\lambda}H_e,\quad R'_e=w^{-A_\lambda}H_e^\vee,$$ $$N_{\rm src}(L)=w^{-\lceil t_I\rceil_+}H(L)\cap\bigcap_{e:\,L_0=L}R_e,\qquad N_{\rm tgt}(L)=w^{-\lceil t_I\rceil_+}H(L)^\vee\cap\bigcap_{e:\,L_1=L}R'_e,$$ where $H^\vee$ consists of linear functionals integral on $H$. For every target lattice $L$ there must be finitely many edges $e_a$ with target $L$ and vectors $F_a\in N_{\rm src}((e_a)_0)$ such that, for every other edge $e\ne e_a$ with the same source, $F_a\in w^{8(D_I+1)}R_e$. There must also be a natural number $d\ge(1-\kappa)\dim_KV$, an $O$-linear map $u:O^d\to N_{\rm tgt}(L)$, and a matrix $B\in M_{d,\{a\}}(O)$ such that $$\sum_a B_{ja}\,(ux)(p^{A_\lambda}F_a)=p^{D_I}x_j\qquad(x\in O^d,\ 1\le j\le d).$$
