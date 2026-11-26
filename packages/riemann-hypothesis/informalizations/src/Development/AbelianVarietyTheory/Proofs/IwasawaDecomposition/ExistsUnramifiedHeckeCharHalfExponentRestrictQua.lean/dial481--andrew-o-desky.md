---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsUnramifiedHeckeCharHalfExponentRestrictQua.lean",
  "declarations": [
    "GlobalTheory.Mem.EtaTilde.exists_etaTilde"
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

## An unramified character with half-integral infinity exponents

[Theorem ANT.1705](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.EtaTilde.exists_etaTilde/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$, real subfield $F$, and its selected CM type. Compatible archimedean families have the definition in the “Character conditions” section of ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)). There is a continuous character $$\widetilde\eta:\mathbb A_E^\times\longrightarrow S^1$$ trivial on $E^\times$, unramified at every finite place, and with half-exponent $1/2$ at each prescribed archimedean coordinate: compatible archimedean families exist, and for every such family its restriction to a single coordinate $z\in\mathbb C^\times$ is $z/|z|$.

There is at least one continuous nontrivial character $\eta:\mathbb A_F^\times\to S^1$ trivial on $F^\times$ and on $N_{E/F}(\mathbb A_E^\times)$. For every character $\eta$ satisfying these conditions, $$\widetilde\eta|_{\mathbb A_F^\times}=\eta.$$ Unramified means trivial on finite integral ideles whose inverses are also integral.
