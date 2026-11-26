---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/DenseSplitFrobInvAway.lean",
  "declarations": [
    "GlobalTheory.SplitAttUniq.repIso_of_dense"
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

## Semisimple representations determined on a dense set

[Theorem AGR.1536](https://andrewodesky.com/rh/lean/GlobalTheory.SplitAttUniq.repIso_of_dense/)

Let $E$ be a number field, $\Omega$ a field with an $E$-algebra structure, $\ell$ a prime, and $a\ge0$. Put $G=\operatorname{Aut}_E(\Omega)$, with the topology used in the source, and let $$r,r':G\longrightarrow\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$$ be continuous semisimple representations. Suppose $D\subseteq G$ is dense and $$\det(T-r(g))=\det(T-r'(g))\qquad(g\in D).$$ Then $r$ and $r'$ are isomorphic: some $A\in\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ intertwines their actions.
