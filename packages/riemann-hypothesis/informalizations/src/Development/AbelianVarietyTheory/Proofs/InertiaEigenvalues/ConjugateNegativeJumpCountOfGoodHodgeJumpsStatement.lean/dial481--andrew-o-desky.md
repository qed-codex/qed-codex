---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ConjugateNegativeJumpCountOfGoodHodgeJumpsStatement.lean",
  "declarations": [
    "GlobalTheory.T.conjugateNegativeJumpCount_of_goodHodgeJumps"
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

## A dimension identity from separated conjugate Hodge jumps

[Theorem PHT.0791](https://andrewodesky.com/rh/lean/GlobalTheory.T.conjugateNegativeJumpCount_of_goodHodgeJumps/)

Fix the source's full CM arithmetic, twisted Galois-family and Bloch–Kato comparison data. Choose a family index $i$ and a representation index $s$. Write $\ell$ for its coefficient prime, $r$ for its rank, $t$ for its weight parameter, $\rho$ for the original representation and $W$ for its specified cyclotomic twist. Choose an embedding of the fraction field of its coefficient ring into $\mathbb C$.

Assume that at every $v\mid\ell$, both $\rho$ and $W$ are de Rham and potentially crystalline, and are crystalline if $\ell$ differs from both auxiliary primes of the datum. Suppose multisets $J_\tau\subset\mathbb Z$, indexed by $\tau:E\hookrightarrow\mathbb C$, give the filtration-jump multiplicities of $W$ at every compatible local embedding. Assume $$|J_\tau|=r,\qquad J_{\tau\circ c}=\{t-1-a:a\in J_\tau\},\qquad a<-1\ \text{or}\ t<a\quad(a\in J_\tau),$$ where $c$ is CM conjugation. Then for every pair of compatible conjugate local embeddings $\tau,\tau'$ above $\ell$, $$\dim D_{\mathrm{dR},\tau}(W)+\dim D_{\mathrm{dR},\tau'}(W) =\dim\operatorname{Fil}^0D_{\mathrm{dR},\tau}(W)+\dim\operatorname{Fil}^0D_{\mathrm{dR},\tau'}(W)+r.$$
