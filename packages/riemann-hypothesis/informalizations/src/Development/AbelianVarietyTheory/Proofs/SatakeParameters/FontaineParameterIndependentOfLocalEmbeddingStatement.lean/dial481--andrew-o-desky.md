---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/FontaineParameterIndependentOfLocalEmbeddingStatement.lean",
  "declarations": [
    "GlobalTheory.T.fontaineParameter_independent_of_localEmbedding"
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

## A Fontaine parameter is independent of the local comparison datum

[Theorem PHT.0921](https://andrewodesky.com/rh/lean/GlobalTheory.T.fontaineParameter_independent_of_localEmbedding/)

Let $\ell$ be prime and choose crystalline, de Rham, and integral period data compatibly identified with Fontaine's rings. Fix $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$. Let $E$ be a number field, $\Omega/E$ an algebraic closure, $A\subseteq\Omega$ a valuation ring above a finite place $w$ of $E$, and $D_A\subseteq\operatorname{Gal}(\Omega/E)$ its decomposition group. Let $O,O'$ be commutative $\mathbb Z_\ell$-algebras with topologies, and choose local comparison data over $O$ and $O'$ for $D_A$ as specified in the conventions. Require both embeddings $j,j':\Omega\to\overline{\mathbb Q}_\ell$ to induce $A$: $$x\in A\ \Longleftrightarrow\ |j(x)|_\ell\le1\ \Longleftrightarrow\ |j'(x)|_\ell\le1.$$ If $r:D_A\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ is continuous entrywise and potentially semistable with respect to both comparison data, the two resulting Fontaine Weil–Deligne parameters at $w$, transported by $\iota$, are equal.
