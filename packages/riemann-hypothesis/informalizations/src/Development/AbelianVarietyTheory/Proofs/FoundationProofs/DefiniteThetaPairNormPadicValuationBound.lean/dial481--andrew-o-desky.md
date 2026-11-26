---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/DefiniteThetaPairNormPadicValuationBound.lean",
  "declarations": [
    "GlobalTheory.NormVal.norm_mem_and_le"
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

## Algebraicity and p-adic size of a theta class-sum norm

[Theorem PHT.1411](https://andrewodesky.com/rh/lean/GlobalTheory.NormVal.norm_mem_and_le/)

Fix the source's full arithmetic datum, with CM field $E$, $f$ its prescribed real-degree parameter, imaginary quadratic discriminant parameter $d_0$, and its theta-norm input package. Let $S$ be a finite set of primes and $b_p\ge0$ numbers supported on $S$, satisfying the source's bounded-coordinate decomposition condition and $$\sum_{p\in S}b_p\log p\le\log\operatorname{rd}_E.$$ Choose a period $\delta$ satisfying the curve-ideal and discriminant-twelfth-root conditions for the unit ideal. In its period lattice $\Lambda$, choose $t_0$ with $$2t_0\in\Lambda,\qquad\frac{1+i\sqrt{d_0}}2t_0\notin\Lambda,\qquad\frac{1-i\sqrt{d_0}}2t_0\notin\Lambda.$$ Let $Q\ge1$ have every prime divisor either $2$ or a prime $p$ with $( {-d_0}/p)=1$. Let $P$ be the source's definite theta-pair datum of level $Q$, with dimensions $a\le d$ and $d$ even, odd vacuum, compatible Weil action, translation presentation, integral-source invariance, finite-index target subgroup and unit-modulus eigencharacter. Suppose $d\le2N$ and its minor multiplicities satisfy $n_\tau\le2B$ for some $N\ge0$, $B\in\mathbb R$.

Let $\mathcal N(P)$ be the finite sum over target classes, weighted by inverse stabilizer orders, of the squared absolute values of all minor-differential class sums; each inner class sum also uses inverse source-stabilizer orders. Then $\mathcal N(P)\in\overline{\mathbb Q}\subset\mathbb C$ and, for every prime $p$ and embedding $\iota:\overline{\mathbb Q}\to\mathbb C_p$, $$|\iota(\mathcal N(P))|_p\le p^{3\left[v_p\!\left(8^{4fN}(8fN)!\right)+4fNB\left(b_p+\frac{\mathbf1_{p=d_0}}4+v_p(Q)\right)+4N^2v_p(Q)\right]}.$$
