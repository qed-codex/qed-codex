---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/AdmissibleSequenceExact.lean",
  "declarations": [
    "UpperTheory.Gal.crystallineComparison.admissible_sequence_exact"
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

## Maximal period dimension passes to subrepresentations and quotients

[Theorem PHT.1627](https://andrewodesky.com/rh/lean/UpperTheory.Gal.crystallineComparison.admissible_sequence_exact/)

Let $F\subseteq L$ be fields, $G$ a group, $B$ an $F$-vector space, and $\sigma_g\in\operatorname{End}_F(B)$ for each $g\in G$. For a finite-dimensional $L$-representation $(U,\rho_U)$ define $$D(U)=\{x\in U\otimes_F B:(\rho_U(g)\otimes\sigma_g)x=x\text{ for all }g\in G\}.$$ Fix $e\in\mathbb N$. Assume $D(U)$ is finite-dimensional over $L$ and $\dim_L D(U)\le e\dim_L U$ for every such representation. Let $f:V\to W$ be an $L$-linear intertwiner between finite-dimensional representations. Then $$f\text{ injective},\quad\dim_L D(W)=e\dim_L W\quad\Longrightarrow\quad\dim_L D(V)=e\dim_L V,$$ and $$f\text{ surjective},\quad\dim_L D(V)=e\dim_L V\quad\Longrightarrow\quad\dim_L D(W)=e\dim_L W,\quad(f\otimes1)D(V)=D(W).$$
