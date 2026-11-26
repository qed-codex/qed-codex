---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/ContinuousAdeleNorm.lean",
  "declarations": [
    "GlobalTheory.GalOfCusp.compNorm"
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

## Cuspidal automorphic representations of GL\_a over a totally complex number field

[Definition / hypothesis AGR.D019](https://andrewodesky.com/rh/lean/GlobalTheory.CuspRep.CuspSub/)

This page defines cusp forms and cuspidal automorphic representations of $\mathrm{GL}_a$ over a totally complex number field, their infinitesimal characters, the property of being regular algebraic, their local components at the finite places and, over a CM field, polarization by a Hecke character.

**Setting.** Let $E$ be a totally complex number field and $a\ge0$ an integer. Write $\mathbb A_E$ for the adele ring of $E$, $\mathbb A_E^\infty$ for the ring of finite adeles, and $E_\infty=E\otimes_{\mathbb Q}\mathbb R=\prod_{v\mid\infty}E_v$; each $E_v$ is isomorphic to $\mathbb C$. The groups $\mathrm{GL}_a(\mathbb A_E^\infty)$, $\mathrm{GL}_a(E_\infty)$ and $\mathrm{GL}_a(E_v)$, for a finite place $v$, are embedded in $\mathrm{GL}_a(\mathbb A_E)$ by putting the identity matrix at the other places, and $\mathrm{GL}_a(E)$ is embedded diagonally. Let $K_\infty=\prod_{v\mid\infty}\mathrm U(a)\subset\mathrm{GL}_a(E_\infty)$ be the group of matrices that are unitary at every infinite place.

**Smooth functions.** Let $\mathcal S$ be the complex vector space of functions $\varphi:\mathrm{GL}_a(\mathbb A_E)\to\mathbb C$ such that, for every $g\in\mathrm{GL}_a(\mathbb A_E)$, the function $y\mapsto\varphi(gy)$ on $\mathrm{GL}_a(E_\infty)$ is infinitely differentiable; here $\mathrm{GL}_a(E_\infty)$ is an open subset of the real vector space $M_a(E_\infty)$ of $a\times a$ matrices. The group $\mathrm{GL}_a(\mathbb A_E)$ acts on $\mathcal S$ by right translation, and the real Lie algebra $\mathfrak{gl}_a(E_\infty)=M_a(E_\infty)$ acts by right differentiation: $$(g\varphi)(x)=\varphi(xg),\qquad (X\varphi)(x)=\frac{d}{dt}\,\varphi\bigl(x(1+tX)\bigr)\Big|_{t=0}.$$ A subspace of $\mathcal S$ is *stable* if it is mapped to itself by $\mathrm{GL}_a(\mathbb A_E^\infty)$, by $K_\infty$ and by $\mathfrak{gl}_a(E_\infty)$.

**Capelli determinants.** Let $\sigma:E\to\mathbb C$ be an embedding and let $v$ be the infinite place of $E$ that it defines, so that $\sigma$ extends to an isomorphism of real algebras $\sigma_v:E_v\to\mathbb C$. For $\lambda\in\mathbb C$ and $1\le i,j\le a$, let $e^\sigma_{ij}(\lambda)\in\mathfrak{gl}_a(E_\infty)$ be the matrix whose entry in position $(i,j)$ has component $\sigma_v^{-1}(\lambda)$ at $v$ and component $0$ at the other infinite places, and whose other entries are $0$. Define the operator $$E^\sigma_{ij}=\tfrac12\Bigl(e^\sigma_{ij}(1)-\sqrt{-1}\cdot e^\sigma_{ij}\bigl(\sqrt{-1}\bigr)\Bigr)$$ on $\mathcal S$, in which the two matrices act by right differentiation and the factor $\sqrt{-1}$ in front of the second is multiplication of functions by this scalar. In the decomposition $\mathfrak{gl}_a(E_\infty)\otimes_{\mathbb R}\mathbb C=\prod_{\sigma:E\to\mathbb C}\mathfrak{gl}_a(\mathbb C)$, where $E$ acts on the factor indexed by $\sigma$ through $\sigma$, the operator $E^\sigma_{ij}$ is the action of the elementary matrix in position $(i,j)$ of the factor indexed by $\sigma$. For $u\in\mathbb C$, the *Capelli determinant* is the operator $$C_\sigma(u)=\sum_{s\in S_a}\operatorname{sgn}(s)\prod_{m=1}^{a}\Bigl(E^\sigma_{s(m),m}+\bigl(u+\tfrac{a+1}2-m\bigr)\delta_{s(m),m}\Bigr)$$ on $\mathcal S$, where $S_a$ is the symmetric group, $\delta$ is the Kronecker symbol, and the factors of each product are composed in increasing order of $m$ from left to right.

**Cusp forms.** A *cusp form* is a function $\varphi\in\mathcal S$ with the following six properties.

1. $\varphi(\gamma g)=\varphi(g)$ for all $\gamma\in\mathrm{GL}_a(E)$ and $g\in\mathrm{GL}_a(\mathbb A_E)$.
2. The set of $h\in\mathrm{GL}_a(\mathbb A_E^\infty)$ with $h\varphi=\varphi$ is open.
3. The functions $\kappa\varphi$, $\kappa\in K_\infty$, span a finite-dimensional space.
4. The functions $T\varphi$, where $T$ runs over the algebra of operators on $\mathcal S$ generated over $\mathbb C$ by all $C_\sigma(u)$, span a finite-dimensional space.
5. For every $g\in\mathrm{GL}_a(\mathbb A_E)$ there are a real number $C_g$ and an integer $M_g\ge0$ such that $$|\varphi(gy)|\le C_g\bigl(1+\|y\|+\|y^{-1}\|\bigr)^{M_g}\qquad(y\in\mathrm{GL}_a(E_\infty)),$$ where $\|y\|$ is the largest absolute value of a component, at an infinite place, of an entry of $y$.
6. For every integer $r$ with $0<r<a$ and every $g\in\mathrm{GL}_a(\mathbb A_E)$, $$\int_{N_r(E)\backslash N_r(\mathbb A_E)}\varphi(ng)\,dn=0,$$ where $N_r$ is the group of matrices $\begin{pmatrix}1_r&x\\0&1_{a-r}\end{pmatrix}$ with $x$ an $r\times(a-r)$ matrix. The integral is taken with respect to a Haar measure of the additive group $M_{r\times(a-r)}(\mathbb A_E)$, over a fundamental domain for its subgroup $M_{r\times(a-r)}(E)$: a subset that is measurable up to a null set of the Haar measure and whose translates by the elements of $M_{r\times(a-r)}(E)$ are pairwise disjoint up to null sets and cover the group up to a null set. The condition is imposed for every Haar measure and every such fundamental domain.

**Cuspidal automorphic representations.** A *cuspidal automorphic representation* $\pi$ of $\mathrm{GL}_a(\mathbb A_E)$ is a subspace $V_\pi\subset\mathcal S$ with these properties: every element of $V_\pi$ is a cusp form; $V_\pi$ is stable and nonzero; and the only stable subspaces of $V_\pi$ are $0$ and $V_\pi$.

**Hecke characters and twists.** A *Hecke character* of a number field $F$ is a continuous homomorphism $\chi:\mathbb A_F^\times\to\mathbb C^\times$ that is trivial on $F^\times$. For a place $v$ of $F$, write $\chi_v$ for the restriction of $\chi$ to $F_v^\times$, embedded in $\mathbb A_F^\times$ with component $1$ at the other places. If $\pi$ is a cuspidal automorphic representation of $\mathrm{GL}_a(\mathbb A_E)$ and $\psi$ is a Hecke character of $E$, then $$V_{\pi\otimes\psi}=\{g\mapsto\varphi(g)\,\psi(\det g):\ \varphi\in V_\pi\}$$ is again a cuspidal automorphic representation, denoted $\pi\otimes\psi$.

**Infinitesimal character.** Let $\sigma:E\to\mathbb C$ be an embedding and let $\mu$ be a multiset of $a$ complex numbers. The representation $\pi$ *has infinitesimal character $\mu$ at $\sigma$* if $$C_\sigma(u)\varphi=\prod_{z\in\mu}(u+z)\cdot\varphi\qquad(u\in\mathbb C,\ \varphi\in V_\pi).$$ At most one multiset $\mu$ has this property. Define $\operatorname{Inf}_\sigma(\pi)$ to be this multiset if it exists, and the multiset consisting of $a$ zeros if it does not.

The representation $\pi$ is *regular algebraic* if, for every embedding $\sigma:E\to\mathbb C$, the $a$ elements of $\operatorname{Inf}_\sigma(\pi)$ are pairwise distinct and all lie in $\tfrac{a-1}2+\mathbb Z$. For $a\ge2$ a regular algebraic $\pi$ has an infinitesimal character at every $\sigma$, since $a$ zeros are not pairwise distinct. For $a=1$ the condition also holds at an embedding $\sigma$ at which $\pi$ has no infinitesimal character, because then $\operatorname{Inf}_\sigma(\pi)=\{0\}$.

**Local components.** Let $v$ be a finite place of $E$. A *local component* of $\pi$ at $v$ is an irreducible smooth complex representation $(\varrho,W)$ of $\mathrm{GL}_a(E_v)$ for which there is a nonzero linear map $f:W\to V_\pi$ with $$f(\varrho(g)w)=g\,f(w)\qquad(g\in\mathrm{GL}_a(E_v),\ w\in W),$$ where $g$ acts on $V_\pi$ by right translation. A representation of $\mathrm{GL}_a(E_v)$ is smooth if every vector has an open stabilizer.

**Polarized pairs.** Suppose now that $E$ is a CM field, with complex conjugation $c$ and maximal totally real subfield $E^+$. The automorphism $c$ of $E$ extends to a continuous automorphism of the ring $\mathbb A_E^\infty$, also written $c$: for each finite place $v$ it maps the component at $v$ to the component at $c(v)$ by the continuous extension $E_v\to E_{c(v)}$ of $c$. On $E_\infty$, write $x\mapsto\bar x$ for complex conjugation in every factor $E_v\simeq\mathbb C$. Both are applied to matrices entry by entry.

Let $\chi$ be a Hecke character of $E^+$ and put $\psi=\chi\circ\operatorname{Nm}_{E/E^+}$, where $\operatorname{Nm}_{E/E^+}:\mathbb A_E^\times\to\mathbb A_{E^+}^\times$ is the norm of the $\mathbb A_{E^+}$-algebra $\mathbb A_E=\mathbb A_{E^+}\otimes_{E^+}E$. Then $\psi$ is a Hecke character of $E$. The pair $(\pi,\chi)$ is *polarized* if the following two conditions hold.

1. $\chi_v(-1)=(-1)^a$ for every infinite place $v$ of $E^+$.
2. There is a complex bilinear form $$B:V_{\pi\otimes\psi^{-1}}\times V_\pi\longrightarrow\mathbb C$$ that is nondegenerate in each variable (only $\varphi=0$ satisfies $B(\varphi,\varphi')=0$ for all $\varphi'$, and only $\varphi'=0$ satisfies $B(\varphi,\varphi')=0$ for all $\varphi$) and satisfies $$B(h\varphi,c(h)\varphi')=B(\varphi,\varphi'),\qquad B(\kappa\varphi,\bar\kappa\varphi')=B(\varphi,\varphi'),\qquad B(X\varphi,\varphi')+B(\varphi,\bar X\varphi')=0$$ for all $\varphi\in V_{\pi\otimes\psi^{-1}}$, $\varphi'\in V_\pi$, $h\in\mathrm{GL}_a(\mathbb A_E^\infty)$, $\kappa\in K_\infty$ and $X\in\mathfrak{gl}_a(E_\infty)$.
