---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean",
  "declarations": [
    "UpperTheory.One.vwin_of_row"
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

## Bound for localization kernels

[Theorem GC.1.0105](https://andrewodesky.com/rh/lean/UpperTheory.One.vwin_of_row/)

Assume that the assertion of ([Galois representations of polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter/)) holds for all its data: every CM field and every algebraic closure of it, every integer $a\ge1$, every prime $\ell$, every isomorphism of fields $\overline{\mathbb Q}_\ell\to\mathbb C$, and every polarized pair formed by a regular algebraic cuspidal automorphic representation of $\mathrm{GL}_a$ over the adeles of the CM field and a Hecke character of its maximal totally real subfield.

Let $\psi$ be a primitive Dirichlet character, let $\varepsilon$ be a real number with $0<\varepsilon<1/52$, and let $\nu:\mathbb R\to\mathbb Z_{\ge0}$ be a function such that $$x^{2+8\varepsilon}\le2^{\nu(x)}\le2x^{2+8\varepsilon}\qquad\text{for every real number }x\ge1.$$ Then there exist real numbers $J\ge1$ and $X_0\ge1$ with the following property. Let $X\ge X_0$ be a real number, put $U=X^{1/J}$, and let $q$ and $d$ be primes that satisfy the following three conditions.

1. $q\equiv3\pmod8$ and $\tfrac12U^{\varepsilon/5}<\log q\le U^{\varepsilon/5}$.
2. $d\equiv7\pmod{16}$ and $\tfrac12U^{\varepsilon/5}(\log U)^2<\log d\le U^{\varepsilon/5}(\log U)^2$.
3. $q$ divides $d+1$, and every odd prime $p\le U^{\varepsilon/5}$ divides $d+1$.

Then there is a real number $Y$ with $U\le Y$ and $Y^2\le X$ such that the following holds for every real number $x$ with $Y\le x\le Y^2$ and every number field $E$ isomorphic to $$\mathbb Q(\zeta_{2^{\nu(x)+2}})^+\,K_\psi\,\mathbb Q(\sqrt{-q},\sqrt{-d}).$$ Put $t=\lfloor x^{401}\rfloor$. For every algebraic closure $\overline E$ of $E$ and every choice, for each prime $\ell$, of a place of $\overline E$ above each place of $E$ above $\ell$, the localization kernels $\mathcal S_{\ell,r}(E)$ formed with $\overline E$ and these places satisfy the following two assertions.

- (i) For every prime $\ell$ and every integer $r$ with $1\le r<t$, the localization kernel $\mathcal S_{\ell,r}(E)$ has finite length as a $\mathbb Z_\ell$-module.
- (ii) For every finite set $\mathcal P$ of primes, $$\sum_{\ell\in\mathcal P}\log\ell\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(E)\le\exp(x^\varepsilon/2).$$
