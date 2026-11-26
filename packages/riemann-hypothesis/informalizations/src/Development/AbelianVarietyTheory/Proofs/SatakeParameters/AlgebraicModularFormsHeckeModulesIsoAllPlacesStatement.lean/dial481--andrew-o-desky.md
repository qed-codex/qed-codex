---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AlgebraicModularFormsHeckeModulesIsoAllPlacesStatement.lean",
  "declarations": [
    "GlobalTheory.T.algebraicModularForms_heckeModules_iso_all_places"
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

## A nonzero Hecke map from matching local automorphic data

[Theorem AGR.0938](https://andrewodesky.com/rh/lean/GlobalTheory.T.algebraicModularForms_heckeModules_iso_all_places/)

Let $E$ be a CM field, $G=U(1_n)$ the definite unitary group, and $W$ an irreducible algebraic weight. Let $S_1,S_2\subseteq\{f:G(\mathbb A_{E^+,f})\to W\}$ be nonzero irreducible automorphic subrepresentations under right translation. Thus $f(\gamma g)=\rho_W(\gamma)f(g)$ for rational $\gamma$, and each $f$ has some positive principal congruence level.

Assume that at every split finite place the two subrepresentations admit smooth irreducible local components that are isomorphic. At every nonsplit place $v$ of $E^+$, assume there are a place $w\mid v$, the source's inert local datum, and $\alpha_v\in\mathbb C^{\lfloor n/2\rfloor}$ with these properties. Each $S_i$ contains a nonzero vector fixed by the maximal compact subgroup supported at $v$. For every subgroup $U\subseteq G(\mathbb A_{E^+,f})$ whose intersection with the subgroup supported at $v$ is that maximal compact, every spherical local Hecke function $h$ acts on all $U$-fixed vectors in either $S_i$ by the scalar $\operatorname{Sat}_v(h;\alpha_v)$.

Let $N>0$, and suppose $S_1^{K(N)}\ne0$. There is a complex-linear map $\Phi$ on the full ambient function space whose restriction gives a nonzero map $$\Phi:S_1^{K(N)}\longrightarrow S_2^{K(N)}$$ commuting with every Hecke operator attached to a double coset $K(N)gK(N)$.
