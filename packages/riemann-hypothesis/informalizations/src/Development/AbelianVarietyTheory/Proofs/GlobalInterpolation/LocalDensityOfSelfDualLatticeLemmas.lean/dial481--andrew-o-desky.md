---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LocalDensityOfSelfDualLatticeLemmas.lean",
  "declarations": [
    "GlobalTheory.LatticeDensity.localDensity_of_selfDualLatticeLemmas"
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

## Volumes and unit fibres for a self-dual Hermitian lattice

[Theorem THETA.1552](https://andrewodesky.com/rh/lean/GlobalTheory.LatticeDensity.localDensity_of_selfDualLatticeLemmas/)

Assume the source's self-dual-lattice lemma package. Let $E/F$ be a CM extension, let $J$ be a nondegenerate Hermitian form on $E^M$ with $M\ge1$, and let $v$ be a finite place of $F$ unramified in $E$. Put $F_v=k$, $E_v=k\otimes_FE$, and $q=\#(\mathcal O_F/v)$. Let $\psi:k\to\mathbb C$ be continuous, unitary and nontrivial, and suppose its dual-exponent integer is $n$: $$\{t:\psi(ts)=1\text{ for all }s\in\mathcal O_k\}=\varpi^{-n}\mathcal O_k,$$ where $\varpi$ is a uniformizer. Let $L\subseteq E_v^M$ be a finitely generated full lattice over the integral closure of $\mathcal O_k$ in $E_v$, self-dual for $J$. Let $\mu$ on $E_v^M$ and $\nu$ on $k$ be self-dual for the trace-Hermitian and multiplication pairings determined by $\psi$. Then $$\mu(L)=q^{-nM},\qquad\nu(\mathcal O_k)=q^{-n/2}.$$ Put $Q(x)=J(x,x)$ and let $\{\mu_t\}$ be any fibre-measure family disintegrating $\mu$ along $Q$ relative to $\nu$, such that every continuous compactly supported real function $\varphi$ is $\mu_t$-integrable for $t\ne0$ and $t\mapsto\int\varphi\,d\mu_t$ is continuous on $k\setminus\{0\}$. For $\beta\in\mathcal O_k^\times$, $$\mu_\beta(\{x\in L:Q(x)=\beta\}) =q^{n(1/2-M)}(1-\eta^M q^{-M}),$$ where $\eta=-1$ if $E_v$ is a field and $\eta=1$ otherwise. If $t-\beta\in\varpi\mathcal O_k$, then $\mu_t(L)=\mu_\beta(L)$.
