---
{
  "module": "src/Formalism/SharpRestriction/CuspSpanNormBounds/Point.lean",
  "declarations": [
    "Formalism.MainNotions.S.Point"
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

## Moment data for the family

[Definition / hypothesis THETA.D137](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Draft.SData/)

Hypothesis (moment data). Use the extension $E/F$ and ranks $k,m$ of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), a finite embedding set $\mathcal T$ and a source set $\mathcal W$. For every $z\in\mathcal W$ and $\tau\in\mathcal T$, choose an array satisfying ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)), and write $U^z_{\tau,i},V^z_{\tau,i}$ for its first two rows. Choose a positive rational $\Delta$, positive real numbers $c_{n,\epsilon}$ for every binary sequence $\epsilon$ of every length $n\ge0$, and an injective map $$z\longmapsto\epsilon_z\in\{0,1\}^{k-2}.$$ For every source and embedding, require $$V^z_{\tau,l}-V^z_{\tau,l+1}=4\Delta\quad(0\le l<k-2),\qquad U^z_{\tau,l+1}=V^z_{\tau,l}-\tfrac12-\Delta\epsilon_z(l)\quad(0\le l<k-2).$$

Choose finite-dimensional complex inner-product spaces $H_{\rm mom},C_z$, complex-linear maps $P_z:C_z\to H_{\rm mom}$, and positive reals $v_N(z),v_H(z)$. For every ordered pair $(z,z')$, choose sets $A_{z,z'},B_{z,z'}$, maps $$a_t:C_{z'}\to C_z\quad(t\in A_{z,z'}),\qquad p_1,p_2:B_{z,z'}\to A_{z,z'},$$ with each $a_t$ complex-linear. Choose five subsets $A^{\rm id}_{z,z'},A^S_{z,z'},A^{\rm rel}_{z,z'},A^F_{z,z'},A^{\rm gen}_{z,z'}$ of $A_{z,z'}$, a subset $B^{\rm sc}_{z,z'}$ of $B_{z,z'}$, a set $\mathcal P_F$ and a subset $R_{z,z'}\subseteq A_{z,z'}\times\mathcal P_F$. These subsets are arbitrary. Assign to each $t\in A_{z,z'}$ scalars $g_t\in F$, $c_t\in\mathbb C$, and to each $b\in B_{z,z'}$ a natural number $s_b$, a complex number $p_b$ and a real number $m_b$.

Put $s=m/2-1$. A point of size $s+1$ is a finite ordered list $x=((a_1,d_1),\ldots,(a_h,d_h))$ with $a_i\in E^\times$, integers $d_i\ge1$ and $\sum_i d_i=s+1$. Its matrix $C(x)$ is block diagonal, with the $i$th block equal to $a_i$ times the $d_i\times d_i$ antidiagonal permutation matrix. Choose a point $x_t$ for each $t$, and real numbers $N_{z,z'}(x)$ for every pair of sources and every such point $x$.

The following local data are chosen for every nonzero prime ideal $\mathfrak p$ of $\mathcal O_F$. Let $\ell$ be its residue characteristic. Choose a nonarchimedean local field $F_\mathfrak p$ of characteristic zero and a commutative $F_\mathfrak p$-algebra $E_\mathfrak p$ of dimension two. Give $E_\mathfrak p$ its finite-dimensional vector-space topology and Borel sigma algebra. Write $v_\mathfrak p$ for the multiplicative prime-ideal valuation on $F$ and $v^{\rm loc}_\mathfrak p$ for a multiplicative valuation defining the topology of $F_\mathfrak p$; both take the value zero at zero. Choose homomorphisms $\iota_F:F\hookrightarrow F_\mathfrak p$, $\iota_E:E\to E_\mathfrak p$ that agree on $F$, with dense image for $\iota_F$ and with $$v_\mathfrak p(x)\le v_\mathfrak p(y)\quad\Longleftrightarrow\quad v^{\rm loc}_\mathfrak p(\iota_F(x))\le v^{\rm loc}_\mathfrak p(\iota_F(y))\qquad(x,y\in F).$$ Require the $F_\mathfrak p$-span of $\iota_E(E)$ to be all of $E_\mathfrak p$.

Choose an $F_\mathfrak p$-algebra automorphism $c_\mathfrak p$ with $c_\mathfrak p\iota_E(x)=\iota_E(\bar x)$, and the subring of elements of $E_\mathfrak p$ integral over the valuation ring of $F_\mathfrak p$. Require $\ell$ to be prime and choose a continuous algebra map $\mathbb Q_\ell\to F_\mathfrak p$ making $F_\mathfrak p$ finite-dimensional over $\mathbb Q_\ell$. Choose an additive character $\psi_\mathfrak p:E_\mathfrak p\to\mathbb C^\times$ such that for every $y\in E_\mathfrak p$ there is a rational $a$ whose denominator in lowest terms is a power of $\ell$, with $$\left|\operatorname{Tr}_{E_\mathfrak p/\mathbb Q_\ell}(y)-a\right|_\ell\le1,\qquad \psi_\mathfrak p(y)=\exp(2\pi\mathrm i a).$$ An optional split datum consists of an $F_\mathfrak p$-algebra isomorphism $E_\mathfrak p\simeq F_\mathfrak p\times F_\mathfrak p$ carrying $c_\mathfrak p$ to interchange of the factors, and a uniformizer $q_\mathfrak p$ of the valuation ring of $F_\mathfrak p$ with $q_\mathfrak p=\ell$.
