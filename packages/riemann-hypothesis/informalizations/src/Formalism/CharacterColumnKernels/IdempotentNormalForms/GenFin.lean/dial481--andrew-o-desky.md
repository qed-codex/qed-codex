---
{
  "module": "src/Formalism/CharacterColumnKernels/IdempotentNormalForms/GenFin.lean",
  "declarations": [
    "Formalism.NG.genericFin"
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

## Simultaneously preserving kernel lengths under matrix compression

[Theorem ALG.0776](https://andrewodesky.com/rh/lean/Formalism.NG.genericFin/)

Let $O$ be a discrete valuation ring with fraction field $K$ and residue field $k$, and let $R$ be an $O$-algebra, possibly noncommutative. Let $M,G,S$ and $D_s$ for $s\in S$ be finite sets, with $$|G|\sum_{s\in S}|D_s|<|k|.$$ For each $s$, let $\rho_s:R\to M_{D_s}(O)$ be a surjective $O$-algebra homomorphism. Given any $P\in M_{M,G}(R)$, there exists $C\in M_{G,M}(R)$ such that, for every $s$, $$\operatorname{length}_O\ker\bigl(\rho_s(CP):(K/O)^{G\times D_s}\to(K/O)^{G\times D_s}\bigr) =\operatorname{length}_O\ker\bigl(\rho_s(P):(K/O)^{G\times D_s}\to(K/O)^{M\times D_s}\bigr).$$
