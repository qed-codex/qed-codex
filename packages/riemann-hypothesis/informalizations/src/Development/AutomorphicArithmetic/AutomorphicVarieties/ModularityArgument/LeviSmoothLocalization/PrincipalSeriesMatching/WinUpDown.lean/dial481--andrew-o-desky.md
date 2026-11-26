---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LeviSmoothLocalization/PrincipalSeriesMatching/WinUpDown.lean",
  "declarations": [
    "UpperTheory.V.Z.ImaginaryQuadraticEtaCharacter.winUpDown"
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

## A local character window is preserved by prime-degree base change

[Theorem AGR.0048](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.ImaginaryQuadraticEtaCharacter.winUpDown/)

Let $L/K$ be a Galois extension of totally complex number fields of prime degree, $n\ge2$, and let $\pi,\Pi$ be cuspidal automorphic representations of $\mathrm{GL}_n(\mathbb A_K)$ and $\mathrm{GL}_n(\mathbb A_L)$ realized as irreducible right-translation subspaces of cuspidal automorphic functions. Assume weak base change: for all but finitely many finite places $w$ of $L$, the Satake multiset of $\Pi_w$ is obtained from that of $\pi_v$ by raising each entry to $f(w/v)$, where $v$ lies below $w$.

Fix a real $t$ and a finite place $v$ of $K$. The following condition on $\pi_v$ is equivalent to the two conditions below at every $w\mid v$: its normalized cuspidal support consists of characters $\xi:K_v^\times\to\mathbb C^\times$, and every such character satisfies $$q_v^{t-1/2}<|\xi(\varpi_v)|<q_v^{t+1/2}.$$ The conditions on $\Pi_w$ are:

- Its normalized cuspidal support consists of characters $\zeta:L_w^\times\to\mathbb C^\times$, each satisfying $q_w^{t-1/2}<|\zeta(\varpi_w)|<q_w^{t+1/2}$.
- For every such $\zeta$, there is a smooth character $\chi:K_v^\times\to\mathbb C^\times$ for which $\zeta(\chi\circ N_{L_w/K_v})$ is unramified.
