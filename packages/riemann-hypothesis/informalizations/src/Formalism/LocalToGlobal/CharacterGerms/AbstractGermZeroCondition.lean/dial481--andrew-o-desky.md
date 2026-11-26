---
{
  "module": "src/Formalism/LocalToGlobal/CharacterGerms/AbstractGermZeroCondition.lean",
  "declarations": [
    "Formalism.L2.FormalSeriesBounds.AbstractGermZero.abstract_germ_zero"
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

## Invariance of integral formal germs under integral coordinate changes

[Theorem PHT.0848](https://andrewodesky.com/rh/lean/Formalism.L2.FormalSeriesBounds.AbstractGermZero.abstract_germ_zero/)

Let $C$ be a field with an additive valuation $v:C\to\mathbb R\cup\{\infty\}$. Assume there is a prime $p$ with $v(p)=1$, and put $\mathcal O_v=\{a:v(a)\ge0\}$. Let $I_0,I_1$ be finite sets. For $g=0,1$, choose vectors of formal series $$t_g,t'_g,\phi_g,\phi'_g\in C[[X_i:i\in I_g]]^{I_g}$$ with zero constant terms. Assume that $\phi_g,\phi'_g$ have coefficients in $\mathcal O_v$ and $$v(\det D\phi_g(0))=v(\det D\phi'_g(0))=0,\qquad \phi_g(t_g(X))=\phi'_g(t'_g(X)).$$ Write $t=(t_0,t_1)$ and $t'=(t'_0,t'_1)$, with each block regarded as a series in the variables indexed by $I_0\sqcup I_1$. Then $$\{\Gamma(t(X)):\Gamma\in\mathcal O_v[[X_i:i\in I_0\sqcup I_1]]\} = \{\Gamma(t'(X)):\Gamma\in\mathcal O_v[[X_i:i\in I_0\sqcup I_1]]\}.$$
