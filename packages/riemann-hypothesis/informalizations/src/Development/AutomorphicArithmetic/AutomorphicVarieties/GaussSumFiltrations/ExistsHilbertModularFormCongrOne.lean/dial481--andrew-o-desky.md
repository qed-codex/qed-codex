---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ExistsHilbertModularFormCongrOne.lean",
  "declarations": [
    "UpperTheory.V.Lit.oneUse",
    "UpperTheory.V.Published.exists_hilbertModularForm_congr_one"
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

## Hilbert modular forms congruent to one

[Theorem AGR.1217](https://andrewodesky.com/rh/lean/UpperTheory.V.Lit.oneUse/)

Let $F$ be a totally real number field, $p$ an odd prime, and $\iota:\overline{\mathbb Q}_p\simeq\mathbb C$ a field isomorphism. For every integer $B\ge0$, there exist $k\ge B$ with $k>0$ and $p-1\mid k$, and a holomorphic Hilbert modular form $\phi$ of parallel weight $k$, level one and trivial central character, with constant Fourier coefficients $c_0(y)$ indexed by finite ideles and nonconstant coefficients $c(\mathfrak m)$ indexed by integral ideals, such that $$|\iota^{-1}(c_0(y))-1|_p<1\quad(y\in\mathbb A_{F,f}^{\times}),\qquad |\iota^{-1}(c(\mathfrak m))|_p<1\quad(\mathfrak m\ne0).$$

## Hilbert modular forms congruent to one

[Theorem AGR.1257](https://andrewodesky.com/rh/lean/UpperTheory.V.Published.exists_hilbertModularForm_congr_one/)

Let $F$ be a totally real number field, $p\ne2$ prime, and $\iota:\overline{\mathbb Q}_p\simeq\mathbb C$ a field isomorphism. There is $N\ge0$ such that for every positive integer $k$ divisible by $(p-1)p^N$ there is a holomorphic Hilbert modular form $\phi$ of parallel weight $k$, conductor exponent zero at every finite prime, and trivial character. It has a Fourier expansion with constant coefficients $c_0(y)$ for $y\in(\mathbb A_{F,f})^\times$ and coefficients $c(\mathfrak m)$ indexed by integral ideals, satisfying $$|\iota^{-1}(c_0(y))-1|_p<1\quad\text{for every }y,\qquad |\iota^{-1}(c(\mathfrak m))|_p<1\quad(\mathfrak m\ne0).$$
