---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/ConnectedSpecialFibreConstantStatement.lean",
  "declarations": [
    "GlobalTheory.T.connected_special_fibre_constant"
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

## A local residue value is a unit throughout a connected special fibre

[Theorem AG.0679](https://andrewodesky.com/rh/lean/GlobalTheory.T.connected_special_fibre_constant/)

Let $O$ be a discrete valuation domain, $\varpi\in O$ irreducible, and $\Omega$ a field with an injective map $O\to\Omega$. Let $s:X\to\operatorname{Spec}O$ be proper and $\xi:\operatorname{Spec}\Omega\to X$ lie over that map. Put $\eta=\xi(*)$ and assume the map $\mathcal O_{X,\eta}\to\Omega$ is bijective and, for every specialization $p$ of $\eta$, the induced map $\mathcal O_{X,p}\to\Omega$ is injective. Write $R_p\subset\Omega$ for its image and $\pi$ for the image of $\varpi$. Suppose $$Z=\{p:\eta\leadsto p,\ \pi\notin R_p^\times\}\subset X$$ is connected.

Let $h$ assign an element $h_p\in\Omega$ to every specialization $p$ of $\eta$. Assume that for each $p\in Z$ there is an open neighbourhood $U$ such that for every $q\in Z\cap U$, $$h_p\in R_q,\qquad (h_p-h_q)/\pi\in R_q.$$ If $h_p$ is a unit of $R_p$ for some $p\in Z$, then it is a unit of $R_p$ for every $p\in Z$.
