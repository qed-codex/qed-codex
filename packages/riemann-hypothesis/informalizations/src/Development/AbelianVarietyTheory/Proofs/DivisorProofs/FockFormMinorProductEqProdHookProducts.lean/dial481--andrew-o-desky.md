---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockFormMinorProductEqProdHookProducts.lean",
  "declarations": [
    "GlobalTheory.LowRowFock.fock_delta"
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

## Fischer norm of a product of minors

[Theorem ALG.0110](https://andrewodesky.com/rh/lean/GlobalTheory.LowRowFock.fock_delta/)

Use the arithmetic datum of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with its finite CM type. For each embedding $\tau$ in that type, take an independent $m\times n$ matrix $X_\tau$, integers $p_\tau,q_\tau\ge0$ with $p_\tau+q_\tau\le m$ and $p_\tau,q_\tau\le n$, and decreasing sequences of nonnegative integers $a^+_{\tau,i}$, $a^-_{\tau,i}$. Retain their first $p_\tau$ and $q_\tau$ entries as partitions $\lambda^+_\tau,\lambda^-_\tau$. Let $\Delta_{\tau,i}^+$ be the determinant in the first $i$ rows and columns, and $\Delta_{\tau,i}^-$ the determinant in rows $p_\tau+1,\ldots,p_\tau+i$ and the last $i$ columns. Set the entry following each partition equal to zero and put $$\Delta=\prod_\tau\prod_{i=1}^{p_\tau}(\Delta_{\tau,i}^+)^{a^+_{\tau,i}-a^+_{\tau,i+1}}\prod_{i=1}^{q_\tau}(\Delta_{\tau,i}^-)^{a^-_{\tau,i}-a^-_{\tau,i+1}}.$$ Rows and columns are numbered from one. For the Fischer pairing in which distinct monomials are orthogonal and $\|X^\alpha\|_F^2=\alpha!$, $$\|\Delta\|_F^2=\prod_\tau\mathcal H(\lambda^+_\tau)\mathcal H(\lambda^-_\tau),$$ where $\alpha$ is the multi-index of a monomial, $\alpha!=\prod_a\alpha_a!$, and $\mathcal H(\lambda)$ is the product of the hook lengths of the partition $\lambda$.
