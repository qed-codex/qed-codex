---
{
  "module": "src/ReciprocityTheory/Hypotheses/GalCoh.lean",
  "declarations": [
    "ReciprocityTheory.Gal.LocalEulerChar",
    "ReciprocityTheory.Gal.LocalFiniteness",
    "ReciprocityTheory.Gal.LocalTateDuality"
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

## Local cohomology conditions at finite primes

[Definition / hypothesis GC.D053](https://andrewodesky.com/rh/lean/ReciprocityTheory.Gal.LocalFiniteness/)

The following three conditions concern continuous cohomology at every finite prime of a number field. Each condition is required for all the data described below.

Let $F$ be a number field, $\Omega/F$ an algebraic closure, $v$ a finite prime of $F$, and $A\subseteq\Omega$ a valuation ring above $v$. Let $$D=\{g\in\operatorname{Gal}(\Omega/F):g(A)=A\},$$ with its profinite topology. Let $\ell$ be any prime, $r\ge1$, and $R=\mathbb Z/\ell^r\mathbb Z$. Let $M$ be any finite discrete $R$-module with a continuous $D$-action. Write $H^i(M)=H^i(D,M)$ for continuous group cohomology.

**(1) Finiteness and vanishing.** The groups $H^0(M),H^1(M),H^2(M)$ are finite, and $H^n(M)=0$ for every $n\ge3$.

**(2) Local duality.** Let $\chi:D\to R^\times$ be the cyclotomic character modulo $\ell^r$, let $R(1)$ be $R$ with this action, and put $L=H^2(D,R(1))$. Let $M'$ be the twisted dual in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), using the group $D$ and the character $\chi$. There is an $R$-linear isomorphism $L\simeq R$. The following four $R$-linear maps are bijective: $$\begin{aligned} H^0(M)&\longrightarrow\operatorname{Hom}_R(H^2(M'),L),&x&\longmapsto(y\longmapsto x\smile y),\\ H^1(M')&\longrightarrow\operatorname{Hom}_R(H^1(M),L),&y&\longmapsto(x\longmapsto y\smile x),\\ H^1(M)&\longrightarrow\operatorname{Hom}_R(H^1(M'),L),&x&\longmapsto(y\longmapsto y\smile x),\\ H^2(M)&\longrightarrow\operatorname{Hom}_R(H^0(M'),L),&x&\longmapsto(y\longmapsto x\smile y). \end{aligned}$$ The degree-zero/two cup products use evaluation $(m,\varphi)\mapsto\varphi(m)$; the degree-one products use $(\varphi,m)\mapsto\varphi(m)$.

**(3) Euler characteristic.** For a set $X$, write $c(X)$ for its cardinality if it is finite and for $0$ if it is infinite. Let $e_v$ and $f_v$ be the ramification index and residue degree of $v$ over the rational prime below it, and put $d_v=e_vf_v$. Then $$c(H^1(M))=\begin{cases} c(H^0(M))\,c(H^2(M))\,|M|^{d_v},&v\mid\ell,\\ c(H^0(M))\,c(H^2(M)),&v\nmid\ell. \end{cases}$$ When condition (1) holds, all these cardinalities are ordinary finite cardinalities. At $v\mid\ell$, $d_v=[F_v:\mathbb Q_\ell]$, where $F_v$ is the completion of $F$ at $v$.
