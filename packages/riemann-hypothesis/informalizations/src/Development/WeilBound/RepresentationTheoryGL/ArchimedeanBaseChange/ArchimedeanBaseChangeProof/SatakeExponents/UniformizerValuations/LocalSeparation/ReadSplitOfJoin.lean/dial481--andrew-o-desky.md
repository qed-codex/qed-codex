---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/LocalSeparation/ReadSplitOfJoin.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.F.RS.joinSat_holds"
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

## Satake parameters of concatenated twisted discrete data

[Theorem REP.1632](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.F.RS.joinSat_holds/)

Let $E$ be a CM number field and let $P_a,P_b,D$ be three finite lists of discrete automorphic subspaces for general linear groups, of total ranks $a,b,n\ge0$. Each list includes positive ranks for its terms, a specified smooth irreducible local component at every finite place, and a specified infinitesimal-character multiset at every complex embedding. Let $\chi_1,\chi_2$ be Hecke characters, and suppose the list of automorphic subspaces in $D$ is exactly the concatenation of the terms of $P_a$ twisted by $\chi_1\circ\det$ and those of $P_b$ twisted by $\chi_2\circ\det$.

For a finite place $w$, say that a list has Satake multiset $B$ when all its specified local components are spherical and their Satake multisets sum to $B$. If $\chi_1,\chi_2$ are unramified at $w$ and $P_a,P_b$ have multisets $B_a,B_b$, then $D$ has multiset $$\{\chi_{1,w}(\varpi_w)\alpha:\alpha\in B_a\}\sqcup\{\chi_{2,w}(\varpi_w)\beta:\beta\in B_b\}.$$ Here $\varpi_w$ is a local uniformizer and multisets retain multiplicity.
