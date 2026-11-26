---
{
  "module": "src/Formalism/SharpRestriction/Divisibility/WeightFamilies.lean",
  "declarations": [
    "Formalism.MainNotions.WeightFamilies.ExpoSet",
    "Formalism.MainNotions.WeightFamilies.Wt"
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

## Cuspidal sections and their integral Fourier data

[Definition / hypothesis ARAK.D171](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.FormsPkg/)

Hypothesis (cuspidal sections and integral Fourier data). Use ([Complex and integral geometric models](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.Dat/)) and ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). For every stage $j\ge0$ put $p_j=k+j-1$, $q_j=\max(0,m-j)$ for the prescribed signature and let $N_j$, component set $C_j$, divisor data $Y_{j,c}$, boundary labels $B_{j,c}$, weight divisors $L_{j,c}$ and chart point sets $P^Y_{j,p}$ be specified. A weight $w=(a^+,a^-,n)$ consists of antitone rows $a^+_\tau\in\mathbb Z_{\ge0}^{p_j}$, $a^-_\tau\in\mathbb Z_{\ge0}^{q_j}$ for every selected embedding and an even integer $n\ge0$. Its divisor weight of length $N_j$ is $$\ell_\tau(i)=\begin{cases}a^+_\tau(i)+n/2,&i<p_j,\\ -a^-_\tau(q_j-1-(i-p_j))-n/2,&p_j\le i<p_j+q_j,\\0,&i\ge p_j+q_j. \end{cases}$$ Weights are added componentwise.

Choose a number field $K_0$, an isomorphism $\mathcal O_{K_0}\simeq\mathcal O$ to the specified coefficient ring, and an embedding $\iota:K_0\to K$ commuting with the two inclusions of integral elements. For every $j,w$, choose a finite-dimensional $K_0$-vector space $S_{j,w}$, with a compatible $\mathcal O_{K_0}$-module structure, and $\iota$-semilinear maps $$c_{j,w,c}:S_{j,w}\to F_{Y_{j,c}}.$$ Every value is a global section of $L_{j,c}(\ell)$ and vanishes on $B_{j,c}$. For $1\le j\le m$, every tuple of global sections of these weight divisors vanishing on the boundary lies in the $K$-span of the tuples $(c_{j,w,c}(s))_{c\in C_j}$. For every $j,w$, the images of every finite $K_0$-linearly independent family in $S_{j,w}$ are $K$-linearly independent as tuples. Choose multiplication maps $S_{j,w}\times S_{j,w'}\to S_{j,w+w'}$ whose component images are the products of the two component sections.

For each embedding $\sigma:K_0\to\mathbb C$, choose functions $N_\sigma,N_{2,\sigma}:S_{j,w}\to\mathbb R$ satisfying, for either function $M$, $$M(s)\ge0,\quad M(s)=0\Longleftrightarrow s=0,\quad M(as)=|\sigma(a)|M(s),\quad M(s+t)\le M(s)+M(t),$$ and $N_{2,\sigma}(s)\le N_\sigma(s)$.

For every $j\ge0$ choose a set $\mathcal C_j^{\rm cusp}$. For $c\in\mathcal C_j^{\rm cusp}$ choose a full $\mathcal O_E$-lattice $X_c\subset E^{q_j}$. Its exponent set consists of the Hermitian matrices $A\in M_{q_j}(E)$ positive definite at every complex embedding, such that $$g_0g_1\,l^{\mathsf T}A\bar t\in\mathcal O_E\qquad(l,t\in X_c^\vee),\qquad X_c^\vee=\{l:l^{\mathsf T}x\in\mathcal O_E\text{ for every }x\in X_c\}.$$ For every such $A$ and every $w$, choose a $K_0$-vector space $F_{j,c,A,w}$ and a linear coefficient map $S_{j,w}\to F_{j,c,A,w}$.

For each finite place $\mathfrak l$ of $K_0$ choose a set $P_{j,\mathfrak l}$, a map $P_{j,\mathfrak l}\to P^Y_{j,p}$ where $p$ is its residue characteristic, and functions $$v_{j,\mathfrak l,y,w}:S_{j,w}\to[-\infty,+\infty].$$ Require $v(0)=+\infty$, $v(s)\ne-\infty$, $v(s+t)\ge\min(v(s),v(t))$, and $$v(as)=\operatorname{ord}_{\mathfrak l}(a)+v(s)\quad(a\ne0),\qquad v_{w+w'}(ss')=v_w(s)+v_{w'}(s').$$ The valuation of $a$ is the integer normalized valuation. Finally choose arbitrary $\mathcal O_{K_0}$-submodules $T_{j,w},T^{\rm short}_{j,w}\subseteq S_{j,w}$.

## Weight gaps for analytic comparisons

[Definition / hypothesis ARAK.D234](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.HostHyp/)

Hypothesis (weight gaps for analytic comparisons). Use the ranks, words and weight arrays of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)) and ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)). Write $U_{\tau,i},V_{\tau,i},B_{\tau,j},E_{\tau,j}$ for the arrays of the distinguished word and $B_{u,\tau,j}$ for those of any word $u$. The indices of $U,V,B,E$ have lengths $k,k-1,m,m$, respectively. At every selected embedding, impose the interlacing and basic gap conditions of ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)).

Set $r=k+m-1$, $N_m=k+m(t+1)$, and define, for every natural $a$, $$\lambda_\tau(a)=\begin{cases}V_{\tau,a},&a<k-1,\\-B_{\tau,a-(k-1)},&k-1\le a<k-1+m,\\0,&\text{otherwise}.\end{cases}$$ Require $$\lambda_\tau(a)-\lambda_\tau(a+1)\ge100r^4\quad(a+1<r),\qquad \lambda_\tau(k-2)-\lambda_\tau(k-1)\ge100r^4.$$ For every word $u$, every $\tau$, and every $j+1<m$, require both $$B_{u,\tau,j+1}-B_{u,\tau,j}\ge4N_m^3+2t+6,\qquad B_{u,\tau,j+1}-B_{u,\tau,j}\ge256r^4.$$

For every $0\le i<m$, choose a weight at stage $i+1$ in the sense of ([Cuspidal sections and their integral Fourier data](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.FormsPkg/)). These weights are additional choices; no equation identifies them with the displayed $U,V,B,E$ arrays.
