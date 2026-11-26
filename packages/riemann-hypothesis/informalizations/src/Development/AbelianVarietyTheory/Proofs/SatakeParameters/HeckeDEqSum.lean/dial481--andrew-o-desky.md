---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/HeckeDEqSum.lean",
  "declarations": [
    "GlobalTheory.HeckeRecon.recon"
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

## Reconstructing an irreducible representation from one level

[Theorem AGR.0974](https://andrewodesky.com/rh/lean/GlobalTheory.HeckeRecon.recon/)

Let $L$ be a CM number field, $L^+$ its maximal totally real subfield, and $G=U(I_n)$ over $L^+$, where $n\ge0$. Let $(W_1,\rho_1)$ and $(W_2,\rho_2)$ be irreducible algebraic coefficient representations of $G(L^+)$. For $i=1,2$, let $S_i$ be a nonzero irreducible right-translation subrepresentation of the algebraic modular forms with coefficients $W_i$.

Let $N\ge1$, let $K(N)\subseteq G(\mathbb A_{L^+,f})$ be the principal congruence subgroup, and let $$\phi:\operatorname{Fun}(G(\mathbb A_{L^+,f}),W_1)\longrightarrow\operatorname{Fun}(G(\mathbb A_{L^+,f}),W_2)$$ be complex-linear. Suppose $\phi(S_1^{K(N)})\subseteq S_2^{K(N)}$, $\phi$ is nonzero on $S_1^{K(N)}$, and $$\phi(T_{K(N)gK(N)}f)=T_{K(N)gK(N)}\phi(f)$$ for every $g\in G(\mathbb A_{L^+,f})$ and $f\in S_1^{K(N)}$. Then $S_1$ and $S_2$ are isomorphic as representations of $G(\mathbb A_{L^+,f})$.
