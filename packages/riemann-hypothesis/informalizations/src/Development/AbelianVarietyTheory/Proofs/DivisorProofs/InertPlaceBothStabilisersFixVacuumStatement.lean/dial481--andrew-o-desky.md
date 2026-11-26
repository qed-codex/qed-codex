---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/InertPlaceBothStabilisersFixVacuumStatement.lean",
  "declarations": [
    "GlobalTheory.T.inert_place_both_stabilisers_fix_vacuum"
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

## Both lattice stabilizers fix an inert local vacuum

[Theorem THETA.1583](https://andrewodesky.com/rh/lean/GlobalTheory.T.inert_place_both_stabilisers_fix_vacuum/)

Let $E/F$ be number fields with $F$-automorphism $\sigma$ of $E$, and assume the source's admissible triple package for ranks $a,a'\ge0$. Its data consist of a good base, spaces $V,V',W$ of ranks $a,a',a+a'$, compatible Schrodinger models, Hecke characters $\alpha,\beta$, disjoint finite sets $S_0,Q$ with $T=S_0\cup Q$, and Weil actions $\omega,\omega'$. Write $p,q\ge0$ for its signature indices and $m_\alpha,m_\beta$ for its lists of archimedean character exponents, and assume all the conditions of that package.

Let $v$ be a finite place of $F$, $w$ a finite place of $E$ inert over $v$, and $v\notin T$. Let $K_{V,v}$ and $K_{W,v}$ consist of the adelic unitary elements supported at $v$ that, together with their inverses, preserve the $O_{F_v}$-lattices induced from the specified global lattices. If $\phi_v$ is the prescribed local vacuum of the Schrodinger model for $(V,W)$, then $$\omega_v(k,k')\phi_v=\phi_v\qquad(k\in K_{V,v},\ k'\in K_{W,v}).$$ Here $\omega_v$ denotes the local action induced by $\omega$ on the finite-place factor.
