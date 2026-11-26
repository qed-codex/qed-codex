---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/ThmBabOfLemmaK.lean",
  "declarations": [
    "UpperTheory.V.Win.thmBab_of_lemmaK"
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

## Simultaneous localization bounds in cyclotomic layers

[Theorem GC.0086](https://andrewodesky.com/rh/lean/UpperTheory.V.Win.thmBab_of_lemmaK/)

Assume the condition in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), the assertions of ([Local cohomology finiteness and dimension](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)) and ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)), the class-group assertion in ([Class-group ranks in cyclotomic towers](https://andrewodesky.com/rh/lean/UpperTheory.V.FW.ferreroWashington/)), and the existence of a real constant satisfying the condition in ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)). There exist functions $R_0,R_\ell$ with values in $\mathbb N$ and a constant $C_K>0$ with the following property. The arguments of $R_0,R_\ell$ are presentations of abelian fields as fixed fields in cyclotomic fields.

Let $F\subseteq\mathbb Q(\mu_m)$ be such a presented field, let $\mathcal B$ be a finite set of odd primes, and, for each $\ell\in\mathcal B$, let $L_\ell$ be a presented abelian field containing $\mu_\ell$. Let $C_t\ge1$, $A\in\mathbb R$, and $0<\varepsilon<1/52$. Put $$R=R_0(F)+\sum_{\ell\in\mathcal B}R_\ell(L_\ell),\qquad J=2^{R+2}\left(\frac{2C_KC_t}{\varepsilon}\right)^R,\qquad j_\ell=\lfloor\log_\ell R_\ell(L_\ell)\rfloor+3.$$ Here the integer logarithm is taken to be $0$ at $0$. There is $X_0$, chosen before the functions below, such that the following holds.

Let $\nu,t:\mathbb R\to\mathbb N$ satisfy, for every $x\ge2$, $$\nu(x)\ge2,\qquad 2^{\nu(x)}\le x^A,\qquad 2\le t(x)\le x^{C_t}.$$ For every $X\ge X_0$ and primes $q,d$ satisfying $$q\equiv3\pmod8,\qquad d\equiv7\pmod{16},\qquad (qd,m)=1,\qquad \log(qd)\le X^{\varepsilon/(4J)},$$ there exists $Y$ with $X^{1/J}\le Y$ and $Y^2\le X$ such that the following two bounds hold simultaneously for every $Y\le x\le Y^2$.

For $$E=F\,\mathbb Q(\mu_{2^{\nu(x)+2}})^+\mathbb Q(\sqrt{-q},\sqrt{-d}),$$ every length in the next sum is finite and $$\sum_{1\le r<t(x)}\operatorname{length}_{\mathbb Z_2}\mathcal S_{2,r}(E)\le\exp(x^{4\varepsilon/5}).$$ For each $\ell\in\mathcal B$ and every cyclotomic layer $L'/L_\ell$ of degree $\ell^{j_\ell}$, every length in the next sum is finite and $$\sum_{1\le r<t(x)}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(L')\le\exp(x^{4\varepsilon/5}).$$ The assertions hold for every isomorphic realization of the specified fields and for all algebraic closures and compatible local coefficient data.
