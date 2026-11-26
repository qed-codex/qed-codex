---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/SubquotientPrinSeriesOfHasVec.lean",
  "declarations": [
    "GlobalTheory.PsType.subquotient_prinSeries_of_hasVec"
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

## Principal-series support from an ordered compact type

[Theorem REP.0699](https://andrewodesky.com/rh/lean/GlobalTheory.PsType.subquotient_prinSeries_of_hasVec/)

Assume the Bernstein–Zelevinsky finiteness package described below. Let $k$ be a nonarchimedean local field, $\pi$ a smooth irreducible complex representation of $\operatorname{GL}_n(k)$, and $\psi_1,\ldots,\psi_n:k^\times\to\mathbb C^\times$ smooth characters. Define $$T(\chi,x)\ \Longleftrightarrow\ \chi(u)=1\text{ for every }u\in\mathcal O_k^\times \text{ with }|u-1|\le|x|.$$ Assume $T(\psi_i/\psi_j,x)$ implies $T(\psi_a/\psi_b,x)$ whenever $i\le a\le b\le j$. Put $$J_\psi=\{g\in\operatorname{GL}_n(\mathcal O_k): T(\psi_i/\psi_j,g_{ij})\text{ for }i<j\}.$$ For $x\in k$, let $e_\chi(x)=\chi(x)$ if $|x|=1$, and $e_\chi(x)=1$ otherwise. With $\psi_{n+1}=1$, define $$\theta_\psi(g)=\prod_{m=1}^n e_{\psi_m/\psi_{m+1}} (\det g_{\{1,\ldots,m\},\{1,\ldots,m\}}).$$ If some $v\ne0$ satisfies $\pi(g)v=\theta_\psi(g)v$ for every $g\in J_\psi$, there are smooth characters $\omega_i:k^\times\to\mathbb C^\times$ with $\omega_i|_{\mathcal O_k^\times}=\psi_i|_{\mathcal O_k^\times}$ such that $\pi$ is a subquotient of the normalized principal series induced from $(\omega_i)$.
