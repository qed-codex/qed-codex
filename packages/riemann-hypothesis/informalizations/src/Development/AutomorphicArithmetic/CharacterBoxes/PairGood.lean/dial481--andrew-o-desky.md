---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/PairGood.lean",
  "declarations": [
    "UpperTheory.Top.PairEx",
    "UpperTheory.Top.PairGood"
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

## Auxiliary primes with controlled twists

[Theorem ANT.1.0101](https://andrewodesky.com/rh/lean/QH.pairEx/)

Let $M\ge1$ be an integer, and let $\varepsilon$ and $A$ be real numbers with $0<\varepsilon<1/52$ and $A\ge1$. There is a real number $U_0\ge1$, depending only on $M$, $\varepsilon$ and $A$, such that for every real number $U\ge U_0$ there are primes $q$ and $d$ with the following properties, in which $z=U^{\varepsilon/5}$ and $z'=z(\log U)^2$. The primes satisfy $$q\equiv3\pmod8,\qquad d\equiv7\pmod{16},\qquad z/2<\log q\le z,\qquad z'/2<\log d\le z',$$ $$(M,qd)=1,\qquad q\mid d+1,\qquad p\mid d+1\ \text{ for every odd prime }p\le z,$$ and the following two assertions hold for the twists by $q$ and $d$, which are defined in the introduction.

1. For every Dirichlet character $\xi$ modulo $M$ and every $(i,j)\in\{0,1\}^2$ with $(i,j)\ne(0,0)$, the twist $\chi=\xi_{i,j}$ satisfies $$|g_\chi(y)|\le y^{1/2+\varepsilon/2}\qquad\text{and}\qquad\left|\frac{L'}{L}(1,\chi)\right|\le4\log y$$ for every real number $y$ with $U\le y\le U^A$. Here $g_\chi$ and $L(s,\chi)$ are the functions of ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)).
2. For every real-valued primitive Dirichlet character $\rho$ whose conductor divides $8M$ and every $(i,j)\in\{0,1\}^2$ with $(i,j)\ne(0,0)$, the twist $\chi=\rho_{i,j}$ satisfies $$L(s,\chi)\ne0\qquad\text{for every }s\in\mathbb C\text{ with }\Re s>399/400\text{ and }|\Im s|\le8Me^{z+jz'}.$$
