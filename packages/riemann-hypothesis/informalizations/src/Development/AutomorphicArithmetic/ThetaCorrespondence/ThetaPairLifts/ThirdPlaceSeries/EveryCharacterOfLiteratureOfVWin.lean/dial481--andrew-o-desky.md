---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean",
  "declarations": [
    "UpperTheory.LiteratureTheorems.cusp_decay_sobolev_of_literature",
    "UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin",
    "UpperTheory.LiteratureTheorems.principalisation_char_zero_of_literature",
    "UpperTheory.LiteratureTheorems.siegel_set_unitary_of_literature"
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

## The main theorem with the existence of automorphic Galois representations as its hypothesis

[Theorem ANT.0003](https://andrewodesky.com/rh/lean/UpperTheory.FinalTheorems.everyCharacter_of_row/)

Assume the assertion of ([Galois representations of polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter/)). Then for every integer $N\ge1$, every complex Dirichlet character $\chi$ modulo $N$ and every $s\in\mathbb C$, $$\Re s>\frac12,\qquad (\chi\ne1\ \text{or}\ s\ne1)\quad\Longrightarrow\quad L(s,\chi)\ne0.$$

## Cuspidal decay controlled by growth seminorms

[Theorem ANT.1673](https://andrewodesky.com/rh/lean/UpperTheory.LiteratureTheorems.cusp_decay_sobolev_of_literature/)

Assume the source's literature input package. Fix the full arithmetic datum specified in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)) with CM extension $E/F$, a unitary space $V$, and compatible archimedean coordinates $\theta$. Put $G=U(V)(\mathbb A_F)$, and write $h$ and $h_q$ for the prescribed adelic and rational-quotient heights. For a function $f:G\to\mathbb C$, define $$P_N(f)=\sup_g\frac{|f(g)|}{h(g)^N},\quad S_{d,N}(f)=\sum_{k=0}^d\ \sum_{a_1,\ldots,a_k}P_N(D_{a_1}\cdots D_{a_k}f),\quad Q_M(f)=\sup_g |f(g)|h_q(g)^M.$$ The finite indices $a$ run over complex matrix-unit derivatives at all prescribed archimedean places. These seminorms take values in $[0,\infty]$.

For every open subgroup $U\subset G$ and $N,M\ge0$, there are $d\ge0$ and $C\ge0$ such that $$Q_M(f)\le C S_{d,N}(f)$$ for every automorphic cuspidal $f$ smooth in $\theta$, invariant on the right under $U$ intersected with the subgroup of finite adelic elements, and satisfying $S_{k,N}(f)<\infty$ for every $k\ge0$.

## Principalization with a prescribed boundary

[Theorem AG.1724](https://andrewodesky.com/rh/lean/UpperTheory.LiteratureTheorems.principalisation_char_zero_of_literature/)

Assume the source's open-literature package of local–global Galois representation conditions and local Langlands existence. Let $k$ have characteristic zero, and let $X\to\operatorname{Spec}k$ be smooth of constant relative dimension $d$, quasi-compact and separated. Let $\mathcal I$ be an ideal sheaf such that $\operatorname{Supp}(\mathcal O_X/\mathcal I)$ contains no irreducible component of $X$, and let $E\subseteq X$ be closed with simple normal crossings at every point.

There are a scheme $X'$, a morphism $\pi:X'\to X$, and a closed boundary $E'$ such that $\pi$ is a finite sequence of blow-ups compatible with the successive simple normal-crossing boundaries, $X'$ is smooth over $k$, and $$\mathcal I\mathcal O_{X'}\text{ is an effective Cartier ideal},\qquad \operatorname{Supp}(\mathcal O_{X'}/\mathcal I\mathcal O_{X'})\text{ has simple normal crossings}.$$ Moreover, $\pi$ is an isomorphism over $X\setminus\operatorname{Supp}(\mathcal O_X/\mathcal I)$.

## Siegel sets and rapid decay for unitary groups

[Theorem AGR.1730](https://andrewodesky.com/rh/lean/UpperTheory.LiteratureTheorems.siegel_set_unitary_of_literature/)

Assume the source's open-literature package of local–global Galois representation conditions and local Langlands existence. Let $E/F$ be a CM extension of number fields, $J$ a nondegenerate Hermitian form on $E^n$, and $G=U(J)$. Choose $n\times r$ matrices $X,Y$ with $$X^*JX=Y^*JY=0,\qquad X^*JY=1,$$ and suppose the common orthogonal complement of their columns is anisotropic. Here $*$ denotes conjugate transpose. Let $P^1\subseteq G(\mathbb A_F)$ consist of elements $p$ such that $pX=XB$ for an upper-triangular adelic matrix $B$ with invertible diagonal entries of adelic absolute value one.

For $t\in\mathbb R_{>0}^r$, let $A(t)$ consist of the adelic elements with finite component $1$ that, at every infinite embedding, scale the columns of $X$ by $t_i$, those of $Y$ by $t_i^{-1}$, and fix their common orthogonal complement. There exist a compact subgroup $K\subseteq G(\mathbb A_F)$, a compact set $\Omega\subseteq P^1$, and $c>0$ with the following properties. Put $$C_c=\{t\in\mathbb R_{>0}^r:t_i\ge ct_{i+1}\ (i<r),\ t_r\ge c\},\qquad \mathfrak S=\{pak:p\in\Omega,\ t\in C_c,\ a\in A(t),\ k\in K\}.$$ When $r=0$, the last-coordinate condition is empty. Every $g\in G(\mathbb A_F)$ is $pak$ with $p\in P^1$, $t_i>0$, $a\in A(t)$ and $k\in K$; the set $\mathfrak S$ is closed and $G(F)\mathfrak S=G(\mathbb A_F)$. All $a^{-1}pa$, for $p\in\Omega$, $t\in C_c$ and $a\in A(t)$, lie in one compact set.

For every Haar measure $\mu$, $\mu(\mathfrak S)<\infty$. There is $C\ge0$ such that for every nonnegative extended-real function $f$ on $G(\mathbb A_F)$ and measurable $h:\mathbb R^r\to[0,\infty]$ satisfying $f(pak)\le h(t)$ on the displayed parameters, $$\int_{\mathfrak S}f(g)\,d\mu(g)\le C\int_{C_c}h(t)\left(\prod_{i=1}^r t_i^{\,2[F:\mathbb Q](n-2i+1)+1}\right)^{-1}dt.$$

Let $H(g)$ be the fixed adelic matrix height used in the source's growth conditions. There are $C_0\ge0$, $A\in\mathbb N$ with $H(g)\le C_0H(\gamma g)^A$ for all $g\in\mathfrak S$, $\gamma\in G(F)$. Finally, suppose $\varphi$ is continuous, left $G(F)$-invariant, invariant under an open finite level, smooth at infinity, and every iterated right Lie derivative has polynomial growth in $H$ with one common exponent. If all its constant terms along nonzero rational isotropic subspaces vanish, then for every $N\in\mathbb N$ there is $C_N\in\mathbb R$ such that $$|\varphi(g)|H(g)^N\le C_N\qquad(g\in\mathfrak S).$$
