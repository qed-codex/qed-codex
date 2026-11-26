---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/HermitianForms/UnitaryLattices/DerivPos.lean",
  "declarations": [
    "PositivityTheory.RgUd.Form.U.Final.derivTop"
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

## Irreducibility and unitarity of the highest derivative

[Theorem REP.1470](https://andrewodesky.com/rh/lean/PositivityTheory.RgUd.Form.U.Final.derivTop/)

Let $k$ be a nonarchimedean local field. Assume the following rigidity property for every smooth irreducible complex representation $\tau$ of $\operatorname{GL}_{r+1}(k)$: if $B$ is an invariant positive-definite Hermitian form, every sesquilinear form invariant under the mirabolic subgroup is a scalar multiple of $B$.

Let $\psi:k\to S^1$ be continuous and nontrivial, let $n\ge0$, $h\ge1$, and let $\pi$ be a smooth irreducible unitarisable complex representation of $\operatorname{GL}_{n+h}(k)$. Write $D^j_\psi\pi$ for its $j$th Bernstein–Zelevinsky derivative, with $D^0_\psi\pi=\pi$. Suppose $D^h_\psi\pi\ne0$ and $D^{h'}_\psi\pi=0$ whenever $h'>h$ and $h'\le n+h$. Then $$D^h_\psi\pi\otimes|\det|_k^{(1-h)/2}$$ is irreducible and unitarisable.
