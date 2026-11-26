---
{
  "module": "src/Formalism/LocalToGlobal/CharacterGerms/WipDworkInvG.lean",
  "declarations": [
    "Formalism.L2.FormalSeriesBounds.AltInv.intS_invG"
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

## Integrality of a formal coordinate solution with unit Jacobian

[Theorem PHT.1018](https://andrewodesky.com/rh/lean/Formalism.L2.FormalSeriesBounds.AltInv.intS_invG/)

Let $C$ be a field with an additive valuation $v:C\to\mathbb R\cup\{+\infty\}$, let $\Sigma$ be a finite index set, and put $O_v=\{c:v(c)\ge0\}$. Let $\Phi=(\Phi_i)$, $t=(t_i)$ and $G=(G_i)$ be tuples in $C[[X_j:j\in\Sigma]]$. Assume $\Phi_i(0)=t_i(0)=0$, all coefficients of $\Phi_i,G_i$ lie in $O_v$, and $$v\left(\det([X_j]\Phi_i)_{i,j\in\Sigma}\right)=0.$$ If $\Phi_i(t(X))=G_i(X)$ for every $i$, all coefficients of every $t_j$ lie in $O_v$.
