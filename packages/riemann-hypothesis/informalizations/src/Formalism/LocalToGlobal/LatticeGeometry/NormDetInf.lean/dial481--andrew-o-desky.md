---
{
  "module": "src/Formalism/LocalToGlobal/LatticeGeometry/NormDetInf.lean",
  "declarations": [
    "Formalism.L2.Geo.CxPkg"
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

## Complex and integral geometric models

[Definition / hypothesis ARAK.D174](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.Dat/)

Hypothesis (complex and integral geometric models). Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), ([Divisor and metric operations for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DV.Geo/)), and ([Flag intersection and reduction data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DV.ShimX/)). Write $\Sigma$ for the selected embedding set, $K$ for the coefficient number field, and $f=|\Sigma|$. Fix a set of level indices $\mathcal K$. A geometric input is a specified Hermitian space $S$ over $E$, a level $\kappa\in\mathcal K$ and an integer $j$ such that $N=\dim_E S\ge2$, $0\le j\le N$, the specified signatures of $S$ equal the signatures of its Gram matrix at every complex embedding, and its signature at every selected embedding is $(j,N-j)$.

Choose embeddings $\jmath_{p,\mathfrak l}:\mathbb K_p\to\mathbb C$ for every prime $p$ and every coefficient place $\mathfrak l\mid p$, where $\mathbb K_p=\operatorname{Frac}W(\overline{\mathbb F}_p)$. Also choose nonempty sets $\mathcal N_g$ for all $g\ge0$, sets $\mathcal F_{g,c}$ for $g,c\ge0$, and arbitrary functions $\nu_{g,c}:\mathcal F_{g,c}\times\mathcal N_g\to\mathbb R$.

For every geometric input choose a finite nonempty set $C$ and the following data. For $c\in C$, choose a subgroup $\Gamma_c\subseteq\prod_{\tau\in\Sigma}\mathrm U(j,N-j)$ and $v_c>0$. Put $$\mathcal D=\{(z_\tau):z_\tau\in M_{j,N-j}(\mathbb C),\ 1-z_\tau^*z_\tau>0\},\qquad X=\coprod_{c\in C}\Gamma_c\backslash\mathcal D,$$ where $\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)$ acts by $(Az+B)(Cz+D)^{-1}$. Choose real functions $r,h_-,h_+,n_{\rm con},n_{\rm curv}$ on $X$ and $d_\infty:\Sigma\times X\to\mathbb R$, requiring $r\ge e$ and $0<h_-\le h_+$. The component map $X\to C$ is the natural projection and $v=\sum_cv_c$.

Let $d=fN(N-1)/2$. On the polynomial ring in variables $(\tau,i)$, $0\le i<N$, define $$\deg_{\rm fl}(P)=(-1)^d\sum_{\sigma\in\prod_\tau\mathfrak S_N}\Bigl(\prod_\tau\operatorname{sgn}\sigma_\tau\Bigr)[\prod_{\tau,i}X_{\tau i}^{N-1-\sigma_\tau(i)}]P.$$ The complex degree functional is $v\deg_{\rm fl}$.

For every $c$, choose a divisor datum $Y_c$, a closed-set label $B_c$, a divisor $b_c$ with support $B_c$, and an additive map $\ell\mapsto L_c(\ell)$ from integer arrays $\Sigma\times\{0,\ldots,N-1\}$ to divisors on $Y_c$. Require $\dim Y_c=d$. Choose a real function $\deg_c$ on its arithmetic line data, with $$\deg_c(\operatorname{of}(\Delta,W,i))=\operatorname{inter}_{Y_c}(\Delta,\ldots,\Delta),\qquad \deg_c(\operatorname{tw}(A,c_\infty,c_f))=\deg_c(A).$$ On $\mathcal A=\prod_c\mathcal A_{Y_c}$ choose predicates $P_{\rm sp},P_{\rm nf}$ and a map $\overline M:\mathbb R\times\mathbb R^{\Sigma\times N}\times\mathbb Q\to\mathcal A$. Its component arithmetic self-intersection is $a_c(A)=a_{\rm top}(A_c)$, component geometric degree is $g_c(A)=\deg_c(A_c)$, arithmetic volume is $\sum_ca_{\rm vol}(A_c)$, and arithmetic nefness means $\operatorname{ANef}(A_c)$ for every $c$. The total self-intersection and geometric degree are the respective sums over $c$.

For every natural number $p$, choose integral-chart data, their extensions, and the distinguished chart objects $X_{m,p},Y_p$ in ([Integral charts and theta representations](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ModuliIntegralCharts.CF/)) and ([Extensions of integral charts and degree filtrations](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ModuliIntegralCharts.ExtA/)). For prime $p$, also choose the data of ([Boundary characters and integral Fourier jets](https://andrewodesky.com/rh/lean/Formalism.MainNotions.BoundaryLocalData.LocB/)). For $c\ge0$, choose maps $\operatorname{pb}_{p,c}$ from $\mathcal F_{fN,c}$ to sections of the distinguished sheaf $\mathcal L_{c,p}$ on $X_{m,p}$.

Choose a predicate $I$ on the natural numbers, a set $\mathcal Z$ with maps $b_p:\mathcal Z\to\mathcal M_p$ to the chart model sets, and sets $D_z$ for $z\in\mathcal Z$. Choose predicates $\operatorname{Eff}_z,\operatorname{NoVert}_z,\operatorname{PosBd}_z$ on $D_z$ and $\operatorname{AmpAb}_z$ on $\mathbb Z_{\ge0}\times D_z$. Choose a set $\mathcal H$ with predicates $P_{\rm fib},P_{\rm gen},P_{\rm lim}$. These are arbitrary specified sets, maps and predicates.

For every $p\ge0$ and coefficient place $\mathfrak l\mid p$, choose a set $M_{p,\mathfrak l}$, sets of curves $C_{p,\mathfrak l,z}$ for $z\in M_{p,\mathfrak l}$, real functions $$d_{p,\mathfrak l,z}:C_{p,\mathfrak l,z}\times(\Sigma\times\{0,\ldots,N-1\})\to\mathbb R,$$ and a distinguished $z^H_{p,\mathfrak l}\in M_{p,\mathfrak l}$. For prime $p$, each $z$ determines reduction intersection data of ([Flag intersection and reduction data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DV.ShimX/)). Its rank at $\tau:E\to\mathbb K_p$ is $j$ when $\jmath_{p,\mathfrak l}\tau$ belongs to the selected CM type, and $N-j$ otherwise.

Choose a set $P$, a map $P\to C$, functions $\phi^D,\phi^M,\phi^F:\mathbb Z_{\ge0}\times P\times(\Sigma\times N)\to\mathbb R$, functions $d_p^T,d_p^H:\Sigma\times P\to\mathbb R$, and $h^T:\mathbb R\times C\times\Sigma\to\mathbb R$. If $E$ is unramified at $p$, require $\phi_p^F=\phi_p^D$.

Choose linear functionals $a_{S,R}:\mathbb R[\Sigma\times N]\to\mathbb R$ and $b_{S,R,p}:\mathbb R[T]\to\mathbb R$ with the variable set $T$ in ([Flag intersection and reduction data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DV.ShimX/)), for all finite sets $S$ of natural numbers, real $R$ and natural $p$. Require $a_{S,R}$ to vanish on every homogeneous degree other than $d+1$, and $$b_{S,R,p}(Q^{(1)})=a_{S\cup\{p\},R}(Q),\qquad b_{S,R,p}(Q^{(0)})=a_{S\setminus\{p\},R}(Q).$$ The associated fiber-component set at $p$ is the specified generic-point set of $X_{m,p}$, with boundary predicate the negation of its abelian predicate. The de Rham curves are the chart curve set, with degree at $(\tau,i)$ equal to the extended graded degree at $(\tau,i+1)$. The Hodge curves are $\coprod_{\mathfrak l\mid p}C_{p,\mathfrak l,z^H_{p,\mathfrak l}}$ with the displayed $d_{p,\mathfrak l,z^H}$.
