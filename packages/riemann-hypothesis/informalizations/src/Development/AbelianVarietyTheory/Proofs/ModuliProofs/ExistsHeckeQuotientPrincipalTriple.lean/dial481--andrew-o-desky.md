---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsHeckeQuotientPrincipalTriple.lean",
  "declarations": [
    "GlobalTheory.exists_heckeQuotient_triple_of_laws"
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

## A polarized quotient by an isotropic subgroup

[Theorem AV.0386](https://andrewodesky.com/rh/lean/GlobalTheory.exists_heckeQuotient_triple_of_laws/)

Assume the first abelian-scheme law package of ([A projective representation of torsion by theta-group operators](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaRep.exists_projective_rep/)), recalled in the conventions below. Let $E$ be a CM number field with the CM host datum of ([Powers of a theta-coordinate bundle and the Hodge bundle](https://andrewodesky.com/rh/lean/GlobalTheory.T.theta_map_pull_O1_power_hodge/)), and let $k$ be algebraically closed of characteristic zero. Let $(A,L)$ be its semiabelian datum over $k$, carrying the prescribed $\mathcal O_E$-action, rigidification, cubical and symmetric structures, and conjugate-adjoint and distinguished-CM-element compatibility isomorphisms. Suppose $A$ is proper and smooth of relative dimension $g$, $L$ is relatively ample, and no nonzero translation makes its translation-difference line bundle locally trivial.

Let $p\ge1$ be an integer and $C\subseteq A(k)$ an $\mathcal O_E$-stable subgroup of cardinality $p^{2g}$, killed by $p^2$, on which the commutator Weil pairing for $L^{\otimes p^2}$ is identically one. There is a datum $(A',L')$ of the same kind and a finite étale surjective group homomorphism $\psi:A\to A'$ with kernel exactly $C$, commuting with the $\mathcal O_E$-action, such that $A'$ is proper, $L'$ is relatively ample, its translation-difference kernel is trivial, and $$L^{\otimes p^2}\simeq\psi^*L'.$$
