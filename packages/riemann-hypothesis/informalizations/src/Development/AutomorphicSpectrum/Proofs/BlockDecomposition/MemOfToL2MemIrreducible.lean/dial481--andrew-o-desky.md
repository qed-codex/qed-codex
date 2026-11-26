---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MemOfToL2MemIrreducible.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.FinitePart.exists_irred_le"
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

## An irreducible subrepresentation in a cuspidal closed subspace

[Theorem REP.0468](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.FinitePart.exists_irred_le/)

Let $E$ be a totally complex number field, let $a\ge0$, and put $G=\operatorname{GL}_a(\mathbb A_E)$. For $t\in\mathbb R$, let $z(t)\in G$ have archimedean component $e^tI_a$ at every infinite place and finite component $I_a$. Put $\Gamma=\langle\operatorname{GL}_a(E),z(1)\rangle$, and choose a Haar measure $\mu$ invariant on both the left and the right.

Let $\mathcal H_{\mathrm{cusp}}\subseteq L^2(\Gamma\backslash G)$ be the closure of the classes of continuous cuspidal functions invariant under left translation by $\operatorname{GL}_a(E)$ and by every $z(t)$. Every nonzero closed right-translation-invariant complex subspace $C\subseteq\mathcal H_{\mathrm{cusp}}$ contains a nonzero closed invariant subspace $H$ with no proper nonzero closed invariant subspace.
